#-*- coding: utf-8 -*-
"""This module contains the FileButtonMacros class which stores the functions
that are executed when a file button in the Time Stamper program is pressed."""

from ntpath import sep as ntpath_sep
from posixpath import sep as posixpath_sep
from os.path import basename
from sys import platform
from tkinter import DISABLED, NORMAL, END, filedialog
from pyglet.media import load, Player
from pyglet.media.codecs.wave import WAVEDecodeException
from .macros_helper_methods import merge_success_message, merge_failure_message_file_not_readable, \
    toggle_widgets, merge_notes, print_to_entry, print_to_text

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


class FileButtonMacros():
    """This class stores all of the macros that execute when file buttons are pressed."""

    def __init__(self, parent):
        self.parent = parent
        self.time_stamper = parent.time_stamper
        self.template = parent.template
        self.settings = parent.settings
        self.widgets = parent.widgets
        self.timer = parent.timer

    def verify_selected_file(self, file_full_path, interpret_as):
        """This method, which is called by file_select_macro, verifies that the file selected by
        the user is manipulable in a way that is consistent with the program's expectations."""

        # Only try to load the file if a non-empty file_full_path argument was passed.
        if file_full_path:

            # If the program should attempt to interpret file_full_path as a text file...
            if interpret_as == "text":
                try:
                    file_encoding = self.settings["output"]["file_encoding"]
                    with open(file_full_path, "a+", encoding=file_encoding) as output_file:
                        output_file.write("")
                    with open(file_full_path, "r", encoding=file_encoding) as output_file:
                        output_file.readlines()
                except (FileNotFoundError, IOError, PermissionError, UnicodeDecodeError):
                    return False
                else:
                    return True

            # If the program should attempt to interpret file_full_path as an audio file...
            elif interpret_as == "audio":
                try:
                    self.time_stamper.audio_source = load(file_full_path)
                except (FileNotFoundError, WAVEDecodeException):
                    return False
                else:
                    self.time_stamper.audio_player = Player()
                    return True

        # This statement will be reached if at least one of the following conditions was met:
        #     1) file_full_path was empty
        #     2) interpret_as did not match "text" or "audio".
        return False

    def file_select_macro(self, label_str_key, entry_str_key, window_title, file_types):
        """This method is called on by button_output_select_macro and
        button_audio_select_macro. Since both "button_output_select" and
        "button_audio_select" prompt the user to select a file, the procedures for
        their macros can, to a large extent, be condensed down into this method."""

        # Store  the template for the label, the widget for the label,
        # and the widget for the entry into abbreviated file names.
        label_template = self.template[label_str_key]
        label_object = self.widgets[label_str_key]
        entry_object = self.widgets[entry_str_key]

        # Get the path to the selected file.
        file_full_path = filedialog.askopenfilename(title=window_title, \
            initialdir=self.template.starting_dir, filetypes=file_types)

        # Check to see whether a valid file has been selected.
        interpret_as = "audio" if entry_str_key == "entry_audio_path" else "text"
        file_is_valid = self.verify_selected_file(file_full_path, interpret_as)

        # If a valid file HAS been selected...
        if file_full_path and file_is_valid:

            # Change the text of the label that appears above the file
            # path entry widget to indicate that a file has been selected.
            if isinstance(label_template["text"], dict):
                label_object["text"] = label_template["text"]["value_if_true"]

            # Change the file path to the Windows format if we are on a Windows computer.
            if platform.startswith("win"):
                file_full_path = file_full_path.replace(posixpath_sep, ntpath_sep)

            # Print the file path to the entry widget.
            print_to_entry(file_full_path, entry_object, wipe_clean=True)

            return file_full_path

        # If a valid file has NOT been selected...

        # Change the text of the label to indicate that a file has not been selected.
        if isinstance(label_template["text"], dict):
            label_object["text"] = label_template["text"]["value_if_false"]

        # Clear the entry widget.
        entry_object["state"] = NORMAL
        entry_object.delete(0, END)
        entry_object["state"] = DISABLED

        return None

    def button_output_select_macro(self):
        """This method will be executed when the "Choose output location" button is pressed."""

        # Get the path to the selected output file.
        file_types = (("text files", "*.txt"), ('All files', '*.*'))
        file_full_path = self.file_select_macro("label_output_path", \
            "entry_output_path", "Select a text file", file_types)

        # Store the notes log widget into an abbreviated file name.
        obj_text_log = self.widgets["text_log"]

        # Clear the text displaying the notes log.
        print_to_text("", obj_text_log, wipe_clean=True)

        # Only repopulate the text in the notes log and enable the
        # relevant buttons if an output file has been selected.
        if file_full_path:

            # Any text already in the output file should be printed to the notes log.
            obj_text_log["state"] = NORMAL
            with open(file_full_path, "r", \
                encoding=self.settings["output"]["file_encoding"]) as out_file:
                for line in out_file.readlines():
                    obj_text_log.insert(END, line)
                    obj_text_log.see(END)
            obj_text_log["state"] = DISABLED

            # Enable the relevant widget if an output file has been selected.
            toggle_widgets(self.template["button_output_select"], True, self.template, self.widgets)

        # If an output file has not been selected, disable the relevant widgets.
        else:
            toggle_widgets(self.template["button_output_select"], \
                False, self.template, self.widgets)

    def button_merge_output_files_macro(self):
        """This method will be executed when the "Merge output files" button is pressed."""

        # Call the function that will display the first window with instructions
        # on how to merge output files, passing a macro that will make the first
        # file explorer window appear when the instructions window is closed,
        # wherein the user should select all output files they would like to merge.
        window_merge_first_message = self.widgets.create_entire_window(\
            "window_merge_first_message", close_window_macro=self.on_close_window_merge_1_macro)
        window_merge_first_message.mainloop()

    def button_audio_select_macro(self):
        """This method will be executed when the "Select synced audio file" button is pressed."""

        # Get the path to the selected audio file.
        file_types = \
            (("Audio files", "*.wav *.mp3 *.flac *.aiff *.aac *.wma *.ogg *.alac *.dsd *.mqa"), \
                ('All files', '*.*'))
        file_full_path = self.file_select_macro("label_audio_path", \
            "entry_audio_path", "Select an audio file", file_types)

        # If a valid audio file WAS selected, enable the
        # relevant widgets and reset the timer/audio slider.
        if file_full_path:

            self.timer.display_time(0.0, pad=2)

            # Enable the relevant widget if an audio file has been selected.
            toggle_widgets(self.template["button_audio_select"], True, self.template, self.widgets)

        # If a valid audio file WAS NOT selected...
        else:

            # Clear the audio source and the audio player.
            self.time_stamper.audio_source = None
            self.time_stamper.audio_player = None

            # Reset and disable the widgets associated with audio.
            self.parent.disable_audio_widgets()

    def on_close_window_merge_1_macro(self, window_merge_1):
        """This method will be executed when the FIRST window displaying
        instructions to the user on how to merge output files is closed."""

        # Destroy the window displaying the first set of merge instructions.
        window_merge_1.destroy()

        # The user will be prompted to select the files whose notes they wish to merge.
        file_types = (("text files", "*.txt"), ('All files', '*.*'))
        files_full_paths = filedialog.askopenfilenames(title="Select output files to merge", \
            initialdir=self.template.starting_dir, filetypes=file_types)

        # Only merge the notes if at least one file was selected.
        if files_full_paths:

            invalid_file_names = []
            for file_path in files_full_paths:
                if not self.verify_selected_file(file_path, "text"):
                    invalid_file_names.append(basename(file_path))

            # If the user selected any files that cannot be opened and read,
            # do not merge the notes and instead display a failure message.
            if invalid_file_names:
                label_merge_failure = self.template["label_merge_failure_file_not_readable"]
                label_merge_failure["text"] = \
                    merge_failure_message_file_not_readable(invalid_file_names)
                merge_failure_window = \
                    self.widgets.create_entire_window("window_merge_failure_file_not_readable")
                merge_failure_window.mainloop()

            # If all of the files that the user selected can
            # be opened and read, proceed with the merge.
            else:

                # Merge the notes from all of the selected files. We cannot write the merged notes
                # to a new file yet because a new file has not yet been selected. The process of
                # writing the merged notes to a new file occurs in on_close_window_merge_2_macro.
                merged_notes = \
                    merge_notes(files_full_paths, self.settings["output"]["file_encoding"])

                # Call the function that will display the second window with instructions on
                # how to merge output files, passing a macro that will make the second file
                # explorer window appear when the second merge instructions window is closed,
                # wherein the user should select a destination file for their merged outputs.
                merge_second_message_window = \
                    self.widgets.create_entire_window("window_merge_second_message", \
                        close_window_macro=self.on_close_window_merge_2_macro, \
                            macro_args=(merged_notes, files_full_paths,))
                merge_second_message_window.mainloop()

    def on_close_window_merge_2_macro(self, window_merge_2, merged_notes, files_full_paths):
        """This method will be executed when the SECOND window displaying
        instructions to the user on how to merge output files is closed."""

        # Destroy the window displaying the second set of merge instructions.
        window_merge_2.destroy()

        # The user will be prompted to select the file to save the merged notes to.
        file_types = (("text files", "*.txt"), ('All files', '*.*'))
        merged_notes_path = \
            filedialog.askopenfilename(title="Select destination for merged outputs", \
            initialdir=self.template.starting_dir, filetypes=file_types)

        # Only proceed with attempting to write the merged notes to a
        # file if the user selected a file to save the merged notes to.
        if merged_notes_path:

            # If the user tried to save the merged notes to a file whose notes
            # were already going to be a part of the merge, do not write the
            # merged notes to a file and instead display a failure message.
            if merged_notes_path in files_full_paths:

                merge_failure_window = \
                    self.widgets.create_entire_window("window_merge_failure_repeated_file")
                merge_failure_window.mainloop()

            # If the user tried to save the merged notes to an unreadable file, do not
            # write the merged notes to a file and instaed display a failure message.
            elif not self.verify_selected_file(merged_notes_path, "text"):
                label_merge_failure = self.template["label_merge_failure_file_not_readable"]
                label_merge_failure["text"] = \
                    merge_failure_message_file_not_readable(basename(merged_notes_path))
                merge_failure_window = \
                    self.widgets.create_entire_window("window_merge_failure_file_not_readable")
                merge_failure_window.mainloop()

            # If the user chose a unique file to save the merged notes to that was NOT already
            # a part of the merge AND the chosen file is readable, proceed with the merge.
            else:

                # Write the merged notes to the requested file.
                with open(merged_notes_path, "a+", \
                    encoding=self.settings["output"]["file_encoding"]) as out:
                    for note in merged_notes:
                        out.write(note)

                # Display a message stating that the notes were successfully merged.
                label_merge_success = self.template["label_merge_success"]
                label_merge_success["text"] = merge_success_message(basename(merged_notes_path))
                merge_success_window = \
                    self.widgets.create_entire_window("window_merge_success")
                merge_success_window.mainloop()
