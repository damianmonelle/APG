# This file contains unit tests for the main functionality of the application. It is located in the tests folder under the name test_main.py.

# Import necessary modules for testing
import unittest
from main import add, subtract, multiply, divide

class TestMainFunctions(unittest.TestCase):
    
    def test_add(self):
        result = add(3, 5)
        self.assertEqual(result, 8)
    
    def test_subtract(self):
        result = subtract(10, 5)
        self.assertEqual(result, 5)
    
    def test_multiply(self):
        result = multiply(4, 6)
        self.assertEqual(result, 24)
    
    def test_divide(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()

# This test file includes test cases for the add, subtract, multiply, and divide functions in the main.py file. Each test asserts the expected result against the actual result returned by the function. To run the tests, simply execute this file.