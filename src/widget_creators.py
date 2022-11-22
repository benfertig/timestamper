#-*- coding: utf-8 -*-
"""This module contains the WidgetCreators class which
contains methods that create various Tkinter widgets."""

from os import path
from sys import platform
from tkinter import Button, Entry, Label, Text, PhotoImage, StringVar, Grid, Tk, font, DISABLED

if platform == "darwin":
    from tkmacosx import Button as MacButton

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


class WidgetCreators():
    """This class stores methods that create various Tkinter widgets based on templates."""

    def __init__(self, root, template):
        self.root = root
        self.template = template

    def create_window(self):
        """This method creates the main window for the Time Stamper program."""

        # Create the main window and set its characteristics.
        window_template = self.template.mapping["window_main"]
        self.root = Tk()
        self.root.title(window_template.title)
        self.root.geometry(f"{window_template.width}x{window_template.height}")
        self.root["background"] = window_template.background
        self.root["foreground"] = window_template.foreground

        # If we are on a Mac, the window icon needs to be a .icns file.
        # On Windows, the window icon needs to be a .ico file.
        if platform == "darwin":
            icon_file_name = window_template.icon_mac
        else:
            icon_file_name = window_template.icon_windows

        # Set the main window icon.
        self.root.iconbitmap(path.join(self.template.images_dir, icon_file_name))

        # Configure the main window's columns.
        for column_num in range(window_template.num_columns):
            Grid.columnconfigure(self.root, column_num, weight=1)

        # Configure the main window's rows.
        for row_num in range(window_template.num_rows):
            Grid.rowconfigure(self.root, row_num, weight=1)

        return self.root

    def create_tk_image(self, obj_template):
        """This method creates an image object for the Time Stamper program."""

        # Return a PhotoImage only if there is an image associated with the object.
        if obj_template.image_file_name:
            return PhotoImage(file=path.join(self.template.images_dir, \
                obj_template.image_file_name))

        # If there is no image associated with the object return None.
        return None

    def create_button(self, button_template, macros, button_image=None):
        """This method creates a Button object for the Time Stamper program."""

        # Create the Button's font.
        button_font = font.Font(family=button_template.font_family, \
            size=button_template.font_size, weight=button_template.font_weight, \
            slant=button_template.font_slant, underline=button_template.font_underline, \
            overstrike=button_template.font_overstrike)

        # Determine whether we should use the Button class from tkmacosx instead of tkinter.
        button_class = Button
        button_background = button_template.background
        button_foreground = button_template.foreground
        button_has_color = button_background is not None or button_foreground is not None
        if platform == "darwin" and (button_has_color or not button_template.text):
            button_class = MacButton

        # Create the Button object.
        button = button_class(self.root, height=button_template.height, \
            width=button_template.width, text=button_template.text, \
            image=button_image, state=button_template.initial_state, font=button_font, \
            background=button_background, foreground=button_foreground, \
            command=macros.button.mapping[button_template.str_key])

        # Place the Button.
        button.grid(column=button_template.column, row=button_template.row, \
            columnspan=button_template.columnspan, rowspan=button_template.rowspan, \
            padx=button_template.padx, pady=button_template.pady, \
            ipadx=button_template.ipadx, ipady=button_template.ipady, sticky=button_template.sticky)

        # Map the Button object to the Button's string
        # key so that the Macros class can reference it.
        macros.button.object_mapping[button_template.str_key] = button

        # Map the Button object's initial background to the Button's string key so that the
        # Button's background can be reset to this color upon reactivation (currently, this
        # change applies only to Buttons from the tkmacosx class with images but no text,
        # since there is no easy way to tell whether these buttons are activated, so we change
        # the button's color upon activation/deactivation as a visual aid to the user). Even
        # when we pass None as the argument for "background" in the Button's constructor, the
        # background is set to a specific color, so we should save the explicit background
        # color because we will need to reference this color if we want to revert to it later.
        macros.original_colors[button_template.str_key] = button.cget("background")

        # If we are on a Mac and this button is BOTH initially disabled AND an instance of the kind
        # of button whose background we would like to change when enabled/disabled, then set this
        # button's initial background color to our predefined color for disabled fields on Macs.
        if platform == "darwin" and isinstance(button, MacButton) \
            and not button.cget("text") and button["state"] == DISABLED:
            button["background"] = self.template.mac_disabled_color

        return button

    def create_entry(self, entry_template, macros):
        """This method creates an Entry object for the Time Stamper program."""

        # Set the Entry's initial text.
        entry_text = StringVar()
        entry_text.set(entry_template.text)

        # Create the Entry's font.
        entry_font = font.Font(family=entry_template.font_family,size=entry_template.font_size, \
            weight=entry_template.font_weight, slant=entry_template.font_slant, \
            underline=entry_template.font_underline, overstrike=entry_template.font_overstrike)

        # Create the Entry object.
        entry = Entry(self.root, width=entry_template.width, \
            textvariable=entry_text, font=entry_font, background=entry_template.background, \
            foreground=entry_template.foreground, state=entry_template.initial_state)

        # Place the Entry.
        entry.grid(column=entry_template.column, row=entry_template.row, \
            columnspan=entry_template.columnspan, rowspan=entry_template.rowspan, \
            padx=entry_template.padx, pady=entry_template.pady, \
            ipadx=entry_template.ipadx, ipady=entry_template.ipady, sticky=entry_template.sticky)

        # Set the Entry input resitrictions.
        entry_text.trace("w", \
            lambda *args: macros.entry_val_limit(entry_text, entry_template.max_val))

        # Map the Entry object to the Entry's string key so that the Macros class can reference it.
        macros.button.object_mapping[entry_template.str_key] = entry

        # Map the Entry object's initial color to the Entry's string key (currently,
        # there is no need to have this mapping for any tkinter objects in this class
        # other than for Buttons, but there is no harm in mapping the original colors
        # for the other objects as well, both for consistency's sake and because of
        # the possibility that we could make use of this mapping in the future).
        macros.original_colors[entry_template.str_key] = entry.cget("background")

        return entry

    def create_label(self, label_template, macros):
        """This method creates a Label object for the Time Stamper program."""

        # Create the Label's font.
        label_font = font.Font(family=label_template.font_family, \
            size=label_template.font_size, weight=label_template.font_weight, \
            slant=label_template.font_slant, underline=label_template.font_underline, \
            overstrike=label_template.font_overstrike)

        # Create the Label object.
        label = Label(self.root, height=label_template.height, \
            width=label_template.width, background=label_template.background, \
            foreground=label_template.foreground, text=label_template.text, \
            font=label_font, highlightthickness=0, wraplength=label_template.wraplength, \
            justify=label_template.justify)

        # Place the Label.
        label.grid(column=label_template.column, row=label_template.row, \
            columnspan=label_template.columnspan, rowspan=label_template.rowspan, \
            padx=label_template.padx, pady=label_template.pady, \
            ipadx=label_template.ipadx, ipady=label_template.ipady, sticky=label_template.sticky)

        # Map the Label object to the Label's string key so that the Macros class can reference it.
        macros.button.object_mapping[label_template.str_key] = label

        # Map the Label object's initial color to the Label's string key (currently,
        # there is no need to have this mapping for any tkinter objects in this class
        # other than for Buttons, but there is no harm in mapping the original colors
        # for the other objects as well, both for consistency's sake and because of
        # the possibility that we could make use of this mapping in the future).
        macros.original_colors[label_template.str_key] = label.cget("background")

        return label

    def create_text(self, text_template, macros):
        """This method creates a Text object for the Time Stamper program."""

        # Create the Text's font.
        text_font = font.Font(family=text_template.font_family, \
            size=text_template.font_size, weight=text_template.font_weight, \
            slant=text_template.font_slant, \
            underline=text_template.font_underline, \
            overstrike=text_template.font_overstrike)

        # Create the Text object.
        text = Text(self.root, height=text_template.height, \
            width=text_template.width, font=text_font, \
            state=text_template.initial_state)

        # Place the Text.
        text.grid(column=text_template.column, row=text_template.row, \
            columnspan=text_template.columnspan, rowspan=text_template.rowspan, \
            padx=text_template.padx, pady=text_template.pady, \
            ipadx=text_template.ipadx, ipady=text_template.ipady, sticky=text_template.sticky)

        # Map the Text object to the Text's string key so that the Macros class can reference it.
        macros.button.object_mapping[text_template.str_key] = text

        # Map the Text object's initial color to the Texts's string key (currently,
        # there is no need to have this mapping for any tkinter objects in this class
        # other than for Buttons, but there is no harm in mapping the original colors
        # for the other objects as well, both for consistency's sake and because of
        # the possibility that we could make use of this mapping in the future).
        macros.original_colors[text_template.str_key] = text.cget("background")

        return text
