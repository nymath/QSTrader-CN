from abc import ABCMeta, abstractmethod
import functools

class DataSource(object):
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    @functools.lru_cache(maxsize=1024 * 1024)
    def get_bid(self, dt, asset):
        raise NotImplementedError(
            "Should implement get_bid()"
        )
    
    @abstractmethod
    @functools.lru_cache(maxsize=1024 * 1024)
    def get_ask(self, dt, asset):
        raise NotImplementedError(
            "Should implement get_ask()"
        )
    
    @abstractmethod
    def get_asset_historical_values(self, start_dt, end_dt, assets, val_type):
        raise NotimplementedError(
            "Should implement get_asset_historical_values()"
        )