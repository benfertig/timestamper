#-*- coding: utf-8 -*-
"""This module contains the FileButtons class which is
called upon by the constructor of the Buttons class."""

from dataclasses import dataclass
from os import getcwd
from tkinter import NORMAL

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
class FileButtons():
    """This class stores the attributes for buttons associated with files."""

    def __init__(self):
        self.output_select = self.ButtonOutputSelect()
        self.merge_output_files = self.ButtonMergeOutputFiles()

    @dataclass
    class ButtonOutputSelect():
        """This class stores the attributes for the output file selection button."""

        initial_state = NORMAL

        text = "Choose output location"

        image_file_name = None
        message_file_name = None

        str_key = "button_output_select"

        window_str_key = "window_main"

        mac_disabled_color = "#d3d3d3"

        image_file_name = None

        starting_dir = getcwd()

        background = None
        foreground = None

        width = None
        height = 1

        column = 8
        row = 0

        columnspan = 2
        rowspan = 1

        padx = None
        pady = (5, 26)

        ipadx = 15
        ipady = None

        sticky = "nsew"

        to_enable_toggle = ("button_record", "button_save_note")

        font_family = ""
        font_size = 10
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class ButtonMergeOutputFiles():
        """This class stores the attributes for the merge output files button."""

        initial_state = NORMAL

        text = "Merge output files"

        image_file_name = None
        message_file_name = None

        str_key = "button_merge_output_files"

        window_str_key = "window_main"

        mac_disabled_color = "#d3d3d3"

        image_file_name = None

        starting_dir = getcwd()

        background = None
        foreground = None

        width = None
        height = 1

        column = 10
        row = 0

        columnspan = 1
        rowspan = 1

        padx = None
        pady = (5, 26)

        ipadx = None
        ipady = None

        sticky = "nsew"

        font_family = ""
        font_size = 10
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0
