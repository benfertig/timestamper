#-*- coding: utf-8 -*-
"""This module contains the Entry class which is
called upon by the constructor of the Fields class."""

from dataclasses import dataclass
from .entries_timer import TimerEntries
from .entries_other import OtherEntries

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
class Entries():
    """This class, which is called upon by the constructor of the Fields class,
    should be seen as an extension of the TimeStamperTemplate class, with attributes
    pertaining specifically to objects of type tkinter.Entry in the Time Stamper program."""

    def __init__(self):

        self.str_key = "entries"

        self.timer = TimerEntries()
        self.other = OtherEntries()

        # Map the entry templates to the windows that they appear in.
        self.template_window_mapping = {
            "window_main":
                (self.timer.num_hours, self.timer.num_minutes, self.timer.num_seconds,
                self.timer.num_subseconds, self.other.rewind, self.other.fast_forward)
        }
