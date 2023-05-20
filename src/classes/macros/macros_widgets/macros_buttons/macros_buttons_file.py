#-*- coding: utf-8 -*-
"""This module stores the functions that are executed when
file buttons in the Time Stamper program are pressed."""

from tkinter import filedialog

import classes
import methods.macros.methods_macros_media as methods_media
import methods.macros.methods_macros_output as methods_output

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


def button_output_select_macro(*_, file_full_path=None):
    """This method will be executed when the "Choose output location" button is pressed."""

    if file_full_path is None:

        # Get the path to the selected output file.
        file_types = (("Text files", "*.txt"), ('All files', '*.*'))

        # Get the path to the selected file.
        file_full_path = filedialog.askopenfilename(title="Select a text file", \
            initialdir=classes.template.starting_dir, filetypes=file_types)

    # Check whether or not the selected output file is valid and respond accordingly.
    methods_output.validate_output_file(file_full_path)


def button_merge_output_files_macro(*_):
    """This method will be executed when the "Merge output files" button is pressed."""

    # Call the function that will display the first window with instructions
    # on how to merge output files, passing a macro that will make the first
    # file explorer window appear when the instructions window is closed,
    # wherein the user should select all output files they would like to merge.
    window_merge_first_message = \
        classes.widgets.create_entire_window("window_merge_first_message")
    window_merge_first_message.mainloop()


def button_media_select_macro(*_, file_full_path=None):
    """This method will be executed when the "Select synced media file" button is pressed.
    This method can also be called independently of pressing of the "Select synced media
    file" button (as is done in the run() method of TimeStamper in time_stamper.py). When
    calling this method from TimeStamper.run() in time_stamper.py, file_full_path is set
    to the value of TimeStamper.settings["media"]["path"]. Even if the initial media file
    validation fails on this value, it is imporant to at least attempt this initial media
    file validation (see the docstring for validate_media_player for more information)."""

    if file_full_path is None:

        # TODO: SOME POTENTIAL FUTURE AUDIO FORMATS TO INCLUDE ARE (but are not limited to):
        # *.aiff *.aac *.m4a *.ogg *.alac *.dsd *.mqa

        # TODO: RESEARCH POTENTIAL VIDEO FORMATS AS WELL:

        media_file_types = set()

        # If we are on Windows...
        if platform.startswith("win"):

            # Store the major and minor versions of the current Windows operating system.
            windows_version_major, windows_version_minor = getwindowsversion()[0:2]

            # If we are on Windows Vista or above...
            if windows_version_major >= 6:

                media_file_types.update({"*.mp3", "*.wma"})

                # If we are on Windows 7 or above (not Windows Vista)...
                if not (windows_version_major == 6 and windows_version_minor == 0):
                    media_file_types.update({"*.aac", "*.adts"})

                    # If we are on Windows 10 or above (not Windows Vista or Windows 7)...
                    if windows_version_major >= 10:
                        media_file_types.update({"*.flac"})

        media_file_types.update({"*.au", "*.mp2", "*.mp3", "*.wav", "*.wma"})

        # INCLUDE "Media files" as an option in the file dialog window if ANY of
        # the media file formats mentioned in this method were determined to be
        # compatible with the user's installation of the Time Stamper program.
        if media_file_types:
            media_file_types = " ".join(sorted(media_file_types))
            file_types = (("Media files", media_file_types), ("All files", "*.*"))

        # DO NOT INCLUDE "Media files" as an option in the file dialog window if NONE
        # of the media file formats mentioned in this method were determined to
        # be compatible with the user's installation of the Time Stamper program.
        else:
            file_types = (("All files", "*.*"),)

        # Get the path to the selected file.
        file_full_path = filedialog.askopenfilename(title="Select a media file", \
            initialdir=classes.template.starting_dir, filetypes=file_types)

    # Check whether or not the selected media file is valid and respond accordingly.
    methods_media.validate_media_player(file_full_path)
