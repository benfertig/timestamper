#-*- coding: utf-8 -*-
"""This module contains the Label class which is
called upon by the constructor of the Fields class."""

from dataclasses import dataclass
from .timer_labels import TimerLabels
from .separate_window_labels import SeparateWindowLabels

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
class Labels():
    """This module, which is called upon by the constructor of the Fields class,
    should be seen as an extension of the TimeStamperTemplate class, with attributes
    pertaining specifically to objects of type tkinter.Label in the Time Stamper program."""

    def __init__(self):

        self.timer = TimerLabels()
        self.separate_windows = SeparateWindowLabels()

        self.output_path = self.LabelOutputPath()
        self.rewind_sec = self.LabelRewindSec()
        self.fast_forward_sec = self.LabelFastForwardSec()
        self.timestamp = self.LabelTimestamp()

        # Do not include any labels from the SeparateWindowLabels class in
        # self.all_templates because self.all_templates is only meant to store the
        # templates for objects that we would like to create immediately when the
        # program starts. Any objects that are part of separate windows will only be
        # created when the user performs an action that triggers that window's creation.
        self.all_templates = (
            self.timer.hrs, self.timer.min, self.timer.dot, self.timer.sec, \
            self.output_path, self.rewind_sec, self.fast_forward_sec, self.timestamp
        )

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

        column = 9
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

        text = "[—:—:—.—]"

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
