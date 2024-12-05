python
import uuid
from typing import List, Union

# utils.py
# This file contains utility functions that can be reused in different parts of the codebase.

def calculate_average(numbers: Union[List[float], List[int]]) -> float:
    """
    Calculates the average of a list of numbers.

    Args:
        numbers: List of numbers.

    Returns:
        The average of the numbers.

    Raises:
        ValueError: If input is not a list or doesn't contain numbers only.
    """
    if not isinstance(numbers, list) or not all(isinstance(i, (int, float)) for i in numbers):
        raise ValueError("Input must be a list containing numbers only.")
        
    if not numbers:
        return 0.0

    return sum(numbers) / len(numbers)


def generate_unique_id(prefix: str = 'ID') -> str:
    """
    Generates a unique ID with a given prefix.

    Args:
        prefix: Prefix for the unique ID. Defaults to 'ID'.

    Returns:
        A unique ID.

    Raises:
        ValueError: If prefix is not a string.
    """
    if not isinstance(prefix, str):
        raise ValueError("Prefix must be a string.")

    return f'{prefix}_{uuid.uuid4().hex}'