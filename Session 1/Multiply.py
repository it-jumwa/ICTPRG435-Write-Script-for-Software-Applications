"""
Name: Jaimee Molina
ID: 202514907
Date Created: 1-10-2026

Receives two values from the user and multiplies the two values together.
The output is printed to the console.
"""
import utils

# Prompt the user to enter 2 values
number1 = utils.validate_input()
number2 = utils.validate_input()

# Multiply the 2 values together
result = number1 * number2

# Print the result
print(result)
