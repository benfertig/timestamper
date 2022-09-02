#-*- coding: utf-8 -*-
"""This module contains the Macros class which stores the functions
that are executed when a button in the TimeStamper program is pressed."""

from re import match
from os import path
from tkinter import Grid, Tk, Label
from tkinter import DISABLED, END, NORMAL, filedialog

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
    """This class stores all of the functions that are executed  when a button
    in the TimeStamper program is pressed. This class' constructor takes one
    argument, shell, which should be an instance of the TimeStamperShell class."""

    def __init__(self, shell):
        """The constructor initializes the Time Stamper shell as well as dictionaries which
        map object string keys to their corresponding objects and corresponding macros."""

        self.shell = shell

        # Create shortened references to common object shells.
        self.buttons = self.shell.fields.buttons
        self.entries = self.shell.fields.entries
        self.labels = self.shell.fields.labels
        self.texts = self.shell.fields.texts

        # Create a dict to map object string keys to their objects.
        self.object_mapping = {}

        # Map buttons to their macros.
        self.macro_mapping = { \

            # Media buttons
            self.buttons.media.pause.str_key: self.button_pause_macro, \
            self.buttons.media.play.str_key: self.button_play_macro, \
            self.buttons.media.stop.str_key: self.button_stop_macro, \
            self.buttons.media.rewind.str_key: self.button_rewind_macro, \
            self.buttons.media.fast_forward.str_key: self.button_fast_forward_macro, \
            self.buttons.media.record.str_key: self.button_record_macro, \
            self.buttons.media.timestamp.str_key: self.button_timestamp_macro, \

            # Other buttons
            self.buttons.other.output_select.str_key: self.button_output_select_macro, \
            self.buttons.other.merge_output_files.str_key: self.button_merge_output_files_macro, \
            self.buttons.other.clear_timestamp.str_key: self.button_clear_timestamp_macro, \
            self.buttons.other.help.str_key: self.button_help_macro, \
            self.buttons.other.license.str_key: self.button_license_macro, \
            self.buttons.other.cancel_note.str_key: self.button_cancel_note_macro, \
            self.buttons.other.save_note.str_key: self.button_save_note_macro, \
        }

    def button_enable_disable_macro(self, button_shell):
        """This method, which is called upon by several button macros, will enable and
        disable the buttons associated with the string keys from the to_enable and
        to_disable attributes of a specific object within the TimeStamperShell class."""

        # Enable the buttons stored in the button shell's to_enable variable.
        for btn_str in button_shell.to_enable:
            self.object_mapping[btn_str]["state"] = NORMAL

        # Disable the buttons stored in the button shell's to_disable variable.
        for btn_str in button_shell.to_disable:
            self.object_mapping[btn_str]["state"] = DISABLED

    def button_pause_macro(self):
        """This method will be executed when the pause button is pressed."""

        # Enable and disable the relevant buttons for when the pause button is pressed.
        self.button_enable_disable_macro(self.buttons.media.pause)

        # Pause the timer.
        t_s_timer = self.object_mapping[self.shell.timer.str_key]
        t_s_timer.pause()

    def button_play_macro(self):
        """This method will be executed when the play button is pressed."""

        # Enable and disable the relevant buttons for when the play button is pressed.
        self.button_enable_disable_macro(self.buttons.media.play)

        # Resume the timer.
        t_s_timer = self.object_mapping[self.shell.timer.str_key]
        t_s_timer.play()

    def button_stop_macro(self):
        """This method will be executed when the stop button is pressed."""

        # Enable and disable the relevant buttons for when the stop button is pressed.
        self.button_enable_disable_macro(self.buttons.media.stop)

        # Print the message that the timer has been stopped
        # with the current timestamp to the screen.
        t_s_timer = self.object_mapping[self.shell.timer.str_key]
        current_timestamp = t_s_timer.current_time_to_timestamp()
        to_write = f"{current_timestamp} {self.buttons.media.stop.print_on_press}\n"
        text_log = self.object_mapping[self.texts.log.str_key]
        text_log["state"] = NORMAL
        text_log.insert(END, to_write)
        text_log["state"] = DISABLED

        # Print the message that the timer has been stopped
        # with the current timestamp to the output file.
        output_path = self.object_mapping[self.labels.output_path.str_key]["text"]
        if output_path != self.labels.output_path.text:
            output_path = output_path[len(self.labels.output_path.display_path_prefix):]
            with open(output_path, "a+", encoding=self.shell.output_file.encoding) as out_file:
                out_file.write(to_write)

        # Stop the timer.
        t_s_timer = self.object_mapping[self.shell.timer.str_key]
        t_s_timer.stop()

    def button_rewind_macro(self):
        """This method will be executed when the rewind button is pressed."""

        # Retrieve the rewind amount from the entry field.
        obj_rewind_amount = self.object_mapping[self.entries.rewind.str_key]
        rewind_amount = obj_rewind_amount.get()

        # Ensure that the requested rewind amount is a number.
        try:
            rewind_amount = int(rewind_amount)

        # Do not rewind if the requested rewind amount is not a number
        # (this should never happen because we have restricted the rewind
        # amount entry field to digits, but it never hurts to add a failsafe).
        except ValueError:
            return

        # Rewind the timer the requested amount.
        else:
            t_s_timer = self.object_mapping[self.shell.timer.str_key]
            t_s_timer.rewind(rewind_amount)

    def button_fast_forward_macro(self):
        """This method will be executed when the fast-forward button is pressed."""

        # Retrieve the fast-forward amount from the entry field.
        obj_fast_forward_amount = \
            self.object_mapping[self.entries.fast_forward.str_key]
        fast_forward_amount = obj_fast_forward_amount.get()

        # Ensure that the requested fast-forward amount is a number.
        try:
            fast_forward_amount = int(fast_forward_amount)

        # Do not rewind if the requested fast-forward amount is not a number
        # (this should never happen because we have restricted the fast-forward
        # amount entry field to digits, but it never hurts to add a failsafe).
        except ValueError:
            return

        # Fast-forward the timer the requested amount.
        else:
            t_s_timer = self.object_mapping[self.shell.timer.str_key]
            t_s_timer.fast_forward(fast_forward_amount)

    def button_record_macro(self):
        """This method will be executed when the record
        button is pressed, and will begin the timer."""

        # Get the currently displayed time from the timer and create a timestamp from it.
        t_s_timer = self.object_mapping[self.shell.timer.str_key]
        current_timestamp = t_s_timer.current_time_to_timestamp()
        to_write = f"{current_timestamp} {self.buttons.media.record.print_on_press}\n"

        # Print the message that the timer has started
        # with the current timestamp to the screen.
        text_log = self.object_mapping[self.texts.log.str_key]
        text_log["state"] = NORMAL
        text_log.insert(END, to_write)
        text_log["state"] = DISABLED

        # Print the message that the timer has started
        # with the current timestamp to the output file.
        out_path = self.object_mapping[self.labels.output_path.str_key]["text"]
        if out_path != self.labels.output_path.text:
            out_path = out_path[len(self.labels.output_path.display_path_prefix):]
            with open(out_path, "a+", encoding=self.shell.output_file.encoding) as out_file:
                out_file.write(to_write)

        # Enable and disable the relevant buttons for when the record button is pressed.
        self.button_enable_disable_macro(self.buttons.media.record)

        # Start the timer.
        t_s_timer.record()

    def button_timestamp_macro(self):
        """This method will be executed when the timestamp button is pressed."""

        # Set the timestamp to the current time.
        t_s_timer = self.object_mapping[self.shell.timer.str_key]
        obj_timestamp = self.object_mapping[self.labels.timestamp.str_key]
        current_timestamp = t_s_timer.current_time_to_timestamp()
        obj_timestamp["text"] = current_timestamp

        # Enable and disable the relevant buttons for when the timestamp button is pressed.
        self.button_enable_disable_macro(self.buttons.media.timestamp)

    def button_output_select_macro(self):
        """This method will be executed when the "Choose output location" button is pressed."""

        # Get the path to the selected output file.
        file_types = (("text files", "*.txt"), ('All files', '*.*'))
        file_full_path = filedialog.askopenfilename(title="Select a file", \
            initialdir=self.buttons.other.output_select.starting_dir, filetypes=file_types)

        # Only display the output file path, enable the relevant buttons and repopulate
        # the text displaying the notes log if an output file has been selected.
        if file_full_path:

            # Set the text of the label that displays the output to the current output file path.
            self.object_mapping[self.labels.output_path.str_key]["text"] = \
                f"{self.labels.output_path.display_path_prefix}{file_full_path}"

            # Indicate that the relevant buttons should be enabled.
            button_toggle_status = NORMAL

            # Clear the text displaying the notes log.
            obj_text_log = self.object_mapping[self.texts.log.str_key]
            obj_text_log["state"] = NORMAL
            obj_text_log.delete(1.0, END)

            # Any text already in the output file should be printed to the notes log.
            with open(file_full_path, "r", encoding=self.shell.output_file.encoding) as out_file:
                for line in out_file.readlines():
                    obj_text_log.insert(END, line)

            obj_text_log["state"] = DISABLED

        # If an output file has not been selected, do not display an
        # output file path and do not enable the relevant buttons.
        else:

            # Set the text of the label that displays the output to the label's default
            # text (the text that displays when no output file has been selected).
            self.object_mapping[self.labels.output_path.str_key]["text"] = \
                 self.labels.output_path.text

            # Indicate that the relevant buttons should be disabled.
            button_toggle_status = DISABLED

        # Either enable or disable the relevant buttons,
        # depending on whether an output file has been selected.
        for str_button in self.buttons.other.output_select.to_enable_toggle:
            button = self.object_mapping[str_button]
            button["state"] = button_toggle_status

    def button_merge_output_files_macro(self):
        """This method will be executed when the "Merge output files" button is pressed."""

        # Store the objects (shells) containining attributes for the first window with output
        # merge instructions, along with its relevant label, into abbreviated variable names.
        window_merge_1 = self.shell.windows.merge_output_files_first_message
        label_merge_1 = self.labels.separate_windows.merge_output_files_first_message

        # Call the function that will display the first window with instructions
        # on how to merge output files, passing a macro that will make the first
        # file explorer window appear when the instructions window is closed,
        # wherein the user should select all output files they would like to merge.
        self.display_window(window_merge_1, label_merge_1, \
            close_window_macro=self.on_close_window_merge_1_macro, macro_args=())

    def display_window(self, window_shell, \
        label_shell, close_window_macro=None, macro_args=()):
        """This method opens a window and displays a message. The attributes of the
        window (window_shell) and label (label_shell) are passed as shells (see the
        time_stamper_shell module). This method also takes the following optional arguments:
            1) close_window_macro: a method that will be executed when the window created by
               this method (whose characteristics are outlined in window_shell) is closed.
            2) macro_args: a tuple containing any arguments for close_window_macro.
               Keep in mind that the first argument for close_window_macro will always
               be the window itself, which will be passed to close_window_macro
               automatically, so you should only pass arguments in macro_args if
               close_window_macro takes any ADDITIONAL arguments besides the window itself.
        """

        # Create the first output file merge window message with
        # the relevant title, dimensions, background and icon.
        window_merge = Tk()
        window_merge.title(window_shell.title)
        window_merge["background"] = window_shell.background
        window_merge["foreground"] = window_shell.foreground
        window_merge.iconbitmap(path.join(self.shell.path.images_dir, window_shell.icon))

        # Configure the window's columns and rows.
        for column_num in range(window_shell.num_columns):
            Grid.columnconfigure(window_merge, column_num, weight=1)
        for row_num in range(window_shell.num_rows):
            Grid.rowconfigure(window_merge, row_num, weight=1)

        # Create the Label that will display the message
        # in the first output file merge window.
        label_merge_font = (f"{label_shell.font_family} {label_shell.font_size}")
        label_merge = Label(window_merge, height=label_shell.height, \
            width=label_shell.width, background=label_shell.background, \
            foreground=label_shell.foreground, text=label_shell.text, \
            justify=label_shell.justify, font=label_merge_font)
        label_merge.grid(column=label_shell.column, row=label_shell.row, \
        columnspan=label_shell.columnspan, rowspan=label_shell.rowspan, \
        padx=label_shell.padx, pady=label_shell.pady, ipadx=label_shell.ipadx, \
        ipady=label_shell.ipady, sticky=label_shell.sticky)

        macro_args = (window_merge,) + macro_args

        if close_window_macro:
            window_merge.protocol("WM_DELETE_WINDOW", lambda: close_window_macro(*macro_args))

        window_merge.mainloop()

    def on_close_window_merge_1_macro(self, window_merge):
        """This method will be executed when the FIRST window displaying
        instructions to the user on how to merge output files is closed."""

        window_merge.destroy()

        # The user will be prompted to select the files whose notes they wish to merge.
        file_types = (("text files", "*.txt"), ('All files', '*.*'))
        files_full_paths = filedialog.askopenfilenames(title="Select output files to merge", \
            initialdir=self.buttons.other.output_select.starting_dir, filetypes=file_types)

        # Only merge the notes if at least one file was selected.
        if files_full_paths:

            # Store the objects (shells) containining attributes for the second window with output
            # merge instructions, along with its relevant label, into abbreviated variable names.
            window_merge_2 = self.shell.windows.merge_output_files_second_message
            label_merge_2 = \
                self.labels.separate_windows.merge_output_files_second_message

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
            initialdir=self.buttons.other.output_select.starting_dir, filetypes=file_types)

        # Only proceed with attempting to merge the notes if
        # the user selected a file to save the merged notes to.
        if merged_notes_path:

            # If the user tried to save the merged notes to a file whose notes were already going to
            # be a part of the merge, do not merge the notes and instead display a failure message.
            if merged_notes_path in files_full_paths:

                window_merge_fail = self.shell.windows.merge_output_files_failure
                label_merge_fail = \
                    self.labels.separate_windows.merge_output_files_failure
                self.display_window(window_merge_fail, label_merge_fail)

            # If the user chose a unique file to save the merged notes to that
            # was NOT already a part of the merge, proceed with the merge.
            else:

                # Merge the notes from all selected files.
                merged_notes = self.merge_notes(files_full_paths)

                # Write the merged notes to the requested file.
                with open(merged_notes_path, "a+", encoding=self.shell.output_file.encoding) as out:
                    for note in merged_notes:
                        out.write(note)

                # Display a message that the notes were successfully merged.
                window_merge_success = self.shell.windows.merge_output_files_success
                label_merge_success = \
                    self.labels.separate_windows.merge_output_files_success
                self.display_window(window_merge_success, label_merge_success)

    def merge_notes(self, files_to_read):
        """This method takes a list of file paths and merges the notes written
        to those files into one list sorted by the time each note was written."""

        all_notes = []
        cur_note = ""

        # Read through the input files of notes and save the lines to a list.
        for input_file in files_to_read:
            with open(input_file, "r", encoding=self.shell.output_file.encoding) as in_file:
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

        # Sort the list of notes gathered from all requested files.
        all_notes.sort()

        # Find the timestamped notes in the selected files
        # that indicate beginnings and endings of recordings.
        beginnings, ends = [], []
        for i, note in enumerate(all_notes):
            if note[14:14+len(self.buttons.media.record.print_on_press)] == \
                self.buttons.media.record.print_on_press:
                beginnings.append(i)
            elif note[14:14 + len(self.buttons.media.stop.print_on_press)] == \
                self.buttons.media.stop.print_on_press:
                ends.append(i)

        # Delete the timestamped notes indicating beginnings and endings
        # of recordings EXCEPT FOR the earliest timestamped note indicating
        # a beginning AND the last timestamped note indicating an ending.
        beginnings.pop(0)
        ends.pop()

        # Convert the LISTS storing the indices of lines indicating beginnings
        # and endings of recordings to SETS to make lookup time faster.
        beginnings = set(beginnings)
        ends = set(ends)

        # Update the list of notes, removing redundant timestamped
        # notes indicating beginnings and endings of recordings.
        all_notes_updated = []
        for j, note in enumerate(all_notes):

            # Remove the timestamped notes indicating the beginning of a recording.
            if j in beginnings:
                note = note[14 + len(self.buttons.media.record.print_on_press) + 1:]

            # Remove the timestamped notes indicating the ending of a recording.
            elif j in ends:
                note = note[14 + len(self.buttons.media.stop.print_on_press) + 1:]

            # Add the note the updated notes list if there is a note to add.
            if note:
                all_notes_updated.append(note)

        return all_notes_updated

    def button_clear_timestamp_macro(self):
        """This method will be executed when the "Clear timestamp" button is pressed."""

        # Set the timestamp text to its default value.
        obj_timestamp = self.object_mapping[self.labels.timestamp.str_key]
        obj_timestamp["text"] = self.labels.timestamp.text

    def button_help_macro(self):
        """This method will be executed when the "Help" button is pressed."""

        # Create the help window with the relevant title, dimensions, background and icon.
        window_help_shell = self.shell.windows.help
        window_help = Tk()
        window_help.title(window_help_shell.title)
        window_help["background"] = window_help_shell.background
        window_help["foreground"] = window_help_shell.foreground
        window_help.iconbitmap(path.join(self.shell.path.images_dir, window_help_shell.icon))

        for column_num in range(window_help_shell.num_columns):
            Grid.columnconfigure(window_help, column_num, weight=1)

        for row_num in range(window_help_shell.num_rows):
            Grid.rowconfigure(window_help, row_num, weight=1)

        # Create the Label that will display the message in the help window.
        label_help_shell = self.labels.separate_windows.help_message
        label_help_font = (f"{label_help_shell.font_family} {label_help_shell.font_size}")
        label_help = Label(window_help, height=label_help_shell.height, \
            width=label_help_shell.width, background=label_help_shell.background, \
            foreground=label_help_shell.foreground, text=label_help_shell.text, \
            justify=label_help_shell.justify, font=label_help_font)
        label_help.grid(column=label_help_shell.column, row=label_help_shell.row, \
        columnspan=label_help_shell.columnspan, rowspan=label_help_shell.rowspan, \
        padx=label_help_shell.padx, pady=label_help_shell.pady, \
        ipadx=label_help_shell.ipadx, ipady=label_help_shell.ipady, sticky=label_help_shell.sticky)

        window_help.mainloop()

    def button_license_macro(self):
        """This method will be executed when the License button is pressed."""

        # Store the objects (shells) containining attributes for the license
        # window, along with its relevant label, into abbreviated variable names.
        window_license = self.shell.windows.license
        label_license_message = self.labels.separate_windows.license_message

        # Display the window containing the license and
        # outside attributions along with its relevant label.
        self.display_window(window_license, label_license_message)

    def button_cancel_note_macro(self):
        """This method will be executed when the "Cancel note" button is pressed."""

        # Clear the current note from the input text box.
        obj_current_note = self.object_mapping[self.texts.current_note.str_key]
        obj_current_note.delete(1.0, END)

        # Enable and disable the relevant buttons for when the cancel note button is pressed.
        self.button_enable_disable_macro(self.buttons.other.cancel_note)

    def button_save_note_macro(self):
        """This method will be executed when the "Save note" button is pressed."""

        # Get the current timestamp displayed next to the input text box.
        obj_timestamp = self.object_mapping[self.labels.timestamp.str_key]
        current_timestamp = obj_timestamp["text"]

        was_timestamp = True

        # Set the current timestamp to the timer's current time if there is no timestamp.
        if current_timestamp == self.labels.timestamp.text:
            t_s_timer = self.object_mapping[self.shell.timer.str_key]
            current_timestamp = t_s_timer.current_time_to_timestamp()
            was_timestamp = False

        # Get the current text in the input text box.
        obj_current_note = self.object_mapping[self.texts.current_note.str_key]
        current_note = obj_current_note.get(1.0, END)
        obj_current_note.delete(1.0, END)

        to_write = f"{current_timestamp} {current_note}"

        # Print the current timestamp along with the current
        # text from the input text box to the screen.
        text_log = self.object_mapping[self.texts.log.str_key]
        text_log["state"] = NORMAL
        text_log.insert(END, to_write)
        text_log["state"] = DISABLED

        if not was_timestamp:
            # Reset the current timestamp.
            obj_timestamp["text"] = self.labels.timestamp.text

        # Print the current timestamp along with the current
        # text from the input text box to the output file.
        output_path = self.object_mapping[self.labels.output_path.str_key]["text"]
        if output_path != self.labels.output_path.text:
            output_path = output_path[len(self.labels.output_path.display_path_prefix):]
            with open(output_path, "a+", encoding=self.shell.output_file.encoding) as out_file:
                out_file.write(to_write)

        # Enable and disable the relevant buttons for when the save note button is pressed.
        self.button_enable_disable_macro(self.buttons.other.save_note)

    def entry_val_limit(self, entry_text, max_val):
        """This method prevents any non-numerical characters from being entered
        into an entry and also sets the maximum value of that entry."""

        if len(entry_text.get()) > 0:

            # Remove any non-digits from the entry.
            try:
                int(entry_text.get()[-1])
            except ValueError:
                entry_text.set(entry_text.get()[:-1])

            # Remove any digits from the entry that put it over max_val.
            if len(entry_text.get()) > 0:
                if int(entry_text.get()) > max_val:
                    entry_text.set(entry_text.get()[:-1])
