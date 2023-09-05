#-*- coding: utf-8 -*-
"""This module stores the functions that are executed when
file buttons in the Time Stamper program are pressed."""

from tkinter import filedialog

from vlc import MediaPlayer

import classes
import methods.macros.methods_macros_helper as methods_helper
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


def button_output_select_macro(*_, file_full_path=None, erase_if_empty=False):
    """This method will be executed when the "Choose output location" button is pressed.
    The optional argument erase_if_empty, which is set to False by default, determines
    whether the previous output file should be cancelled if no output file is specified."""

    if file_full_path is None:

        # Get the path to the selected output file.
        file_types = (("Text files", "*.txt"), ('All files', '*.*'))

        # Get the path to the selected file.
        file_full_path = filedialog.askopenfilename(title="Select a text file", \
            initialdir=classes.template.starting_dir, filetypes=file_types)

    # Check whether or not the selected output file is valid and respond accordingly.
    methods_output.validate_output_file(file_full_path, erase_if_empty=erase_if_empty)


def button_cancel_output_macro(*_):
    """This method will be executed when the cancel output button is pressed."""

    # Enable and disable the relevant widgets for when the cancel output button is pressed.
    methods_helper.button_enable_disable_macro(classes.template["button_cancel_output"])

    # Reset the output path in the TimeStamper class.
    classes.time_stamper.output_path = ""

    # Configure the relevant widgets to reflect that a valid output
    # file IS NOT active (distinct from enabling/disabling widgets).
    methods_output.reset_output_widgets()

    # Enable/disable the relevant widgets to reflect that a valid output file IS NOT active.
    methods_helper.toggle_widgets(classes.template["button_output_select"], False)

def button_merge_output_files_macro(*_):
    """This method will be executed when the "Merge output files" button is pressed."""

    # Call the function that will display the first window with instructions
    # on how to merge output files, passing a macro that will make the first
    # file explorer window appear when the instructions window is closed,
    # wherein the user should select all output files they would like to merge.
    window_merge_first_message = \
        classes.widgets.create_entire_window("window_merge_first_message")
    window_merge_first_message.mainloop()


def button_media_select_macro(*_, file_full_path=None, erase_if_empty=False):
    """This method will be executed when the "Select synced media file" button is pressed.
    This method can also be called independently of pressing of the "Select synced media
    file" button, as is done in the run() method of TimeStamper in time_stamper.py. When
    calling this method from TimeStamper.run() in time_stamper.py, file_full_path is set
    to the value of TimeStamper.settings["media"]["path"]. Even if the initial media file
    validation fails on this value, it is imporant to at least attempt this initial media
    file validation (see the docstring for validate_media_player for more information).
    The optional argument erase_if_empty, which is set to False by default, determines
    whether the previous media file should be cancelled if no media file is specified."""

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
    methods_media.validate_media_player(file_full_path, erase_if_empty=erase_if_empty)


def button_cancel_media_macro(*_):
    """This method will be executed when the cancel media button is pressed."""

    # Enable and disable the relevant widgets for when the cancel media button is pressed.
    methods_helper.button_enable_disable_macro(classes.template["button_cancel_media"])

    # Stop the Time Stamper program's media player if it exists.
    if isinstance(classes.time_stamper.media_player, MediaPlayer):
        classes.time_stamper.media_player.stop()

    # Try to release the current media player.
    methods_media.attempt_media_player_release()
    classes.time_stamper.media_player = None

    # Reset and disable the widgets associated with media.
    methods_media.reset_media_widgets()
    methods_helper.toggle_widgets(classes.template["button_media_select"], False)
