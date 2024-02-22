""" This is a python module that has functions to generate window application
    view and it's various methods.
"""

import logging
import os
import platform
import subprocess
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import customtkinter
from PIL import Image, ImageTk

from utils.generator_utils import decode_qr_code, generate_qr_code_without_logo
from utils.results_utils import properties

customtkinter.set_appearance_mode(
    "System"
)  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):  # pylint: disable=too-many-instance-attributes
    """Class representing an app window"""

    def __init__(self):
        super().__init__()

        configs = properties()
        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1100}x{580}")

        ico = Image.open("./resources/app_icon.png")
        photo = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(False, photo)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame,
            text="CustomTkinter",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(
            self.sidebar_frame, text="Results", command=self.open_results_dir
        )
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Appearance Mode:", anchor="w"
        )
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="UI Scaling:", anchor="w"
        )
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=self.change_scaling_event,
        )
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.tabview.add("Generate").grid_columnconfigure(0, weight=1)
        self.tabview.add("Encode").grid_columnconfigure(0, weight=1)

        # create decode entry and button
        self.entry_decode = customtkinter.CTkEntry(
            self.tabview.tab("Generate"), placeholder_text="Data to decode as QR code"
        )
        self.entry_decode.grid(
            row=1, column=0, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew"
        )

        self.button_decode = customtkinter.CTkButton(
            master=self.tabview.tab("Generate"),
            fg_color="transparent",
            border_width=2,
            text="Decode",
            text_color=("gray10", "#DCE4EE"),
            command=lambda: self.generate_qr_code_from_input(
                configs, self.get_entry_value(self.entry_decode)
            ),
        )
        self.button_decode.grid(
            row=1, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew"
        )

        # create encode entry and button
        self.label_encode = customtkinter.CTkLabel(
            self.tabview.tab("Encode"), text="..."
        )
        self.label_encode.grid(
            row=1, column=0, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew"
        )

        self.button_encode = customtkinter.CTkButton(
            master=self.tabview.tab("Encode"),
            fg_color="transparent",
            border_width=2,
            text="Decode",
            text_color=("gray10", "#DCE4EE"),
            command=lambda: self.open_file(self.label_encode),
        )
        self.button_encode.grid(
            row=1, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew"
        )

        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

    def generate_qr_code_from_input(self, configs, input_field):
        """
        This method shows the popup window with welcoming message.

        Parameters:
        configs (): Object with all the parameters set in the project configuration file
        input_field (): name of the tkinter Entry element
        """

        generate_qr_code_without_logo(configs, input_field, "input")
        messagebox.showinfo("Message", "All QR codes were generated")

    def open_results_dir(self):
        """
        This method opens results directory in system explorer.
        """

        path = "./results"
        if platform.system() == "Windows":
            path = os.path.join(os.path.dirname(__file__), "../results")
            # Line below has to be disabled in pylint due to the lack of this method in Unix os
            # which the pylint is ran on.
            os.startfile(path)  # pylint: disable=no-member
            logging.info("The results directory has been opened (windows)")
        elif platform.system() == "Darwin":
            with subprocess.Popen(["open", path]) as sub:
                logging.info(
                    "The results directory has been opened (linux): %s", sub.returncode
                )
        else:
            with subprocess.Popen(["xdg-open", path]) as sub:
                logging.info(
                    "The results directory has been opened (macOS): %s", sub.returncode
                )

    def get_entry_value(self, entry_element):
        """
        This method returns the value of the given Entry element.

        Parameters:
        entry_element (): name of the tkinter Entry element

        Returns:
        str:Value of an entry element
        """

        current_value = entry_element.get()
        return current_value

    def open_file(self, label_to_update):
        """
        This method updates the Label element with the filename of the choosen file.

        Parameters:
        label_to_update (): name of the tkinter Label element that should be updated
        """

        file_path = askopenfilename(
            filetypes=[("Image Files", "*jpeg"), ("Image Files", "*png")]
        )
        if file_path is not None:
            label_to_update.configure(text=decode_qr_code(file_path))

    def change_appearance_mode_event(self, new_appearance_mode: str):
        """
        This method updates the appearance of the GUI.

        Parameters:
        new_appearance_mode (string): name of style/mode that GUI should be updated by.
        """

        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        """
        This method updates the scale of the GUI.

        Parameters:
        new_scaling (string): value of scale that GUI should be updated by.
        """

        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
