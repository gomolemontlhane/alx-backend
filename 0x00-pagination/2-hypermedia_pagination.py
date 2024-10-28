#!/usr/bin/env python3
"""Server class with hypermedia pagination support."""

import csv
import math
from typing import List, Dict
from 1-simple_pagination import Server, index_range

class Server:
    """Server class to paginate a database of popular baby names with hypermedia metadata."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns hypermedia pagination dictionary."""
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
