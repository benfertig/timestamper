#-*- coding: utf-8 -*-
"""This module contains the TimeStamper class which runs the Time Stamper program."""

from dataclasses import dataclass
from os import path
from tkinter import Button, Entry, font, Grid, Label, PhotoImage, StringVar, Text, Tk
from time_stamper_timer import TimeStamperTimer
from macros import Macros

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


class TimeStamper():
    """This class runs the Time Stamper program."""

    @dataclass
    class TimeFields():
        """This class stores the fields where the time is displayed in the Time Stamper program."""

        hours_field = None
        minutes_field = None
        seconds_field = None
        subseconds_field = None

    def __init__(self, shell):
        """This constructor initializes the Time Stamper shell (which stores
        all of the attributes for objects in the the Time Stamper program), the
        macros (which store all of the macros for buttons in the Time Stamper
        program) and the timer (which runs the timer for the Time Stamper program)."""

        self.shell = shell
        self.macros = Macros(self.shell)
        self.timer = TimeStamperTimer(self)
        self.root = None
        self.entries, self.images = None, None
        self.time_fields = self.TimeFields()

    def create_tk_image(self, obj_shell):
        """This method creates an image object for the Time Stamper program."""

        # Return a PhotoImage only if there is an image associated with the object.
        if obj_shell.image_file_name:
            return PhotoImage(file=path.join(self.shell.path.images_dir, \
                obj_shell.image_file_name))

        # If there is no image associated with the object return None.
        return None

    def create_button(self, button_shell, button_image=None):
        """This method creates a Button object for the Time Stamper program."""

        # Create the Button's font.
        button_font = font.Font(family=button_shell.font_family, size=button_shell.font_size, \
            weight=button_shell.font_weight, slant=button_shell.font_slant, \
            underline=button_shell.font_underline, overstrike=button_shell.font_overstrike)

        # Create the Button object.
        button = Button(self.root, height=button_shell.height, \
            width=button_shell.width, text=button_shell.text, \
            image=button_image, state=button_shell.initial_state, font=button_font, \
            background=button_shell.background, \
            foreground=button_shell.foreground, \
            command=self.macros.macro_mapping[button_shell.str_key])

        # Place the Button.
        button.grid(column=button_shell.column, row=button_shell.row, \
            columnspan=button_shell.columnspan, rowspan=button_shell.rowspan, \
            padx=button_shell.padx, pady=button_shell.pady, \
            ipadx=button_shell.ipadx, ipady=button_shell.ipady, sticky=button_shell.sticky)

        # Map the Button object to the Button's string
        # key so that the Macros class can reference it.
        self.macros.object_mapping[button_shell.str_key] = button

        return button

    def create_entry(self, entry_shell):
        """This method creates an Entry object for the Time Stamper program."""

        # Set the Entry's initial text.
        entry_text = StringVar()
        entry_text.set(entry_shell.text)

        # Create the Entry's font.
        entry_font = font.Font(family=entry_shell.font_family,size=entry_shell.font_size, \
            weight=entry_shell.font_weight, slant=entry_shell.font_slant, \
            underline=entry_shell.font_underline, overstrike=entry_shell.font_overstrike)

        # Create the Entry object.
        entry = Entry(self.root, width=entry_shell.width, \
            textvariable=entry_text, font=entry_font, background=entry_shell.background, \
            foreground=entry_shell.foreground, state=entry_shell.initial_state)

        # Place the Entry.
        entry.grid(column=entry_shell.column, row=entry_shell.row, \
            columnspan=entry_shell.columnspan, rowspan=entry_shell.rowspan, \
            padx=entry_shell.padx, pady=entry_shell.pady, \
            ipadx=entry_shell.ipadx, ipady=entry_shell.ipady, sticky=entry_shell.sticky)

        # Set the Entry input resitrictions.
        entry_text.trace("w", \
            lambda *args: self.macros.entry_val_limit(entry_text, entry_shell.max_val))

        # Map the Entry object to the Entry's string key so that the Macros class can reference it.
        self.macros.object_mapping[entry_shell.str_key] = entry

        return entry

    def create_label(self, label_shell):
        """This method creates a Label object for the Time Stamper program."""

        # Create the Label's font.
        label_font = font.Font(family=label_shell.font_family, \
            size=label_shell.font_size, weight=label_shell.font_weight, \
            slant=label_shell.font_slant, underline=label_shell.font_underline, \
            overstrike=label_shell.font_overstrike)

        # Create the Label object.
        label = Label(self.root, height=label_shell.height, \
            width=label_shell.width, background=label_shell.background, \
            foreground=label_shell.foreground, text=label_shell.text, \
            font=label_font, highlightthickness=0, wraplength=label_shell.wraplength, \
            justify=label_shell.justify)

        # Place the Label.
        label.grid(column=label_shell.column, row=label_shell.row, \
            columnspan=label_shell.columnspan, rowspan=label_shell.rowspan, \
            padx=label_shell.padx, pady=label_shell.pady, \
            ipadx=label_shell.ipadx, ipady=label_shell.ipady, sticky=label_shell.sticky)

        # Map the Label object to the Label's string key so that the Macros class can reference it.
        self.macros.object_mapping[label_shell.str_key] = label

        return label

    def create_text(self, text_shell):
        """This method creates a Text object for the Time Stamper program."""

        # Create the Text's font.
        text_font = font.Font(family=text_shell.font_family, \
            size=text_shell.font_size, weight=text_shell.font_weight, \
            slant=text_shell.font_slant, \
            underline=text_shell.font_underline, \
            overstrike=text_shell.font_overstrike)

        # Create the Text object.
        text = Text(self.root, height=text_shell.height, \
            width=text_shell.width, font=text_font, \
            state=text_shell.initial_state)

        # Place the Text.
        text.grid(column=text_shell.column, row=text_shell.row, \
            columnspan=text_shell.columnspan, rowspan=text_shell.rowspan, \
            padx=text_shell.padx, pady=text_shell.pady, \
            ipadx=text_shell.ipadx, ipady=text_shell.ipady, sticky=text_shell.sticky)

        # Map the Text object to the Text's string key so that the Macros class can reference it.
        self.macros.object_mapping[text_shell.str_key] = text

        return text

    def run(self):
        """This method runs the Time Stamper program."""

        # Create the main window and set its characteristics.
        window_shell = self.shell.windows.main
        self.root = Tk()
        self.root.title(window_shell.title)
        self.root.geometry(f"{window_shell.width}x{window_shell.height}")
        self.root["background"] = window_shell.background
        self.root["foreground"] = window_shell.foreground
        self.root.iconbitmap(path.join(self.shell.path.images_dir, window_shell.icon))

        for column_num in range(window_shell.num_columns):
            Grid.columnconfigure(self.root, column_num, weight=1)

        for row_num in range(window_shell.num_rows):
            Grid.rowconfigure(self.root, row_num, weight=1)

        # Create the labels.
        assert [self.create_label(sh) for sh in self.shell.fields.labels.all_shells]

        # Create the texts.
        assert [self.create_text(sh) for sh in self.shell.fields.texts.all_shells]

        # Create the buttons.
        button_str_mapping = {btn.str_key: btn for btn in self.shell.fields.buttons.all_shells}
        self.images = \
            {str_key: self.create_tk_image(btn) for str_key, btn in button_str_mapping.items()}
        assert [self.create_button(button_str_mapping[str_key], img) \
            for str_key, img in self.images.items()]

        # Create the entries.
        self.entries = \
            {sh.str_key: self.create_entry(sh) for sh in self.shell.fields.entries.all_shells}

        # Pass the entries containing the hours, minutes, seconds and subseconds to the timer.
        self.time_fields.hours_field = \
            self.entries[self.shell.fields.entries.timer.num_hours.str_key]
        self.time_fields.minutes_field = \
            self.entries[self.shell.fields.entries.timer.num_minutes.str_key]
        self.time_fields.seconds_field = \
            self.entries[self.shell.fields.entries.timer.num_seconds.str_key]
        self.time_fields.subseconds_field = \
            self.entries[self.shell.fields.entries.timer.num_subseconds.str_key]

        # Map the timer to the timer's string key so that the Macros class can reference it.
        self.macros.object_mapping[self.shell.timer.str_key] = self.timer

        self.root.mainloop()
