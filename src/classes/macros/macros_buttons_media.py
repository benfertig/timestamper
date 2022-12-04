#-*- coding: utf-8 -*-
"""This module contains the MediaButtonMacros class which stores the functions
that are executed when a media button in the Time Stamper program is pressed."""

from tkinter import DISABLED, NORMAL, END
from .macros_helper_methods import button_enable_disable_macro

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


class MediaButtonMacros():
    """This class stores all of the macros that execute when media buttons are pressed."""

    def __init__(self, template, widgets, timer):
        self.template = template
        self.widgets = widgets
        self.timer = timer

    def button_pause_macro(self):
        """This method will be executed when the pause button is pressed."""

        # Enable and disable the relevant buttons for when the pause button is pressed.
        button_pause_template = self.template.mapping["button_pause"]
        button_enable_disable_macro(button_pause_template, self.widgets)

        # Pause the timer.
        self.timer.pause()

    def button_play_macro(self):
        """This method will be executed when the play button is pressed."""

        # Enable and disable the relevant buttons for when the play button is pressed.
        button_play_template = self.template.mapping["button_play"]
        button_enable_disable_macro(button_play_template, self.widgets)

        # Resume the timer.
        self.timer.play()

    def button_stop_macro(self):
        """This method will be executed when the stop button is pressed."""

        # Store the template for the stop button into an abbreviated file name.
        button_stop_template = self.template.mapping["button_stop"]

        # Enable and disable the relevant buttons for when the stop button is pressed.
        button_enable_disable_macro(button_stop_template, self.widgets)

        # Print the message that the timer has been stopped
        # with the current timestamp to the screen.
        current_timestamp = self.timer.current_time_to_timestamp()
        to_write = f"{current_timestamp} {button_stop_template['print_on_press']}\n"
        text_log = self.widgets.mapping["text_log"]
        text_log["state"] = NORMAL
        text_log.insert(END, to_write)
        text_log.see(END)
        text_log["state"] = DISABLED

        # Print the message that the timer has been stopped
        # with the current timestamp to the output file.
        label_output_path_template = self.template.mapping["label_output_path"]
        output_path = self.widgets.mapping["label_output_path"]["text"]
        if output_path != label_output_path_template["text"]:
            output_path = output_path[len(label_output_path_template["display_path_prefix"]):]
            with open(output_path, "a+", encoding=self.template.output_file_encoding) as out_file:
                out_file.write(to_write)

        # Stop the timer.
        self.timer.pause()

    def button_rewind_macro(self):
        """This method will be executed when the rewind button is pressed."""

        # Retrieve the rewind amount from the entry field.
        obj_rewind_amount = self.widgets.mapping["entry_rewind"]
        rewind_amount = obj_rewind_amount.get()

        # Ensure that the requested rewind amount is a number.
        try:
            rewind_amount = int(rewind_amount)

        # Do not rewind if the requested rewind amount is not a number
        # (this should never happen because we have restricted the rewind
        # amount entry field to digits, but it never hurts to add a failsafe).
        except ValueError:
            return

        # Rewind the timer the requested amount.
        else:
            self.timer.adjust_timer(-rewind_amount)

    def button_fast_forward_macro(self):
        """This method will be executed when the fast-forward button is pressed."""

        # Retrieve the fast-forward amount from the entry field.
        obj_fast_forward_amount = self.widgets.mapping["entry_fast_forward"]
        fast_forward_amount = obj_fast_forward_amount.get()

        # Ensure that the requested fast-forward amount is a number.
        try:
            fast_forward_amount = int(fast_forward_amount)

        # Do not rewind if the requested fast-forward amount is not a number
        # (this should never happen because we have restricted the fast-forward
        # amount entry field to digits, but it never hurts to add a failsafe).
        except ValueError:
            return

        # Fast-forward the timer the requested amount.
        else:
            self.timer.adjust_timer(fast_forward_amount)

    def button_record_macro(self):
        """This method will be executed when the record
        button is pressed, and will begin the timer."""

        # Store the template for the record button into an abbreviated file name.
        button_record_template = self.template.mapping["button_record"]

        # Get the currently displayed time from the timer and create a timestamp from it.
        current_timestamp = self.timer.current_time_to_timestamp()
        to_write = f"{current_timestamp} {button_record_template['print_on_press']}\n"

        # Print the message that the timer has started
        # with the current timestamp to the screen.
        text_log = self.widgets.mapping["text_log"]
        text_log["state"] = NORMAL
        text_log.insert(END, to_write)
        text_log.see(END)
        text_log["state"] = DISABLED

        # Print the message that the timer has started
        # with the current timestamp to the output file.
        label_output_path_template = self.template.mapping["label_output_path"]
        output_path = self.widgets.mapping["label_output_path"]["text"]
        if output_path != label_output_path_template["text"]:
            output_path = output_path[len(label_output_path_template["display_path_prefix"]):]
            with open(output_path, "a+", encoding=self.template.output_file_encoding) as out_file:
                out_file.write(to_write)

        # Enable and disable the relevant buttons for when the record button is pressed.
        button_enable_disable_macro(button_record_template, self.widgets)

        # Start the timer.
        self.timer.play()
