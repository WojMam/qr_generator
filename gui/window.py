""" This is a python module that has functions to generate window application
    view and it's various methods.
"""

import os
import platform
import subprocess
import tkinter as tk
from tkinter import messagebox

from generator_utils import generate_qr_code_for_all_set
from results_utils import properties

def generate_all_qr_codes():
    """
    This method shows the popup window with welcoming message.
    """
    generate_qr_code_for_all_set(configs=properties())
    messagebox.showinfo("Message", "All QR codes were generated")

def open_results_dir():
    """
    This method opens results directory in system explorer.
    """
    path="./results"
    if platform.system() == "Windows":
        path = os.path.join(os.path.dirname(__file__), "../results")
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])

def initialize_window():
    """
    This method create the main app window.
    """
    root = tk.Tk()
    root.title("QR generator")

    label = tk.Label(root, text="Click the button to show a message box")
    label.pack(pady=10)

    button_generate = tk.Button(root, text="Generate", command=generate_all_qr_codes)
    button_generate.pack()

    button_open_results_dir = tk.Button(root, text="Open results", command=open_results_dir)
    button_open_results_dir.pack()

    root.mainloop()
