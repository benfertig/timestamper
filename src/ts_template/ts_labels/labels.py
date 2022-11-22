#-*- coding: utf-8 -*-
"""This module contains the Label class which is
called upon by the constructor of the Fields class."""

from dataclasses import dataclass
from .timer_labels import TimerLabels
from .info_labels import InfoLabels
from .merge_labels import MergeLabels
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

        self.str_key = "labels"

        self.timer = TimerLabels()
        self.info = InfoLabels()
        self.merge = MergeLabels()
        self.other = OtherLabels()

        # Do not include any labels from the InfoLabels or MergeLabels class in
        # self.main_window_templates because self.main_window_templates is only meant
        # to store the templates for objects that we would like to create immediately when
        # the program starts. Any objects that are part of separate windows will only be
        # created when the user performs an action that triggers that window's creation.
        self.main_window_templates = (
            self.timer.hrs, self.timer.min, self.timer.dot,\
            self.timer.sec, self.other.output_path, self.other.rewind_sec, \
            self.other.fast_forward_sec, self.other.timestamp
        )
