#!/usr/bin/env python3
""" Basic Cache Module """

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache defines a basic caching system without limit """

    def put(self, key, item):
        """ Assigns item to key in cache_data """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value in cache_data linked to key """
        return self.cache_data.get(key, None)
