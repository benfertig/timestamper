#-*- coding: utf-8 -*-
"""This module contains the TimerEntries class which is
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
class TimerEntries():
    """This class contains subclasses storing attributes of Tkinter entries
    pertaining specifically to the timer in the Time Stamper program."""

    def __init__(self):

        self.num_hours = self.EntryHours()
        self.num_minutes = self.EntryMinutes()
        self.num_seconds = self.EntrySeconds()
        self.num_subseconds = self.EntrySubSeconds()

    @dataclass
    class EntryHours():
        """This class stores the attributes for the entry where
        the timer's current number of hours is displayed."""

        initial_state = NORMAL

        str_key = "entry_hours"

        text = "00"

        max_val = 99

        background = None
        foreground = None

        width = 2

        column = 12
        row = 5

        columnspan = 1
        rowspan = 2

        padx = (3, 0)
        pady = (8, 8)

        ipadx = None
        ipady = None

        sticky = "ne"

        font_family = ""
        font_size = 30
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class EntryMinutes():
        """This class stores the attributes for the entry where
        the timer's current number of minutes is displayed."""

        initial_state = NORMAL

        str_key = "entry_minutes"

        text = "00"

        max_val = 59

        width = 2

        background = None
        foreground = None

        column = 14
        row = 5

        columnspan = 1
        rowspan = 2

        padx = None
        pady = (8, 8)

        ipadx = None
        ipady = None

        sticky = "ne"

        font_family = ""
        font_size = 30
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class EntrySeconds():
        """This class stores the attributes for the entry where
        the timer's current number of seconds is displayed."""

        initial_state = NORMAL

        str_key = "entry_seconds"

        text = "00"

        max_val = 59

        width = 2

        background = None
        foreground = None

        column = 16
        row = 5

        columnspan = 1
        rowspan = 2

        padx = None
        pady = (8, 8)

        ipadx = None
        ipady = None

        sticky = "ne"

        font_family = ""
        font_size = 30
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class EntrySubSeconds():
        """This class stores the attributes for the entry where
        the timer's current number of subseconds is displayed."""

        initial_state = NORMAL

        str_key = "entry_subseconds"

        text = "00"

        max_val = 99

        width = 2

        background = None
        foreground = None

        column = 18
        row = 5

        columnspan = 1
        rowspan = 2

        padx = None
        pady = (8, 8)

        ipadx = None
        ipady = None

        sticky = "ne"

        font_family = ""
        font_size = 30
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0
