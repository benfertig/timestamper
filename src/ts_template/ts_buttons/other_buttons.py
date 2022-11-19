#-*- coding: utf-8 -*-
"""This module contains the OtherButtons class which is
called upon by the constructor of the Buttons class."""

from dataclasses import dataclass
from os import getcwd
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
class OtherButtons():
    """This class stores the attributes the non-media
    buttons in the Time Stamper program."""

    def __init__(self):
        self.output_select = self.ButtonOutputSelect()
        self.merge_output_files = self.ButtonMergeOutputFiles()
        self.help = self.ButtonHelp()
        self.license = self.ButtonLicense()
        self.cancel_note = self.ButtonCancelNote()
        self.save_note = self.ButtonSaveNote()
        self.timestamp = self.ButtonTimestamp()
        self.clear_timestamp = self.ButtonClearTimestamp()

    @dataclass
    class ButtonOutputSelect():
        """This class stores the attributes for the output file selection button."""

        initial_state = NORMAL

        text = "Choose output location"
        image_file_name = None

        str_key = "button_output_select"

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

        str_key = "button_merge_output_files"

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

    @dataclass
    class ButtonTimestamp():
        """This class stores the attributes for the timestamp button."""

        initial_state = NORMAL

        text = None
        image_file_name = "timestamp.png"

        str_key = "button_timestamp"

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

    @dataclass
    class ButtonHelp():
        """This class stores the attributes for the help button."""

        initial_state = NORMAL

        text = "Help"
        image_file_name = None

        str_key = "button_help"

        background = None
        foreground = None

        width = 5
        height = 1

        column = 0
        row = 5

        columnspan = 2
        rowspan = 1

        padx = (10, 10)
        pady = (8, 0)

        ipadx = None
        ipady = None

        sticky = "nsew"

        font_family = ""
        font_size = 10
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class ButtonLicense():
        """This class stores the attributes for the license button."""

        initial_state = NORMAL

        text = "License/Credit"
        image_file_name = None

        str_key = "button_license"

        background = None
        foreground = None

        width = 5
        height = 1

        column = 0
        row = 6

        columnspan = 2
        rowspan = 1

        padx = (10, 10)
        pady = (0, 8)

        ipadx = None
        ipady = None

        sticky = "nsew"

        font_family = ""
        font_size = 10
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class ButtonCancelNote():
        """This class stores the attributes for the cancel note button."""

        initial_state = NORMAL

        text = "Cancel note"
        image_file_name = None

        str_key = "button_cancel_note"

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
