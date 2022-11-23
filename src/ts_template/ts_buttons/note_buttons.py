#-*- coding: utf-8 -*-
"""This module contains the NoteButtons class which is
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
class NoteButtons():
    """This class stores the attributes for buttons associated with typing notes."""

    def __init__(self):
        self.cancel_note = self.ButtonCancelNote()
        self.save_note = self.ButtonSaveNote()

    @dataclass
    class ButtonCancelNote():
        """This class stores the attributes for the cancel note button."""

        initial_state = NORMAL

        text = "Cancel note"
        image_file_name = None

        str_key = "button_cancel_note"

        window_str_key = "window_main"

        mac_disabled_color = "#d3d3d3"

        to_enable = ()
        to_disable = ()

        background = "#E06666"
        foreground = None

        width = 12
        height = 1

        column = 2
        row = 5

        columnspan = 6
        rowspan = 2

        padx = (0, 4)
        pady = (8, 8)

        ipadx = None
        ipady = None

        sticky = "nsew"

        font_family = ""
        font_size = 19
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class ButtonSaveNote():
        """This class stores the attributes for the save note button."""

        initial_state = DISABLED

        text = "Save note"

        str_key = "button_save_note"

        window_str_key = "window_main"

        mac_disabled_color = "#d3d3d3"

        image_file_name = None

        to_enable = ()
        to_disable = ()

        background = "#93C47D"
        foreground = None

        width = 12
        height = 1

        column = 8
        row = 5

        columnspan = 4
        rowspan = 2

        padx = (4, 3)
        pady = (8, 8)

        ipadx = None
        ipady = None

        sticky = "nsew"

        font_family = ""
        font_size = 19
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0
