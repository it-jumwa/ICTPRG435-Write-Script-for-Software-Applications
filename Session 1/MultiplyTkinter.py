"""
Name: Jaimee Molina
ID: 202514907
Date Created: 09-10-2026

Receives two values from the user and multiplies the two values together.
User input is accepted through tkinter GUI and validated prior to calculation.
"""
from tkinter import *


def calculate_product():
    """
    Calculates the product of two values and updates the result label text when
    the `Calculate` button is clicked

    :return: None
    """
    val1 = check_for_float_value(val1_entry.get())
    val2 = check_for_float_value(val2_entry.get())

    # If the input is invalid, do not calculate the product
    if (val1 is None) or (val2 is None):
        return

    # Hide the error label when inputs pass the validation checks
    error.pack_forget()

    # Calculate the product
    product = val1 * val2
    # Update the result label text
    if (product % 1) == 0:
        result.config(text="The product is: " + f"{product:.0f}")
    else:
        result.config(text="The product is: " + f"{product}")


def exit_button():
    """
    Closes the application window

    :return: None
    """
    window.destroy()


def clear():
    """
    Resets the result label text and clears the entry widgets

    :return: None
    """
    result.config(text="The product is: ")
    val1_entry.delete(0, "end")
    val2_entry.delete(0, "end")


def check_for_float_value(val: str):
    """
    Attempts to convert a string value to a float

    :param val: The string value to convert to a float
    :return: The value as a float if the conversion is successful, otherwise
    None.
    """
    try:
        # Attempts to convert the string input to a float
        val = float(val)
        return val
    # If the parameter can not be converted to a float
    except ValueError:
        # Prompt the user to enter a numeric value
        error.config(text="Enter a numeric value")
        error.pack()
        # Reset the result label
        result.config(text="The product is: ")
        return None


"""Initialise the application"""

# Creates the main application window
window = Tk()

# Adds a title to the application window
window.title("Calculate Product")

# Sets the size of the application window
window.geometry("360x360")

# Blank Error Label
error = Label(text="Error: ...")

"""Value 1"""

# Creates a text label
val1_label = Label(window, text="Enter first value: ")
# Adds the label to the application window
val1_label.pack()

# Creates an entry widget that accepts a single-line of text input from
# the user
val1_entry = Entry(window)
# Adds the entry widget to the application window
val1_entry.pack()

"""Value 2"""

# Creates a text label
val2_label = Label(window, text="Enter second value: ")
# Adds the label to the application window
val2_label.pack()

# Creates an entry widget that accepts a single-line of text input from
# the user
val2_entry = Entry(window)
# Adds the entry widget to the application window
val2_entry.pack()

"""Result"""

# Creates a label widget
result = Label(window, text="The product is: ")
# Adds the label widget to the application window
result.pack()

"""Buttons"""

# Creates a button widget, for calculating the product
calculate_button = Button(window, text="Calculate", command=calculate_product)
# Adds the button widget to the application window
calculate_button.pack()

# Creates a button widget for
clear_button = Button(window, text="Clear", command=clear)
clear_button.pack()

# Creates a button widget, for closing the application
exit_button = Button(window, text="Exit", command=exit_button)
# Adds the button widget to the application window
exit_button.pack()

# Starts the event loop, keeping the window responsive
window.mainloop()