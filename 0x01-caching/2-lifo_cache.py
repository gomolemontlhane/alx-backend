#!/usr/bin/env python3
""" LIFO Cache Module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines a caching system using LIFO algorithm """

    def __init__(self):
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Assigns item to key in cache_data using LIFO """
        if key is not None and item is not None:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
               key not in self.cache_data):

                if self.last_key:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")
            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """ Returns the value in cache_data linked to key """
        return self.cache_data.get(key, None)
