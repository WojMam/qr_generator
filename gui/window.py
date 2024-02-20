""" This is a python module that has functions to generate window application
    view and it's various methods.
"""

import logging
import os
import platform
import subprocess
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import customtkinter
import tkinterDnD
from PIL import Image, ImageTk

from utils.generator_utils import decode_qr_code, generate_qr_code_without_logo
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

def open_file(label_to_update):
    """
    This method updates the Label element with the filename of the choosen file.

    Parameters:
    label_to_update (): name of the tkinter Label element that should be updated
    """

    file_path = askopenfilename(filetypes=[('Image Files', '*jpeg'), ('Image Files', '*png')])
    if file_path is not None:
        label_to_update.configure(text = decode_qr_code(file_path))

def initialize_window():
    """
    This method create the main app window.
    """

    configs=properties()

    customtkinter.set_ctk_parent_class(tkinterDnD.Tk)

    customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

    # root = tk.Tk()
    root = customtkinter.CTk()
    root.title("QR generator")
    root.geometry("600x580")

    ico = Image.open('./resources/app_icon.png')
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)

    title_frame = customtkinter.CTkFrame(root)
    title_label = customtkinter.CTkLabel(title_frame, text="QR generator")
    title_label.pack()
    title_frame.pack(pady=10)
    label = customtkinter.CTkLabel(title_frame,
                     text="This is a simple application to generate QR codes.\n"+
                     "Use Generate button to start and Open Results to check your QR codes.")
    label.pack(pady=10)

    luczniczqa_webstie = tk.StringVar(value=configs.get("luczniczqa_website").data)

    input_frame = customtkinter.CTkFrame(root)
    label = customtkinter.CTkLabel(input_frame, text="Data to encode:")
    label.pack()
    entry = customtkinter.CTkEntry(input_frame, textvariable=luczniczqa_webstie, width=400)
    entry.pack()
    input_frame.pack(pady=5)

    button_generate = customtkinter.CTkButton(root, text="Generate",
                                command=lambda:
                                    generate_qr_code_from_input(configs, get_entry_value(entry)))
    button_generate.pack(pady=5)

    button_open_results_dir = customtkinter.CTkButton(root, text="Open results",
                                                      command=open_results_dir)
    button_open_results_dir.pack(pady=5)

    file_upload_label = customtkinter.CTkLabel(
        root,
        text='QR code image to encode: '
        )
    file_upload_label.pack(pady=5)

    file_upload_button = customtkinter.CTkButton(
        root,
        text ='Choose File',
        command = lambda:open_file(file_upload_results_label)
        )
    file_upload_button.pack(pady=5)

    file_upload_results_label = customtkinter.CTkLabel(
        root,
        text='...'
        )
    file_upload_results_label.pack(pady=5)

    root.mainloop()
