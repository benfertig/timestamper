#-*- coding: utf-8 -*-
"""This module contains the TimestampingButtons class which is
called upon by the constructor of the Buttons class."""

from dataclasses import dataclass
from tkinter import DISABLED, NORMAL

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


@dataclass
class TimestampingButtons():
    """This class stores the attributes for buttons associated with the timestamp function."""

    def __init__(self):
        self.timestamp = self.ButtonTimestamp()
        self.clear_timestamp = self.ButtonClearTimestamp()

    @dataclass
    class ButtonTimestamp():
        """This class stores the attributes for the timestamp button."""

        initial_state = NORMAL

        text = None
        image_file_name = "timestamp.png"

        str_key = "button_timestamp"

        window_str_key = "window_main"

        mac_disabled_color = "#d3d3d3"

        to_enable = ("button_clear_timestamp",)
        to_disable = ("button_timestamp",)

        background = None
        foreground = None

        width = None
        height = None

        column = 0
        row = 4

        columnspan = 1
        rowspan = 1

        padx = (10, 0)
        pady = None

        ipadx = None
        ipady = None

        sticky = "nsew"

        font_family = ""
        font_size = 12
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class ButtonClearTimestamp():
        """This class stores the attributes for the clear timestamp button."""

        initial_state = DISABLED

        text = None
        image_file_name = "clear_timestamp.png"

        str_key = "button_clear_timestamp"

        window_str_key = "window_main"

        mac_disabled_color = "#d3d3d3"

        to_enable = ("button_timestamp",)
        to_disable = ("button_clear_timestamp",)

        background = None
        foreground = None

        width = None
        height = 1

        column = 1
        row = 4

        columnspan = 1
        rowspan = 1

        padx = (0, 10)
        pady = None

        ipadx = None
        ipady = None

        sticky = "nsew"

        font_family = ""
        font_size = 10
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0
