#!/bin/python3

def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs a specified arithmetic operation on two numbers.

    Parameters:
    - num1 (float): The first number.
    - num2 (float): The second number.
    - operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
    - float or str: The result of the operation, or a specific message for division by zero.
    """
    operation = operation.lower() # converting the string to lowercase characters

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error! Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'."

