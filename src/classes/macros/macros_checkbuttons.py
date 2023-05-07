#-*- coding: utf-8 -*-
"""This module contains the CheckbuttonMacros class which stores the functions
that are executed when a checkbutton in the Time Stamper program is pressed."""

from .macros_helper_methods import checkbutton_enable_disable_macro

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


class CheckbuttonMacros():
    """This class stores all of the macros that execute when checkbuttons are pressed."""

    def __init__(self, parent):
        self.template = parent.template
        self.widgets = parent.widgets

    def checkbutton_pause_settings_macro(self):
        """This method will be executed when the pause settings checkbutton is pressed."""

        checkbutton_enable_disable_macro(self.template["checkbutton_pause_settings"], self.widgets)

    def checkbutton_play_settings_macro(self):
        """This method will be executed when the play settings checkbutton is pressed."""

        checkbutton_enable_disable_macro(self.template["checkbutton_play_settings"], self.widgets)

    def checkbutton_rewind_settings_macro(self):
        """This method will be executed when the rewind settings checkbutton is pressed."""

        checkbutton_enable_disable_macro(self.template["checkbutton_rewind_settings"], self.widgets)

    def checkbutton_fast_forward_settings_macro(self):
        """This method will be executed when the fast-forward settings checkbutton is pressed."""

        checkbutton_enable_disable_macro(\
            self.template["checkbutton_fast_forward_settings"], self.widgets)
