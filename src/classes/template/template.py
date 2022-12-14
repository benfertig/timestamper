#-*- coding: utf-8 -*-
"""This module contains the TimeStamperTemplate class which contains all
of the custom attributes for all of the objects called upon in the
TimeStamper run() method (the method that runs the Time Stamper program)."""

from dataclasses import dataclass
from os import getcwd
from os.path import dirname, join
from .template_helper_methods import map_all_templates

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
class TimeStamperTemplate():
    """
    This class does not store the Time Stamper objects themselves, but rather, stores all of
    the attributes for all of the Time Stamper objects in an organized way. This serves two
    purposes:

        1) People will be able to locate and/or make changes
           to the attributes of Time Stamper objects quickly.

        2) The amount of code that needs to be written in other modules is reduced. For example,
           in the main "time_stamper" class, all objects that are of the same type (Buttons,
           Labels, Entries, Texts, etc.) are placed by running a loop, where for each object
           template "x_template", the row, column, initial state, etc. of its corresponding
           object x can be retrieved by referencing template.mapping["x_template"]["row"],
           template.mapping["x_template"]["column"], and
           template.mapping["x_template"]["initial_state"] among other attributes.

    To edit the attributes of ANY widget in the Time Stamper program, edit the JSON
    files inside of the subdirectories that this file (template.py) is located in.
    """

    def __init__(self):

        source_dir = join(dirname(__file__), "..", "..")

        self.starting_dir = getcwd()
        self.images_dir = join(source_dir, "images")
        self.messages_dir = join(source_dir, "messages")

        self.mapping = map_all_templates(dirname(__file__))

    def __getitem__(self, item):
        return self.mapping[item]
