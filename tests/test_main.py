# arithmetic_operations.py

"""
This module contains functions for performing basic arithmetic operations and checking number properties.
"""

def calculate_sum(num1, num2):
    """
    Calculate the sum of two numbers

    Args:
    num1 (int or float): The first number
    num2 (int or float): The second number

    Returns:
    int or float: The sum of num1 and num2
    """
    return num1 + num2


def calculate_product(num1, num2):
    """
    Calculate the product of two numbers

    Args:
    num1 (int or float): The first number
    num2 (int or float): The second number

    Returns:
    int or float: The product of num1 and num2
    """
    return num1 * num2


def is_even(num):
    """
    Check if a number is even

    Args:
    num (int): The number to check

    Returns:
    bool: True if the number is even, False otherwise
    """
    return num % 2 == 0


def is_prime(num):
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
