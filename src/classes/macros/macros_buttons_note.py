#-*- coding: utf-8 -*-
"""This module contains the NoteButtonMacros class which stores the functions
that are executed when a note button in the Time Stamper program is pressed."""

from tkinter import END
from .macros_helper_methods import print_to_text, print_to_file

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

    def __init__(self, template, widgets):
        self.template = template
        self.widgets = widgets

    def button_cancel_note_macro(self):
        """This method will be executed when the "Cancel note" button is pressed."""

        # Clear the current note from the input text box.
        self.widgets.mapping["text_current_note"].delete(1.0, END)

    def button_save_note_macro(self):
        """This method will be executed when the "Save note" button is pressed."""

        # Get the current timestamp displayed next to the input text box.
        current_timestamp = self.widgets.mapping["label_timestamp"]["text"]

        # Store the output path.
        output_path = self.template.output_path

        # Get the current text in the input text box.
        obj_current_note = self.widgets.mapping["text_current_note"]
        current_note = obj_current_note.get(1.0, END)

        # Clear the current text in the input text box.
        obj_current_note.delete(1.0, END)

        # Generate the note that should be printed to the log and the output file.
        to_write = f"{current_timestamp} {current_note}"

        # Print the current timestamp along with the current
        # text from the input text box to the screen.
        print_to_text(to_write, self.widgets.mapping["text_log"])

        # Print the current timestamp along with the current
        # text from the input text box to the output file.
        print_to_file(to_write, output_path, self.template.output_file_encoding)
