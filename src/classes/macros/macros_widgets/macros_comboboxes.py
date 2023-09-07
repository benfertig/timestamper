#-*- coding: utf-8 -*-
"""This module stores the functions that are executed when
comboboxes in the Time Stamper program are manipulated."""

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


def combobox_round_timestamp_settings_macro(*_):
    """This method will be executed when the combobox that alters the
    increment to which the timestamp gets rounded is manipulated."""

    # Enable and disable the relevant widgets for when the round timestamp combobox is manipulated.
    methods_helper.combobox_enable_disable_macro(\
        classes.template["combobox_round_timestamp_settings"])

    # Save the combobox's updated text in the combobox's template.
    combobox = classes.widgets["combobox_round_timestamp_settings"]
    combobox_template = classes.template["combobox_round_timestamp_settings"]
    combobox_template["text_loaded_value"] = combobox.get()
