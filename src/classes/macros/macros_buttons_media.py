#-*- coding: utf-8 -*-
"""This module contains the MediaButtonMacros class which stores the functions
that are executed when a media button in the Time Stamper program is pressed."""

from .macros_helper_methods import button_enable_disable_macro, \
    record_or_stop, rewind_or_fast_forward

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

        # Enable and disable the relevant buttons, print a timestamped note indiciating
        # the end of a recording to the log and the output file, and stop the timer.
        button_stop_template = self.template.mapping["button_stop"]
        record_or_stop(self.template, button_stop_template, self.widgets, \
            self.timer.current_time_to_timestamp, self.timer.pause)

    def button_rewind_macro(self):
        """This method will be executed when the rewind button is pressed."""

        # Rewind the timer the specified number of seconds.
        rewind_input = self.widgets.mapping["entry_rewind"].get()
        rewind_or_fast_forward(rewind_input, True, self.timer.adjust_timer)

    def button_fast_forward_macro(self):
        """This method will be executed when the fast-forward button is pressed."""

        # Fast-forward the timer the specified number of seconds.
        fast_forward_input = self.widgets.mapping["entry_fast_forward"].get()
        rewind_or_fast_forward(fast_forward_input, False, self.timer.adjust_timer)

    def button_record_macro(self):
        """This method will be executed when the record
        button is pressed, and will begin the timer."""

        # Enable and disable the relevant buttons, print a timestamped note indiciating
        # the beginning of a recording to the log and the output file, and stop the timer.
        button_record_template = self.template.mapping["button_record"]
        record_or_stop(self.template, button_record_template, self.widgets, \
            self.timer.current_time_to_timestamp, self.timer.play)
