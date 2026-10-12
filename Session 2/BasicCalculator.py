"""
Name: Jaimee Molina
ID: 202514907
Date Created: xx-xx-2026

A calculator that can receives two values and can perform basic functions such
as add, subtract, multiplication and division. Inputs are accepted via tkinter
GUI. The result is also displayed to the GUI
"""
from tkinter import *

"""
Pseudocode

Start Program
 - Receive first value
 - Receive second value
 - If `Add` button is clicked
   - Sum the two values together
 - If the `Subtract` button is clicked
   - Subtract the second value from the first value
   - Display the result
 - If the `Multiply` button is clicked
   - Multiply both values together
   - Display the result
 - If the `Division` button is clicked
   - Divide the first value by the second value
   - Display the result
 - If the `Clear` button is clicked
   - Clear the entry boxes
   - Reset the result label
 - If the `Exit` button is clicked
   - Exit the application
End Program
"""
# TODO: Remove pseudocode


def calculate():
# TODO: Add back-end calculation
    return


def clear():
    """
    Resets the result label text and clears the entry widgets
    :return: None
    """
    result.config(text="The product is: ")
    val1_entry.delete(0, "end")


def exit_button():
    """
    Closes the application window
    :return: None
    """
    window.destroy()


def input_validation(val: str):
    # TODO: Add input validation
    return


"""Initialise the application"""

# Creates the main application window
window = Tk()

# Adds a title to the application window
window.title("App Window Title")
# TODO: Add app window title

# Sets the size of the application window
window.geometry("360x360")
# TODO: Scale window appropriately

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
result = Label(window, text="The result is: ")
# Adds the label widget to the application window
result.pack()

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
