#-*- coding: utf-8 -*-
"""This module contains the Widgets class which contains methods associated with
various Tkinter widgets as well as a mapping of widgets to their string keys. This
allows for easy reference of widgets. Also see the "widgets_creation_methods.py" and
"widgets_helper_methods.py" modules for additional methods associated with widgets."""

from traceback import format_exception
from .widgets_creation_methods import create_button, create_checkbutton, \
    create_entry, create_label, create_scale, create_spinbox, create_text
from .widgets_helper_methods import create_image, create_window, determine_widget_text

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
    reference Widgets["button_pause"]. Also see the "widgets_creation_methods.py" and
    "widgets_helper_methods.py" modules for additional methods associated with widgets."""

    def __init__(self, time_stamper, settings, main_window_str):

        self.time_stamper = time_stamper
        self.template = time_stamper.template
        self.settings = settings
        self.main_window_str = main_window_str
        self.original_colors = {}
        self.determine_widget_text = determine_widget_text

        self.mapping = {"time_stamper_timer": time_stamper.timer}

    def __getitem__(self, item):
        return self.mapping[item]

    def report_callback_exception(self, *args):
        """This function replaces the default
        report_callback_exception function for the root window."""

        error_message = format_exception(*args)
        self.template["text_error"]["text"] = error_message
        self.create_entire_window("window_error")

    def create_widgets(self, window_str, macros=None):
        """This method creates all of the widgets that are meant
        to appear in the window indicated by window_str."""

        self.create_extra_images()
        self.create_buttons(window_str, macros)
        self.create_checkbuttons(window_str, macros)
        self.create_entries(window_str)
        self.create_labels(window_str)
        self.create_scales(window_str, macros)
        self.create_spinboxes(window_str)
        self.create_texts(window_str)

    def create_extra_images(self):
        """Some Tkinter image objects need to be created even if they are not immediately
        displayed. Create those images here so that they can be referenced later (if needed)."""

        extra_image_file_names = ("blank.png", "volume_medium.png", \
            "volume_low.png", "volume_zero.png", "volume_mute.png")

        for image_file_name in extra_image_file_names:
            extra_image = create_image(self.template.images_dir, image_file_name=image_file_name)
            self.mapping[image_file_name] = extra_image

    def create_buttons(self, window_str, macros):
        """This method creates all of the buttons that are meant
        to appear in the window indicated by window_str."""

        button_window = self[window_str]
        for button_template in self.template["buttons"][window_str]:
            button_macro = macros[button_template["str_key"]] \
                if button_template["str_key"] in macros.mapping else None
            button, button_image, button_orig_color = \
                create_button(self.template, self.settings, \
                    button_template, button_window, button_macro)
            button.image = button_image
            self.original_colors[button_template["str_key"]] = button_orig_color
            if button_image:
                self.mapping[button_template["image_file_name"]] = button_image
            self.mapping[button_template["str_key"]] = button

    def create_checkbuttons(self, window_str, macros):
        """This method creates all of the checkbuttons that are
        meant to appear in the window indicated by window_str."""

        checkbutton_window = self[window_str]
        for checkbutton_template in self.template["checkbuttons"][window_str]:
            checkbutton_macro = macros[checkbutton_template["str_key"]] \
                if checkbutton_template["str_key"] in macros.mapping else None
            checkbutton = create_checkbutton(self.template, self.settings, \
                checkbutton_template, checkbutton_window, checkbutton_macro)
            self.mapping[checkbutton_template["str_key"]] = checkbutton

    def create_entries(self, window_str):
        """This method creates all of the entries that are meant
        to appear in the window indicated by window_str."""

        entry_window = self[window_str]
        for entry_template in self.template["entries"][window_str]:
            entry = create_entry(self.template, self.settings, entry_template, entry_window, self)
            self.mapping[entry_template["str_key"]] = entry

    def create_labels(self, window_str):
        """This method creates all of the labels that are meant
        to appear in the window indicated by window_str."""

        label_window = self[window_str]
        for label_template in self.template["labels"][window_str]:
            label, label_image = \
                create_label(self.template, self.settings, label_template, label_window)
            if label_image:
                self.mapping[label_template["image_file_name"]] = label_image
            self.mapping[label_template["str_key"]] = label

    def create_scales(self, window_str, macros):
        """This method creates all of the scales that are meant
        to appear in the window indicated by window_str."""

        scale_window = self[window_str]
        for scale_template in self.template["scales"][window_str]:
            str_key = scale_template["str_key"]
            scale_macro = macros[str_key] if str_key in macros.mapping else None
            release_macro = \
                macros[f"{str_key}_ONRELEASE"] if f"{str_key}_ONRELEASE" in macros.mapping else None
            scale = create_scale(self, scale_template, scale_window, scale_macro, release_macro)
            self.mapping[scale_template["str_key"]] = scale


    def create_spinboxes(self, window_str):
        """This method creates all of the spinboxes that are
        meant to appear in the window indicated by window_str."""

        spinbox_window = self[window_str]
        for spinbox_template in self.template["spinboxes"][window_str]:
            spinbox = create_spinbox(self.template, self.settings, spinbox_template, spinbox_window)
            self.mapping[spinbox_template["str_key"]] = spinbox


    def create_texts(self, window_str):
        """This method creates all of the texts that are meant
        to appear in the window indicated by window_str."""

        text_window = self[window_str]
        for text_template in self.template["texts"][window_str]:
            text = create_text(self.template, self.settings, text_template, text_window)
            self.mapping[text_template["str_key"]] = text

    def create_entire_window(self, window_str, macros=None, close_window_macro=None, macro_args=()):
        """This method creates an entire window with all of its widgets
        based on the string key for a particular window (window_str_key)."""

        # Create the window.
        window_template = self.template[window_str]
        window = create_window(window_template, self.main_window_str, self.template.images_dir)
        self.mapping[window_str] = window

        # Define how the window should treat error messages
        window.report_callback_exception = self.report_callback_exception

        # Create the widgets that should appear in the current window.
        self.create_widgets(window_str, macros)

        # If a function should be executed when this
        # new window is closed, set that function here.
        if close_window_macro:
            macro_args = (window,) + macro_args
            window.protocol("WM_DELETE_WINDOW", lambda: close_window_macro(*macro_args))

        # Return the window object.
        return window
