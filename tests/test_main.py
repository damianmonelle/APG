python
# arithmetic_operations.py

"""
This module contains functions for performing basic arithmetic operations and checking number properties.
"""

from enum import Enum
from math import sqrt
from typing import Union

class Operation(Enum):
    ADD = "add"
    MULTIPLY = "multiply"

def perform_operation(operation: Operation, first_number: Union[int, float], second_number: Union[int, float]) -> Union[int, float]:
    """
    Perform the specified arithmetic operation on two numbers

    Args:
        operation (Operation): The operation to perform
        first_number (Union[int, float]): The first number
        second_number (Union[int, float]): The second number

    Returns:
        Union[int, float]: The result of the operation
    """
    if operation == Operation.ADD:
        return first_number + second_number
    elif operation == Operation.MULTIPLY:
        return first_number * second_number
    else:
        raise ValueError(f"Unsupported operation: {operation}")

def is_even(number: int) -> bool:
    """
    Check if a number is even

    Args:
        number (int): The number to check

    Returns:
        bool: True if the number is even, False otherwise
    """
    return number % 2 == 0

def is_prime(number: int) -> bool:
    """
    Check if a number is prime

    Args:
        number (int): The number to check

    Returns:
        bool: True if the number is prime, False otherwise
    """
    if number < 2:
        return False
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += w
        w = 6 - w
    return True