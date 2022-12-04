#-*- coding: utf-8 -*-
"""This module contains helper methods for button
macros. These methods do not rely on class variables."""

from re import match
from sys import platform
from tkinter import DISABLED, NORMAL, END

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


def button_enable_disable_macro(button_template, widgets):
    """This method, which is called upon by several button macros, will enable and
    disable the buttons associated with the string keys from the "to_enable" and
    "to_disable" attributes of a specific Button from the TimeStamperTemplate class."""

    # Enable the buttons stored in the button template's "to_enable" variable.
    for str_to_enable in button_template["to_enable"]:
        if str_to_enable in widgets.original_colors:
            original_color = widgets.original_colors[str_to_enable]
        else:
            original_color = None
        enable_button(widgets.mapping[str_to_enable], original_color)

    # Disable the buttons stored in the button template's "to_disable" variable.
    for str_to_disable in button_template["to_disable"]:
        disable_button(widgets.mapping[str_to_disable], \
            button_template["mac_disabled_color"])


def print_to_text(to_print, text_obj):
    """This method prints the value stored in to_print to the text widget text_obj."""

    initial_state = text_obj["state"]
    text_obj["state"] = NORMAL
    text_obj.insert(END, to_print)
    text_obj.see(END)
    text_obj["state"] = initial_state


def print_to_file(to_print, file_path, file_encoding="utf-8"):
    """This method prints the value stored in to_print to the file specified in file_path."""

    if file_path:
        with open(file_path, "a+", encoding=file_encoding) as out_file:
            out_file.write(to_print)


def record_or_stop(template, button_template, widgets, timestamp_method, button_method):
    """This method is called by button_record_macro and button_stop_macro in
    macros_buttons_media.py. The functions performed by both the record and stop buttons
    are very similar, so their procedures have been condensed down to a single method
    here, and different parameters are passed depending on which button was pressed."""

    # Enable and disable the relevant buttons for when the record/stop button is pressed.
    button_enable_disable_macro(button_template, widgets)

    # Get the currently displayed time from the timer and create a timestamp from it.
    current_timestamp = timestamp_method()

    # Add the record/stop message to the timestamped note.
    to_write = f"{current_timestamp} {button_template['print_on_press']}\n"

    # Print the message that the timer has begun recording/been stopped
    # with the current timestamp to the screen.
    print_to_text(to_write, widgets.mapping["text_log"])

    # Print the message that the timer has begun recording/been stopped
    # with the current timestamp to the output file.
    print_to_file(to_write, template.output_path, template.output_file_encoding)

    # Begin/stop the timer.
    button_method()


def rewind_or_fast_forward(user_input, is_rewind, adjust_timer_method):
    """This method is called by button_rewind_macro and button_fast_forward_macro in
    macros_buttons_media.py. The functions performed by both the rewind and fast-forward
    buttons are very similar, so their procedures have been condensed down to a single method
    here, and different parameters are passed depending on which button was pressed."""

    # Ensure that the requested rewind/fast-forward amount is a number.
    try:
        adjust_amount = int(user_input)

    # Do not rewind/fast-forward the timer if the requested rewind amount is not a number.
    # This should never happen because we have restricted the rewind/fast-forward
    # amount entry field to digits, but it never hurts to add a failsafe).
    except ValueError:
        return

    # Rewind the timer the requested amount.
    else:
        adjust_timer_method(adjust_amount * -1 if is_rewind else adjust_amount)


def store_timestamper_output(output_file_paths, output_file_encoding="utf-8"):
    """This method reads through timestamper output files saved in "all_files" (which should
    be a list of file paths) and saves the notes stored in these files to a list."""

    header, notes_body, cur_note = [], [], ""

    # Iterate over every file specified in "output_file_paths".
    for input_file in output_file_paths:

        on_header = True

        with open(input_file, "r", encoding=output_file_encoding) as in_file:

            # Iterate over every line in the current file.
            for line in in_file:

                # If the current line begins with a timestamp...
                if match("\\[\\d{2}:\\d{2}:\\d{2}.\\d{2}\\]", line[:13]):

                    # If the current line begins with a timestamp, we can be certain that the
                    # program is finished reading in any non-timestamped lines at the top of the
                    # current file, so all new lines should not be considered part of the header.
                    on_header = False

                    # If a current note exists, append it to the
                    # notes list and begin generating a new note.
                    if cur_note:
                        notes_body.append(cur_note)
                        cur_note = ""

                    # Add the current line to the note that is currently being generated.
                    cur_note += line

                # If we have not yet reached a timestamped line in the current
                # file, consider the current line as part of the header.
                elif on_header:
                    header.append(line)

                # If the current line is neither timestamped nor a part of the header,
                # then add the current line to the note that is currently being
                # generated (this should only occur when we have a non-timestamped note
                # that we want to group with a timestamped note that appears above it).
                else:
                    cur_note += line

    if cur_note:
        notes_body.append(cur_note)

    return header, notes_body


def find_beginnings_and_ends(button_record_message, button_stop_message, notes):
    """This method takes raw timestamper output as an argument and returns the line
    indices from that output marking the beginnings and endings of recordings."""

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
    """This method takes 5 arguments:
        1) record_message: a string representing the message that gets timestamped
           and printed to the current output file whenever a recording begins
        2) stop_message: a string representing the message that gets timestamped
           and printed to the current output file whenever a recording ends
        3) notes: raw timestamper output which has been stored in a list and sorted
        4) beginnings_to_remove: a list of line indices marking the beginnings of
           timestamper recordings (i.e. timestamped notes beginning with record_message)
        5) ends_to_remove: a list of line indices marking the ends of timestamper
           recordings (i.e. timestamped notes beginning with stop_message)
    This method then returns the data stored in "notes" with the following modifications made:
        -  record_message and its timestamp will be removed from the
           lines whose indices are stored in beginnings_to_remove.
        -  stop_message and its timestamp will be removed from the
           lines whose indices are stored in ends_to_remove."""

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
    """This method takes a list of file paths and merges the notes written to
    those files into one list sorted according the time each note was written."""

    # Read through the input files of notes and save the lines to a list.
    header, notes_body = store_timestamper_output(files_to_read, output_file_encoding)

    # Sort the list of notes gathered from all requested files.
    notes_body.sort()

    # Find the timestamped notes in the selected files
    # that indicate beginnings and endings of recordings.
    beginnings, ends = find_beginnings_and_ends(button_record_message, \
        button_stop_message, notes_body)

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
        button_stop_message, notes_body, beginnings, ends)

    return header + notes_updated
