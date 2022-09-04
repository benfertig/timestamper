#-*- coding: utf-8 -*-
"""This module contains the ButtonMacros class which stores the
functions that are executed immediately when a button in the TimeStamper
program is pressed. This module excludes external helper functions."""

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


class ButtonMacros():
    """This class stores all of the macros that execute immediately
    when buttons are pressed, excluding helper methods."""

    def __init__(self, parent):

        self.parent = parent
        self.template = self.parent.template

        self.buttons = self.template.fields.buttons
        self.entries = self.template.fields.entries
        self.labels = self.template.fields.labels
        self.texts = self.template.fields.texts

        # Map buttons to their macros.
        self.mapping = { \

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
            self.buttons.other.merge_output_files.str_key: \
                self.button_merge_output_files_macro, \
            self.buttons.other.clear_timestamp.str_key: self.button_clear_timestamp_macro, \
            self.buttons.other.help.str_key: self.button_help_macro, \
            self.buttons.other.license.str_key: self.button_license_macro, \
            self.buttons.other.cancel_note.str_key: self.button_cancel_note_macro, \
            self.buttons.other.save_note.str_key: self.button_save_note_macro, \
        }

    def button_pause_macro(self):
        """This method will be executed when the pause button is pressed."""

        # Enable and disable the relevant buttons for when the pause button is pressed.
        self.parent.button_enable_disable_macro(self.buttons.media.pause)

        # Pause the timer.
        t_s_timer = self.parent.object_mapping[self.template.timer.str_key]
        t_s_timer.pause()

    def button_play_macro(self):
        """This method will be executed when the play button is pressed."""

        # Enable and disable the relevant buttons for when the play button is pressed.
        self.parent.button_enable_disable_macro(self.buttons.media.play)

        # Resume the timer.
        t_s_timer = self.parent.object_mapping[self.template.timer.str_key]
        t_s_timer.play()

    def button_stop_macro(self):
        """This method will be executed when the stop button is pressed."""

        # Enable and disable the relevant buttons for when the stop button is pressed.
        self.parent.button_enable_disable_macro(self.buttons.media.stop)

        # Print the message that the timer has been stopped
        # with the current timestamp to the screen.
        t_s_timer = self.parent.object_mapping[self.template.timer.str_key]
        current_timestamp = t_s_timer.current_time_to_timestamp()
        to_write = f"{current_timestamp} {self.buttons.media.stop.print_on_press}\n"
        text_log = self.parent.object_mapping[self.texts.log.str_key]
        text_log["state"] = NORMAL
        text_log.insert(END, to_write)
        text_log.see(END)
        text_log["state"] = DISABLED

        # Print the message that the timer has been stopped
        # with the current timestamp to the output file.
        output_path = self.parent.object_mapping[self.labels.output_path.str_key]["text"]
        if output_path != self.labels.output_path.text:
            output_path = output_path[len(self.labels.output_path.display_path_prefix):]
            with open(output_path, "a+", encoding=self.template.output_file.encoding) as out_file:
                out_file.write(to_write)

        # Stop the timer.
        t_s_timer = self.parent.object_mapping[self.template.timer.str_key]
        t_s_timer.stop()

    def button_rewind_macro(self):
        """This method will be executed when the rewind button is pressed."""

        # Retrieve the rewind amount from the entry field.
        obj_rewind_amount = self.parent.object_mapping[self.entries.rewind.str_key]
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
            t_s_timer = self.parent.object_mapping[self.template.timer.str_key]
            t_s_timer.rewind(rewind_amount)

    def button_fast_forward_macro(self):
        """This method will be executed when the fast-forward button is pressed."""

        # Retrieve the fast-forward amount from the entry field.
        obj_fast_forward_amount = \
            self.parent.object_mapping[self.entries.fast_forward.str_key]
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
            t_s_timer = self.parent.object_mapping[self.template.timer.str_key]
            t_s_timer.fast_forward(fast_forward_amount)

    def button_record_macro(self):
        """This method will be executed when the record
        button is pressed, and will begin the timer."""

        # Get the currently displayed time from the timer and create a timestamp from it.
        t_s_timer = self.parent.object_mapping[self.template.timer.str_key]
        current_timestamp = t_s_timer.current_time_to_timestamp()
        to_write = f"{current_timestamp} {self.buttons.media.record.print_on_press}\n"

        # Print the message that the timer has started
        # with the current timestamp to the screen.
        text_log = self.parent.object_mapping[self.texts.log.str_key]
        text_log["state"] = NORMAL
        text_log.insert(END, to_write)
        text_log.see(END)
        text_log["state"] = DISABLED

        # Print the message that the timer has started
        # with the current timestamp to the output file.
        out_path = self.parent.object_mapping[self.labels.output_path.str_key]["text"]
        if out_path != self.labels.output_path.text:
            out_path = out_path[len(self.labels.output_path.display_path_prefix):]
            with open(out_path, "a+", encoding=self.template.output_file.encoding) as out_file:
                out_file.write(to_write)

        # Enable and disable the relevant buttons for when the record button is pressed.
        self.parent.button_enable_disable_macro(self.buttons.media.record)

        # Start the timer.
        t_s_timer.record()

    def button_timestamp_macro(self):
        """This method will be executed when the timestamp button is pressed."""

        # Set the timestamp to the current time.
        t_s_timer = self.parent.object_mapping[self.template.timer.str_key]
        obj_timestamp = self.parent.object_mapping[self.labels.timestamp.str_key]
        current_timestamp = t_s_timer.current_time_to_timestamp()
        obj_timestamp["text"] = current_timestamp

        # Enable and disable the relevant buttons for when the timestamp button is pressed.
        self.parent.button_enable_disable_macro(self.buttons.media.timestamp)

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
            self.parent.object_mapping[self.labels.output_path.str_key]["text"] = \
                f"{self.labels.output_path.display_path_prefix}{file_full_path}"

            # Indicate that the relevant buttons should be enabled.
            button_toggle_status = NORMAL

            # Clear the text displaying the notes log.
            obj_text_log = self.parent.object_mapping[self.texts.log.str_key]
            obj_text_log["state"] = NORMAL
            obj_text_log.delete(1.0, END)

            # Any text already in the output file should be printed to the notes log.
            with open(file_full_path, "r", encoding=self.template.output_file.encoding) as out_file:
                for line in out_file.readlines():
                    obj_text_log.insert(END, line)
                    obj_text_log.see(END)

            obj_text_log["state"] = DISABLED

        # If an output file has not been selected, do not display an
        # output file path and do not enable the relevant buttons.
        else:

            # Set the text of the label that displays the output to the label's default
            # text (the text that displays when no output file has been selected).
            self.parent.object_mapping[self.labels.output_path.str_key]["text"] = \
                self.labels.output_path.text

            # Indicate that the relevant buttons should be disabled.
            button_toggle_status = DISABLED

        # Either enable or disable the relevant buttons,
        # depending on whether an output file has been selected.
        if button_toggle_status == NORMAL:
            for str_button in self.buttons.other.output_select.to_enable_toggle:
                self.parent.enable_button(str_button)
        else:
            for str_button in self.buttons.other.output_select.to_enable_toggle:
                self.parent.disable_button(str_button)

    def button_merge_output_files_macro(self):
        """This method will be executed when the "Merge output files" button is pressed."""

        # Store the objects (templates) containining attributes for the first window with output
        # merge instructions, along with its relevant label, into abbreviated variable names.
        window_merge_1 = self.template.windows.merge_output_files_first_message
        label_merge_1 = self.labels.separate_windows.merge_output_files_first_message

        # Call the function that will display the first window with instructions
        # on how to merge output files, passing a macro that will make the first
        # file explorer window appear when the instructions window is closed,
        # wherein the user should select all output files they would like to merge.
        self.parent.display_window(window_merge_1, label_merge_1, \
            close_window_macro=self.parent.on_close_window_merge_1_macro, macro_args=())

    def button_clear_timestamp_macro(self):
        """This method will be executed when the "Clear timestamp" button is pressed."""

        # Set the timestamp text to its default value.
        obj_timestamp = self.parent.object_mapping[self.labels.timestamp.str_key]
        obj_timestamp["text"] = self.labels.timestamp.text

    def button_help_macro(self):
        """This method will be executed when the "Help" button is pressed."""

        # Create the help window with the relevant title, dimensions, background and icon.
        window_help_template = self.template.windows.help
        window_help = Tk()
        window_help.title(window_help_template.title)
        window_help["background"] = window_help_template.background
        window_help["foreground"] = window_help_template.foreground
        window_help.iconbitmap(path.join(self.template.path.images_dir, window_help_template.icon))

        for column_num in range(window_help_template.num_columns):
            Grid.columnconfigure(window_help, column_num, weight=1)

        for row_num in range(window_help_template.num_rows):
            Grid.rowconfigure(window_help, row_num, weight=1)

        # Create the Label that will display the message in the help window.
        label_help_template = self.labels.separate_windows.help_message
        label_help_font = (f"{label_help_template.font_family} {label_help_template.font_size}")
        label_help = Label(window_help, height=label_help_template.height, \
            width=label_help_template.width, background=label_help_template.background, \
            foreground=label_help_template.foreground, text=label_help_template.text, \
            justify=label_help_template.justify, font=label_help_font)
        label_help.grid(column=label_help_template.column, row=label_help_template.row, \
        columnspan=label_help_template.columnspan, rowspan=label_help_template.rowspan, \
        padx=label_help_template.padx, pady=label_help_template.pady, \
        ipadx=label_help_template.ipadx, ipady=label_help_template.ipady, \
        sticky=label_help_template.sticky)

        window_help.mainloop()

    def button_license_macro(self):
        """This method will be executed when the License button is pressed."""

        # Store the objects (templates) containining attributes for the license
        # window, along with its relevant label, into abbreviated variable names.
        window_license = self.template.windows.license
        label_license_message = self.labels.separate_windows.license_message

        # Display the window containing the license and
        # outside attributions along with its relevant label.
        self.parent.display_window(window_license, label_license_message)

    def button_cancel_note_macro(self):
        """This method will be executed when the "Cancel note" button is pressed."""

        # Clear the current note from the input text box.
        obj_current_note = self.parent.object_mapping[self.texts.current_note.str_key]
        obj_current_note.delete(1.0, END)

        # Enable and disable the relevant buttons for when the cancel note button is pressed.
        self.parent.button_enable_disable_macro(self.buttons.other.cancel_note)

    def button_save_note_macro(self):
        """This method will be executed when the "Save note" button is pressed."""

        # Get the current timestamp displayed next to the input text box.
        obj_timestamp = self.parent.object_mapping[self.labels.timestamp.str_key]
        current_timestamp = obj_timestamp["text"]

        was_timestamp = True

        # Set the current timestamp to the timer's current time if there is no timestamp.
        if current_timestamp == self.labels.timestamp.text:
            t_s_timer = self.parent.object_mapping[self.template.timer.str_key]
            current_timestamp = t_s_timer.current_time_to_timestamp()
            was_timestamp = False

        # Get the current text in the input text box.
        obj_current_note = self.parent.object_mapping[self.texts.current_note.str_key]
        current_note = obj_current_note.get(1.0, END)
        obj_current_note.delete(1.0, END)

        to_write = f"{current_timestamp} {current_note}"

        # Print the current timestamp along with the current
        # text from the input text box to the screen.
        text_log = self.parent.object_mapping[self.texts.log.str_key]
        text_log["state"] = NORMAL
        text_log.insert(END, to_write)
        text_log.see(END)
        text_log["state"] = DISABLED

        if not was_timestamp:
            # Reset the current timestamp.
            obj_timestamp["text"] = self.labels.timestamp.text

        # Print the current timestamp along with the current
        # text from the input text box to the output file.
        output_path = self.parent.object_mapping[self.labels.output_path.str_key]["text"]
        if output_path != self.labels.output_path.text:
            output_path = output_path[len(self.labels.output_path.display_path_prefix):]
            with open(output_path, "a+", encoding=self.template.output_file.encoding) as out_file:
                out_file.write(to_write)

        # Enable and disable the relevant buttons for when the save note button is pressed.
        self.parent.button_enable_disable_macro(self.buttons.other.save_note)
