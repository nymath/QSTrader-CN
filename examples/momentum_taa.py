# tactical asset allocation (策略性分配资产策略)
# Momentum, HPR(Holding Period Return)
# 过去一段时间内收益高的股票, 未来收益也会更高
import operator
import os
import sys
sys.path.append(os.getcwd())
import pandas as pd
import pytz


from qstrader.api import Equity
from qstrader.api import (DynamicUniverse, StaticUniverse)
from qstrader.api import (Monthly, BuyAndHoldRebalance)
from qstrader.api import (ZeroFeeModel, PercentFeeModel)

from qstrader.api import (CSVDailyBarDataSource, BacktestDataHandler)
from qstrader.signals.momentum import MomentumSignal
from qstrader.api import SignalsCollection
from qstrader.api import (AlphaModel, FixedSignalsAlphaModel)
from qstrader.api import (TearsheetStatistics, BacktestTradingSession)


class TopNMomentumAlphaModel(AlphaModel):

    def __init__(
        self, signals, mom_lookback, mom_top_n, universe, data_handler
    ):
        """
        Initialise the TopNMomentumAlphaModel

        Parameters
        ----------
        signals : `SignalsCollection`
            The entity for interfacing with various pre-calculated
            signals. In this instance we want to use 'momentum'.
        mom_lookback : `integer`
            The number of business days to calculate momentum
            lookback over.
        mom_top_n : `integer`
            The number of assets to include in the portfolio,
            ranking from highest momentum descending.
        universe : `Universe`
            The collection of assets utilised for signal generation.
        data_handler : `DataHandler`
            The interface to the CSV data.

        Returns
        -------
        None
        """
        self.signals = signals
        self.mom_lookback = mom_lookback
        self.mom_top_n = mom_top_n
        self.universe = universe
        self.data_handler = data_handler

    def _select_assets(
        self, dt
    ):
        assets = self.signals['momentum_hpr'].assets
        
        # Calculate the holding-period return momenta for each asset,
        # for the particular provided momentum lookback period
        all_momenta = {
            asset: self.signals['momentum_hpr'](
                asset, self.mom_lookback
            ) for asset in assets
        } # FIXME: 新加入的资产并没有126天的收益率数据, 但是仍然进行了计算
        # TODO: 将结果写出, 以构建因子库
        # TODO: 如何根据已有因子进行测试
        # Obtain a list of the top performing assets by momentum
        # restricted by the provided number of desired assets to
        # trade per month
        return [
            asset[0] for asset in sorted(
                all_momenta.items(),
                key=lambda x: x[1],
                reverse=True
            )
        ][:self.mom_top_n]

    def _generate_weights(self, dt):
        """
        Calculate the highest performing momentum for each
        asset then assign 1 / N of the signal weight to each
        of these assets.

        Parameters
        ----------
        dt : `pd.Timestamp`
            The datetime for which the signal weights
            should be calculated.

        Returns
        -------
        `dict{str: float}`
            The newly created signal weights dictionary.
        """
        assets = self.universe.get_assets(dt) #FIXME: 当股票池更换时, 会出现一些问题
        weights =  {asset: 0.0 for asset in assets}
        top_assets = self._select_assets(dt)
        
        if self.signals.warmup >= self.mom_lookback:
            for asset in top_assets:
                weights[asset] = 1.0 / self.mom_top_n
        return weights

    def __call__(self, dt):
        return self._generate_weights(dt)



if __name__ == "__main__":
    # Duration of the backtest
    start_dt = pd.Timestamp('2006-01-01 01:30:00', tz=pytz.UTC)
    burn_in_dt = pd.Timestamp('2006-12-22 01:30:00', tz=pytz.UTC)
    end_dt = pd.Timestamp('2022-12-31 23:59:00', tz=pytz.UTC)

    # Model parameters
    mom_lookback = 126  # Six months worth of business days
    mom_top_n = 3  # Number of assets to include at any one time

    # Construct the symbols and assets necessary for the backtest, this utilises the SPDR US sector ETFs, all beginning with XL
    strategy_symbols = ["000001.XSHE", "000002.XSHE", "600519.XSHG", "601398.XSHG", "601728.XSHG", "601988.XSHG"] 
    assets = ['EQ:%s' % symbol for symbol in strategy_symbols]
    
    asset_dates = {asset: start_dt for asset in assets}
    # asset_dates['EQ:XLC'] = pd.Timestamp('2018-06-18 00:00:00', tz=pytz.UTC) 
    strategy_universe = DynamicUniverse(asset_dates)

    # To avoid loading all CSV files in the directory, set the data source to load only those provided symbols
    csv_dir = os.environ.get('QSTRADER_CSV_DATA_DIR', './datasource')
    strategy_data_source = CSVDailyBarDataSource(csv_dir, Equity, csv_symbols=strategy_symbols)
    strategy_data_handler = BacktestDataHandler(strategy_universe, data_sources=[strategy_data_source])

    momentum_hpr = MomentumSignal(start_dt, strategy_universe, lookbacks=[mom_lookback])
    signals = SignalsCollection({'momentum_hpr': momentum_hpr}, strategy_data_handler)

    
    strategy_alpha_model = TopNMomentumAlphaModel(
        signals, mom_lookback, mom_top_n, strategy_universe, strategy_data_handler
    )
    
    # set the rebalance schedule
    rebalancer = Monthly(start_dt, end_dt, pre_market=False, day_nums=[-1])
    
    strategy_backtest = BacktestTradingSession(
        start_dt,
        end_dt,
        strategy_universe,
        strategy_alpha_model,
        signals=signals,
        rebalance= rebalancer,
        long_only=True,
        cash_buffer_percentage=0.01,
        burn_in_dt=burn_in_dt,
        data_handler=strategy_data_handler,
        fee_model=PercentFeeModel(commission_pct=0.003, tax_pct=0.0)
    )
    strategy_backtest.run()

    # Construct benchmark assets (buy & hold SPY)
    benchmark_symbols = ['000300.XSHG']
    benchmark_assets = ['EQ:000300.XSHG']
    benchmark_universe = StaticUniverse(benchmark_assets)
    benchmark_data_source = CSVDailyBarDataSource(csv_dir, Equity, csv_symbols=benchmark_symbols)
    benchmark_data_handler = BacktestDataHandler(benchmark_universe, data_sources=[benchmark_data_source])

    # Construct a benchmark Alpha Model that provides
    # 100% static allocation to the SPY ETF, with no rebalance
    benchmark_alpha_model = FixedSignalsAlphaModel({'EQ:000300.XSHG': 1.0})
    
    # 注意benckmark开始的时间是burn_in_dt
    rebalancer = BuyAndHoldRebalance(burn_in_dt, end_dt, pre_market=False)
    benchmark_backtest = BacktestTradingSession(
        burn_in_dt,
        end_dt,
        benchmark_universe,
        benchmark_alpha_model,
        rebalance=rebalancer,
        long_only=True,
        cash_buffer_percentage=0.01,
        data_handler=benchmark_data_handler,
        fee_model=PercentFeeModel()
    )
    benchmark_backtest.run()

    # Performance Output
    tearsheet = TearsheetStatistics(
        strategy_equity=strategy_backtest.get_equity_curve(),
        benchmark_equity=benchmark_backtest.get_equity_curve(),
        title='US Sector Momentum - Top 3 Sectors'
    )
    tearsheet.plot_results()
