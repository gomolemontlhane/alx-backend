#!/usr/bin/env python3
""" MRU Cache Module """

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """ MRUCache defines a caching system using MRU algorithm """

    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Assigns item to key in cache_data using MRU """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded = self.order.pop()
                del self.cache_data[discarded]
                print(f"DISCARD: {discarded}")
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Returns the value in cache_data linked to key and updates usage """
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
        return self.cache_data.get(key, None)
