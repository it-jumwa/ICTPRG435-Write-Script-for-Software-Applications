"""
Name: Jaimee Molina
ID: 202514907
Date Created: 05-10-2026

Receives an hourly pay rate and hours worked from the user and calculates the
pay. The result is printed to the terminal.
"""
import os
import utils

# Clears the terminal
os.system("cls")


def receive_positive_float_input(prompt: str):
    """
    Prompts the user for an input using a provided message.
    The input is validated, checking that it is a positive float value

    :param prompt: The message to display when prompting the user for an input
    :return: The validated positive numeric value
    """
    while True:
        # Receive an input from the user, using a given prompt
        val = input(prompt)
        # Check if the input is a float value
        val = utils.check_for_float(val)

        # If the value is a float, check if it is a positive value
        if isinstance(val, float):
            val = utils.check_for_positive_value(val)
        # If the value is not a NoneType, return the value
        if val is not None:
            return val
        # Otherwise, iterate again


# Prompt the user to input an hourly rate
rate = receive_positive_float_input("Enter your hourly rate: ")

# Prompt the user to input hours worked
hours = receive_positive_float_input("Enter your hours worked: ")

# Calculate the pay
pay = rate * hours

# Output the pay to the user
print(f"\nHourly Rate: ${rate}\n"
      f"Hours Worked: {hours}\n"
      f"Calculated Pay: ${pay}")
