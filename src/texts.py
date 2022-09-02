#-*- coding: utf-8 -*-
"""This module contains the Text class which is
called upon by the constructor of the Fields class."""

from dataclasses import dataclass
from tkinter import NORMAL, DISABLED

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
class Texts():
    """This module, which is called upon by the constructor of the Fields class,
    should be seen as an extension of the TimeStamperShell class, with attributes
    pertaining specifically to objects of type tkinter.Text in the Time Stamper program."""

    def __init__(self):

        self.log = self.TextLog()
        self.current_note = self.TextCurrentNote()

        self.all_shells = (
            self.log, self.current_note
        )

    @dataclass
    class TextLog():
        """This class stores the attributes for the text
        box where the user's past notes are displayed."""

        initial_state = DISABLED

        str_key = "text_log"

        width = 105
        height = 14

        column = 0
        row = 2

        columnspan = 19
        rowspan = 1

        padx = (5, 5)
        pady = None

        ipadx = None
        ipady = 33

        sticky = "nsew"

        font_family = ""
        font_size = 12
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class TextCurrentNote():
        """This class stores the attributes for the text
        box where the user's current note is displayed."""

        initial_state = NORMAL

        str_key = "text_current_note"

        width = 93
        height = 3

        column = 2
        row = 3

        columnspan = 17
        rowspan = 2

        padx = (0, 5)
        pady = (6, 0)

        ipadx = None
        ipady = None

        sticky = "nsew"

        font_family = ""
        font_size = 12
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0
