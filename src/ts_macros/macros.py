#-*- coding: utf-8 -*-
"""This module contains the Macros class which stores the functions
that are executed when a button in the TimeStamper program is pressed."""

from re import match
from os import path
from ntpath import basename
from sys import platform
from tkinter import Grid, Tk
from tkinter import DISABLED, NORMAL, END, filedialog
from .button_macros import ButtonMacros

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


class Macros():
    """This class stores all of the functions that are executed when a button
    in the TimeStamper program is pressed. This class' constructor takes one
    argument, template, which should be an instance of the TimeStamperTemplate class."""

    def __init__(self, template, widget_creators, widget_creators_separate_window):
        """The constructor initializes the Time Stamper template as well as dictionaries which
        map object string keys to their corresponding objects and corresponding macros."""

        self.template = template

        self.widget_creators = widget_creators
        self.widget_creators_separate_window = widget_creators_separate_window

        self.button = ButtonMacros(self)

        # Create a dict to save the original colors of tkinter objects so
        # that those colors can be restored when an object is reactivated.
        self.original_colors = {}

    def enable_button(self, str_button):
        """This method enables a button. For certain buttons on Mac computers, visual modifications
        are also made to the button to make it easier to tell that the button is enabled."""

        # Retrieve the button object associated with the passed string key.
        button = self.button.object_mapping[str_button]

        # Enable the button.
        button["state"] = NORMAL

        # If 1) we are on a Mac, 2) the current button is a tkmacosx Button and
        # 3) the button has no text, then it will be hard to tell whether this
        # button is enabled unless we change its appearance. Therefore, the
        # tkmocosx button's background would be changed to its original color here.
        if platform == "darwin" and isinstance(button, MacButton) and not button.cget("text"):
            button["background"] = self.original_colors[str_button]

    def disable_button(self, str_button):
        """This method disables a button. For certain buttons on Mac computers, visual modifications
        are also made to the button to make it easier to tell that the button is disabled."""

        # Retrieve the button object associated with the passed string key.
        button = self.button.object_mapping[str_button]

        # Enable the button temporarily.
        button["state"] = NORMAL

        # If 1) we are on a Mac, 2) the current button is a tkmacosx Button and
        # 3) the button has no text, then it will be hard to tell whether this button
        # is disabled unless we change its appearance. Therefore, the tkmacosx button's
        # background would be changed to the predetermined disabled color here.
        if platform == "darwin" and isinstance(button, MacButton) and not button.cget("text"):
            button["background"] = self.template.mac_disabled_color

        # Disable the button.
        button["state"] = DISABLED

    def button_enable_disable_macro(self, button_template):
        """This method, which is called upon by several button macros, will enable and
        disable the buttons associated with the string keys from the "to_enable" and
        "to_disable" attributes of a specific Button from the TimeStamperTemplate class."""

        # Enable the buttons stored in the button template's to_enable variable.
        for str_button in button_template.to_enable:
            self.enable_button(str_button)

        # Disable the buttons stored in the button template's to_disable variable.
        for str_button in button_template.to_disable:
            self.disable_button(str_button)

    def display_window(self, window_template, to_display_template, \
        close_window_macro=None, macro_args=()):
        """This method opens a window and displays a message. The attributes of the window
        (window_template) and entry/label/text (to_display_template) are passed as templates (see
        the time_stamper_template module). This method also takes the following optional arguments:
            1) close_window_macro: a method that will be executed when the window created by
               this method (whose characteristics are outlined in window_template) is closed.
            2) macro_args: a tuple containing any arguments for close_window_macro.
               Keep in mind that the first argument for close_window_macro will always
               be the window itself, which will be passed to close_window_macro
               automatically, so you should only pass arguments in macro_args if
               close_window_macro takes any ADDITIONAL arguments besides the window itself.
        """

        # Create the window with the relevant title, dimensions, background and icon.
        window = Tk()
        window.title(window_template.title)
        window["background"] = window_template.background
        window["foreground"] = window_template.foreground

        # If we are on a Mac, the window icon needs to be a .icns file.
        # On Windows, the window icon needs to be a .ico file.
        if platform == "darwin":
            icon_file_name = window_template.icon_mac
        else:
            icon_file_name = window_template.icon_windows

        # Set the window icon.
        window.iconbitmap(path.join(self.template.images_dir, icon_file_name))

        # Configure the window's columns and rows.
        for column_num in range(window_template.num_columns):
            Grid.columnconfigure(window, column_num, weight=1)
        for row_num in range(window_template.num_rows):
            Grid.rowconfigure(window, row_num, weight=1)

        # The method that will be used to create the widget in the new
        # window changes depending on the type of widget we want to create.
        # We can find the widget type from the widget template's string key.
        widget_create_method_mapping = { \
            "button": self.widget_creators_separate_window.create_button, \
            "entry": self.widget_creators_separate_window.create_entry, \
            "label": self.widget_creators_separate_window.create_label, \
            "text": self.widget_creators_separate_window.create_text}

        # Set the root for the widget_creators object to the new window.
        self.widget_creators_separate_window.root = window

        # Call the appropriate widget creation method based on the widget template's string key.
        widget_type = to_display_template.str_key[:to_display_template.str_key.find("_")]
        new_widget = widget_create_method_mapping[widget_type](to_display_template, self)

        if widget_type == "text":
            new_widget["state"] = NORMAL
            new_widget.insert(END, to_display_template.text)
            new_widget["state"] = DISABLED

        # If a function should be executed when this new window is closed, set that function here.
        if close_window_macro:
            macro_args = (window,) + macro_args
            window.protocol("WM_DELETE_WINDOW", lambda: close_window_macro(*macro_args))

        window.mainloop()

    def on_close_window_merge_1_macro(self, window_merge):
        """This method will be executed when the FIRST window displaying
        instructions to the user on how to merge output files is closed."""

        window_merge.destroy()

        # The user will be prompted to select the files whose notes they wish to merge.
        file_types = (("text files", "*.txt"), ('All files', '*.*'))
        files_full_paths = filedialog.askopenfilenames(title="Select output files to merge", \
            initialdir=self.template.mapping["button_output_select"].starting_dir, \
            filetypes=file_types)

        # Only merge the notes if at least one file was selected.
        if files_full_paths:

            # Store the objects (templates) containining attributes for
            # the second window with output merge instructions, along
            # with its relevant label, into abbreviated variable names.
            window_merge_2 = self.template.mapping["window_merge_second_message"]
            label_merge_2 = self.template.mapping["label_merge_second_message"]

            # Call the function that will display the second window with instructions
            # on how to merge output files, passing a macro that will make the second
            # file explorer window appear when the instructions window is closed,
            # wherein the user should select a destination file for their merged outputs.
            self.display_window(window_merge_2, label_merge_2, \
                self.on_close_window_merge_2_macro, (files_full_paths,))

    def on_close_window_merge_2_macro(self, window_merge, files_full_paths):
        """This method will be executed when the SECOND window displaying
        instructions to the user on how to merge output files is closed."""

        window_merge.destroy()

        # The user will be prompted to select the file to save the merged notes to.
        file_types = (("text files", "*.txt"), ('All files', '*.*'))
        merged_notes_path = \
            filedialog.askopenfilename(title="Select destination for merged outputs", \
            initialdir=self.template.mapping["button_output_select"].starting_dir, \
            filetypes=file_types)

        # Only proceed with attempting to merge the notes if
        # the user selected a file to save the merged notes to.
        if merged_notes_path:

            # If the user tried to save the merged notes to a file whose notes were already going to
            # be a part of the merge, do not merge the notes and instead display a failure message.
            if merged_notes_path in files_full_paths:

                window_merge_fail = self.template.mapping["window_merge_failure"]
                label_merge_fail = self.template.mapping["label_merge_failure"]
                self.display_window(window_merge_fail, label_merge_fail)

            # If the user chose a unique file to save the merged notes to that
            # was NOT already a part of the merge, proceed with the merge.
            else:

                # Merge the notes from all selected files.
                merged_notes = self.merge_notes(files_full_paths)

                # Write the merged notes to the requested file.
                with open(merged_notes_path, "a+", \
                    encoding=self.template.output_file_encoding) as out:
                    for note in merged_notes:
                        out.write(note)

                # Display a message that the notes were successfully merged.
                window_merge_success = self.template.mapping["window_merge_success"]
                label_merge_success = self.template.mapping["label_merge_success"]
                merged_notes_file = basename(merged_notes_path)
                label_merge_success.text = label_merge_success.success_message(merged_notes_file)
                self.display_window(window_merge_success, label_merge_success)

    def store_timestamper_output(self, output_file_paths):
        """This method reads through timestamper output files saved in "all_files" (which should
        be a list of file paths) and saves the notes stored in these files to a list."""

        all_notes = []
        cur_note = ""

        # Iterate over every file specified in "output_file_paths".
        for input_file in output_file_paths:
            with open(input_file, "r", encoding=self.template.output_file_encoding) as in_file:
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

    def find_beginnings_and_ends(self, notes):
        """This method takes raw timestamper outputs as an argument and returns all of
        the lines from that output marking the beginnings and endings of recordings."""

        # Store the record and stop messages into abbreviated file names.
        button_record_message = self.template.mapping["button_record"].print_on_press
        button_stop_message = self.template.mapping["button_stop"].print_on_press

        beginnings, ends = [], []
        for i, note in enumerate(notes):
            len_start_note = 14 + len(button_record_message)
            len_end_note = 14 + len(button_stop_message)
            if len(note) >= len_start_note and note[14:len_start_note] == button_record_message:
                beginnings.append(i)
            elif len(note) >= len_end_note and note[14:len_end_note] == button_stop_message:
                ends.append(i)

        return beginnings, ends

    def remove_from_notes(self, notes, beginnings_to_remove, ends_to_remove):
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
                note = note[14 + len(self.template.mapping["button_record"].print_on_press) + 1:]

            # Remove the timestamped notes indicating the ending of a recording.
            elif j in ends_to_remove:
                note = note[14 + len(self.template.mapping["button_stop"].print_on_press) + 1:]

            # Add the note to the updated notes list if there is a note to add.
            if note:
                notes_updated.append(note)

        return notes_updated

    def merge_notes(self, files_to_read):
        """This method takes a list of file paths and merges the notes written
        to those files into one list sorted by the time each note was written."""

        # Read through the input files of notes and save the lines to a list.
        all_notes = self.store_timestamper_output(files_to_read)

        # Sort the list of notes gathered from all requested files.
        all_notes.sort()

        # Find the timestamped notes in the selected files
        # that indicate beginnings and endings of recordings.
        beginnings, ends = self.find_beginnings_and_ends(all_notes)

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
        all_notes_updated = self.remove_from_notes(all_notes, beginnings, ends)

        return all_notes_updated

    def entry_val_limit(self, entry_text, max_val):
        """This method prevents any non-numerical characters from being entered
        into an entry and also sets the maximum value of that entry."""

        if len(entry_text.get()) > 0:

            # Remove any non-digits from the entry.
            try:
                int(entry_text.get()[-1])
            except ValueError:
                entry_text.set(entry_text.get()[:-1])

            # Remove any digits from the entry that put the entry over max_val.
            if len(entry_text.get()) > 0:
                if int(entry_text.get()) > max_val:
                    entry_text.set(entry_text.get()[:-1])
