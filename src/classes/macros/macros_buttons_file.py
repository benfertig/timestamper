#-*- coding: utf-8 -*-
"""This module contains the FileButtonMacros class which stores the functions
that are executed when a file button in the Time Stamper program is pressed."""

from ntpath import sep as ntpath_sep
from posixpath import sep as posixpath_sep
from os.path import basename
from tkinter import filedialog
from pyglet import options as pyglet_options
from pyglet.media import have_ffmpeg
from .macros_helper_methods import merge_success_message, merge_failure_message_file_not_readable, \
    merge_notes, print_to_entry, print_to_text, verify_text_file
try:
    from sys import getwindowsversion
except ImportError:
    pass
finally:
    from sys import platform

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

    def file_select_macro(self, label_str_key, entry_str_key, window_title, file_types):
        """This method is called on by button_output_select_macro and
        button_audio_select_macro. Since both "button_output_select" and
        "button_audio_select" prompt the user to select a file, the procedures for
        their macros can, to a large extent, be condensed down into this method."""

        # Store the template for the label, the widget for the label,
        # and the widget for the entry into abbreviated file names.
        label_template = self.template[label_str_key]
        label_object = self.widgets[label_str_key]
        entry_object = self.widgets[entry_str_key]

        # Get the path to the selected file.
        file_full_path = filedialog.askopenfilename(title=window_title, \
            initialdir=self.template.starting_dir, filetypes=file_types)

        # Change the text of the label that appears above the file
        # path entry widget to indicate that a file has been selected.
        if isinstance(label_template["text"], dict):
            label_object["text"] = label_template["text"]["value_if_true"]

        # Change the file path to the Windows format if we are on a Windows computer.
        if platform.startswith("win"):
            file_full_path = file_full_path.replace(posixpath_sep, ntpath_sep)

        # Print the file path to the entry widget.
        print_to_entry(file_full_path, entry_object, wipe_clean=True)

    def button_output_select_macro(self):
        """This method will be executed when the "Choose output location" button is pressed."""

        # Get the path to the selected output file.
        file_types = (("Text files", "*.txt"), ('All files', '*.*'))
        self.file_select_macro("label_output_path", \
            "entry_output_path", "Select a text file", file_types)

        # Clear the text displaying the notes log.
        print_to_text("", self.widgets["text_log"], wipe_clean=True)

        # Check whether or not the selected output file is valid and respond accordingly.
        self.parent.validate_output_file()

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

        # TODO: SOME POTENTIAL FUTURE AUDIO FORMATS TO INCLUDE ARE (but are not limited to):
        # *.aiff *.aac *.m4a *.ogg *.alac *.dsd *.mqa

        pyglet_options["search_local_libs"] = True
        audio_file_types = set()

        # If we are on Windows...
        if platform.startswith("win"):

            # Store the major and minor versions of the current Windows operating system.
            windows_version_major, windows_version_minor = getwindowsversion()[0:2]

            # If we are on Windows Vista or above...
            if windows_version_major >= 6:

                audio_file_types.update({"*.mp3", "*.wma"})

                # If we are on Windows 7 or above (not Windows Vista)...
                if not (windows_version_major == 6 and windows_version_minor == 0):
                    audio_file_types.update({"*.aac", "*.adts"})

                    # If we are on Windows 10 or above (not Windows Vista or Windows 7)...
                    if windows_version_major >= 10:
                        audio_file_types.update({"*.flac"})

        # If Pyglet has determined that it has ffmpeg at its disposal, then the following additional
        # audio file formats should be made available to the user under the "Audio files" option in
        # the file dialog window labeled "Select an audio file". However, keep in mind that if
        # Pyglet has determined that it has ffmpeg at its disposal, then Pyglet can play more audio
        # file formats other than just those that are listed directly below. The audio file formats
        # listed directly below are simply some of the most common audio file formats that Pyglet
        # can play when it is able to make use of ffmpeg. Therefore, it may be wise to include
        # more audio file formats directly below in the future (see the TODO at the top of this
        # method). Although, regardless of whether or not more audio file formats are added directly
        # below in the future, the user should always be able to select ANY file they want by
        # selecting the "All files" option in the file dialog window labeled "Select an audio file".
        if have_ffmpeg():
            audio_file_types.update({"*.au", "*.mp2", "*.mp3", "*.wav", "*.wma"})

        # INCLUDE "Audio files" as an option in the file dialog window if ANY of
        # the audio file formats mentioned in this method were determined to be
        # compatible with the user's installation of the Time Stamper program.
        if audio_file_types:
            audio_file_types = " ".join(sorted(audio_file_types))
            file_types = (("Audio files", audio_file_types), ("All files", "*.*"))

        # DO NOT INCLUDE "Audio files" as an option in the file dialog window if NONE
        # of the audio file formats mentioned in this method were determined to
        # be compatible with the user's installation of the Time Stamper program.
        else:
            file_types = (("All files", "*.*"))

        # Get the path to the selected audio file.
        self.file_select_macro("label_audio_path", \
            "entry_audio_path", "Select an audio file", file_types)

        # Check whether or not the selected audio file is valid and respond accordingly.
        self.parent.validate_audio_player()

    def on_close_window_merge_1_macro(self, window_merge_1):
        """This method will be executed when the FIRST window displaying
        instructions to the user on how to merge output files is closed."""

        # Destroy the window displaying the first set of merge instructions.
        window_merge_1.destroy()

        # The user will be prompted to select the files whose notes they wish to merge.
        file_types = (("Text files", "*.txt"), ('All files', '*.*'))
        files_full_paths = filedialog.askopenfilenames(title="Select output files to merge", \
            initialdir=self.template.starting_dir, filetypes=file_types)

        # Only merge the notes if at least one file was selected.
        if files_full_paths:

            # Save the specified output file encoding into an abbreviated file name.
            file_encoding = self.settings["output"]["file_encoding"]

            # Verify the validity of the text files whose notes the user would like to merge.
            invalid_file_names = []
            for file_path in files_full_paths:
                if not verify_text_file(file_path, file_encoding, True, False):
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
                merged_notes = merge_notes(files_full_paths, file_encoding)

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
        file_types = (("Text files", "*.txt"), ('All files', '*.*'))
        merged_notes_path = \
            filedialog.askopenfilename(title="Select destination for merged outputs", \
            initialdir=self.template.starting_dir, filetypes=file_types)

        # Only proceed with attempting to write the merged notes to a
        # file if the user selected a file to save the merged notes to.
        if merged_notes_path:

            # Save the specified output file encoding into an abbreviated file name.
            file_encoding = self.settings["output"]["file_encoding"]

            # If the user tried to save the merged notes to a file whose notes
            # were already going to be a part of the merge, do not write the
            # merged notes to a file and instead display a failure message.
            if merged_notes_path in files_full_paths:

                merge_failure_window = \
                    self.widgets.create_entire_window("window_merge_failure_repeated_file")
                merge_failure_window.mainloop()

            # If the user tried to save the merged notes to an unreadable file, do not
            # write the merged notes to a file and instaed display a failure message.
            elif not verify_text_file(merged_notes_path, file_encoding, False, True):
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
                with open(merged_notes_path, "a+", encoding=file_encoding) as out:
                    for note in merged_notes:
                        out.write(note)

                # Display a message stating that the notes were successfully merged.
                label_merge_success = self.template["label_merge_success"]
                label_merge_success["text"] = merge_success_message(basename(merged_notes_path))
                merge_success_window = \
                    self.widgets.create_entire_window("window_merge_success")
                merge_success_window.mainloop()
