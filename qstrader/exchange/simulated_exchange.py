import datetime

from qstrader.exchange.exchange import Exchange
from pandas_market_calendars import get_calendar
import pandas as pd

class SimulatedExchange(Exchange): 
    """
    The SimulatedExchange class is used to model a live
    trading venue.

    It exposes methods to inform a client class intance of
    when the exchange is open to determine when orders can
    be executed.

    Parameters
    ----------
    start_dt : `pd.Timestamp`
        The starting time of the simulated exchange.
    """

    def __init__(self, start_dt):
        self.start_dt = start_dt

        # TODO: Eliminate hardcoding of NYSE
        # TODO: Make these timezone-aware
        self.open_dt = datetime.time(1, 30) 
        self.close_dt = datetime.time(7, 00)
        self.name = '上海深圳交易所合并版'
    
    def is_open_at_datetime(self, dt):
        """
        Check if the SimulatedExchange is open at a particular
        provided pandas Timestamp.

        This logic is simplistic in that it only checks whether
        the provided time is between market hours on a weekday.

        There is no historical calendar handling or concept of
        exchange holidays.

        Parameters
        ----------
        dt : `pd.Timestamp`
            The timestamp to check for open market hours.

        Returns
        -------
        `Boolean`
            Whether the exchange is open at this timestamp.
        """
        if dt.weekday() > 4:
            return False
        return self.open_dt <= dt.time() and dt.time() < self.close_dt

class SimulatedExchangePro(Exchange): 
    """
    The SimulatedExchange class is used to model a live
    trading venue.

    It exposes methods to inform a client class intance of
    when the exchange is open to determine when orders can
    be executed.

    Parameters
    ----------
    start_dt : `pd.Timestamp`
        The starting time of the simulated exchange.
    """

    def __init__(self, start_dt):
        self.start_dt = start_dt

        self.open_dt = datetime.time(1, 30) 
        self.close_dt = datetime.time(7, 00)
        self.name = '上海深圳交易所合并版'
        self.trade_dates = self._create_trade_dates() 
    
    def _create_trade_dates(self):
        shanghai_calendar = get_calendar('SSE')
        today = pd.Timestamp(datetime.datetime.now())
        trade_days = shanghai_calendar.valid_days(start_date=self.start_dt.date(), end_date=today.date())
        return [x.date() for x in trade_days]
        
    def is_open_at_datetime(self, dt):
        if dt.date() not in self.trade_dates:
            return False
        return self.open_dt <= dt.time() and dt.time() < self.close_dt