#-*- coding: utf-8 -*-
"""This module contains the TimerLabels class which is
called upon by the constructor of the Labels class."""

from dataclasses import dataclass

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
class TimerLabels():
    """This class contains subclasses storing attributes of Tkinter labels
    pertaining specifically to the timer in the Time Stamper program."""

    def __init__(self):

        self.hrs = self.LabelHrs()
        self.min = self.LabelMin()
        self.dot = self.LabelDot()
        self.sec = self.LabelSec()

    @dataclass
    class LabelHrs():
        """This class stores the attributes for the
        label (by default "h") of the timer's hour field."""

        text = "h"

        str_key = "label_hrs"

        background = None
        foreground = None

        wraplength = None

        justify = "left"

        width = 1
        height = 1

        column = 13
        row = 5

        columnspan = 1
        rowspan = 2

        padx = None
        pady = (7, 0)

        ipadx = None
        ipady = None

        sticky = "nw"

        font_family = ""
        font_size = 30
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class LabelMin():
        """This class stores the attributes for the
        label (by default "m") of the timer's minutes field."""

        text = "m"

        str_key = "label_min"

        background = None
        foreground = None

        wraplength = None

        justify = "left"

        width = 1
        height = 1

        column = 15
        row = 5

        columnspan = 1
        rowspan = 2

        padx = 2
        pady = (7, 0)

        ipadx = None
        ipady = None

        sticky = "nw"

        font_family = ""
        font_size = 30
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class LabelDot():
        """This class stores the attributes for the label
        (by default ".") displayed before timer's subseconds field."""

        text = "."

        str_key = "label_dot"

        background = None
        foreground = None

        wraplength = None

        justify = "left"

        width = 1
        height = 1

        column = 17
        row = 5

        columnspan = 1
        rowspan = 2

        padx = None
        pady = (7, 0)

        ipadx = None
        ipady = None

        sticky = "nw"

        font_family = ""
        font_size = 30
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class LabelSec():
        """This class stores the attributes for the label
        (by default "s") of the timer's seconds field."""

        text = "s"

        str_key = "label_s"

        background = None
        foreground = None

        wraplength = None

        justify = "left"

        width = 1
        height = 1

        column = 19
        row = 5

        columnspan = 1
        rowspan = 2

        padx = None
        pady = (7, 0)

        ipadx = None
        ipady = None

        sticky = "nw"

        font_family = ""
        font_size = 30
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0
