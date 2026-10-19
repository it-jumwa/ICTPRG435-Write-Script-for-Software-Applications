"""
Name: Jaimee Molina
ID: 202514907
Date Created: 13-10-2026

Accepts 4 Windows commands from the user and executes them
Inputs are accepted via tkinter GUI
Results are displayed to the tkinter GUI
"""
from tkinter import *


def process():
    # TODO: Add functionality
    return


def clear():
    """
    Resets the result label text and clears the entry widgets
    :return: None
    """
    result.config(text="The product is: ")
    cmd1_entry.delete(0, "end")
    cmd2_entry.delete(0, "end")
    cmd3_entry.delete(0, "end")
    cmd4_entry.delete(0, "end")


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
window.title("Windows Command Executor")

# Sets the size of the application window
window.geometry("360x360")

# Blank Error Label
error = Label(text="Error: ...")

"""Command 1"""

cmd1_label = Label(window, text="Enter first Windows command: ", padx=10,
                   pady=10)
cmd1_label.pack()

cmd1_entry = Entry(window)
cmd1_entry.pack()

"""Command 2"""
cmd2_label = Label(window, text="Enter second Windows command: ", padx=10,
                   pady=10)
cmd2_label.pack()

cmd2_entry = Entry(window)
cmd2_entry.pack()

"""Command 3"""
cmd3_label = Label(window, text="Enter third Windows command: ")
cmd3_label.pack()

cmd3_entry = Entry(window)
cmd3_entry.pack()

"""Command 4"""
cmd4_label = Label(window, text="Enter fourth Windows command: ")
cmd4_label.pack()

cmd4_entry = Entry(window)
cmd4_entry.pack()


"""Result"""

# Creates a label widget
result = Label(window, text="The result is: ")
# Adds the label widget to the application window
result.pack()

"""Buttons"""

# Creates a button widget, for calculating the product
process_button = Button(window, text="Process", command=process)
# Adds the button widget to the application window
process_button.pack()

# Creates a button widget for
clear_button = Button(window, text="Clear", command=clear)
clear_button.pack()

# Creates a button widget, for closing the application
exit_button = Button(window, text="Exit", command=exit_button)
# Adds the button widget to the application window
exit_button.pack()

# Starts the event loop, keeping the window responsive
window.mainloop()
