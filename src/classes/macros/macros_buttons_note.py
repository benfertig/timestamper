#-*- coding: utf-8 -*-
"""This module contains the NoteButtonMacros class which stores the functions
that are executed when a note button in the Time Stamper program is pressed."""

from tkinter import END
from .macros_helper_methods import print_button_message, print_to_text, print_to_file

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


class NoteButtonMacros():
    """This class stores all of the macros that execute when note buttons are pressed."""

    def __init__(self, template, settings, widgets, timer):
        self.template = template
        self.settings = settings
        self.widgets = widgets
        self.timer = timer

    def button_hotkey_1_macro(self):
        """This method will be executed when hotkey 1 is pressed."""

        # Print the message associated with hotkey 1.
        print_button_message(self.template["button_hotkey_1"], \
            self.template, self.settings, self.widgets, self.timer)

    def button_hotkey_2_macro(self):
        """This method will be executed when hotkey 2 is pressed."""

        # Print the message associated with hotkey 2.
        print_button_message(self.template["button_hotkey_2"], \
            self.template, self.settings, self.widgets, self.timer)

    def button_hotkey_3_macro(self):
        """This method will be executed when hotkey 3 is pressed."""

        # Print the message associated with hotkey 3.
        print_button_message(self.template["button_hotkey_3"], \
            self.template, self.settings, self.widgets, self.timer)

    def button_cancel_note_macro(self):
        """This method will be executed when the "Cancel note" button is pressed."""

        # Clear the current note from the input text box.
        print_to_text("", self.widgets["text_current_note"], wipe_clean=True)

    def button_save_note_macro(self):
        """This method will be executed when the "Save note" button is pressed."""

        # Get the current output path from the output path entry widget.
        output_path = self.widgets["entry_output_path"].get()

        # Get the current timestamp displayed next to the input text box.
        current_timestamp = self.widgets["label_timestamp"]["text"]

        # Get the current text in the input text box.
        obj_current_note = self.widgets["text_current_note"]
        current_note = obj_current_note.get(1.0, END)

        # Clear the current text in the input text box.
        print_to_text("", obj_current_note, wipe_clean=True)

        # Generate the note that should be printed to the log and the output file.
        to_write = f"{current_timestamp} {current_note}"

        # Print the current timestamp along with the current
        # text from the input text box to the screen.
        print_to_text(to_write, self.widgets["text_log"])

        # Print the current timestamp along with the current
        # text from the input text box to the output file.
        print_to_file(to_write, output_path, self.settings["output"]["file_encoding"])
