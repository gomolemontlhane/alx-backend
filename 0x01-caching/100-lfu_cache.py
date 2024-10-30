#!/usr/bin/env python3
""" LFU Cache Implementation """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU Cache class that inherits from BaseCaching."""

    def __init__(self):
        """Initialize the LFU Cache."""
        super().__init__()
        self.usage_count = {}  # Dictionary to track usage count
        self.last_used = {}     # Dictionary to track the last used time

    def put(self, key, item):
        """Assign an item to a key in the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_count[key] += 1
            self.last_used[key] = self._current_time()
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Find the least frequently used item
            lfu_key = self._find_lfu_key()
            if lfu_key is not None:
                print(f"DISCARD: {lfu_key}")
                del self.cache_data[lfu_key]
                del self.usage_count[lfu_key]
                del self.last_used[lfu_key]

        # Insert the new item
        self.cache_data[key] = item
        self.usage_count[key] = 1
        self.last_used[key] = self._current_time()

    def get(self, key):
        """Return the value associated with a key."""
        if key is None or key not in self.cache_data:
            return None

        # Update usage count and last used time
        self.usage_count[key] += 1
        self.last_used[key] = self._current_time()
        return self.cache_data[key]

    def _find_lfu_key(self):
        """Find the key with the least frequency used."""
        if not self.cache_data:
            return None

        # Find the least frequently used items
        min_frequency = min(self.usage_count.values())
        lfu_candidates = [
            key for key, count in self.usage_count.items()
            if count == min_frequency
          ]

        # If there are ties, apply LRU policy
        if len(lfu_candidates) > 1:
            lru_key = min(lfu_candidates, key=lambda k: self.last_used[k])
            return lru_key
        return lfu_candidates[0]

    def _current_time(self):
        """Return the current time."""
        from time import time
        return time()
