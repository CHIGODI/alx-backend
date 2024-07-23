#!/usr/bin/env pyhon3
"""
Create a class LRUCache that inherits from BaseCaching and is a caching system:
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LLRUCache """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache."""
        if key is not None and item is not None:
            if key in self.cache_data:
                # IF the key exists move it to the end as
                # the recntly accessed
                self.cache_data.move_to_end(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                oldest_key, oldest_item = self.cache_data.popitem(last=False)
                print(f'DISCARD: {oldest_key}')

    def get(self, key):
        """ get key from cache """
        if key in self.cache_data and key is not None:
            return self.cache_data[key]
        else:
            return None
