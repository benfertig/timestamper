#-*- coding: utf-8 -*-
"""This module stores the functions that are executed when
timestamping buttons in the Time Stamper program are pressed."""

import classes
import methods.macros.methods_macros_helper as methods_helper

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


def button_timestamp_macro(*_):
    """This method will be executed when the timestamp button is pressed."""

    # Make note of the fact that a timestamp has been set.
    classes.template["label_timestamp"]["timestamp_set"] = True

    # Set the timestamp to the timer's current reading.
    obj_timestamp = classes.widgets["label_timestamp"]
    obj_timestamp["text"] = classes.timer.current_time_to_timestamp()

    # Enable and disable the relevant buttons for when the timestamp button is pressed.
    methods_helper.button_enable_disable_macro(classes.template["button_timestamp"])


def button_clear_timestamp_macro(*_):
    """This method will be executed when the "Clear timestamp" button is pressed."""

    # Make note of the fact that a timestamp has been cleared.
    classes.template["label_timestamp"]["timestamp_set"] = False

    # Set the timestamp to the timer's current reading.
    obj_timestamp = classes.widgets["label_timestamp"]
    obj_timestamp["text"] = classes.timer.current_time_to_timestamp()

    # Enable and disable the relevant buttons for when the clear timestamp button is pressed.
    methods_helper.button_enable_disable_macro(classes.template["button_clear_timestamp"])
