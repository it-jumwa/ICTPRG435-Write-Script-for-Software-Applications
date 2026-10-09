"""
Name: Jaimee Molina
ID: 202514907
Date Created: 06-10-2026

This is a program that receives 2 values from the user. The values are validated
to be integers. The product and the modulus of the 2 values are calculated and
printed to the terminal.
"""
import os

os.system("cls")


def receive_integer_value():
    while True:
        val = input("Enter a value: ")

        try:
            return int(val)
        except ValueError:
            print("Not a Number\n")


value1 = receive_integer_value()
value2 = receive_integer_value()

product = value1 * value2
# TODO: Add error handling for ZeroDivisionError
modulo1 = value1 % value2
modulo2 = value2 % value1

print(f"\nValue 1: {value1}\n"
      f"Value 2: {value2}\n"
      f"Product: {product}\n"
      f"Modulo 1 ({value1} % {value2}): {modulo1}\n"
      f"Modulo 2 ({value2} % {value1}): {modulo2}\n")
