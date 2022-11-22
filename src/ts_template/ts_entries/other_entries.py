#-*- coding: utf-8 -*-
"""This module contains the OtherEntries class which is
called upon by the constructor of the Entries class."""

from dataclasses import dataclass
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
class OtherEntries():
    """This class contains subclasses storing attributes of Tkinter
    entries that do not fall into any other category of entry."""

    def __init__(self):
        self.rewind = self.EntryRewind()
        self.fast_forward = self.EntryFastForward()

    @dataclass
    class EntryRewind():
        """This class stores the attributes for the entry
        where the number of seconds to rewind is displayed."""

        initial_state = NORMAL

        max_digits = 2

        str_key = "entry_rewind"

        text = ""

        max_val = 99

        width = 2

        background = None
        foreground = None

        column = 3
        row = 1

        columnspan = 1
        rowspan = 1

        padx = None
        pady = 2

        ipadx = None
        ipady = None

        sticky = "ne"

        font_family = ""
        font_size = 11
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class EntryFastForward():
        """This class stores the attributes for the entry where
        the number of seconds to fast-forward is displayed."""

        initial_state = NORMAL

        max_digits = 2

        str_key = "entry_fast_forward"

        text = ""

        max_val = 99

        width = 2

        background = None
        foreground = None

        column = 5
        row = 1

        columnspan = 1
        rowspan = 1

        padx = None
        pady = 2

        ipadx = None
        ipady = None

        sticky = "ne"

        font_family = ""
        font_size = 11
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0
