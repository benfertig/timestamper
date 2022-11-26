#-*- coding: utf-8 -*-
"""This module contains additional methods that the widgets module relies on."""

from json import load
from os import path
from sys import platform
from tkinter import DISABLED, NORMAL, END, Button, Entry, font, \
    Grid, Label, PhotoImage, StringVar, Text, Tk, Toplevel

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


def entry_value_limit(entry_text, max_val):
    """This method prevents any non-numerical characters from being entered
    into an entry and also sets the maximum value of that entry."""

    if len(entry_text.get()) > 0:

        # Remove any non-digits from the entry.
        try:
            int(entry_text.get()[-1])
        except ValueError:
            entry_text.set(entry_text.get()[:-1])

        # Remove any digits from the entry that put the entry over max_val.
        if len(entry_text.get()) > 0:
            if int(entry_text.get()) > max_val:
                entry_text.set(entry_text.get()[:-1])


def determine_widget_text(widget_template, messages_dir):
    """There are different ways that a widget's text can be set. Sometimes, the widget's text
    is stored in a file. Other times, the widget's text is stored in its template's .text
    attribute. This method determines where to find the widget's text and returns that text."""

    # If there is a file associated with this widget,
    # determine the widget's initial text using that file.
    if widget_template.message_file_name is not None:
        if widget_template.text is not None:
            print(f"\nWARNING for widget template \"{widget_template.str_key}\":" \
                "\nA template's \"text\" and \"message_file_name\" attributes should "\
                "not both be set to non-None values simultaneously. The \"message_file_name\" " \
                "attribute takes precedence, so the text for the widget based on this template " \
                "will be generated using the information stored in " \
                f"\"{widget_template.message_file_name}\", as opposed to the information stored " \
                f"in this template's \"text\" attribute (i.e. \"{widget_template.text}\").")
        message_file_loc = path.join(messages_dir, widget_template.message_file_name)
        message_encoding = widget_template.message_file_encoding
        with open(message_file_loc, "r", encoding=message_encoding) as message_file:

            # If the file associated with this widget is a json file, set the widget's initial
            # text to the value paired with the key asssociated with the initial message.
            if path.splitext(message_file_loc)[1] == ".json":
                json_text = load(message_file)
                widget_template.loaded_message_text = json_text
                widget_text = json_text[widget_template.json_first_message_key]

            # If the file associated with this widget is not a json file,
            # set the widget's initial text to the exact reading of the file.
            else:
                widget_text = message_file.read()
                widget_template.loaded_message_text = widget_text

    # If there is no file associated with this widget, set the widget's initial text
    # to the widget template's .text attribute (unless the .text attribute is None,
    # in which case you would set the widget's initial text to an empty string).
    elif widget_template.text is not None:
        widget_text = widget_template.text
    else:
        widget_text = ""

    return widget_text


def create_font(widget_template):
    """This method creates a widget's font based on its template."""
    return font.Font(family=widget_template.font_family, \
        size=widget_template.font_size, weight=widget_template.font_weight, \
        slant=widget_template.font_slant, underline=widget_template.font_underline, \
        overstrike=widget_template.font_overstrike)


def grid_widget(widget, widget_template):
    """This method grids a widget based on its template."""
    widget.grid(column=widget_template.column, row=widget_template.row, \
        columnspan=widget_template.columnspan, rowspan=widget_template.rowspan, \
        padx=widget_template.padx, pady=widget_template.pady, \
        ipadx=widget_template.ipadx, ipady=widget_template.ipady, sticky=widget_template.sticky)


def create_window(window_template, main_window_str, images_dir):
    """This method creates the main window for the Time Stamper program."""

    # Create the main window and set its characteristics.
    if window_template.str_key == main_window_str:
        window = Tk()
    else:
        window = Toplevel()

    window.title(window_template.title)
    if window_template.width is not None and window_template.height is not None:
        window.geometry(f"{window_template.width}x{window_template.height}")
    window["background"] = window_template.background
    window["foreground"] = window_template.foreground

    # If we are on a Mac, the window icon needs to be a .icns file.
    # On Windows, the window icon needs to be a .ico file.
    if platform == "darwin":
        icon_file_name = window_template.icon_mac
    else:
        icon_file_name = window_template.icon_windows

    # Set the main window icon.
    window.iconbitmap(path.join(images_dir, icon_file_name))

    # Configure the main window's columns.
    for column_num in range(window_template.num_columns):
        Grid.columnconfigure(window, column_num, weight=1)

    # Configure the main window's rows.
    for row_num in range(window_template.num_rows):
        Grid.rowconfigure(window, row_num, weight=1)

    return window


def create_image(obj_template, images_dir):
    """This method creates an image object for the Time Stamper program."""

    # Return a PhotoImage only if there is an image associated with the object.
    if obj_template.image_file_name:
        return PhotoImage(file=path.join(images_dir, obj_template.image_file_name))

    # If there is no image associated with the object return None.
    return None


def create_button(button_template, button_window, button_macro, messages_dir, button_image):
    """This method creates a Button object for the Time Stamper program."""

    # Create the Button's font.
    button_font = create_font(button_template)

    # Determine whether we should use the Button class from tkmacosx instead of tkinter.
    button_class = Button
    button_background = button_template.background
    button_foreground = button_template.foreground
    button_has_color = button_background is not None or button_foreground is not None
    if platform == "darwin" and (button_has_color or not button_template.text):
        button_class = MacButton

    # Determine what the button's initial text should be.
    button_text = determine_widget_text(button_template, messages_dir)

    # Create the Button object.
    button = button_class(button_window, height=button_template.height, \
        width=button_template.width, text=button_text, image=button_image, \
        state=button_template.initial_state, font=button_font, \
        background=button_background, foreground=button_foreground, \
        command=button_macro)

    # Place the Button.
    grid_widget(button, button_template)

    original_color = button.cget("background")

    # If we are on a Mac and this button is BOTH initially disabled AND an instance of the kind
    # of button whose background we would like to change when enabled/disabled, then set this
    # button's initial background color to our predefined color for disabled fields on Macs.
    if platform == "darwin" and isinstance(button, MacButton) \
        and not button.cget("text") and button["state"] == DISABLED:
        button["background"] = button_template.mac_disabled_color

    return button, original_color


def create_entry(entry_template, entry_window, e_v_limit, messages_dir):
    """This method creates an Entry object for the Time Stamper program."""

    # Create the Entry's font.
    entry_font = create_font(entry_template)

    # Determine what the entry's initial text should be.
    entry_text_str = determine_widget_text(entry_template, messages_dir)
    entry_text = StringVar()
    entry_text.set(entry_text_str)

    # Create the Entry object.
    entry = Entry(entry_window, width=entry_template.width, \
        textvariable=entry_text, font=entry_font, background=entry_template.background, \
        foreground=entry_template.foreground, state=entry_template.initial_state)

    # Place the Entry.
    grid_widget(entry, entry_template)

    # Set the Entry input resitrictions.
    entry_text.trace("w", lambda *args: e_v_limit(entry_text, entry_template.max_val))

    return entry


def create_label(label_template, label_window, messages_dir, label_image=None):
    """This method creates a Label object for the Time Stamper program."""

    # Create the Label's font.
    label_font = create_font(label_template)

    # Determine what the label's initial text should be.
    label_text = determine_widget_text(label_template, messages_dir)

    # Create the Label object.
    label = Label(label_window, height=label_template.height, \
        width=label_template.width, background=label_template.background, \
        foreground=label_template.foreground, text=label_text, \
        image=label_image, font=label_font, highlightthickness=0, \
        wraplength=label_template.wraplength, justify=label_template.justify)

    # Place the Label.
    grid_widget(label, label_template)

    return label


def create_text(text_template, text_window, messages_dir):
    """This method creates a Text object for the Time Stamper program."""

    # Create the Text's font.
    text_font = create_font(text_template)

    # Create the Text object.
    text = Text(text_window, height=text_template.height, \
        width=text_template.width, font=text_font, \
        state=text_template.initial_state)

    # Determine what the text object's initial text should be.
    text_text = determine_widget_text(text_template, messages_dir)

    # Display the Text object's text.
    text["state"] = NORMAL
    text.insert(END, text_text)
    text["state"] = text_template.initial_state

    # Place the Text.
    grid_widget(text, text_template)

    return text
