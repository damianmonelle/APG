# arithmetic_operations.py

"""
This module contains functions for performing basic arithmetic operations and checking number properties.
"""

def add_two_numbers(first_number: float, second_number: float) -> float:
    """
    Calculate the sum of two numbers

    Args:
        first_number (float): The first number
        second_number (float): The second number

    Returns:
        float: The sum of first_number and second_number
    """
    return first_number + second_number


def multiply_two_numbers(first_number: float, second_number: float) -> float:
    """
    Calculate the product of two numbers

    Args:
        first_number (float): The first number
        second_number (float): The second number

    Returns:
        float: The product of first_number and second_number
    """
    return first_number * second_number


def check_if_even(number: int) -> bool:
    """
    Check if a number is even

    Args:
        number (int): The number to check

    Returns:
        bool: True if the number is even, False otherwise
    """
    return number % 2 == 0


def check_if_prime(number: int) -> bool:
    """
    Check if a number is prime

    Args:
        number (int): The number to check

    Returns:
        bool: True if the number is prime, False otherwise
    """
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Changes made:
# 1. Renamed function parameters to more descriptive names.
# 2. Added type hints to function signatures and return types for better readability and understanding of the function.
# 3. Consistent use of float for arithmetic operations to accommodate non-integer inputs.
# 4. Indented the docstrings properly.