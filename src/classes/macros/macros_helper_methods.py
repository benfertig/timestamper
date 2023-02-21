#-*- coding: utf-8 -*-
"""This module contains helper methods for button
macros. These methods do not rely on class variables."""

from os.path import exists, isdir
from re import match
from sys import platform
from tkinter import DISABLED, NORMAL, END, Button
from pyglet.media import load, Player
from pyglet.media.codecs.wave import WAVEDecodeException

if platform.startswith("darwin"):
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


def merge_success_message(merged_output_file_name):
    """This method generates the message that is displayed
    when the program has successfully merged output files."""

    return "MERGE SUCCESS\n\nYour merged notes have been saved in:\n" \
           f"\"{merged_output_file_name}\".\n\nClose this window to proceed."


def merge_failure_message_file_not_readable(unreadable_files):
    """This method generates the message that is displayed when the program
    cannot read one or more of the files that have been selected for a merge."""

    unreadable_files_str = \
        "\n".join(unreadable_files) if isinstance(unreadable_files, list) else unreadable_files

    return "MERGE FAILED\n\nThe following file(s) could not be opened:\n\n" \
           f"{unreadable_files_str}\n\nAre you sure you selected only text files?"


def enable_button(button, original_color=None):
    """This method enables a button. For certain buttons on Mac computers, visual modifications
    are also made to the button to make it easier to tell that the button is enabled."""

    # Enable the button.
    button["state"] = NORMAL

    # If 1) we are on a Mac, 2) the current button is a tkmacosx Button and
    # 3) the button has no text, then it will be hard to tell whether this
    # button is enabled unless we change its appearance. Therefore, the
    # tkmacosx button's background would be changed to its original color here.
    if platform.startswith("darwin") and isinstance(button, MacButton) and not button.cget("text"):
        button["background"] = original_color


def disable_button(button, mac_disabled_color=None):
    """This method disables a button. For certain buttons on Mac computers, visual modifications
    are also made to the button to make it easier to tell that the button is disabled."""

    # Enable the button temporarily.
    button["state"] = NORMAL

    # If 1) we are on a Mac, 2) the current button is a tkmacosx Button and
    # 3) the button has no text, then it will be hard to tell whether this button
    # is disabled unless we change its appearance. Therefore, the tkmacosx button's
    # background would be changed to the predetermined disabled color here.
    if platform.startswith("darwin") and isinstance(button, MacButton) and not button.cget("text"):
        button["background"] = mac_disabled_color

    # Disable the button.
    button["state"] = DISABLED


def button_enable_disable_macro(button_template, widgets):
    """This method, which is called upon by several button macros, will enable and
    disable the buttons associated with the string keys from the "to_enable" and
    "to_disable" attributes of a specific button from the TimeStamperTemplate class."""

    # Enable the buttons stored in the button template's "to_enable" variable.
    for str_to_enable in button_template["to_enable"]:
        if str_to_enable in widgets.original_colors:
            original_color = widgets.original_colors[str_to_enable]
        else:
            original_color = None
        enable_button(widgets[str_to_enable], original_color)

    # Disable the buttons stored in the button template's "to_disable" variable.
    for str_to_disable in button_template["to_disable"]:
        disable_button(widgets[str_to_disable], \
            button_template["mac_disabled_color"])


def toggle_widgets(widget_template, to_enable, template, widgets):
    """This method enables/disables the widgets in a template's to_enable_toggle attribute."""

    # Iterate through the widget string keys in this template's "to_enable_toggle" attribute.
    for str_widget in widget_template["to_enable_toggle"]:

        widget_toggle = widgets[str_widget]

        # Call the custom enable_button or disable_button method if the widget is a button.
        if isinstance(widget_toggle, Button) or \
            (platform.startswith("darwin") and isinstance(widget_toggle, MacButton)):
            if to_enable:
                enable_button(widget_toggle, widgets.original_colors[str_widget])
            else:
                disable_button(widget_toggle, template[str_widget]["mac_disabled_color"])

        # Simply enable/disable the widget if it is not a button.
        else:
            widget_toggle["state"] = NORMAL if to_enable else DISABLED


def checkbutton_enable_disable_macro(checkbutton_template, widgets):
    """This method, which is called upon by several checkbutton macros, will either
    enable (if the user has just checked the checkbutton) or disable (if the user has
    just unchecked the checkbutton) the widgets associated with the string keys from
    the "to_enable_toggle" attribute of the template associated with checkbutton_str."""

    # Store the checkbutton widget into a variable.
    checkbutton = widgets[checkbutton_template["str_key"]]

    # When a checkbutton is clicked, there may be some widgets that should
    # be enabled or disabled regardless of whether that click checked or
    # unchecked the checkbutton. Enable and disable any such widgets here.
    button_enable_disable_macro(checkbutton_template, widgets)

    # If this checkbutton is checked...
    if checkbutton.variable.get() == 1:

        # Record that this checkbutton is checked in this checkbutton's template.
        checkbutton_template["is_checked_loaded_value"] = True

        # Activate the relevant widgets for when this checkbutton is checked.
        for str_to_enable in checkbutton_template["to_enable_toggle"]:
            to_enable = widgets[str_to_enable]
            to_enable["state"] = NORMAL

    # If this checkbutton is unchecked...
    else:

        # Record that this checkbutton is unchecked in this checkbutton's template.
        checkbutton_template["is_checked_loaded_value"] = False

        # Deactivate the relevant widgets for when this checkbutton is unchecked.
        for str_to_disable in checkbutton_template["to_enable_toggle"]:
            to_disable = widgets[str_to_disable]
            to_disable["state"] = DISABLED


def copy_text_file_to_text_widget(file_full_path, file_encoding, text_obj):
    """This method prints the entire contents of the text file
    indicated by file_full_path to the text widget text_obj."""

    text_obj_initial_state = text_obj["state"]
    text_obj["state"] = NORMAL
    with open(file_full_path, "r", encoding=file_encoding) as out_file:
        for line in out_file.readlines():
            text_obj.insert(END, line)
            text_obj.see(END)
    text_obj["state"] = text_obj_initial_state


def verify_text_file(file_full_path, file_encoding, test_readability, test_writability):
    """This method verifies the readability and writability of a text file. Of
    the two boolean arguments, test_readability and test_writability, AT LEAST
    ONE of these should be set to True (they can also BOTH be set to True
    simultaneously). The reason that test_readability and test_writability should
    not both be set to False simultaneously is because, if this is the case, then
    this method will return True as long as the path corresponding to file_full_path
    exists and that path does not point to a directory, without checking whether
    the path provided in file_full_path corresponds to an actual text file."""

    # If the provided file path is actually a path to a directory, return False.
    if isdir(file_full_path) or not exists(file_full_path):
        return False

    # Try to load the file specified by file_full_path and see
    # if it can be read and written to as if it were a text file.
    try:
        if test_readability:
            with open(file_full_path, "r", encoding=file_encoding) as output_file:
                output_file.readlines()
        if test_writability:
            with open(file_full_path, "a+", encoding=file_encoding) as output_file:
                output_file.write("")

    # If the file CANNOT be read and written to like a text file, return False.
    except (FileNotFoundError, IOError, PermissionError, UnicodeDecodeError):
        return False

    # IF the file CAN be read and written to like a text file, return True.
    else:
        return True


def verify_audio_file(file_full_path, time_stamper):
    """This method verifies that an audio file can be loaded by Pyglet,
    and if so, stores the relevant audio source and audio player into
    class attributes of the passed instance of the time_stamper class."""

    # If the provided file path is actually a path to a
    # directory, erase the current audio source/audio player.
    if isdir(file_full_path) or not exists(file_full_path):
        time_stamper.audio_source, time_stamper.audio_player = None, None

    # Try loading the file specified by file_full_path into
    # a Pyglet media source and storing that media source.
    try:
        time_stamper.audio_source = load(file_full_path)

    # If the file CANNOT be loaded into a Pyglet media
    # source, erase the current audio source/audio player.
    except (EOFError, FileNotFoundError, WAVEDecodeException):
        time_stamper.audio_source, time_stamper.audio_player = None, None

    # If the file CAN be loaded into a Pyglet media player, declare
    # a new, empty audio player for the Time Stamper program.
    else:
        time_stamper.audio_player = Player()


def print_to_entry(to_print, entry_obj, wipe_clean=False):
    """This method prints the value stored in to_print to the entry widget entry_obj. An optional
    argument wipe_clean, which is set to False by default, determines whether any text currently
    displayed in the entry widget should be removed before the new text is displayed."""

    initial_state = entry_obj["state"]
    entry_obj["state"] = NORMAL
    if wipe_clean:
        entry_obj.delete(0, END)
    entry_obj.insert(END, to_print)
    entry_obj["state"] = initial_state


def print_to_text(to_print, text_obj, wipe_clean=False):
    """This method prints the value stored in to_print to the text widget text_obj. An optional
    argument wipe_clean, which is set to False by default, determines whether any text currently
    displayed in the text widget should be removed before the new text is displayed."""

    initial_state = text_obj["state"]
    text_obj["state"] = NORMAL
    if wipe_clean:
        text_obj.delete(1.0, END)
    text_obj.insert(END, to_print)
    text_obj.see(END)
    text_obj["state"] = initial_state


def print_to_file(to_print, file_path, file_encoding="utf-8", access_mode="a+"):
    """This method prints the value stored in to_print to the file specified in file_path."""

    if file_path:
        with open(file_path, access_mode, encoding=file_encoding) as out_file:
            out_file.write(to_print)


def rewind_or_fast_forward(user_input, is_rewind, adjust_timer_method):
    """This method is called by button_rewind_macro and button_fast_forward_macro in
    macros_buttons_media.py. The functions performed by both the rewind and fast-forward
    buttons are very similar, so their procedures have been condensed down to a single method
    here, and different parameters are passed depending on which button was pressed."""

    # Ensure that the requested rewind/fast-forward amount is a number.
    try:
        adjust_amount = int(user_input)

    # Do not rewind/fast-forward the timer if the requested rewind/fast-forward
    # amount is not a number (this should never happen because we have restricted the
    # rewind/fast-forward entry field to digits, but it never hurts to add a failsafe).
    except ValueError:
        return 0

    # Rewind the timer the requested amount.
    return adjust_timer_method(adjust_amount * -1 if is_rewind else adjust_amount)


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
                    # current file, so all new lines should NOT be considered part of the header.
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

                # If the current line is neither timestamped nor a part of the header, then add
                # the current line to the note that is currently being generated (this should only
                # occur when we have a non-timestamped note that appears below a timestamped note).
                else:
                    cur_note += line

    if cur_note:
        notes_body.append(cur_note)

    return header, notes_body


def merge_notes(files_to_read, output_file_encoding):
    """This method takes a list of file paths and merges the notes written to
    those files into one list sorted according the time each note was written."""

    # Read through the input files of notes and save the lines to a list.
    header, notes_body = store_timestamper_output(files_to_read, output_file_encoding)

    # Sort the list of notes gathered from all requested files.
    notes_body.sort()

    return header + notes_body
