# test_main.py

# This file contains functions for performing basic arithmetic operations and checking number properties

# This function calculates the sum of two numbers
def calculate_sum(num1, num2):
    """
    Calculate the sum of two numbers

    Args:
    num1 (int): The first number
    num2 (int): The second number

    Returns:
    int: The sum of num1 and num2
    """
    return num1 + num2

# This function calculates the product of two numbers
def calculate_product(num1, num2):
    """
    Calculate the product of two numbers

    Args:
    num1 (int): The first number
    num2 (int): The second number

    Returns:
    int: The product of num1 and num2
    """
    return num1 * num2

# This function determines if a number is even
def is_even(num):
    """
    Check if a number is even

    Args:
    num (int): The number to check

    Returns:
    bool: True if the number is even, False otherwise
    """
    return num % 2 == 0

# This function determines if a number is prime
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