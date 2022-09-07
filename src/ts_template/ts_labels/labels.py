#-*- coding: utf-8 -*-
"""This module contains the Label class which is
called upon by the constructor of the Fields class."""

from dataclasses import dataclass
from .timer_labels import TimerLabels
from .separate_window_labels import SeparateWindowLabels
from .other_labels import OtherLabels

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

        other_labels = OtherLabels()
        self.output_path = other_labels.LabelOutputPath()
        self.rewind_sec = other_labels.LabelRewindSec()
        self.fast_forward_sec = other_labels.LabelFastForwardSec()
        self.timestamp = other_labels.LabelTimestamp()

        # Do not include any labels from the SeparateWindowLabels class in
        # self.all_templates because self.all_templates is only meant to store the
        # templates for objects that we would like to create immediately when the
        # program starts. Any objects that are part of separate windows will only be
        # created when the user performs an action that triggers that window's creation.
        self.all_templates = (
            self.timer.hrs, self.timer.min, self.timer.dot, self.timer.sec, \
            self.output_path, self.rewind_sec, self.fast_forward_sec, self.timestamp
        )
