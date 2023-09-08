#-*- coding: utf-8 -*-
"""This module stores some extra methods associated with printing text output."""

from os.path import exists, isdir
from re import match
from tkinter import NORMAL, END

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


def attempt_button_message(button_str_key, timestamp=None, **user_variables):
    """This method determines whether a message should be printed when a media
    button is pressed, and, if it is determined that a message should be
    printed, prints that message to the notes log and the output file."""

    # Only attempt to print the button's message if there is an output path.
    if classes.time_stamper.output_path:

        # Get the button's message before replacements.
        button_message_pre_replace = get_button_message_input(button_str_key)

        # Only attempt to print a message if there is a message associated with the button.
        if button_message_pre_replace is not None:

            # Generate a timestamp if one was not provided.
            if timestamp is None:

                # Determine whether hours should be included in the
                # timestamp even when the time is below one hour.
                force_include_hours = \
                    classes.settings["always_include_hours_in_timestamp"]["is_enabled"]

                # Determine what increment the timestamp should be rounded to.
                round_to = classes.settings["round_timestamp"]["round_to_last"]

                # Generate the current timestamp.
                timestamp = classes.timer.current_time_to_timestamp(\
                    force_include_hours=force_include_hours, round_to=round_to)

            # Replace any variables in the button's message.
            button_message = replace_button_message_variables(\
                button_message_pre_replace, **user_variables)

            # Print the button's message.
            print_timestamped_message(button_message, timestamp)


def validate_output_file(file_full_path, erase_if_empty=False):
    """This method will check the validity of the path that is currently displayed in
    the output path entry widget to make sure it corresponds to a valid text file that
    can be read and written to. This method will then edit the configuration of the
    program depending on whether or not that path corresponds to a valid text file.
    The optional argument erase_if_empty, which is set to False by default, determines
    whether the previous output file should be cancelled if no output file is specified."""

    valid_text_file = True

    # If the a non-empty value was specified for the file path...
    if file_full_path:

        # Check whether the specified file path corresponds to a valid text file.
        valid_text_file = verify_text_file(file_full_path, True, True)

        # If the specified file path corresponds to a valid text file...
        if valid_text_file:

            # Store the output path as a class attribute of the TimeStamper class.
            classes.time_stamper.output_path = file_full_path

            # Configure the relevant widgets to reflect that a valid output
            # file IS active (distinct from enabling/disabling widgets).
            set_output_widgets(file_full_path)

            # Enable/disable the relevant widgets to reflect that a valid output file IS active.
            methods_helper.toggle_widgets(classes.template["button_output_select"], True)

            # The rewind/fast-forward buttons should NOT be enabled when a
            # media file is loaded, even when a valid output file IS loaded.
            if classes.time_stamper.media_player:
                methods_helper.disable_button(classes.widgets["button_rewind"], \
                    classes.template["button_rewind"]["mac_disabled_color"])
                methods_helper.disable_button(classes.widgets["button_fast_forward"], \
                    classes.template["button_fast_forward"]["mac_disabled_color"])

    # If EITHER no file path was specified and it was requested that the current output file be
    # disabled when no file path is specified, OR if a file path was specified and the file path
    # does not correspond to a valid text file, then reset and disable the relevant widgets.
    if (erase_if_empty and not file_full_path) or not valid_text_file:

        # Reset the output path in the TimeStamper class.
        classes.time_stamper.output_path = ""

        # Configure the relevant widgets to reflect that a valid output
        # file IS NOT active (distinct from enabling/disabling widgets).
        reset_output_widgets()

        # Enable/disable the relevant widgets to reflect that a valid output file IS NOT active.
        methods_helper.toggle_widgets(classes.template["button_output_select"], False)


def print_timestamped_message(message, timestamp=None):
    """This method takes a message, timestamps it, and then prints that timestamped
    message to the notes log and the output file (if no timestamp is provided,
    then a timestamp will be generated using the timer's current time)."""

    # If no timestamp was provided, set the timestamp to the timer's current time.
    if timestamp is None:

        # Determine whether hours should be included in the
        # timestamp even when the time is below one hour.
        force_include_hours = classes.settings["always_include_hours_in_timestamp"]["is_enabled"]

        # Determine what increment the timestamp should be rounded to.
        round_to = classes.settings["round_timestamp"]["round_to_last"]

        # Generate the current timestamp.
        timestamp = classes.timer.current_time_to_timestamp(\
            force_include_hours=force_include_hours, round_to=round_to)

    # Generate the complete message that should be printed, including the timestamp.
    to_print = f"\n{timestamp} {message}"

    # Print the message passed in the argument "message" along with
    # the current timestamp to the notes log and the output file.
    print_to_text(to_print, classes.widgets["text_log"])
    print_to_file(to_print, classes.time_stamper.output_path)


def get_button_message_input(button_str_key):
    """This method, which is called upon by several button macros, uses a button's
    template to determine whether a message should be printed when the button is pressed.
    If this method determines that a message should be printed when the button is pressed,
    then this method will return that message. Otherwise, this method will return None.
    Keep in mind that this method does not substitute potential variables (e.g., $amount
    and $dest for the skip backward and skip forward messages) in the returned message. Any
    variable substitution will need to be performed on the string returned by this method."""

    button_template = classes.template[button_str_key]

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
            if linked_dict_str in classes.settings.user:
                linked_dict = classes.settings[linked_dict_str]
            else:
                linked_dict = classes.template[linked_dict_str]

            # Determine the button's message.
            print_message_key = print_on_press_dict["print_message_attribute"]
            print_on_press_val = linked_dict[print_message_key]

            # Determine whether the button's associated message should be printed.
            if "print_bool_attribute" in print_on_press_dict:
                print_bool_key = print_on_press_dict["print_bool_attribute"]
                should_print = linked_dict[print_bool_key]

        # If it is determined that this button's message should be printed, return its message.
        if should_print:
            return print_on_press_val

    # If it was determined that nothing should be
    # printed when this button is pressed, return None.
    return None


def set_output_widgets(file_full_path):
    """This method alters all of the relevant widgets in the Time Stamper program to
    indicate that a valid output file IS currently active. Note that this method does
    not handle the actual enabling/disabling of widgets associated with an output file."""

    # Change the text of the label that appears above the file
    # path entry widget to indicate that a file has been selected.
    if isinstance(classes.template["label_output_path"]["text"], dict):

        classes.widgets["label_output_path"]["text"] = \
            classes.template["label_output_path"]["text"]["value_if_true"]

    # Print the file path to the entry widget.
    print_to_entry(file_full_path, classes.widgets["entry_output_path"], wipe_clean=True)

    # Any text already in the output file should be printed to the notes log.
    file_encoding = classes.settings["output"]["file_encoding"]
    copy_text_file_to_text_widget(file_full_path, file_encoding, classes.widgets["text_log"])


def reset_output_widgets():
    """This method alters all of the relevant widgets in the Time Stamper program to
    indicate that a valid output file IS NOT currently active. Note that this method does
    not handle the actual enabling/disabling of widgets associated with an output file."""

    # Set the text of the label that displays above the output path entry widget
    # to the value that should be displayed when no output file is active.
    classes.widgets["label_output_path"]["text"] = \
        classes.template["label_output_path"]["text"]["value_if_false"]

    # Clear the entry displaying the output path.
    print_to_entry("", classes.widgets["entry_output_path"], wipe_clean=True)

    # Clear the text displaying the notes log.
    print_to_text("", classes.widgets["text_log"], wipe_clean=True)


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


def copy_text_file_to_text_widget(file_full_path, file_encoding, text_obj, wipe_clean=True):
    """This method prints the entire contents of the text file indicated by
    file_full_path to the text widget text_obj. An optional argument wipe_clean,
    which is set to True by default, determines whether any text currently displayed
    in the text widget should be removed before the new text is displayed."""

    text_obj_initial_state = text_obj["state"]
    text_obj["state"] = NORMAL
    with open(file_full_path, "r", encoding=file_encoding) as out_file:
        if wipe_clean:
            text_obj.delete(1.0, END)
        for line in out_file.readlines():
            text_obj.insert(END, line)
            text_obj.see(END)
    text_obj["state"] = text_obj_initial_state


def verify_text_file(file_full_path, test_readability, test_writability):
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
        file_encoding = classes.settings["output"]["file_encoding"]
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
    return True


def print_to_entry(to_print, entry_obj, wipe_clean=False):
    """This method prints the value stored in to_print to the entry widget
    entry_obj. An optional argument wipe_clean, which is set to False
    by default, determines whether any text currently displayed in the
    entry widget should be removed before the new text is displayed."""

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


def print_to_file(to_print, file_path, access_mode="a+"):
    """This method prints the value stored in to_print to the file specified in file_path."""

    if file_path:
        file_encoding = classes.settings["output"]["file_encoding"]
        with open(file_path, access_mode, encoding=file_encoding) as out_file:
            out_file.write(to_print)


def replace_button_message_variables(button_message, **user_variables):
    """This method takes a user-entered button message and replaces
    any user-entered variables with their appropriate values."""

    for var_key, var_value in user_variables.items():
        button_message = button_message.replace(f"${var_key}", var_value)

    return button_message


def store_timestamper_output(output_file_paths):
    """This method reads through timestamper output files saved in "all_files" (which should
    be a list of file paths) and saves the notes stored in these files to a list."""

    header, notes_body, cur_note = [], [], ""

    # Iterate over every file specified in "output_file_paths".
    for input_file in output_file_paths:

        on_header = True

        file_encoding = classes.settings["output"]["file_encoding"]
        with open(input_file, "r", encoding=file_encoding) as in_file:

            # Iterate over every line in the current file.
            for line in in_file:

                # If the current line begins with a timestamp...
                if match("\\[\\d{2}:\\d{2}:\\d{2}.\\d{2}\\]", line[:13]):

                    # If the current line begins with a timestamp, we can be certain that the
                    # program is finished reading in any non-timestamped lines at the top of the
                    # current file, so new lines should NOT be considered part of the header.
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

                # If the current line is neither timestamped nor a part of the
                # header, then add the current line to the note that is currently
                # being generated (this should only occur when we have a
                # non-timestamped note that appears below a timestamped note).
                else:
                    cur_note += line

    if cur_note:
        notes_body.append(cur_note)

    return header, notes_body


def merge_notes(files_to_read):
    """This method takes a list of file paths and merges the notes written to
    those files into one list sorted according the time each note was written."""

    # Read through the input files of notes and save the lines to a list.
    header, notes_body = store_timestamper_output(files_to_read)

    # Sort the list of notes gathered from all requested files.
    notes_body.sort()

    return header + notes_body
