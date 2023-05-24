#-*- coding: utf-8 -*-
"""This module stores the functions that are executed when
windows in the Time Stamper program are manipulated."""

from os.path import basename
from tkinter import filedialog

from vlc import MediaPlayer

import classes
import methods.macros.methods_macros_helper as methods_helper
import methods.macros.methods_macros_media as methods_media
import methods.macros.methods_macros_output as methods_output

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


def on_close_window_video_macro(window_video):
    """This method will be executed when the video window is closed."""

    # Pause the timer.
    classes.macros["button_pause"]()

    # Stop the media player.
    if isinstance(classes.time_stamper.media_player, MediaPlayer):
        classes.time_stamper.media_player.stop()

    # Destroy the video window.
    window_video.destroy()

    # Configure the program to reflect that a media file is NOT enabled.
    methods_media.attempt_media_player_release()
    classes.time_stamper.media_player = None
    methods_media.reset_media_widgets()
    methods_helper.toggle_widgets(classes.template["button_media_select"], False)


def on_close_window_help_macro(window_help):
    """This method will be executed when the help window is closed."""

    # Destroy the help window.
    window_help.destroy()

    # Reset the page number in the help page number label template to the first page.
    label_help_page_number_template = classes.template["label_help_page_number"]
    first_page_num = label_help_page_number_template["first_page"]
    label_help_page_number_template["current_page"] = first_page_num


def on_close_window_merge_first_message_macro(window_merge_1):
    """This method will be executed when the FIRST window displaying
    instructions to the user on how to merge output files is closed."""

    # Destroy the window displaying the first set of merge instructions.
    window_merge_1.destroy()

    # The user will be prompted to select the files whose notes they wish to merge.
    file_types = (("Text files", "*.txt"), ('All files', '*.*'))
    files_full_paths = filedialog.askopenfilenames(title="Select output files to merge", \
        initialdir=classes.template.starting_dir, filetypes=file_types)

    # Only merge the notes if at least one file was selected.
    if files_full_paths:

        # Verify the validity of the text files whose notes the user would like to merge.
        invalid_file_names = []
        for file_path in files_full_paths:
            if not methods_output.verify_text_file(file_path, True, False):
                invalid_file_names.append(basename(file_path))

        # If the user selected any files that cannot be opened and read,
        # do not merge the notes and instead display a failure message.
        if invalid_file_names:
            label_merge_failure = classes.template["label_merge_failure_file_not_readable"]
            label_merge_failure["text"] = \
                methods_output.merge_failure_message_file_not_readable(invalid_file_names)
            merge_failure_window = \
                classes.widgets.create_entire_window("window_merge_failure_file_not_readable")
            merge_failure_window.mainloop()

        # If all of the files that the user selected can
        # be opened and read, proceed with the merge.
        else:

            # Merge the notes from all of the selected files. We cannot write the merged notes
            # to a new file yet because a new file has not yet been selected. The process of
            # writing the merged notes to a new file occurs in on_close_window_merge_2_macro.
            merged_notes = methods_output.merge_notes(files_full_paths)

            # Call the function that will display the second window with instructions on
            # how to merge output files, passing a macro that will make the second file
            # explorer window appear when the second merge instructions window is closed,
            # wherein the user should select a destination file for their merged outputs.
            merge_second_message_window = classes.widgets.create_entire_window(\
                "window_merge_second_message", macro_args=(merged_notes, files_full_paths,))
            merge_second_message_window.mainloop()


def on_close_window_merge_second_message_macro(window_merge_2, merged_notes, files_full_paths):
    """This method will be executed when the SECOND window displaying
    instructions to the user on how to merge output files is closed."""

    # Destroy the window displaying the second set of merge instructions.
    window_merge_2.destroy()

    # The user will be prompted to select the file to save the merged notes to.
    file_types = (("Text files", "*.txt"), ('All files', '*.*'))
    merged_notes_path = \
        filedialog.askopenfilename(title="Select destination for merged outputs", \
        initialdir=classes.template.starting_dir, filetypes=file_types)

    # Only proceed with attempting to write the merged notes to a
    # file if the user selected a file to save the merged notes to.
    if merged_notes_path:

        # Save the specified output file encoding into an abbreviated file name.
        file_encoding = classes.settings["output"]["file_encoding"]

        # If the user tried to save the merged notes to a file whose notes
        # were already going to be a part of the merge, do not write the
        # merged notes to a file and instead display a failure message.
        if merged_notes_path in files_full_paths:

            merge_failure_window = \
                classes.widgets.create_entire_window("window_merge_failure_repeated_file")
            merge_failure_window.mainloop()

        # If the user tried to save the merged notes to an unreadable file, do not
        # write the merged notes to a file and instead display a failure message.
        elif not methods_output.verify_text_file(merged_notes_path, False, True):
            label_merge_failure = classes.template["label_merge_failure_file_not_readable"]
            label_merge_failure["text"] = methods_output.\
                merge_failure_message_file_not_readable(basename(merged_notes_path))
            merge_failure_window = \
                classes.widgets.create_entire_window("window_merge_failure_file_not_readable")
            merge_failure_window.mainloop()

        # If the user chose a unique file to save the merged notes to that was NOT already
        # a part of the merge AND the chosen file is readable, proceed with the merge.
        else:

            # Write the merged notes to the requested file.
            with open(merged_notes_path, "a+", encoding=file_encoding) as out:
                for note in merged_notes:
                    out.write(note)

            # Display a message stating that the notes were successfully merged.
            label_merge_success = classes.template["label_merge_success"]
            label_merge_success["text"] = \
                methods_output.merge_success_message(basename(merged_notes_path))
            merge_success_window = classes.widgets.create_entire_window("window_merge_success")
            merge_success_window.mainloop()
