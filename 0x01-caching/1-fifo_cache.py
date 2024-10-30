#!/usr/bin/env python3
""" FIFO Cache Module """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines a caching system using FIFO algorithm """

    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Assigns item to key in cache_data using FIFO """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded = self.order.pop(0)
                del self.cache_data[discarded]
                print(f"DISCARD: {discarded}")
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Returns the value in cache_data linked to key """
        return self.cache_data.get(key, None)
