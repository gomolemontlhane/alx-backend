#!/usr/bin/env python3
"""Simple helper function to calculate the range of indexes for pagination."""


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple containing a start index
    and an end index for pagination."""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
