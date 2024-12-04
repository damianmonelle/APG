# arithmetic_operations.py

"""
This module contains functions for performing basic arithmetic operations and checking number properties.
"""

def add_numbers(num1: float, num2: float) -> float:
    """
    Calculate the sum of two numbers

    Args:
    num1 (float): The first number
    num2 (float): The second number

    Returns:
    float: The sum of num1 and num2
    """
    return num1 + num2


def multiply_numbers(num1: float, num2: float) -> float:
    """
    Calculate the product of two numbers

    Args:
    num1 (float): The first number
    num2 (float): The second number

    Returns:
    float: The product of num1 and num2
    """
    return num1 * num2


def is_even(num: int) -> bool:
    """
    Check if a number is even

    Args:
    num (int): The number to check

    Returns:
    bool: True if the number is even, False otherwise
    """
    return num % 2 == 0


def is_prime(num: int) -> bool:
    """
    Check if a number is prime

    Args:
    num (int): The number to check

    Returns:
    bool: True if the number is prime, False otherwise
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Changes made:
# 1. Changed function names to more descriptive ones.
# 2. Added type hints to function signatures and return types for better readability and understanding of the function.
# 3. Consistent use of float for arithmetic operations to accommodate non-integer inputs.