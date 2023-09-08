#-*- coding: utf-8 -*-
"""This module stores the functions that are executed when
note buttons in the Time Stamper program are pressed."""

import classes
import methods.macros.methods_macros_output as methods_output

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


def button_hotkey_1_macro(*_):
    """This method will be executed when hotkey 1 is pressed."""

    # Timestamp and print the message associated with hotkey 1.
    button_hotkey_1_message = methods_output.get_button_message_input("button_hotkey_1")
    methods_output.print_timestamped_message(button_hotkey_1_message)


def button_hotkey_2_macro(*_):
    """This method will be executed when hotkey 2 is pressed."""

    # Timestamp and print the message associated with hotkey 2.
    button_hotkey_2_message = methods_output.get_button_message_input("button_hotkey_2")
    methods_output.print_timestamped_message(button_hotkey_2_message)


def button_hotkey_3_macro(*_):
    """This method will be executed when hotkey 3 is pressed."""

    # Timestamp and print the message associated with hotkey 3.
    button_hotkey_3_message = methods_output.get_button_message_input("button_hotkey_3")
    methods_output.print_timestamped_message(button_hotkey_3_message)


def button_cancel_note_macro(*_):
    """This method will be executed when the "Cancel note" button is pressed."""

    # Clear the current note from the input text box.
    methods_output.print_to_text("", classes.widgets["text_current_note"], wipe_clean=True)


def button_save_note_macro(*_):
    """This method will be executed when the "Save note" button is pressed."""

    # Get the current text in the input text box.
    obj_current_note = classes.widgets["text_current_note"]
    current_note = obj_current_note.get(1.0, "end-1c")

    # Clear the current text in the input text box.
    methods_output.print_to_text("", obj_current_note, wipe_clean=True)

    timestamp = classes.widgets["label_timestamp"]["text"]

    # Print the message in the input text box with the timestamp.
    methods_output.print_timestamped_message(current_note, timestamp)
