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
    # tkmacosx button's background would be changed to its original color here.
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


def print_button_message(button_template, template, settings, widgets, timer):
    """This method, which is called upon by several button macros, uses a
    button's template to determine whether a message should be printed when
    the button is pressed. If a determination is made to print a message, then
    the button's message will be printed to both the log and the output file."""

    # Determine whether a potential message exists for this button.
    if "print_on_press" in button_template:

        should_print = True
        print_on_press_val = button_template["print_on_press"]

        # If the text that gets printed when this button is
        # pressed is based on attributes stored elsewhere.
        if isinstance(print_on_press_val, dict):

            print_on_press_dict = print_on_press_val
            linked_dict_str = print_on_press_dict["linked_dict"]

            # Determine whether this button's message information
            # is stored in the settings or in the template.
            if linked_dict_str in settings.user:
                linked_dict = settings[linked_dict_str]
            else:
                linked_dict = template[linked_dict_str]

            # Determine the button's message.
            print_message_key = print_on_press_dict["print_message_attribute"]
            print_on_press_val = linked_dict[print_message_key]

            # Determine whether the button's associated message should be printed.
            if "print_bool_attribute" in print_on_press_dict:
                print_bool_key = print_on_press_dict["print_bool_attribute"]
                should_print = linked_dict[print_bool_key]

        if should_print:

            # Add the current timestamp to the message that will be printed.
            to_print = f"{timer.current_time_to_timestamp()} {print_on_press_val}\n"

            # Retrieve the putput path settings.
            output_settings = settings["output"]

            # Print the button's message, along with the current
            # timestamp, to the notes log and the output file.
            print_to_text(to_print, widgets["text_log"])
            print_to_file(to_print, output_settings["path"], output_settings["file_encoding"])


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
