#-*- coding: utf-8 -*-
"""This module stores some extra methods associated with printing text output."""

from os.path import exists, isdir
from tkinter import NORMAL, END

import classes
import methods.macros.methods_macros_helper as methods_helper
from methods.timing import methods_timing_helper

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

            # If a timestamp was not provided, generate a timestamp from the current time.
            if timestamp is None:

                # Generate the current timestamp.
                timestamp = classes.timer.current_time_to_timestamp()

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


def determine_last_character(file_name):
    """This method efficiently determines the last character in a text
    file. If the text file is empty, this method will return None."""

    # Open the file.
    with open(file_name, "rb+") as file:

        # See if there is any text in the file.
        try:
            file.seek(-1, 2)

        # If there is NO text currently in the file, return None.
        except OSError:
            return None

        # If there IS text currently in the file, return the last character of the file.
        return str(file.read(1), classes.settings["output"]["file_encoding"])


def print_timestamped_message(message, timestamp=None):
    """This method takes a message, timestamps it, and then prints that timestamped
    message to the notes log and the output file (if no timestamp is provided,
    then a timestamp will be generated using the timer's current time)."""

    # If no timestamp was provided, generate a timestamp using the timer's current time.
    if timestamp is None:
        timestamp = classes.timer.current_time_to_timestamp()

    # Generate the complete message that should be printed, including the timestamp.
    to_print = f"{timestamp} {message}"

    # If the last character of the current output file is not
    # a new line, add a new line before the upcoming message.
    if determine_last_character(classes.time_stamper.output_path) != "\n":
        to_print = f"\n{to_print}"

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
        entry_obj.textvariable.set(to_print)
    else:
        entry_obj.textvariable.set(f"{entry_obj.textvariable.get()}{to_print}")
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


def reconcile_or_sort_macro(is_reconcile):
    """This method contains the entire functionality for the "Reconcile" and "Sort"
    buttons. The functions performed by these two buttons are very similar, so their
    procedures have been condensed down to a single method here and different parameters
    are passed depending on whether the skip backward or skip forward button was pressed."""

    out_path, text_log = classes.time_stamper.output_path, classes.widgets["text_log"]

    # If the output file is valid (this should already be the case, but just double-checking)...
    if verify_text_file(out_path, True, True):

        # Determine the last character of the output file (before reconciling/sorting).
        last_character_of_file = determine_last_character(out_path)

        # Read through the input files of notes and save the lines to a list.
        header, consistent_h_m_s, body = store_timestamper_output([out_path])

        # If we are RECONCILING notes, make the degree of precision of all timestamps in
        # the output consistent with the degree of precision of the most precise timestamp.
        if is_reconcile:
            for i, note in enumerate(body):
                consistent_timestamp = \
                    methods_timing_helper.h_m_s_to_timestamp(*consistent_h_m_s[i])
                body[i] = f"{consistent_timestamp}{note[note.find(']') + 1:]}"

        # If we are not reconciling notes but are instead SORTING notes, sort the notes
        # gathered from all requested files according to their precise timestamps.
        else:
            body = [ln for _, ln in sorted(zip(consistent_h_m_s, body), key=lambda pair: pair[0])]

        # Erase the current contents of the notes log and the output file.
        print_to_text("", text_log, wipe_clean=True)
        print_to_file("", out_path, access_mode="w+")

        # Print the sorted notes to the notes log and to the output file (except for the last note).
        all_lines = header + body
        for line_index in range(len(all_lines) - 1):
            print_to_text(all_lines[line_index], text_log, wipe_clean=False)
            print_to_file(all_lines[line_index], out_path, access_mode="a+")

        # If the last character of the file WAS NOT originally a new line, then
        # erase the final new line character from the last note if it exists.
        if last_character_of_file != "\n" and all_lines[-1][-1] == "\n":
            all_lines[-1] = all_lines[-1][:-1]

        # Print the final line to the notes log and the output file.
        print_to_text(all_lines[-1], text_log, wipe_clean=False)
        print_to_file(all_lines[-1], out_path, access_mode="a+")


def make_timestamp_formats_consistent(original_h_m_s):
    """This method takes a list of lists, where each constituent list has the form [hours,
    minutes, seconds, subseconds] (if any of these four values is None, that is okay). This
    method then modifies the input list so that the precision of each [hours, minutes,
    seconds, subseconds] entry becomes as precise as the most precise entry in the list."""

    # Check whether minutes were included in any of the timestamps,
    # and if they were, ensure that all timestamps include minutes.
    for orig_outer in original_h_m_s:
        if orig_outer[1] is not None:
            for i, orig_inner in enumerate(original_h_m_s):
                original_h_m_s[i][1] = "00" if orig_inner[1] is None else orig_inner[1]
            break

    # Check whether hours were included in any of the timestamps,
    # and if they were, ensure that all timestamps include hours.
    for orig_outer in original_h_m_s:
        if orig_outer[0] is not None:
            for i, orig_inner in enumerate(original_h_m_s):
                original_h_m_s[i][0] = "00" if orig_inner[0] is None else orig_inner[0]
            break

    # Check the precision of the decimal of the most precise timestamp.
    most_precise_subsecond = 0
    for orig in original_h_m_s:
        if orig[3] is not None:
            most_precise_subsecond = max(most_precise_subsecond, len(orig[3]))

    # Ensure that the decimals of each timestamp are as
    # precise as the decimal of the most precise timestamp.
    if most_precise_subsecond > 0:
        for i, orig in enumerate(original_h_m_s):
            if orig[3] is None or len(orig[3]) < most_precise_subsecond:
                orig[3] = methods_timing_helper.pad_number(\
                    orig[3] if orig[3] else "0", most_precise_subsecond, False)

    return original_h_m_s


def store_timestamper_output(output_file_paths):
    """This method reads through timestamper output files saved in "all_files" (which should
    be a list of file paths) and saves the notes stored in these files to a list."""

    header, notes_body, original_h_m_s= [], [], []
    cur_note = ""

    # Iterate over every file specified in "output_file_paths".
    for file_path in output_file_paths:

        # Assume that any new lines at the beginning of the current file are part
        # of the header (until we reach a timestamped line in the current file).
        on_header = True

        # Open the current file.
        with open(file_path, "r", encoding=classes.settings["output"]["file_encoding"]) as out_file:

            # Iterate over every line in the current file.
            for line in out_file:

                # If the last character of the current line is not a new line
                # character, add a new line character to the end of the current line.
                if line[-1] != "\n":
                    line = f"{line}\n"

                is_timestamped_line = False

                # If the current line begins with an open square bracket and contains a closed
                # square bracket somewhere later, it could potentially be a timestamped line.
                if line[0] == "[" and line.find("]") != -1:

                    # If the characters in the current line up to the first
                    # closed square bracket were successfully parsed as a
                    # timestamp, then that means this is a timestamped line.
                    original_timestamp = line[:line.find("]") + 1]
                    h_m_s = methods_timing_helper.timestamp_to_h_m_s(\
                        original_timestamp, pad=2, pad_subseconds=False)
                    if h_m_s is not None:

                        is_timestamped_line = True
                        original_h_m_s.append(h_m_s)

                # If the current line begins with a timestamp...
                if is_timestamped_line:

                    # We can now be certain that the program is finished reading
                    # in any non-timestamped lines at the top of the current file,
                    # so new lines should NOT be considered part of the header.
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

    # Flush out any final note that has not yet been added to the notes list.
    if cur_note:
        notes_body.append(cur_note)

    # Make the degree of precision of all [hours, minutes, seconds, subseconds]
    # lists from the output consistent with the degree of precision
    # of the most precise [hours, minutes, seconds, subseconds] list.
    consistent_h_m_s = make_timestamp_formats_consistent(original_h_m_s)

    return header, consistent_h_m_s, notes_body
