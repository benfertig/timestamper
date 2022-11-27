#-*- coding: utf-8 -*-
"""This module contains the Timing class, which is called upon by
the TimeStamperTimer class, and contains some helper methods for the
TimeStamperTimer that do not directly reference Tkinter widgets."""

from tkinter import DISABLED, NORMAL, END

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


def print_to_field(field, to_print):
    """This method displays the text stored in the argument to_print to the argument field."""

    # Determine whether the field is enabled.
    was_enabled = field["state"] == NORMAL

    # Print the passed information to the field.
    field["state"] = NORMAL
    field.delete(0, END)
    field.insert(0, to_print)

    # Disable field if is was disabled to begin with.
    if not was_enabled:
        field["state"] = DISABLED


def pad_number(number, target_length, pad_before):
    """This method pads a number to the desired length with leading zeros (if
    pad_before is set to True) or trailing zeros (if pad_before is set to False)."""

    str_number = str(number) if number else "0"
    zeros_to_add = "0" * (target_length - len(str_number))
    if pad_before:
        return zeros_to_add + str_number
    return str_number + zeros_to_add


def h_m_s_to_seconds(hours, minutes, seconds, subseconds):
    """This method converts a time in hours, minutes and seconds to a time in seconds."""
    return (hours * 3600) + (minutes * 60) + seconds + (subseconds / 100)


def seconds_to_h_m_s(seconds_exact, pad=0):
    """This method converts a time in seconds to a time in hours, minutes, seconds and subseconds.
    The optional integer argument pad, which is set to zero by default, will pad the returned
    hours, minutes, seconds and subseconds with zeros to the length specified by its value."""

    # Convert the seconds to hours, minutes, seconds and subseconds.
    hours = int(seconds_exact // 3600)
    seconds_exact = round(seconds_exact - (hours * 3600), 2)
    minutes = int(seconds_exact // 60)
    seconds_exact = round(seconds_exact - (minutes * 60), 2)
    seconds = int(seconds_exact)
    seconds_exact = round((seconds_exact % 1) * 100, 0)
    subseconds = int(seconds_exact)

    # Pad the timer's values with zeros if a pad value is passed as an argument.
    if pad > 0:
        hours = pad_number(hours, pad, True)
        minutes = pad_number(minutes, pad, True)
        seconds = pad_number(seconds, pad, True)
        subseconds = pad_number(subseconds, pad, True)

    return hours, minutes, seconds, subseconds
