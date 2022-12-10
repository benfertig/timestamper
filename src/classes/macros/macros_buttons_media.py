#-*- coding: utf-8 -*-
"""This module contains the MediaButtonMacros class which stores the functions
that are executed when a media button in the Time Stamper program is pressed."""

from .macros_helper_methods import button_enable_disable_macro, \
    print_button_message, rewind_or_fast_forward

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

    def __init__(self, template, settings, widgets, timer):
        self.template = template
        self.settings = settings
        self.widgets = widgets
        self.timer = timer

    def media_button_macro(self, button_template):
        """This method is called on by the macros for the pause, play, stop, rewind,
        fast-forward and record buttons. Since similar processes are executed for
        all of these buttons, their shared procedures have been condensed down to
        this method, where the arguments specific to each button can be passed."""

        # Enable and disable the relevant widgets for when this button is pressed.
        button_enable_disable_macro(button_template, self.widgets)

        # If the user has set a message to be printed
        # when this button is pressed, print that message.
        print_button_message(button_template, self.template, \
            self.settings, self.widgets, self.timer)

    def button_pause_macro(self):
        """This method will be executed when the pause button is pressed."""

        self.media_button_macro(self.template["button_pause"])

        # Stop the timer.
        self.timer.pause()

    def button_play_macro(self):
        """This method will be executed when the play button is pressed."""

        self.media_button_macro(self.template["button_play"])

        # Start the timer.
        self.timer.play()

    def button_stop_macro(self):
        """This method will be executed when the stop button is pressed."""

        self.media_button_macro(self.template["button_stop"])

        # Stop the timer.
        self.timer.pause()

    def button_rewind_macro(self):
        """This method will be executed when the rewind button is pressed."""

        self.media_button_macro(self.template["button_rewind"])

        # Rewind the timer the specified number of seconds.
        rewind_input = self.widgets["entry_rewind"].get()
        rewind_or_fast_forward(rewind_input, True, self.timer.adjust_timer)

    def button_fast_forward_macro(self):
        """This method will be executed when the fast-forward button is pressed."""

        self.media_button_macro(self.template["button_fast_forward"])

        # Fast-forward the timer the specified number of seconds.
        fast_forward_input = self.widgets["entry_fast_forward"].get()
        rewind_or_fast_forward(fast_forward_input, False, self.timer.adjust_timer)

    def button_record_macro(self):
        """This method will be executed when the record
        button is pressed, and will begin the timer."""

        self.media_button_macro(self.template["button_record"])

        # Start the timer.
        self.timer.play()
