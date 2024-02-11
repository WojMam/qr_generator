""" This is a python module that has functions to generate window application
    view and it's various methods.
"""

import tkinter as tk
from tkinter import messagebox

def show_message_box():
    """
    This method shows the popup window with welcoming message.
    """
    messagebox.showinfo("Message", "Hello, this is a message box!")

def initialize_window():
    """
    This method create the main app window.
    """
    root = tk.Tk()
    root.title("Simple Window App")

    label = tk.Label(root, text="Click the button to show a message box")
    label.pack(pady=10)

    button = tk.Button(root, text="Click Me!", command=show_message_box)
    button.pack()

    root.mainloop()
