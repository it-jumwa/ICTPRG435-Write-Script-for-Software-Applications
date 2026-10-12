"""
Name: Jaimee Molina
ID: 202514907
Date Created: 12-10-2026

This is a program that receives 2 values from the user via Tkinter GUI
The product and the modulus of the 2 values are calculated and displayed
on the GUI.
"""
from tkinter import *


def calculate():
    val1 = float(val1_entry.get())
    val2 = float(val2_entry.get())

    product = val1 * val2
    first_modulus = val1 % val2
    second_modulus = val2 % val1

    product_label.config(text=f"Product: {product}")
    first_modulus_label.config(text=f"Modulo 1 (Value 1 % Value 2): "
                                    f"{first_modulus}")
    second_modulus_label.config(text=f"Modulu 2 (Value 2 % Value 1): "
                                     f"{second_modulus}")
    return


def clear():
    """
    Resets the result label text and clears the entry widgets
    :return: None
    """
    product_label.config(text="Product: ")
    first_modulus_label.config(text="Modulo 1 (Value 1 % Value 2): ")
    second_modulus_label.config(text="Modulu 2 (Value 2 % Value 1): ")
    val1_entry.delete(0, "end")
    val2_entry.delete(0, "end")


def exit_button():
    """
    Closes the application window
    :return: None
    """
    window.destroy()


"""Initialise the application"""

# Creates the main application window
window = Tk()

# Adds a title to the application window
window.title("Calculate Product and Modulus")

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

# Product
product_label = Label(window, text="Product: ")
# Adds the label widget to the application window
product_label.pack()

first_modulus_label = Label(window, text="Modulo 1 (Value 1 % Value 2): ")
first_modulus_label.pack()

second_modulus_label = Label(window, text="Modulu 2 (Value 2 % Value 1): ")
second_modulus_label.pack()

"""Buttons"""

# Creates a button widget, for calculating the product
calculate_button = Button(window, text="Calculate", command=calculate)
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
