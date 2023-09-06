#-*- coding: utf-8 -*-
"""This module stores the functions that are executed when
checkbuttons in the Time Stamper program are pressed."""

import classes
import methods.macros.methods_macros_helper as methods_helper

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


def checkbutton_pause_settings_macro():
    """This method will be executed when the pause settings checkbutton is pressed."""

    methods_helper.checkbutton_enable_disable_macro(\
        classes.template["checkbutton_pause_settings"])


def checkbutton_play_settings_macro():
    """This method will be executed when the play settings checkbutton is pressed."""

    methods_helper.checkbutton_enable_disable_macro(\
        classes.template["checkbutton_play_settings"])


def checkbutton_rewind_settings_macro():
    """This method will be executed when the rewind settings checkbutton is pressed."""

    methods_helper.checkbutton_enable_disable_macro(\
        classes.template["checkbutton_rewind_settings"])


def checkbutton_fast_forward_settings_macro():
    """This method will be executed when the fast-forward settings checkbutton is pressed."""

    methods_helper.checkbutton_enable_disable_macro(\
        classes.template["checkbutton_fast_forward_settings"])


def checkbutton_skip_backward_settings_macro():
    """This method will be executed when the skip backward settings checkbutton is pressed."""

    methods_helper.checkbutton_enable_disable_macro(\
        classes.template["checkbutton_skip_backward_settings"])


def checkbutton_skip_forward_settings_macro():
    """This method will be executed when the skip forward settings checkbutton is pressed."""

    methods_helper.checkbutton_enable_disable_macro(\
        classes.template["checkbutton_skip_forward_settings"])
