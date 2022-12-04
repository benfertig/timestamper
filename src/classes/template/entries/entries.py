#-*- coding: utf-8 -*-
"""This module contains the Entries class which is called upon by
the constructor of the Fields class (which is found in template.py)"""

from dataclasses import dataclass
from json import load
from os.path import dirname, join

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

        # Map the entry templates to their string keys.
        mapping = {}
        cur_dir = dirname(__file__)
        with open(join(cur_dir, "entries_timer.json"), encoding="utf-8") as entries_timer_json:
            mapping.update(load(entries_timer_json))
        with open(join(cur_dir, "entries_other.json"), encoding="utf-8") as entries_other_json:
            mapping.update(load(entries_other_json))
        self.mapping = mapping

        # Map the entry templates to the windows that they appear in.
        self.template_window_mapping = {
            "window_main":
                (mapping["entry_hours"], mapping["entry_minutes"],
                mapping["entry_seconds"], mapping["entry_subseconds"],
                mapping["entry_rewind"], mapping["entry_fast_forward"])
        }
