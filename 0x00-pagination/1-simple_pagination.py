#!/usr/bin/env python3
"""Server class to paginate a database of popular baby names."""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of the start and end indexes
    for the given page and page size."""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a page of dataset."""
        assert isinstance(page, int) and page > 0, "positive integer only"
        assert isinstance(page_size, int) and page_size > 0, "positive only"

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):  # If start index is out of dataset range
            return []

        return dataset[start:end]
