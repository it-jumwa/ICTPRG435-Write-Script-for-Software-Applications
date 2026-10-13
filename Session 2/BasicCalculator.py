"""
Name: Jaimee Molina
ID: 202514907
Date Created: 13-10-2026

A calculator that can receives two values and can perform basic functions such
as add, subtract, multiplication and division. Inputs are accepted via tkinter
GUI. The result is also displayed to the GUI
"""
from tkinter import *

# TODO: Add input validation


def get_first_value():
    return float(first_value_entry.get())


def get_second_value():
    return float(second_value_entry.get())


def add():
    val1 = get_first_value()
    val2 = get_second_value()
    sum = val1 + val2
    add_result.config(text=f"Sum: {sum}")
    add_result.pack()
    return sum


def subtract():
    val1 = get_first_value()
    val2 = get_second_value()
    subtraction = val1 - val2
    subtract_result.config(text=f"Subtraction: {subtraction}")
    return subtraction


def multiply():
    val1 = get_first_value()
    val2 = get_second_value()
    product = val1 * val2
    product_result.config(text=f"Product: {product}")
    return product


def divide():
    val1 = get_first_value()
    val2 = get_second_value()
    division = val1 / val2
    division_result.config(text=f"Division: {division}")
    return division


def clear():
    """
    Resets the result label text and clears the entry widgets
    :return: None
    """
    first_value_entry.delete(0, "end")
    second_value_entry.delete(0, "end")
    add_result.config(text="Sum: ")
    subtract_result.config(text="Subtraction: ")
    product_result.config(text="Product: ")
    division_result.config(text="Division: ")


def exit_button():
    """
    Closes the application window
    :return: None
    """
    window.destroy()


"""Initialise Application"""

# Creates the main application window
window = Tk()

# Adds a title to the application window
window.title("Basic Calculator")

# Sets the size of the application window
window.geometry("360x360")


"""Value 1"""
first_value_label = Label(window, text="First Number: ")
first_value_label.pack()
first_value_entry = Entry(window)
first_value_entry.pack()

"""Value 2"""
second_value_label = Label(window, text="Second Number: ")
second_value_label.pack()
second_value_entry = Entry(window)
second_value_entry.pack()

"""Add Result"""
add_result = Label(window, text="Sum: ")
add_result.pack()

"""Subtraction Result"""
subtract_result = Label(window, text="Subtraction: ")
subtract_result.pack()

"""Product Result"""
product_result = Label(window, text="Product: ")
product_result.pack()

"""Division Result"""
division_result = Label(window, text="Division: ")
division_result.pack()

"""Buttons"""

add_button = Button(window, text="Add", command=add)
add_button.pack()

subtract_button = Button(window, text="Subtract", command=subtract)
subtract_button.pack()

multiply_button = Button(window, text="Multiply", command=multiply)
multiply_button.pack()

divide_button = Button(window, text="Divide", command=divide)
divide_button.pack()

# Creates a button widget for
clear_button = Button(window, text="Clear", command=clear)
clear_button.pack()

# Creates a button widget, for closing the application
exit_button = Button(window, text="Exit", command=exit_button)
# Adds the button widget to the application window
exit_button.pack()


# Blank Error Label
error = Label(text="Error: ...")

# Starts the event loop, keeping the app responsive
window.mainloop()
