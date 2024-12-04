# utils.py

# This file contains utility functions that can be reused in different parts of the codebase.

from typing import List
import uuid

def calculate_average(numbers: List[float]) -> float:
    """
    Calculate the average of a list of numbers.

    :param numbers: List of numbers
    :return: Average of the numbers
    """
    if not numbers:
        return 0.0

    return sum(numbers) / len(numbers)


def generate_unique_id(prefix: str = 'ID') -> str:
    """
    Generate a unique ID with a given prefix.

    :param prefix: Prefix for the unique ID
    :return: Unique ID
    """
    return f'{prefix}_{uuid.uuid4().hex}'
  
# As per best practices, import statements are always at the top of the file. 
# Also, added type hinting for function parameters and return types for better understanding and readability of the code. 
# For calculate_average function, if the numbers list is empty, it returns 0.0 instead of 0 for consistency, as the function is expected to return a float.