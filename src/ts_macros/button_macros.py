#-*- coding: utf-8 -*-
"""This module contains the ButtonMacros class which stores the
functions that are executed immediately when a button in the TimeStamper
program is pressed. This module excludes external helper functions."""

from ntpath import basename
from tkinter import DISABLED, END, NORMAL, filedialog
from .helper_methods import enable_button, disable_button, merge_notes

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

    def __init__(self, template, widget_creators, timer):

        self.template = template
        self.timer = timer
        self.widget_creators = widget_creators

        # Map buttons to their macros.
        self.mapping = { \

            # File buttons
            "button_output_select": self.button_output_select_macro,
            "button_merge_output_files": self.button_merge_output_files_macro,

            # Info buttons
            "button_help": self.button_help_macro,
            "button_help_left_arrow": self.button_help_left_arrow_macro,
            "button_help_right_arrow": self.button_help_right_arrow_macro,
            "button_license": self.button_license_macro,
            "button_attribution": self.button_attribution_macro,

            # Media buttons
            "button_pause": self.button_pause_macro,
            "button_play": self.button_play_macro,
            "button_stop": self.button_stop_macro,
            "button_rewind": self.button_rewind_macro,
            "button_fast_forward": self.button_fast_forward_macro,
            "button_record": self.button_record_macro,

            # Note buttons
            "button_cancel_note": self.button_cancel_note_macro,
            "button_save_note": self.button_save_note_macro,

            # Timestamping buttons
            "button_timestamp": self.button_timestamp_macro,
            "button_clear_timestamp": self.button_clear_timestamp_macro,

        }

    def button_enable_disable_macro(self, str_button):
        """This method, which is called upon by several button macros, will enable and
        disable the buttons associated with the string keys from the "to_enable" and
        "to_disable" attributes of a specific Button from the TimeStamperTemplate class."""

        button_template = self.template.mapping[str_button]

        # Enable the buttons stored in the button template's to_enable variable.
        for str_to_enable in button_template.to_enable:
            if str_to_enable in self.widget_creators.original_colors:
                original_color = self.widget_creators.original_colors[str_to_enable]
            else:
                original_color = None
            enable_button(self.widget_creators.mapping[str_to_enable], original_color)

        # Disable the buttons stored in the button template's to_disable variable.
        for str_to_disable in button_template.to_disable:
            disable_button(self.widget_creators.mapping[str_to_disable], \
                button_template.mac_disabled_color)

    def button_pause_macro(self):
        """This method will be executed when the pause button is pressed."""

        # Enable and disable the relevant buttons for when the pause button is pressed.
        self.button_enable_disable_macro("button_pause")

        # Pause the timer.
        self.timer.pause()

    def button_play_macro(self):
        """This method will be executed when the play button is pressed."""

        # Enable and disable the relevant buttons for when the play button is pressed.
        self.button_enable_disable_macro("button_play")

        # Resume the timer.
        self.timer.play()

    def button_stop_macro(self):
        """This method will be executed when the stop button is pressed."""

        # Store the template for the stop button into an abbreviated file name.
        button_stop_template = self.template.mapping["button_stop"]

        # Enable and disable the relevant buttons for when the stop button is pressed.
        self.button_enable_disable_macro("button_stop")

        # Print the message that the timer has been stopped
        # with the current timestamp to the screen.
        current_timestamp = self.timer.current_time_to_timestamp()
        to_write = f"{current_timestamp} {button_stop_template.print_on_press}\n"
        text_log = self.widget_creators.mapping["text_log"]
        text_log["state"] = NORMAL
        text_log.insert(END, to_write)
        text_log.see(END)
        text_log["state"] = DISABLED

        # Print the message that the timer has been stopped
        # with the current timestamp to the output file.
        label_output_path_template = self.template.mapping["label_output_path"]
        output_path = self.widget_creators.mapping["label_output_path"]["text"]
        if output_path != label_output_path_template.text:
            output_path = output_path[len(label_output_path_template.display_path_prefix):]
            with open(output_path, "a+", encoding=self.template.output_file_encoding) as out_file:
                out_file.write(to_write)

        # Stop the timer.
        self.timer.stop()

    def button_rewind_macro(self):
        """This method will be executed when the rewind button is pressed."""

        # Retrieve the rewind amount from the entry field.
        obj_rewind_amount = self.widget_creators.mapping["entry_rewind"]
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
            self.timer.rewind(rewind_amount)

    def button_fast_forward_macro(self):
        """This method will be executed when the fast-forward button is pressed."""

        # Retrieve the fast-forward amount from the entry field.
        obj_fast_forward_amount = self.widget_creators.mapping["entry_fast_forward"]
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
            self.timer.fast_forward(fast_forward_amount)

    def button_record_macro(self):
        """This method will be executed when the record
        button is pressed, and will begin the timer."""

        # Store the template for the record button into an abbreviated file name.
        button_record_template = self.template.mapping["button_record"]

        # Get the currently displayed time from the timer and create a timestamp from it.
        current_timestamp = self.timer.current_time_to_timestamp()
        to_write = f"{current_timestamp} {button_record_template.print_on_press}\n"

        # Print the message that the timer has started
        # with the current timestamp to the screen.
        text_log = self.widget_creators.mapping["text_log"]
        text_log["state"] = NORMAL
        text_log.insert(END, to_write)
        text_log.see(END)
        text_log["state"] = DISABLED

        # Print the message that the timer has started
        # with the current timestamp to the output file.
        label_output_path_template = self.template.mapping["label_output_path"]
        output_path = self.widget_creators.mapping["label_output_path"]["text"]
        if output_path != label_output_path_template.text:
            output_path = output_path[len(label_output_path_template.display_path_prefix):]
            with open(output_path, "a+", encoding=self.template.output_file_encoding) as out_file:
                out_file.write(to_write)

        # Enable and disable the relevant buttons for when the record button is pressed.
        self.button_enable_disable_macro("button_record")

        # Start the timer.
        self.timer.play()

    def button_timestamp_macro(self):
        """This method will be executed when the timestamp button is pressed."""

        # Make note of the fact that a timestamp has been set.
        self.timer.timestamp_set = True

        # Set the timestamp to the current time.
        obj_timestamp = self.widget_creators.mapping["label_timestamp"]
        current_timestamp = self.timer.current_time_to_timestamp()
        obj_timestamp["text"] = current_timestamp

        # Enable and disable the relevant buttons for when the timestamp button is pressed.
        self.button_enable_disable_macro("button_timestamp")

    def button_output_select_macro(self):
        """This method will be executed when the "Choose output location" button is pressed."""

        # Store the template for the output select button and
        # the output path label into abbreviated file names.
        button_output_select_template = self.template.mapping["button_output_select"]
        label_output_path_template = self.template.mapping["label_output_path"]

        # Get the path to the selected output file.
        file_types = (("text files", "*.txt"), ('All files', '*.*'))
        file_full_path = filedialog.askopenfilename(title="Select a file", \
            initialdir=button_output_select_template.starting_dir, filetypes=file_types)

        # Only display the output file path, enable the relevant buttons and repopulate
        # the text displaying the notes log if an output file has been selected.
        if file_full_path:

            # Set the text of the label that displays the output to the current output file path.
            self.widget_creators.mapping["text"] = \
                f"{label_output_path_template.display_path_prefix}{file_full_path}"

            # Indicate that the relevant buttons should be enabled.
            button_toggle_status = NORMAL

            # Clear the text displaying the notes log.
            obj_text_log = self.widget_creators.mapping["text_log"]
            obj_text_log["state"] = NORMAL
            obj_text_log.delete(1.0, END)

            # Any text already in the output file should be printed to the notes log.
            with open(file_full_path, "r", encoding=self.template.output_file_encoding) as out_file:
                for line in out_file.readlines():
                    obj_text_log.insert(END, line)
                    obj_text_log.see(END)

            obj_text_log["state"] = DISABLED

        # If an output file has not been selected, do not display an
        # output file path and do not enable the relevant buttons.
        else:

            # Set the text of the label that displays the output to the label's default
            # text (the text that displays when no output file has been selected).
            self.widget_creators.mapping["label_output_path"]["text"] = \
                label_output_path_template.text

            # Indicate that the relevant buttons should be disabled.
            button_toggle_status = DISABLED

        # Enable the relevant buttons if an output file has been selected.
        if button_toggle_status == NORMAL:
            for str_button in button_output_select_template.to_enable_toggle:
                enable_button(self.widget_creators.mapping[str_button], \
                    self.widget_creators.original_colors[str_button])

        # Disable the relevant buttons if an output file has not been selected.
        else:
            for str_button in button_output_select_template.to_enable_toggle:
                disable_button(self.widget_creators.mapping[str_button], \
                    self.template.mapping[str_button].mac_disabled_color)

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

            # Call the function that will display the second window with instructions
            # on how to merge output files, passing a macro that will make the second
            # file explorer window appear when the instructions window is closed,
            # wherein the user should select a destination file for their merged outputs.
            merge_second_message_window = \
                self.widget_creators.create_entire_window("window_merge_second_message", \
                    close_window_macro=self.on_close_window_merge_2_macro, \
                        macro_args=(files_full_paths,))
            merge_second_message_window.mainloop()

    def on_close_window_merge_2_macro(self, window_merge, files_full_paths):
        """This method will be executed when the SECOND window displaying
        instructions to the user on how to merge output files is closed."""

        window_merge.destroy()

        button_record_message = self.template.mapping["button_record"].print_on_press
        button_stop_message = self.template.mapping["button_stop"].print_on_press

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

                merge_failure_window = \
                    self.widget_creators.create_entire_window("window_merge_failure")
                merge_failure_window.mainloop()

            # If the user chose a unique file to save the merged notes to that
            # was NOT already a part of the merge, proceed with the merge.
            else:

                # Merge the notes from all selected files.
                merged_notes = \
                    merge_notes(files_full_paths, button_record_message, \
                        button_stop_message, self.template.output_file_encoding)

                # Write the merged notes to the requested file.
                with open(merged_notes_path, "a+", \
                    encoding=self.template.output_file_encoding) as out:
                    for note in merged_notes:
                        out.write(note)

                # Display a message that the notes were successfully merged.
                label_merge_success = self.template.mapping["label_merge_success"]
                label_merge_success.text = \
                    label_merge_success.success_message(basename(merged_notes_path))
                merge_success_window = \
                    self.widget_creators.create_entire_window("window_merge_success")
                merge_success_window.mainloop()

    def button_merge_output_files_macro(self):
        """This method will be executed when the "Merge output files" button is pressed."""

        # Call the function that will display the first window with instructions
        # on how to merge output files, passing a macro that will make the first
        # file explorer window appear when the instructions window is closed,
        # wherein the user should select all output files they would like to merge.
        window_merge_first_message = self.widget_creators.create_entire_window(\
            "window_merge_first_message", close_window_macro=self.on_close_window_merge_1_macro)
        window_merge_first_message.mainloop()

    def button_clear_timestamp_macro(self):
        """This method will be executed when the "Clear timestamp" button is pressed."""

        # Make note of the fact that a timestamp has been cleared.
        self.timer.timestamp_set = False

        # Set the timestamp text to the timer's current time.
        obj_timestamp = self.widget_creators.mapping["label_timestamp"]
        hours, minutes, seconds, subseconds = self.timer.read_current_time(raw=True)
        obj_timestamp["text"] = f"[{hours}:{minutes}:{seconds}.{subseconds}]"

        # Enable and disable the relevant buttons for when the clear timestamp button is pressed.
        self.button_enable_disable_macro("button_clear_timestamp")

    def button_help_macro(self):
        """This method will be executed when the "Help" button is pressed."""

        # Display the window containing the help message along with its relevant label.
        window_help = self.widget_creators.create_entire_window("window_help", \
            self.mapping, close_window_macro=self.on_close_window_help_macro)
        window_help.mainloop()

    def change_help_page(self, next_page):
        """This method is called upon by the macros for the left/right arrow buttons in
        the help page. Since the procedure for both of these buttons is nearly identical,
        we can use the same function for both buttons with only one parameter changed."""

        label_page_number_template = self.template.mapping["label_help_page_number"]
        page_numbers = label_page_number_template.page_numbers
        cur_page = label_page_number_template.current_page_number

        if page_numbers[cur_page][1 if next_page else 0] is not None:

            # Display the new page number.
            new_page = page_numbers[cur_page][1 if next_page else 0]
            label_page_number_template.current_page_number = new_page
            obj_page_number = self.widget_creators.mapping["label_help_page_number"]
            obj_page_number["text"] = str(new_page)

            # Display the new help message.
            label_help_message_template = self.template.mapping["label_help_message"]
            obj_label_help = self.widget_creators.mapping["label_help_message"]
            new_message = label_help_message_template.help_data[str(new_page)]
            label_help_message_template.text = new_message
            obj_label_help["text"] = new_message

            # Disable the left arrow button if we are at the first help page.
            obj_button_help_left_arrow = self.widget_creators.mapping["button_help_left_arrow"]
            if page_numbers[new_page][0] is None:
                obj_button_help_left_arrow["state"] = DISABLED
            else:
                obj_button_help_left_arrow["state"] = NORMAL

            # Disable the right arrow button if we are at the last help page.
            obj_button_help_right_arrow = self.widget_creators.mapping["button_help_right_arrow"]
            if page_numbers[new_page][1] is None:
                obj_button_help_right_arrow["state"] = DISABLED
            else:
                obj_button_help_right_arrow["state"] = NORMAL

    def button_help_left_arrow_macro(self):
        """This method will be executed when the left arrow button in the help window is pressed."""
        self.change_help_page(False)

    def button_help_right_arrow_macro(self):
        """This method will be executed when the right
        arrow button in the help window is pressed."""
        self.change_help_page(True)

    def on_close_window_help_macro(self, window_help):
        """This method will be executed when the help window is closed."""

        window_help.destroy()

        # Reset the page number in the page numbe label template.
        label_page_number_template = self.template.mapping["label_help_page_number"]
        first_page_num = label_page_number_template.first_page
        label_page_number_template.current_page_number = first_page_num

        # Reset the help message in the help message label template.
        label_help_message_template = self.template.mapping["label_help_message"]
        help_data = label_help_message_template.help_data
        label_help_message_template.text = help_data[str(first_page_num)]

    def button_license_macro(self):
        """This method will be executed when the License button is pressed."""

        # Display the window containing the license and
        # outside attributions along with its relevant label.
        window_license = self.widget_creators.create_entire_window("window_license")
        window_license.mainloop()

    def button_attribution_macro(self):
        """This method will be executed when the Attribution button is pressed."""

        window_attribution = self.widget_creators.create_entire_window("window_attribution")
        window_attribution.mainloop()

    def button_cancel_note_macro(self):
        """This method will be executed when the "Cancel note" button is pressed."""

        # Clear the current note from the input text box.
        obj_current_note = self.widget_creators.mapping["text_current_note"]
        obj_current_note.delete(1.0, END)

        # Enable and disable the relevant buttons for when the cancel note button is pressed.
        self.button_enable_disable_macro("button_cancel_note")

    def button_save_note_macro(self):
        """This method will be executed when the "Save note" button is pressed."""

        # Get the current timestamp displayed next to the input text box.
        obj_timestamp = self.widget_creators.mapping["label_timestamp"]
        current_timestamp = obj_timestamp["text"]

        # Store the template for the timestamp and output path labels into abbreviated file names.
        label_output_path_template = self.template.mapping["label_output_path"]

        # Get the current text in the input text box.
        obj_current_note = self.widget_creators.mapping["text_current_note"]
        current_note = obj_current_note.get(1.0, END)
        obj_current_note.delete(1.0, END)

        to_write = f"{current_timestamp} {current_note}"

        # Print the current timestamp along with the current
        # text from the input text box to the screen.
        text_log = self.widget_creators.mapping["text_log"]
        text_log["state"] = NORMAL
        text_log.insert(END, to_write)
        text_log.see(END)
        text_log["state"] = DISABLED

        # Print the current timestamp along with the current
        # text from the input text box to the output file.
        output_path = self.widget_creators.mapping["label_output_path"]["text"]
        if output_path != label_output_path_template.text:
            output_path = output_path[len(label_output_path_template.display_path_prefix):]
            with open(output_path, "a+", encoding=self.template.output_file_encoding) as out_file:
                out_file.write(to_write)

        # Enable and disable the relevant buttons for when the save note button is pressed.
        self.button_enable_disable_macro("button_save_note")
