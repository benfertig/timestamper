#-*- coding: utf-8 -*-
"""This module contains the TimeStamperTemplate class which contains all
of the custom attributes for all of the objects called upon in the
TimeStamper run() method (the method that runs the Time Stamper program)."""

from dataclasses import dataclass
import sys
from os import getcwd, path
from .buttons.buttons import Buttons
from .entries.entries import Entries
from .labels.labels import Labels
from .texts.texts import Texts
from .windows.windows import Windows

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


def resource_path():
    """This method gets the absolute path to the resource."""

    try:
        res_path = sys._MEIPASS
    except AttributeError:
        res_path = path.abspath(".")

    return res_path


@dataclass
class TimeStamperTemplate():
    """
    This class does not store the TimeStamper objects themselves, but rather stores all of
    the attributes for all of the TimeStamper objects in an organized way. This serves two
    purposes:

        1) People will be able to locate and/or make changes to attributes quickly.

        2) The amount of code that needs to be written in other modules is reduced.
           For example, in the main TimeStamper class, all objects that are of
           the same type (Buttons, Labels, Entries, Texts, etc.) are placed by
           running a loop, where for each object template x_template, the position,
           dimensions, initial state, etc. of its corresponding object x can be
           retrieved by referencing x_template.x_coord, x_template.y_coord, x_template.width,
           x_template.height and x_template.initial_state among other attributes.
    """

    def __init__(self):

        self.output_file_encoding = "utf-8"
        self.output_path = None
        self.starting_dir = getcwd()
        self.images_dir = path.join(resource_path(), "images")
        self.messages_dir = path.join(resource_path(), "messages")

        widget_templates = (Buttons(), Entries(), Labels(), Texts(), Windows())
        self.mapping = {k: v for w_t in widget_templates for k, v in w_t.mapping.items()}
        for template in widget_templates:
            self.mapping[template.str_key] = template
