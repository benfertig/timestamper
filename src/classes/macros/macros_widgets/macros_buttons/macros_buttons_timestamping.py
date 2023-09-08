#-*- coding: utf-8 -*-
"""This module stores the functions that are executed when
timestamping buttons in the Time Stamper program are pressed."""

import methods.macros.methods_macros_timing as methods_timing

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


def button_timestamp_macro(*_):
    """This method will be executed when the timestamp button is pressed."""

    methods_timing.set_or_clear_timestamp(True)


def button_clear_timestamp_macro(*_):
    """This method will be executed when the "Clear timestamp" button is pressed."""

    methods_timing.set_or_clear_timestamp(False)
