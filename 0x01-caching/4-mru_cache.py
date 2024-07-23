#!/usr/bin/env pyhon3
"""
Create a class MRUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the most recently used item (MRU algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""

from base_caching import BaseCaching
from collections import OrderedDict

class MRUCache(BaseCaching):
    """ MRUCache using the Most Recently Used caching algorithm """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()  # Use OrderedDict to maintain access order

    def put(self, key, item):
        """Add an item to the cache."""
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update item and move it to the end to mark it as recently used
                self.cache_data.move_to_end(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Pop the most recently used item (last item)
                most_recent_key, _ = self.cache_data.popitem(last=True)
                print(f'DISCARD: {most_recent_key}')

    def get(self, key):
        """Retrieve an item from the cache."""
        if key is not None and key in self.cache_data:
            # Move the accessed item to the end to mark it as recently used
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
