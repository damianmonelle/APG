# Placeholder for utils.py

# Add your implementation here.

# This file will contain utility functions that can be reused in different parts of the codebase.

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    :param numbers: List of numbers
    :return: Average of the numbers
    """
    if not numbers:
        return 0

    total = sum(numbers)
    average = total / len(numbers)
    return average

def generate_unique_id(prefix='ID'):
    """
    Generate a unique ID with a given prefix.

    :param prefix: Prefix for the unique ID
    :return: Unique ID
    """
    import uuid
    return f'{prefix}_{uuid.uuid4().hex}'