#-*- coding: utf-8 -*-
"""This module contains the Windows class which is called
upon by the constructor of the TimeStamperTemplate class."""

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
class Windows():
    """This class, which is called upon by the constructor of the TimeStamperTemplate class,
    should be seen as an extension of the TimeStamperTemplate class with attributes pertaining
    specifically to objects of type tkinter.Tk or tkinter.Toplevel in the Time Stamper program."""

    def __init__(self):

        self.str_key = "windows"

        # Map the window templates to their string keys.
        mapping = {}
        cur_dir = dirname(__file__)
        with open(join(cur_dir, "windows_main.json"), encoding="utf-8") as windows_main_json:
            mapping.update(load(windows_main_json))
        with open(join(cur_dir, "windows_info.json"), encoding="utf-8") as windows_info_json:
            mapping.update(load(windows_info_json))
        with open(join(cur_dir, "windows_merge.json"), encoding="utf-8") as windows_merge_json:
            mapping.update(load(windows_merge_json))
        self.mapping = mapping
