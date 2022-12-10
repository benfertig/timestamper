#-*- coding: utf-8 -*-
"""This module contains helper methods for the TimeStamperTimer class
that do not directly rely on class variables of TimeStamperTimer."""

from tkinter import NORMAL, END

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
    """This method sets the text of "field" (which should be a Tkinter
    Entry) to whatever is stored in "to_print" (which should be a string)."""

    # Determine the field's state.
    initial_state = field["state"]

    # Print the passed information to the field.
    field["state"] = NORMAL
    field.delete(0, END)
    field.insert(0, to_print)

    # Set the field's state to whatever it was before this method began.
    field["state"] = initial_state


def pad_number(number, target_length, pad_before):
    """This method pads a number to target_length with leading zeros (if
    pad_before is set to True) or trailing zeros (if pad_before is set to False)."""

    str_number = str(number) if number else "0"
    zeros_to_add = "0" * (target_length - len(str_number))
    if pad_before:
        return zeros_to_add + str_number
    return str_number + zeros_to_add


def h_m_s_to_timestamp(hours, minutes, seconds, subseconds):
    """This method converts a time in hours, minutes, seconds and subseconds to a
    timestamp with the following format: [hours:minutes:seconds:subseconds]."""

    return f"[{hours}:{minutes}:{seconds}.{subseconds}]"


def h_m_s_to_seconds(hours, minutes, seconds, subseconds):
    """This method converts a time in hours, minutes,
    seconds and subseconds to a time in seconds."""

    return (hours * 3600) + (minutes * 60) + seconds + (subseconds / 100)


def seconds_to_h_m_s(seconds_exact, pad=0):
    """This method converts a time in seconds to a time in hours, minutes, seconds and
    subseconds. The optional integer argument pad, which is set to zero by default, provides
    the length to which the returned hours, minutes, seconds and subseconds should be padded."""

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

    return str(hours), str(minutes), str(seconds), str(subseconds)
