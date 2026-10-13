"""
Name: Jaimee Molina
ID: 202514907
Date Created: 13-10-2026

Calculates the cost of purchasing hard drives based on the number of hard drives
purchased and the cost of the hard drives. This application assumes that each
hard drive is the same price and one another. The application also accepts the
name of the customer.
Inputs are outputs are received and displayed via tkinter GUI
"""
from tkinter import *


def calculate():
    hard_drive_num = int(hard_drive_num_entry.get())
    cost = float(cost_entry.get())
    purchase_cost = hard_drive_num * cost
    customer = customer_entry.get()
    result.config(text=f"Customer: {customer}\nThe purchase cost is:"
                       f" {purchase_cost}")
    return purchase_cost


def clear():
    """
    Resets the result label text and clears the entry widgets
    :return: None
    """
    result.config(text="The product is: ")
    customer_entry.delete(0, "end")
    hard_drive_num_entry.delete(0, "end")
    cost_entry.delete(0, "end")


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
window.title("HardDrive Purchase")

# Sets the size of the application window
window.geometry("360x360")

# Blank Error Label
error = Label(text="Error: ...")

"""Customer Name"""

customer_label = Label(window, text="Enter Customer Name: ", padx=10, pady=10)
customer_label.pack()
customer_entry = Entry(window)
customer_entry.pack()

"""No. of HardDrives Purchase"""

hard_drive_num_label = Label(window, text="Enter number of hard drives "
                                          "purchased: ", padx=10, pady=10)
hard_drive_num_label.pack()
hard_drive_num_entry = Entry(window)
hard_drive_num_entry.pack()

"""HardDrive Cost"""
cost_label = Label(window, text="Enter hard drive cost", padx=10, pady=10)
cost_label.pack()
cost_entry = Entry(window)
cost_entry.pack()


"""Result"""

# Creates a label widget
result = Label(window, text="The purchase cost is: ", padx=10, pady=10)
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