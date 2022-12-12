#-*- coding: utf-8 -*-
"""This module contains the MediaButtonMacros class which stores the functions
that are executed when a media button in the Time Stamper program is pressed."""

from .macros_helper_methods import button_enable_disable_macro, \
    print_to_file, print_to_text, rewind_or_fast_forward

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

    def __init__(self, parent):
        self.parent = parent
        self.template = parent.template
        self.settings = parent.settings
        self.widgets = parent.widgets
        self.timer = parent.timer

    def media_button_macro(self, button_str_key, entry_str_key=None, is_rewind=True):
        """This method is called on by the macros for the pause, play, stop, rewind,
        fast-forward and record buttons. Since similar processes are executed for
        all of these buttons, their shared procedures have been condensed down to
        this method, where the arguments specific to each button can be passed."""

        button_template = self.template[button_str_key]

        # Enable and disable the relevant widgets for when this button is pressed.
        button_enable_disable_macro(button_template, self.widgets)

        # Get the timestamp before rewinding/fast-forwarding.
        first_timestamp = self.timer.current_time_to_timestamp()

        seconds_to_adjust_by = None

        # If there is an entry associated with this button, then that means
        # we are either rewinding or fast-forwarding, so we should rewind or
        # fast-forward the amount of seconds indicated by the relevant entry.
        if entry_str_key:

            # Rewind/fast-forward the timer the specified number of seconds.
            adjustment_input = self.widgets[entry_str_key].get()
            seconds_to_adjust_by = \
                rewind_or_fast_forward(adjustment_input, is_rewind, self.timer.adjust_timer)

            # Get the timestamp after rewinding/fast-forwarding.
            second_timestamp = self.timer.current_time_to_timestamp()

        # If the user has set a message to be printed
        # when this button is pressed, retrieve that message.
        button_message = self.parent.get_button_message_input(button_str_key)

        # Only print a message for this button if:
        #     1) a message was specified for this button
        #     2) the rewind/fast-forward amount was not zero seconds (this condition does not apply
        #        if the user pressed a media button other than the rewind or fast-forward button).
        if button_message is not None and seconds_to_adjust_by != 0:

            # If there is an entry associated with this button, then that means
            # we are either rewinding or fast-forwarding and we potentially need
            # to swap the user's input for the button's message with other values.
            if entry_str_key:

                seconds_to_adjust_by = str(abs(round(seconds_to_adjust_by, 2)))

                # Map the variables to their appropriate values.
                variable_mapping = {"$amount": seconds_to_adjust_by, "$dest": second_timestamp}

                # Replace any variables in the button message with their mapped values.
                button_message = " ".join([variable_mapping[word] \
                    if word in variable_mapping else word for word in button_message.split()])

            # Add the current timestamp to the message that will be printed.
            to_print = f"{first_timestamp} {button_message}\n"

            # Get the current output path from the output path entry widget.
            output_path = self.widgets["entry_output_path"].get()

            # Print the button's message, along with the current
            # timestamp, to the notes log and the output file.
            print_to_text(to_print, self.widgets["text_log"])
            print_to_file(to_print, output_path, self.settings["output"]["file_encoding"])

    def button_pause_macro(self):
        """This method will be executed when the pause button is pressed."""

        self.media_button_macro("button_pause")

        # Stop the timer.
        self.timer.pause()

    def button_play_macro(self):
        """This method will be executed when the play button is pressed."""

        self.media_button_macro("button_play")

        # Start the timer.
        self.timer.play()

    def button_stop_macro(self):
        """This method will be executed when the stop button is pressed."""

        self.media_button_macro("button_stop")

        # Stop the timer.
        self.timer.pause()

    def button_rewind_macro(self):
        """This method will be executed when the rewind button is pressed."""

        self.media_button_macro("button_rewind", "entry_rewind", is_rewind=True)

    def button_fast_forward_macro(self):
        """This method will be executed when the fast-forward button is pressed."""

        self.media_button_macro("button_fast_forward", "entry_fast_forward", is_rewind=False)

    def button_record_macro(self):
        """This method will be executed when the record
        button is pressed, and will begin the timer."""

        self.media_button_macro("button_record")

        # Start the timer.
        self.timer.play()
