```python
import uuid
from typing import List, Union

def calculate_average(numbers: List[Union[float, int]]) -> float:
    """
    Calculate the average of a list of numbers.

    Parameters:
    numbers (List[Union[float, int]]): List of numbers.

    Returns:
    float: The average of the numbers.

    Raises:
    ValueError: If the input is not a list or doesn't contain only numbers.
    """
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list.")
    if not all(isinstance(i, (int, float)) for i in numbers):
        raise ValueError("List must contain numbers only.")
    if not numbers:
        return 0.0

    return sum(numbers) / len(numbers)


def generate_unique_id(prefix: str = 'ID') -> str:
    """
    Generate a unique ID with a given prefix.

    Parameters:
    prefix (str): Prefix for the unique ID. Defaults to 'ID'.

    Returns:
    str: A unique ID.
    """
    return f'{prefix}_{uuid.uuid4().hex}'
```