"""
Name: Jaimee Molina
ID: 202514907
Date Created: 12-10-2026

Receives an hourly pay rate and hours worked from the user and calculates the
pay. User input is accepted and results are displayed through tkinter GUI.
"""
from tkinter import *


def calculate_pay():
    hourly_rate = validate_hourly_rate(rate_entry.get())
    hours_worked = validate_hours_worked(hours_entry.get())

    # If the input is invalid, do not calculate the pay
    if hourly_rate is None:
        return
    elif hours_worked is None:
        return

    # Hide the error label when inputs pass the validation checks
    rate_error.pack_forget()
    hours_error.pack_forget()

    # Calculate the pay
    pay = hourly_rate * hours_worked
    # Update the result label text
    result.config(text="Your calculated pay is: " + f"{pay}")


def check_for_integer(val):
    """
    Checks whether a value can be converted to an integer

    :param val: The numeric value to check
    :return: Returns the value as an integer if it is a whole number, otherwise
    returns None
    """
    try:
        # If the value has decimals, return None
        # The modulo operator, %, returns the remainder after dividing a value
        val = float(val)
        if (val % 1) == 0:
            return int(val)
    except ValueError:
        return
    except TypeError:
        # Reset the result label
        result.config(text="Your calculated pay is: ")
        return None


def check_for_float(val):
    """
    Attempts to convert a value to a float

    :param val: The value to convert to a float
    :return: Returns the value as a float, otherwise None
    """
    # Attempt to convert the value to a float data type
    try:
        return float(val)
    except ValueError:
        # Reset the result label
        result.config(text="Your calculated pay is: ")
        # If the input is NaN, return None
        return None


def check_for_positive_value(val):
    """
    Checks whether a value is greater than or equal to 0

    :param val: The numeric value to check
    :return: Returns the value if it is greater than 0, otherwise returns None
    """
    if val > 0:
        return val
    else:
        return None


def validate_hourly_rate(val):
    val = check_for_integer(val)

    if val is None:
        rate_error.config(text="Hourly Rate: Enter an integer value")
        rate_error.pack()
        return
    else:
        val = check_for_positive_value(val)
        if val is None:
            rate_error.config(text="Hourly Rate: Enter a positive value")
            rate_error.pack()
            return
        else:
            rate_error.pack_forget()
            return val


def validate_hours_worked(val):
    val = check_for_float(val)

    if val is None:
        hours_error.config(text="Hours Worked: Enter a numeric value")
        hours_error.pack()
        return
    else:
        val = check_for_positive_value(val)
        if val is None:
            hours_error.config(text="Hours Worked: Enter a positive value")
            hours_error.pack()
        else:
            hours_error.pack_forget()
            return val


def close_window():
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
    result.config(text="Your calculated pay is: ")
    rate_entry.delete(0, "end")
    hours_entry.delete(0, "end")
    rate_error.pack_forget()
    hours_error.pack_forget()


"""Initialise the application"""

# Creates the main application window
window = Tk()

# Adds a title to the application window
window.title("Calculate Pay")

# Sets the size of the application window
window.geometry("360x360")

# Blank Error Labels
rate_error = Label(window)
hours_error = Label(window)

"""Hourly Rate"""

# Creates a text label
rate_label = Label(window, text="Enter your hourly rate: ")
# Adds the label to the application window
rate_label.pack()

# Creates an entry widget that accepts a single-line of text input from
# the user
rate_entry = Entry(window)
# Adds the entry widget to the application window
rate_entry.pack()

"""Hours Worked"""

# Creates a text label
hours_label = Label(window, text="Enter your hours worked: ")
# Adds the label to the application window
hours_label.pack()

# Creates an entry widget that accepts a single-line of text input from
# the user
hours_entry = Entry(window)
# Adds the entry widget to the application window
hours_entry.pack()

"""Result"""

# Creates a label widget
result = Label(window, text="Your calculated pay is: ")
# Adds the label widget to the application window
result.pack()

"""Buttons"""

# Creates a button widget, for calculating the product
calculate_button = Button(window, text="Calculate", command=calculate_pay)
# Adds the button widget to the application window
calculate_button.pack()

# Creates a button widget for
clear_button = Button(window, text="Clear", command=clear)
clear_button.pack()

# Creates a button widget, for closing the application
exit_button = Button(window, text="Exit", command=close_window)
# Adds the button widget to the application window
exit_button.pack()

# Starts the event loop, keeping the window responsive
window.mainloop()
