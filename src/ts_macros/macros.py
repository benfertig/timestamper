#-*- coding: utf-8 -*-
"""This module contains the Macros class which stores the functions
that are executed when a button in the TimeStamper program is pressed."""

from ntpath import basename
from tkinter import filedialog
from .button_macros import ButtonMacros
from .helper_methods import merge_notes

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

    def __init__(self, template, widget_creators, timer):
        """The constructor initializes the Time Stamper template as well as dictionaries which
        map object string keys to their corresponding objects and corresponding macros."""

        self.template = template
        self.widget_creators = widget_creators

        self.button = ButtonMacros(template, timer, \
            widget_creators, self.on_close_window_merge_1_macro)

    def on_close_window_merge_1_macro(self, window_merge):
        """This method will be executed when the FIRST window displaying
        instructions to the user on how to merge output files is closed."""

        window_merge.destroy()

        widg_create = self.widget_creators
        on_close_window_merge_2_macro = self.on_close_window_merge_2_macro

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
                widg_create.create_entire_window("window_merge_second_message", \
                    close_window_macro=on_close_window_merge_2_macro, \
                        macro_args=(files_full_paths, self.template.mapping, \
                            self.template.output_file_encoding))
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
