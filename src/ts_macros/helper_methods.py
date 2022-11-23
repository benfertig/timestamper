#-*- coding: utf-8 -*-
"""This module contains helper methods for Macros and ButtonMacros
classes. These methods do not rely on class variables."""

from re import match
from sys import platform
from tkinter import DISABLED, NORMAL

if platform == "darwin":
    from tkmacosx.widget import Button as MacButton

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


def enable_button(button, original_color):
    """This method enables a button. For certain buttons on Mac computers, visual modifications
    are also made to the button to make it easier to tell that the button is enabled."""

    # Enable the button.
    button["state"] = NORMAL

    # If 1) we are on a Mac, 2) the current button is a tkmacosx Button and
    # 3) the button has no text, then it will be hard to tell whether this
    # button is enabled unless we change its appearance. Therefore, the
    # tkmocosx button's background would be changed to its original color here.
    if platform == "darwin" and isinstance(button, MacButton) and not button.cget("text"):
        button["background"] = original_color


def disable_button(button, mac_disabled_color):
    """This method disables a button. For certain buttons on Mac computers, visual modifications
    are also made to the button to make it easier to tell that the button is disabled."""

    # Enable the button temporarily.
    button["state"] = NORMAL

    # If 1) we are on a Mac, 2) the current button is a tkmacosx Button and
    # 3) the button has no text, then it will be hard to tell whether this button
    # is disabled unless we change its appearance. Therefore, the tkmacosx button's
    # background would be changed to the predetermined disabled color here.
    if platform == "darwin" and isinstance(button, MacButton) and not button.cget("text"):
        button["background"] = mac_disabled_color

    # Disable the button.
    button["state"] = DISABLED


def store_timestamper_output(output_file_paths, output_file_encoding="utf-8"):
    """This method reads through timestamper output files saved in "all_files" (which should
    be a list of file paths) and saves the notes stored in these files to a list."""

    all_notes = []
    cur_note = ""

    # Iterate over every file specified in "output_file_paths".
    for input_file in output_file_paths:
        with open(input_file, "r", encoding=output_file_encoding) as in_file:
            for line in in_file:

                # If we come across a line that begins with a timestamp, we should start with
                # a new entry in the notes list. Any non-timestamped lines will be added to the
                # entry that is already being generated. Doing it this way allows us to group
                # non-timestamped lines with the closest timestamped line that appears above.
                # If the user did not edit the text files after writing to them with the
                # Time Stamper program, there should be no non-timestamped lines. However,
                # if the user did add their own lines afterwards, those lines will appear
                # below the closest timestamped line that they were originally written under.
                if match("\\[\\d{2}:\\d{2}:\\d{2}.\\d{2}\\]", line[:13]) and cur_note:
                    all_notes.append(cur_note)
                    cur_note = ""
                cur_note += line
    if cur_note:
        all_notes.append(cur_note)

    return all_notes


def find_beginnings_and_ends(button_record_message, button_stop_message, notes):
    """This method takes raw timestamper outputs as an argument and returns all of
    the lines from that output marking the beginnings and endings of recordings."""

    beginnings, ends = [], []
    for i, note in enumerate(notes):
        len_start_note = 14 + len(button_record_message)
        len_end_note = 14 + len(button_stop_message)
        if len(note) >= len_start_note and note[14:len_start_note] == button_record_message:
            beginnings.append(i)
        elif len(note) >= len_end_note and note[14:len_end_note] == button_stop_message:
            ends.append(i)

    return beginnings, ends


def remove_from_notes(record_message, stop_message, notes, beginnings_to_remove, ends_to_remove):
    """This method takes 3 arguments:
        1)  "notes": raw timestamper output which has been stored in a list
        2)  "beginnings_to_remove": a list of line indices marking the beginnings of
            timestamper recordings whose corresponding lines should be removed from "notes"
        3)  "ends_to_remove": a list of line indices marking the ends of timestamper
            recordings whose corresponding lines should be removed from "notes"
    This method then returns the data stored in "notes" with the lines at the
    indices stored in "beginnings_to_remove" and "ends_to_remove" excluded."""

    notes_updated = []

    for j, note in enumerate(notes):

        # Remove the timestamped notes indicating the beginning of a recording.
        if j in beginnings_to_remove:
            note = note[14 + len(record_message) + 1:]

        # Remove the timestamped notes indicating the ending of a recording.
        elif j in ends_to_remove:
            note = note[14 + len(stop_message) + 1:]

        # Add the note to the updated notes list if there is a note to add.
        if note:
            notes_updated.append(note)

    return notes_updated


def merge_notes(files_to_read, button_record_message, \
    button_stop_message, output_file_encoding):
    """This method takes a list of file paths and merges the notes written
    to those files into one list sorted by the time each note was written."""

    # Read through the input files of notes and save the lines to a list.
    all_notes = store_timestamper_output(files_to_read, output_file_encoding)

    # Sort the list of notes gathered from all requested files.
    all_notes.sort()

    # Find the timestamped notes in the selected files
    # that indicate beginnings and endings of recordings.
    beginnings, ends = find_beginnings_and_ends(button_record_message, \
        button_stop_message, all_notes)

    # Prepare the timestamped notes indicating beginnings and endings
    # of recordings for deletion by excluding from the deletion:
    #   1) the earliest timestamped note indicating a beginning
    #   2) the last timestamped note indicating an ending.
    if beginnings:
        beginnings.pop(0)
    if ends:
        ends.pop()

    # Convert the LISTS storing the indices of lines indicating beginnings
    # and endings of recordings to SETS to make lookup time faster.
    beginnings = set(beginnings)
    ends = set(ends)

    # Update the list of notes, removing redundant timestamped
    # notes indicating beginnings and endings of recordings.
    notes_updated = remove_from_notes(button_record_message, \
        button_stop_message, all_notes, beginnings, ends)

    return notes_updated
