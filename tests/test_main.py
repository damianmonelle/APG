```python
from enum import Enum
from typing import Union

class Operation(Enum):
    ADD = "add"
    MULTIPLY = "multiply"

OPERATIONS = {
    Operation.ADD: lambda x, y: x + y,
    Operation.MULTIPLY: lambda x, y: x * y
}

def perform_operation(operation: Operation, first_number: Union[int, float], second_number: Union[int, float]) -> Union[int, float]:
    if operation not in OPERATIONS:
        raise ValueError(f"Unsupported operation: {operation}")
    return OPERATIONS[operation](first_number, second_number)

def _validate_integer_input(number: int):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")

def is_even(number: int) -> bool:
    _validate_integer_input(number)
    return number % 2 == 0

def is_prime(number: int) -> bool:
    _validate_integer_input(number)
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
```