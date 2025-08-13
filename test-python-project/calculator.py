"""
Test Python Project for COAI Functionality Testing
This project contains various Python files with intentional issues for testing:
- Bug scenarios for debugging assistance
- Code that needs review and optimization
- Documentation gaps
- Multi-file dependencies
"""

# Main calculator module with some bugs and improvement opportunities
import math
from typing import List, Optional

class Calculator:
    """A simple calculator with various mathematical operations"""
    
    def __init__(self):
        self.history = []
        self.memory = 0
    
    def add(self, a, b):
        # Missing type hints and docstring
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def divide(self, a, b):
        # Bug: No zero division check
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, base, exponent):
        # Could be optimized and needs error handling
        if exponent == 0:
            return 1
        result = 1
        for i in range(exponent):
            result *= base
        return result
    
    def factorial(self, n):
        # Inefficient recursive implementation, could cause stack overflow
        if n == 0:
            return 1
        return n * self.factorial(n - 1)
    
    def get_statistics(self, numbers):
        # Missing error handling for empty list
        total = sum(numbers)
        average = total / len(numbers)
        return {
            "sum": total,
            "average": average,
            "min": min(numbers),
            "max": max(numbers),
            "count": len(numbers)
        }
    
    def store_memory(self, value):
        self.memory = value
    
    def recall_memory(self):
        return self.memory
    
    def clear_history(self):
        self.history = []
    
    def get_history(self):
        return self.history.copy()

# Example usage with potential issues
if __name__ == "__main__":
    calc = Calculator()
    
    # This will work fine
    print(calc.add(5, 3))
    
    # This will crash - division by zero
    # print(calc.divide(10, 0))
    
    # This might be slow for large numbers
    print(calc.factorial(5))
    
    # This will crash - empty list
    # print(calc.get_statistics([]))
    
    print("Calculator history:", calc.get_history())
