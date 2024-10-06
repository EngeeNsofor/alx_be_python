#!/bin/python3

def safe_divide(numerator, denominator):
   
    try:
        # Convert the inputs to float
        num = float(numerator)
        denom = float(denominator)

        # Attempt division
        if denom == 0:
            return "Error: Cannot divide by zero."
        
        result = num / denom
        return f"The result of the division is {result:.2f}"

    except ValueError:
        # This will catch any non-numeric input error
        return "Error: Please enter numeric values only."
