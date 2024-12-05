python
# utils.py

# This file contains utility functions that can be reused in different parts of the codebase.

from typing import List, Union
import uuid

def calculate_average(numbers: Union[List[float], List[int]]) -> float:
    """
    Calculate the average of a list of numbers.

    :param numbers: List of numbers
    :return: Average of the numbers
    :raises ValueError: If input is not a list or doesn't contain numbers only
    """
    if not isinstance(numbers, list) or not all(isinstance(i, (int, float)) for i in numbers):
        raise ValueError("Input must be a list of numbers")
        
    if not numbers:
        return 0.0

    return sum(numbers) / len(numbers)


def generate_unique_id(prefix: str = 'ID') -> str:
    """
    Generate a unique ID with a given prefix.

    :param prefix: Prefix for the unique ID
    :return: Unique ID
    :raises ValueError: If prefix is not a string
    """
    if not isinstance(prefix, str):
        raise ValueError("Prefix must be a string")

    return f'{prefix}_{uuid.uuid4().hex}'