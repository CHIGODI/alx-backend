#!/usr/bin/env python3
"""
Create a class LRUCache that inherits from BaseCaching and is a caching system:
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRUCache using the Least Recently Used caching algorithm """

    def __init__(self):
        """ Init """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache."""
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update item and move it to the end to mark it
                # as recently used
                self.cache_data.move_to_end(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Pop the oldest item (least recently used)
                oldest_key, _ = self.cache_data.popitem(last=False)
                print(f'DISCARD: {oldest_key}')

    def get(self, key):
        """Retrieve an item from the cache."""
        if key is not None and key in self.cache_data:
            # Move the accessed item to the end to mark it as recently used
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
