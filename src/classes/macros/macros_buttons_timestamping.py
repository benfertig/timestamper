#-*- coding: utf-8 -*-
"""This module contains the TimestampingButtonMacros class which stores the functions
that are executed when a timestamping button in the Time Stamper program is pressed."""

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

class TimestampingButtonMacros():
    """This class stores all of the macros that execute when timestamping buttons are pressed."""

    def __init__(self, parent):
        self.template = parent.template
        self.widgets = parent.widgets
        self.timer = parent.timer

    def button_timestamp_macro(self, *_):
        """This method will be executed when the timestamp button is pressed."""

        # Make note of the fact that a timestamp has been set.
        self.template["label_timestamp"]["timestamp_set"] = True

        # Set the timestamp to the timer's current reading.
        obj_timestamp = self.widgets["label_timestamp"]
        obj_timestamp["text"] = self.timer.current_time_to_timestamp()

        # Enable and disable the relevant buttons for when the timestamp button is pressed.
        button_enable_disable_macro(self.template["button_timestamp"], self.widgets)

    def button_clear_timestamp_macro(self, *_):
        """This method will be executed when the "Clear timestamp" button is pressed."""

        # Make note of the fact that a timestamp has been cleared.
        self.template["label_timestamp"]["timestamp_set"] = False

        # Set the timestamp to the timer's current reading.
        obj_timestamp = self.widgets["label_timestamp"]
        obj_timestamp["text"] = self.timer.current_time_to_timestamp()

        # Enable and disable the relevant buttons for when the clear timestamp button is pressed.
        button_enable_disable_macro(self.template["button_clear_timestamp"], self.widgets)
