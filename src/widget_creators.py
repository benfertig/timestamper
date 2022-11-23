#-*- coding: utf-8 -*-
"""This module contains the WidgetCreators class which
contains methods that create various Tkinter widgets."""

from os import path
from sys import platform
from tkinter import Button, Entry, Label, Text, PhotoImage, \
    StringVar, Grid, Tk, Toplevel, font, DISABLED, NORMAL, END

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


def entry_val_limit(entry_text, max_val):
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


class WidgetCreators():
    """This class stores methods that create various Tkinter widgets based on templates."""

    def __init__(self, template_mapping, images_dir, main_window_str):
        self.template_mapping = template_mapping
        self.images_dir = images_dir
        self.main_window_str = main_window_str
        self.mapping = {}
        self.original_colors = {}

    def create_entire_window(self, window_str, button_macro_mapping=None, \
        close_window_macro=None, macro_args=()):
        """This method creates an entire window with all of its widgets. For
        this method to work properly, the widget templates must already be mapped
        to the window's string key in the "template_window_mapping" dictionaries
        in "buttons.py", "entries.py", "labels.py" and "texts.py"."""

        # Create the window.
        window_templ = self.template_mapping[window_str]
        self.create_window(window_templ, self.images_dir)

        # Create the buttons.
        button_mapping = self.template_mapping["buttons"].template_window_mapping
        if button_macro_mapping is not None and window_str in button_mapping:
            button_window_templs = button_mapping[window_str]
            self.create_buttons(button_window_templs, \
                self.images_dir, button_macro_mapping)

        # Create the entries.
        entry_mapping = self.template_mapping["entries"].template_window_mapping
        if window_str in entry_mapping:
            entry_window_templs = entry_mapping[window_str]
            self.create_entries(entry_window_templs, entry_val_limit)

        # Create the labels.
        label_mapping = self.template_mapping["labels"].template_window_mapping
        if window_str in label_mapping:
            label_window_templs = label_mapping[window_str]
            self.create_labels(label_window_templs, self.images_dir)

        # Create the texts.
        text_mapping = self.template_mapping["texts"].template_window_mapping
        if window_str in text_mapping:
            text_window_templs = text_mapping[window_str]
            self.create_texts(text_window_templs)

        root = self.mapping[window_str]

        # If a function should be executed when this new window is closed, set that function here.
        if close_window_macro:
            macro_args = (root,) + macro_args
            root.protocol("WM_DELETE_WINDOW", lambda: close_window_macro(*macro_args))

        # Return the window object
        return root

    def create_window(self, window_template, images_dir):
        """This method creates the main window for the Time Stamper program."""

        # Create the main window and set its characteristics.
        if window_template.str_key == self.main_window_str:
            new_root = Tk()
        else:
            new_root = Toplevel()

        self.mapping[window_template.str_key] = new_root
        new_root.title(window_template.title)
        if window_template.width is not None and window_template.height is not None:
            new_root.geometry(f"{window_template.width}x{window_template.height}")
        new_root["background"] = window_template.background
        new_root["foreground"] = window_template.foreground

        # If we are on a Mac, the window icon needs to be a .icns file.
        # On Windows, the window icon needs to be a .ico file.
        if platform == "darwin":
            icon_file_name = window_template.icon_mac
        else:
            icon_file_name = window_template.icon_windows

        # Set the main window icon.
        new_root.iconbitmap(path.join(images_dir, icon_file_name))

        # Configure the main window's columns.
        for column_num in range(window_template.num_columns):
            Grid.columnconfigure(new_root, column_num, weight=1)

        # Configure the main window's rows.
        for row_num in range(window_template.num_rows):
            Grid.rowconfigure(new_root, row_num, weight=1)

        return new_root

    def create_tk_image(self, obj_template, images_dir):
        """This method creates an image object for the Time Stamper program."""

        # Return a PhotoImage only if there is an image associated with the object.
        if obj_template.image_file_name:
            image = PhotoImage(file=path.join(images_dir, obj_template.image_file_name))
            self.mapping[obj_template.image_file_name] = image
            return image

        # If there is no image associated with the object return None.
        return None

    def create_button(self, button_template, button_macro, button_image=None):
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
        root = self.mapping[button_template.window_str_key]
        button = button_class(root, height=button_template.height, \
            width=button_template.width, text=button_template.text, \
            image=button_image, state=button_template.initial_state, font=button_font, \
            background=button_background, foreground=button_foreground, \
            command=button_macro)

        # Place the Button.
        button.grid(column=button_template.column, row=button_template.row, \
            columnspan=button_template.columnspan, rowspan=button_template.rowspan, \
            padx=button_template.padx, pady=button_template.pady, \
            ipadx=button_template.ipadx, ipady=button_template.ipady, sticky=button_template.sticky)

        # Map the Button object to the Button's string
        # key so that the Macros class can reference it.
        self.mapping[button_template.str_key] = button

        # Map the Button object's initial background to the Button's string key so that the
        # Button's background can be reset to this color upon reactivation (currently, this
        # change applies only to Buttons from the tkmacosx class with images but no text,
        # since there is no easy way to tell whether these buttons are activated, so we change
        # the button's color upon activation/deactivation as a visual aid to the user). Even
        # when we pass None as the argument for "background" in the Button's constructor, the
        # background is set to a specific color, so we should save the explicit background
        # color because we will need to reference this color if we want to revert to it later.
        self.original_colors[button_template.str_key] = button.cget("background")

        # If we are on a Mac and this button is BOTH initially disabled AND an instance of the kind
        # of button whose background we would like to change when enabled/disabled, then set this
        # button's initial background color to our predefined color for disabled fields on Macs.
        if platform == "darwin" and isinstance(button, MacButton) \
            and not button.cget("text") and button["state"] == DISABLED:
            button["background"] = button_template.mac_disabled_color

        return button

    def create_buttons(self, button_templates, images_dir, button_macro_mapping):
        """This method creates all of the buttons specified by the templates in
        button_templates, searching for images in the directory provided by images_dir."""

        buttons = {}
        for b_templ in button_templates:
            image = self.create_tk_image(b_templ, images_dir)
            button = self.create_button(b_templ, button_macro_mapping[b_templ.str_key], image)
            buttons[b_templ.str_key] = button
        return buttons

    def create_entry(self, entry_template, e_v_limit):
        """This method creates an Entry object for the Time Stamper program."""

        # Set the Entry's initial text.
        entry_text = StringVar()
        entry_text.set(entry_template.text)

        # Create the Entry's font.
        entry_font = font.Font(family=entry_template.font_family,size=entry_template.font_size, \
            weight=entry_template.font_weight, slant=entry_template.font_slant, \
            underline=entry_template.font_underline, overstrike=entry_template.font_overstrike)

        # Create the Entry object.
        root = self.mapping[entry_template.window_str_key]
        entry = Entry(root, width=entry_template.width, \
            textvariable=entry_text, font=entry_font, background=entry_template.background, \
            foreground=entry_template.foreground, state=entry_template.initial_state)

        # Place the Entry.
        entry.grid(column=entry_template.column, row=entry_template.row, \
            columnspan=entry_template.columnspan, rowspan=entry_template.rowspan, \
            padx=entry_template.padx, pady=entry_template.pady, \
            ipadx=entry_template.ipadx, ipady=entry_template.ipady, sticky=entry_template.sticky)

        # Set the Entry input resitrictions.
        entry_text.trace("w", lambda *args: e_v_limit(entry_text, entry_template.max_val))

        # Map the Entry object to the Entry's string key so that the Macros class can reference it.
        self.mapping[entry_template.str_key] = entry

        return entry

    def create_entries(self, entry_templates, e_v_limit):
        """This method creates all of the entries specified by the templates in entry_templates."""

        entries = {}
        for e_templ in entry_templates:
            entry = self.create_entry(e_templ, e_v_limit)
            entries[e_templ.str_key] = entry
        return entries

    def create_label(self, label_template, label_image=None):
        """This method creates a Label object for the Time Stamper program."""

        # Create the Label's font.
        label_font = font.Font(family=label_template.font_family, \
            size=label_template.font_size, weight=label_template.font_weight, \
            slant=label_template.font_slant, underline=label_template.font_underline, \
            overstrike=label_template.font_overstrike)

        # Create the Label object.
        root = self.mapping[label_template.window_str_key]
        label = Label(root, height=label_template.height, \
            width=label_template.width, background=label_template.background, \
            foreground=label_template.foreground, text=label_template.text, \
            image=label_image, font=label_font, highlightthickness=0, \
            wraplength=label_template.wraplength, justify=label_template.justify)

        # Place the Label.
        label.grid(column=label_template.column, row=label_template.row, \
            columnspan=label_template.columnspan, rowspan=label_template.rowspan, \
            padx=label_template.padx, pady=label_template.pady, \
            ipadx=label_template.ipadx, ipady=label_template.ipady, sticky=label_template.sticky)

        # Map the Label object to the Label's string key so that the Macros class can reference it.
        self.mapping[label_template.str_key] = label

        return label

    def create_labels(self, label_templates, images_dir):
        """This method creates all of the labels specified by the templates in label_templates."""

        labels = {}
        for l_templ in label_templates:
            image = self.create_tk_image(l_templ, images_dir)
            label = self.create_label(l_templ, image)
            labels[l_templ.str_key] = label
        return labels

    def create_text(self, text_template):
        """This method creates a Text object for the Time Stamper program."""

        # Create the Text's font.
        text_font = font.Font(family=text_template.font_family, \
            size=text_template.font_size, weight=text_template.font_weight, \
            slant=text_template.font_slant, \
            underline=text_template.font_underline, \
            overstrike=text_template.font_overstrike)

        # Create the Text object.
        root = self.mapping[text_template.window_str_key]
        text = Text(root, height=text_template.height, \
            width=text_template.width, font=text_font, \
            state=text_template.initial_state)

        # Display the Text object's text.
        text["state"] = NORMAL
        text.insert(END, text_template.text)
        text["state"] = text_template.initial_state

        # Place the Text.
        text.grid(column=text_template.column, row=text_template.row, \
            columnspan=text_template.columnspan, rowspan=text_template.rowspan, \
            padx=text_template.padx, pady=text_template.pady, \
            ipadx=text_template.ipadx, ipady=text_template.ipady, sticky=text_template.sticky)

        # Map the Text object to the Text's string key so that the Macros class can reference it.
        self.mapping[text_template.str_key] = text

        return text

    def create_texts(self, text_templates):
        """This method creates all of the texts specified by the templates in text_templates."""

        texts = {}
        for t_templ in text_templates:
            text = self.create_text(t_templ)
            texts[t_templ.str_key] = text
        return texts
