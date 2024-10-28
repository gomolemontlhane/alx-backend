#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination."""

import csv
from typing import List, Dict
from 2-hypermedia_pagination import Server

class Server:
    """Server class for deletion-resilient pagination."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def indexed_dataset(self) -> Dict[int, List]:
        """Indexed dataset, truncated to the first 1000 entries."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """Returns data with deletion-resilient pagination."""
        assert 0 <= index < len(self.indexed_dataset())
        data = []
        next_index = index

        for _ in range(page_size):
            while next_index in self.indexed_dataset():
                data.append(self.indexed_dataset()[next_index])
                next_index += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
