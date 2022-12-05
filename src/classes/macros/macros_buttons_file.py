#-*- coding: utf-8 -*-
"""This module contains the FileButtonMacros class which stores the functions
that are executed when a file button in the Time Stamper program is pressed."""

from ntpath import basename
from tkinter import DISABLED, NORMAL, END, filedialog
from .macros_helper_methods import enable_button, disable_button, merge_notes, print_to_text

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


def success_message(merged_output_file_name):
    """This method generates the message that is displayed
    when the program has successfully merged output files."""

    return "MERGE SUCCESS\n\n" \
        "Your merged notes have been saved in:\n" \
        f"\"{merged_output_file_name}\".\n\n" \
        "Close this window to proceed."


class FileButtonMacros():
    """This class stores all of the macros that execute when file buttons are pressed."""

    def __init__(self, template, widgets):
        self.template = template
        self.widgets = widgets

    def button_output_select_macro(self):
        """This method will be executed when the "Choose output location" button is pressed."""

        # Store the template for the output select button, the template for the output
        # path label, and the widget for the output path label into abbreviated file names.
        button_output_select_template = self.template.mapping["button_output_select"]
        label_output_path_template = self.template.mapping["label_output_path"]
        obj_label_output_path = self.widgets.mapping["label_output_path"]
        obj_text_output_path = self.widgets.mapping["text_output_path"]
        obj_text_log = self.widgets.mapping["text_log"]

        # Get the path to the selected output file.
        file_types = (("text files", "*.txt"), ('All files', '*.*'))
        file_full_path = filedialog.askopenfilename(title="Select a file", \
            initialdir=self.template.starting_dir, filetypes=file_types)

        # Only display the output file path, enable the relevant buttons and repopulate
        # the text displaying the notes log if an output file has been selected.
        if file_full_path:

            # Store the output path in the template.
            self.template.output_path = file_full_path

            # Set the text of the label that displays the output to the current output file path.
            obj_label_output_path["text"] = label_output_path_template['display_path_prefix']

            # Print the current output file path to the output path text widget.
            print_to_text(file_full_path, obj_text_output_path, wipe_clean=True)

            # Clear the text displaying the notes log.
            print_to_text("", obj_text_log, wipe_clean=True)

            # Enable the relevant buttons if an output file has been selected.
            for str_button in button_output_select_template["to_enable_toggle"]:
                enable_button(self.widgets.mapping[str_button], \
                    self.widgets.original_colors[str_button])

            # Any text already in the output file should be printed to the notes log.
            obj_text_log["state"] = NORMAL
            with open(file_full_path, "r", encoding=self.template.output_file_encoding) as out_file:
                for line in out_file.readlines():
                    obj_text_log.insert(END, line)
                    obj_text_log.see(END)
            obj_text_log["state"] = DISABLED

        # If an output file has not been selected, do not display an
        # output file path and do not enable the relevant buttons.
        else:

            # Clear the output path in the template.
            self.template.output_path = None

            # Set the text of the label that displays the output to the label's default
            # text (the text that displays when no output file has been selected).
            obj_label_output_path["text"] = label_output_path_template["text"]

            # Clear the output path text widget.
            print_to_text("", obj_text_output_path, wipe_clean=True)

            # Clear the text log.
            print_to_text("", obj_text_log, wipe_clean=True)

            # Disable the relevant buttons if an output file has not been selected.
            for str_button in button_output_select_template["to_enable_toggle"]:
                disable_button(self.widgets.mapping[str_button], \
                    self.template.mapping[str_button]["mac_disabled_color"])

    def on_close_window_merge_1_macro(self, window_merge):
        """This method will be executed when the FIRST window displaying
        instructions to the user on how to merge output files is closed."""

        window_merge.destroy()

        # The user will be prompted to select the files whose notes they wish to merge.
        file_types = (("text files", "*.txt"), ('All files', '*.*'))
        files_full_paths = filedialog.askopenfilenames(title="Select output files to merge", \
            initialdir=self.template.starting_dir, filetypes=file_types)

        # Only merge the notes if at least one file was selected.
        if files_full_paths:

            # Merge the notes from all of the selected files. We cannot write the merged notes
            # to a new file yet because a new file has not yet been selected. The process of
            # writing the merged notes to a new file occurs in on_close_window_merge_2_macro.
            button_record_message = self.template.mapping["button_record"]["print_on_press"]
            button_stop_message = self.template.mapping["button_stop"]["print_on_press"]
            merged_notes = \
                merge_notes(files_full_paths, button_record_message, \
                    button_stop_message, self.template.output_file_encoding)

            # Call the function that will display the second window with instructions
            # on how to merge output files, passing a macro that will make the second
            # file explorer window appear when the instructions window is closed,
            # wherein the user should select a destination file for their merged outputs.
            merge_second_message_window = \
                self.widgets.create_entire_window("window_merge_second_message", \
                    close_window_macro=self.on_close_window_merge_2_macro, \
                        macro_args=(merged_notes, files_full_paths,))
            merge_second_message_window.mainloop()

    def on_close_window_merge_2_macro(self, window_merge, merged_notes, files_full_paths):
        """This method will be executed when the SECOND window displaying
        instructions to the user on how to merge output files is closed."""

        window_merge.destroy()

        # The user will be prompted to select the file to save the merged notes to.
        file_types = (("text files", "*.txt"), ('All files', '*.*'))
        merged_notes_path = \
            filedialog.askopenfilename(title="Select destination for merged outputs", \
            initialdir=self.template.starting_dir, filetypes=file_types)

        # Only proceed with attempting to merge the notes if
        # the user selected a file to save the merged notes to.
        if merged_notes_path:

            # If the user tried to save the merged notes to a file whose notes were already going to
            # be a part of the merge, do not merge the notes and instead display a failure message.
            if merged_notes_path in files_full_paths:

                merge_failure_window = \
                    self.widgets.create_entire_window("window_merge_failure")
                merge_failure_window.mainloop()

            # If the user chose a unique file to save the merged notes to that
            # was NOT already a part of the merge, proceed with the merge.
            else:

                # Write the merged notes to the requested file.
                with open(merged_notes_path, "a+", \
                    encoding=self.template.output_file_encoding) as out:
                    for note in merged_notes:
                        out.write(note)

                # Display a message stating that the notes were successfully merged.
                label_merge_success = self.template.mapping["label_merge_success"]
                label_merge_success["text"] = success_message(basename(merged_notes_path))
                merge_success_window = \
                    self.widgets.create_entire_window("window_merge_success")
                merge_success_window.mainloop()

    def button_merge_output_files_macro(self):
        """This method will be executed when the "Merge output files" button is pressed."""

        # Call the function that will display the first window with instructions
        # on how to merge output files, passing a macro that will make the first
        # file explorer window appear when the instructions window is closed,
        # wherein the user should select all output files they would like to merge.
        window_merge_first_message = self.widgets.create_entire_window(\
            "window_merge_first_message", close_window_macro=self.on_close_window_merge_1_macro)
        window_merge_first_message.mainloop()
