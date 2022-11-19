#-*- coding: utf-8 -*-
"""This module contains the OtherLabels class which is
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
class OtherLabels():
    """This class contains subclasses storing attributes of Tkinter
    labels that do not fall under any other category of label."""

    @dataclass
    class LabelOutputPath():
        """This class stores the attributes for the label
        displaying the path to the current output file."""

        display_path_prefix = "Saving notes to: "

        text = "-----PLEASE SELECT AN OUTPUT FILE-----"

        str_key = "label_output_path"

        background = None
        foreground = None

        wraplength = 550

        justify = "left"

        width = None
        height = 1

        column = 8
        row = 0

        columnspan = 9
        rowspan = 1

        padx = None
        pady = None

        ipadx = None
        ipady = None

        sticky = "sw"

        font_family = ""
        font_size = 10
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class LabelRewindSec():
        """This class stores the attributes for the label (by default "sec") of
        the entry where the desired number of seconds to rewind is entered."""

        text = "sec"

        str_key = "label_rewind_sec"

        background = None
        foreground = None

        wraplength = None

        justify = "left"

        width = 3
        height = 1

        column = 4
        row = 1

        columnspan = 1
        rowspan = 1

        padx = None
        pady = None

        ipadx = None
        ipady = None

        sticky = "nw"

        font_family = ""
        font_size = 11
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class LabelFastForwardSec():
        """This class stores the attributes for the label (by default "sec") of the
        entry where the desired number of seconds to fast-forward is entered."""

        text = "sec"

        str_key = "label_fast_forward_sec"

        background = None
        foreground = None

        wraplength = None

        justify = "left"

        width = 3
        height = 1

        column = 6
        row = 1

        columnspan = 1
        rowspan = 1

        padx = None
        pady = None

        ipadx = None
        ipady = None

        sticky = "nw"

        font_family = ""
        font_size = 11
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class LabelTimestamp():
        """This class stores the attributes for the
        label displaying the current timestamp."""

        text = "[00:00:00.00]"

        str_key = "label_timestamp"

        background = None
        foreground = None

        wraplength = None

        justify = "center"

        width = None
        height = None

        column = 0
        row = 3

        columnspan = 2
        rowspan = 1

        padx = None
        pady = (5, 0)

        ipadx = None
        ipady = None

        sticky = "nsew"

        font_family = ""
        font_size = 12
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0
