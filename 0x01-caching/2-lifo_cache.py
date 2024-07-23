#!/usr/bin/env python3
"""
Creates a class LIFOCache that inherits from BaseCaching and
is a caching system:
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Class LIFOCache """
    def __init__(self):
        """ Init """
        super().__init__()

    def put(self, key, item):
        """ add items to cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                cache_data_keys = list(self.cache_data.keys())
                self.cache_data.pop(cache_data_keys[-1])
                print(f'DISCARD: {cache_data_keys[-1]}')
            self.cache_data[key] = item

    def get(self, key):
        """ get key from cache """
        if key in self.cache_data and key is not None:
            return self.cache_data[key]
        else:
            return None
