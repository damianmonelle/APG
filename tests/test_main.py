# This is a placeholder for the test_main.py file

# Add your implementation code below

# This function calculates the sum of two numbers
def calculate_sum(num1, num2):
    return num1 + num2

# This function calculates the product of two numbers
def calculate_product(num1, num2):
    return num1 * num2

# This function determines if a number is even
def is_even(num):
    return num % 2 == 0

# This function determines if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True