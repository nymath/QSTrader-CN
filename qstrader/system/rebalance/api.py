import pandas as pd
import pytz
import sys
import os
sys.path.append(os.getcwd())

import datetime
from qstrader.system.rebalance.rebalance import Rebalance

from qstrader.exchange.simulated_exchange import SimulatedExchangePro

from pandas_market_calendars import get_calendar
from itertools import groupby
import copy

class Monthly(Rebalance):
    def __init__(
        self,
        start_dt,
        end_dt,
        pre_market=False,
        day_nums = [-1], 
    ):
        self.start_dt = start_dt
        self.end_dt = end_dt
        self.day_nums = day_nums
        self.market_time = self._set_market_time(pre_market)
        self.rebalances = self._generate_rebalances()
    
    def _set_market_time(self, pre_market):

        return "01:30:00" if pre_market else "07:00:00"

    def _generate_rebalances(self):
        """
        Utilise the Pandas date_range method to create the appropriate
        list of rebalance timestamps.

        Returns
        -------
        `List[pd.Timestamp]`
            The list of rebalance timestamps.
        """
        trade_dates = get_calendar('SSE').valid_days(start_date=self.start_dt, end_date=self.end_dt)
        trade_dates = [x.date() for x in trade_dates]
        rebalance_dates = []
        for t, x in groupby(trade_dates, lambda x:(x.year,x.month)):
            y = copy.deepcopy(list(x))
            for i in self.day_nums:
                try:
                    rebalance_dates.append(y[i])
                except:
                    continue
        rebalance_times = [
            pd.Timestamp(
                "%s %s" % (date, self.market_time), tz=pytz.utc
            )
            for date in rebalance_dates
        ]
        return rebalance_times

class Weekly(Rebalance):
    def __init__(
        self,
        start_dt,
        end_dt,
        pre_market=False,
        day_nums = [-1], 
    ):
        self.start_dt = start_dt
        self.end_dt = end_dt
        self.day_nums = day_nums
        self.market_time = self._set_market_time(pre_market)
        self.rebalances = self._generate_rebalances()
    
    def _set_market_time(self, pre_market):

        return "01:30:00" if pre_market else "07:00:00"

    def _generate_rebalances(self):
        """
        Utilise the Pandas date_range method to create the appropriate
        list of rebalance timestamps.

        Returns
        -------
        `List[pd.Timestamp]`
            The list of rebalance timestamps.
        """
        trade_dates = get_calendar('SSE').valid_days(start_date=self.start_dt, end_date=self.end_dt)
        trade_dates = [x.date() for x in trade_dates]
        rebalance_dates = []
        for t, x in groupby(trade_dates, lambda x:(x.year,x.week)):
            y = copy.deepcopy(list(x))
            for i in self.day_nums:
                try:
                    rebalance_dates.append(y[i])
                except:
                    continue
        rebalance_times = [
            pd.Timestamp(
                "%s %s" % (date, self.market_time), tz=pytz.utc
            )
            for date in rebalance_dates
        ]
        return rebalance_times


class Daily(Rebalance):
    def __init__(
        self,
        start_dt,
        end_dt,
        pre_market=False, 
    ):
        self.start_dt = start_dt
        self.end_dt = end_dt
        self.market_time = self._set_market_time(pre_market)
        self.rebalances = self._generate_rebalances()
    
    def _set_market_time(self, pre_market):

        return "01:30:00" if pre_market else "07:00:00"

    def _generate_rebalances(self):
        """
        Utilise the Pandas date_range method to create the appropriate
        list of rebalance timestamps.

        Returns
        -------
        `List[pd.Timestamp]`
            The list of rebalance timestamps.
        """
        trade_dates = get_calendar('SSE').valid_days(start_date=self.start_dt, end_date=self.end_dt)
        trade_dates = [x.date() for x in trade_dates]
        rebalance_dates = trade_dates
        rebalance_times = [
            pd.Timestamp(
                "%s %s" % (date, self.market_time), tz=pytz.utc
            )
            for date in rebalance_dates
        ]
        return rebalance_times

class BuyAndHoldRebalance(Rebalance):
    """
    Generates a single rebalance timestamp at the start date in
    order to create a single set of orders at the beginning of
    a backtest, with no further rebalances carried out.

    Parameters
    ----------
    start_dt : `pd.Timestamp`
        The starting datetime of the buy and hold rebalance.
    """

    def __init__(self, start_dt, end_dt, pre_market=False):
        self.start_dt = start_dt
        self.end_dt = end_dt
        self.market_time = self._set_market_time(pre_market)
        self.rebalances = self._generate_rebalances()
    
    def _set_market_time(self, pre_market):

        return "01:30:00" if pre_market else "07:00:00"

    def _generate_rebalances(self):
        trade_dates = get_calendar('SSE').valid_days(start_date=self.start_dt, end_date=self.end_dt)
        rebalance_dates = trade_dates[0].date()
        rebalance_times = pd.Timestamp("%s %s" % (rebalance_dates, self.market_time), tz=pytz.utc)
        
        return [rebalance_times]