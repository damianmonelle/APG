python
# arithmetic_operations.py

"""
This module contains functions for performing basic arithmetic operations and checking number properties.
"""

from enum import Enum
from math import sqrt
from typing import Union

class Operation(Enum):
    """
    Enum for arithmetic operations
    """
    ADD = "add"
    MULTIPLY = "multiply"

# Move operations dictionary outside the function for better performance
OPERATIONS = {
    Operation.ADD: lambda x, y: x + y,
    Operation.MULTIPLY: lambda x, y: x * y
}

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
    if operation in OPERATIONS:
        return OPERATIONS[operation](first_number, second_number)
    else:
        raise ValueError(f"Unsupported operation: {operation}")

def _validate_integer_input(number: int):
    """
    Validate that the input is an integer

    Args:
        number (int): The number to validate

    Raises:
        ValueError: If the input is not an integer
    """
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")

def is_even(number: int) -> bool:
    """
    Check if a number is even

    Args:
        number (int): The number to check

    Returns:
        bool: True if the number is even, False otherwise
    """
    _validate_integer_input(number)
    return number % 2 == 0

def is_prime(number: int) -> bool:
    """
    Check if a number is prime

    Args:
        number (int): The number to check

    Returns:
        bool: True if the number is prime, False otherwise
    """
    _validate_integer_input(number)
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