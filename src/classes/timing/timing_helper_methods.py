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

def pad_number(number, target_length):
    """This method pads a number with leading zeros to the desired length."""
    str_number = str(int(number)) if number else "0"
    str_number = "0" * (target_length - len(str_number)) + str_number
    return str_number

def h_m_s_to_seconds(hours, minutes, seconds, subseconds):
    """This method converts a time in hours, minutes and seconds to a time in seconds."""
    return (hours * 3600) + (minutes * 60) + seconds + (subseconds / 100)

def seconds_to_h_m_s(seconds_exact, pad=0):
    """This method converts a time in seconds to a time in hours, minutes and seconds."""

    # Convert the seconds to hours, minutes, seconds and subseconds.
    hours = seconds_exact // 3600
    seconds_exact -= (hours * 3600)
    minutes = seconds_exact // 60
    seconds_exact -= (minutes * 60)
    seconds = int(seconds_exact)
    subseconds = int((seconds_exact % 1) * 100)

    # Pad the timer's values with zeros if a pad value is passed as an argument.
    if pad > 0:
        hours = pad_number(hours, pad)
        minutes = pad_number(minutes, pad)
        seconds = pad_number(seconds, pad)
        subseconds = pad_number(subseconds, pad)

    return hours, minutes, seconds, subseconds
