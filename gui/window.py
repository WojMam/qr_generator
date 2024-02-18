""" This is a python module that has functions to generate window application
    view and it's various methods.
"""

import logging
import os
import platform
import subprocess
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

from utils.generator_utils import generate_qr_code_without_logo
from utils.results_utils import properties


def generate_qr_code_from_input(configs, input_field):
    """
    This method shows the popup window with welcoming message.
    """

    generate_qr_code_without_logo(configs, input_field, 'input')
    messagebox.showinfo("Message", "All QR codes were generated")

def open_results_dir():
    """
    This method opens results directory in system explorer.
    """

    path="./results"
    if platform.system() == "Windows":
        path = os.path.join(os.path.dirname(__file__), "../results")
        # Line below has to be disabled in pylint due to the lack of this method in Unix os
        # which the pylint is ran on.
        os.startfile(path) # pylint: disable=no-member
        logging.info('The results directory has been opened (windows)')
    elif platform.system() == "Darwin":
        with subprocess.Popen(["open", path]) as sub:
            logging.info('The results directory has been opened (linux): %s', sub.returncode)
    else:
        with subprocess.Popen(["xdg-open", path]) as sub:
            logging.info('The results directory has been opened (macOS): %s', sub.returncode)

def get_entry_value(entry_element):
    """
    This method returns the value of the given Entry element.

    Parameters:
    entry_element (): name of the tkinter Entry element

    Returns:
    str:Value of an entry element
    """

    current_value = entry_element.get()
    return current_value

def initialize_window():
    """
    This method create the main app window.
    """

    configs=properties()

    root = tk.Tk()
    root.title("QR generator")

    ico = Image.open('./resources/app_icon.png')
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)

    title_frame = tk.Frame(root, relief="raised", bd=2)
    title_label = tk.Label(title_frame, text="QR generator")
    title_label.pack()
    title_frame.pack(pady=10)
    label = tk.Label(title_frame, text="This is a simple application to generate QR codes.\n"+
                     "Use Generate button to start and Open Results to check your QR codes.")
    label.pack(pady=10)

    luczniczqa_webstie = tk.StringVar(value=configs.get("luczniczqa_website").data)

    input_frame = tk.Frame(root)
    label = tk.Label(input_frame, text="Data to encode:")
    label.pack()
    entry = tk.Entry(input_frame, textvariable=luczniczqa_webstie, width=50)
    entry.pack()
    input_frame.pack(pady=5)

    button_generate = tk.Button(root, text="Generate",
                                command=lambda:
                                    generate_qr_code_from_input(configs, get_entry_value(entry)))
    button_generate.pack(pady=5)

    button_open_results_dir = tk.Button(root, text="Open results", command=open_results_dir)
    button_open_results_dir.pack(pady=5)

    root.mainloop()
