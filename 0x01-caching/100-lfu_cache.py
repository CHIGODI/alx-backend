#!/usr/bin/env python3
"""
Create a class LFUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the least frequency used item (LFU algorithm)
if you find more than 1 item to discard, you must use the LRU algorithm to discard only the least recently used
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""

from base_caching import BaseCaching
from collections import OrderedDict, defaultdict

class LFUCache(BaseCaching):
    """ MRUCache using the Most Recently Used caching algorithm """

    def __init__(self):
        """ Init """
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = defaultdict(int)
        self.freq_items = defaultdict(OrderedDict)

    def _evict_lfu(self):
        """ Evict the least frequently used item """
        # Find the lowest frequency
        min_freq = min(self.freq_items)
        # Find the oldest item within that frequency
        evict_key, _ = self.freq_items[min_freq].popitem(last=False)
        # Remove from the main cache
        del self.cache_data[evict_key]
        del self.frequency[evict_key]
        # If the frequency list is empty, remove it
        if not self.freq_items[min_freq]:
            del self.freq_items[min_freq]

    def get(self, key):
        """Retrieve an item from the cache."""
        if key not in self.cache_data:
            return None

        # Move the accessed item to the next frequency list
        freq = self.frequency[key]
        value = self.cache_data[key]

        # Remove the key from current frequency list
        self.freq_items[freq].pop(key)
        if not self.freq_items[freq]:
            del self.freq_items[freq]

        # Increment frequency and add to the new frequency list
        self.frequency[key] += 1
        self.freq_items[self.frequency[key]][key] = value

        return value

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the item and its frequency
            self.cache_data[key] = item
            self.get(key)  # To update the frequency
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self._evict_lfu()
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.freq_items[1][key] = item
