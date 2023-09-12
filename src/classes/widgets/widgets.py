#-*- coding: utf-8 -*-
"""This module contains the Widgets class which contains methods associated with
various Tkinter widgets as well as a mapping of widgets to their string keys. This
allows for easy reference of widgets. Also see the "widgets_creation_methods.py" and
"widgets_helper_methods.py" modules for additional methods associated with widgets."""

from traceback import format_exception

import classes

import methods.widgets.methods_widgets_creation as methods_creation
import methods.widgets.methods_widgets_helper as methods_helper

# Time Stamper: Run a timer and write automatically timestamped notes.
# Copyright (C) 2022 Benjamin Fertig

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Contact: github.cqrde@simplelogin.com


class Widgets():
    """This class contains methods associated with various Tkinter widgets as
    well as a mapping of widgets to their string keys. Widgets can be referenced
    based on their string keys. For example, to access the pause button, one would
    reference Widgets["button_pause"]. Also see the "methods_widgets_creation.py" and
    "methods_widgets_helper.py" modules for additional methods associated with widgets."""

    def __init__(self):

        self.original_colors = {}

        self.mapping = {}

    def __getitem__(self, item):
        return self.mapping[item]

    def report_callback_exception(self, *args):
        """This function replaces the default
        report_callback_exception function for the root window."""

        error_message = format_exception(*args)
        classes.template["text_error"]["text"] = error_message
        self.create_entire_window("window_error")

    def create_widgets(self, window_str):
        """This method creates all of the widgets that are meant
        to appear in the window indicated by window_str."""

        self.create_extra_images()
        self.create_buttons(window_str)
        self.create_checkbuttons(window_str)
        self.create_comboboxes(window_str)
        self.create_entries(window_str)
        self.create_labels(window_str)
        self.create_menus(window_str)
        self.create_scales(window_str)
        self.create_spinboxes(window_str)
        self.create_texts(window_str)

    def create_extra_images(self):
        """Some Tkinter image objects need to be created even if they are not immediately
        displayed. Create those images here so that they can be referenced later (if needed)."""

        extra_image_file_names = ("blank.png", "rewind_half.png", "fast_forward_half.png", \
            "volume_medium.png", "volume_low.png", "volume_zero.png", "volume_mute.png")

        for image_file_name in extra_image_file_names:
            extra_image = methods_helper.create_image(image_file_name=image_file_name)
            self.mapping[image_file_name] = extra_image

    def create_buttons(self, window_str):
        """This method creates all of the buttons that are meant
        to appear in the window indicated by window_str."""

        for button_template in classes.template["buttons"][window_str]:
            str_key = button_template["str_key"]
            button, button_image, button_orig_color = \
                methods_creation.create_button(button_template, self[window_str])
            button.image = button_image
            self.original_colors[str_key] = button_orig_color
            if button_image:
                self.mapping[button_template["image_file_name"]] = button_image
            self.mapping[str_key] = button

    def create_checkbuttons(self, window_str):
        """This method creates all of the checkbuttons that are
        meant to appear in the window indicated by window_str."""

        for checkbutton_template in classes.template["checkbuttons"][window_str]:
            checkbutton = \
                methods_creation.create_checkbutton(checkbutton_template, self[window_str])
            self.mapping[checkbutton_template["str_key"]] = checkbutton

    def create_comboboxes(self, window_str):
        """This method creates all of the comboboxes that are
        meant to appear in the window indicated by window_str."""

        for combobox_template in classes.template["comboboxes"][window_str]:
            combobox = methods_creation.create_combobox(combobox_template, self[window_str])
            self.mapping[combobox_template["str_key"]] = combobox

    def create_entries(self, window_str):
        """This method creates all of the entries that are meant
        to appear in the window indicated by window_str."""

        for entry_template in classes.template["entries"][window_str]:
            entry = methods_creation.create_entry(entry_template, self[window_str])
            self.mapping[entry_template["str_key"]] = entry

    def create_labels(self, window_str):
        """This method creates all of the labels that are meant
        to appear in the window indicated by window_str."""

        for label_template in classes.template["labels"][window_str]:
            label, label_image = methods_creation.create_label(label_template, self[window_str])
            if label_image:
                self.mapping[label_template["image_file_name"]] = label_image
            self.mapping[label_template["str_key"]] = label

    def create_menus(self, window_str):
        """This method creates all of the menus that are meant
        to appear in the window indicated by window_str."""

        # Only create a menu if any menus were specified for the current window.
        if window_str in classes.template["menus"]:

            menu_window = self[window_str]

            # Create the menubar.
            menubar = methods_creation.create_menubar(menu_window, window_str)
            self.mapping[f"menubar_{window_str}"] = menubar

            # Add the menu to the window.
            menu_window.config(menu=menubar)

    def create_scales(self, window_str):
        """This method creates all of the scales that are meant
        to appear in the window indicated by window_str."""

        for scale_template in classes.template["scales"][window_str]:
            scale = methods_creation.create_scale(scale_template, self[window_str])
            self.mapping[scale_template["str_key"]] = scale

    def create_spinboxes(self, window_str):
        """This method creates all of the spinboxes that are
        meant to appear in the window indicated by window_str."""

        for spinbox_template in classes.template["spinboxes"][window_str]:
            spinbox = methods_creation.create_spinbox(spinbox_template, self[window_str])
            self.mapping[spinbox_template["str_key"]] = spinbox

    def create_texts(self, window_str):
        """This method creates all of the texts that are meant
        to appear in the window indicated by window_str."""

        for text_template in classes.template["texts"][window_str]:
            text = methods_creation.create_text(text_template, self[window_str])
            self.mapping[text_template["str_key"]] = text

    def create_entire_window(self, window_str, is_main_window=False, macro_args=()):
        """This method creates an entire window with all of its widgets
        based on the string key for a particular window (window_str_key)."""

        # Create the window.
        window_template = classes.template[window_str]
        window = methods_helper.create_window(window_template, is_main_window)
        self.mapping[window_str] = window

        # Define how the window should treat error messages.
        window.report_callback_exception = self.report_callback_exception

        # Create the widgets that should appear in the current window.
        self.create_widgets(window_str)

        # If a function should be executed when this
        # new window is closed, set that function here.
        if f"{window_str}_ONCLOSE" in classes.macros.mapping:
            macro_args = (window,) + macro_args
            window.protocol("WM_DELETE_WINDOW", \
                lambda: classes.macros.mapping[f"{window_str}_ONCLOSE"](*macro_args))

        # Return the window object.
        return window
