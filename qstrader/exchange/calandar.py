import pandas as pd
from pandas_market_calendars import get_calendar

class CalendarSS(object):
    calendar = get_calendar('SSE')
        
    def __init__(self, start_dt, end_dt):
        self.start_dt = start_dt
        self.end_dt = end_dt
        self.trade_dates = CalendarSS.create_calendar(self.start_dt, self.end_dt)
        
    @classmethod
    def create_calendar(cls, start_dt, end_dt):
        trade_dates = cls.calendar.valid_days(start_date=start_dt, end_date=end_dt)
        return trade_dates
    
    def get_his_trade_day(self, dt, N):
        return self.trade_days.shift(N, freq='D')[0]
