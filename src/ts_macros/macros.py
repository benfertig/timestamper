#-*- coding: utf-8 -*-
"""This module contains the Macros class which stores the functions
that are executed when a button in the TimeStamper program is pressed."""

from .button_macros import ButtonMacros

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


class Macros():
    """This class stores all of the functions that are executed when a button
    in the TimeStamper program is pressed. This class' constructor takes one
    argument, template, which should be an instance of the TimeStamperTemplate class."""

    def __init__(self, template, widget_creators, timer):
        """The constructor initializes the Time Stamper template as well as dictionaries which
        map object string keys to their corresponding objects and corresponding macros."""

        self.template = template
        self.widget_creators = widget_creators

        self.button = ButtonMacros(template, widget_creators, timer)
