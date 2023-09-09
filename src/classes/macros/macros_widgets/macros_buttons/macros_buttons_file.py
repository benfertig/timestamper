#-*- coding: utf-8 -*-
"""This module stores the functions that are executed when
file buttons in the Time Stamper program are pressed."""

from ntpath import sep as ntpath_sep
from posixpath import sep as posixpath_sep
from sys import platform
from tkinter import filedialog

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


def button_output_select_macro(*_, file_full_path=None, erase_if_empty=False):
    """This method will TYPICALLY be executed when the "Select output file" button is pressed.
    The optional argument file_full_path, which is set to None by default, accepts a pre-determined
    file path and will bypass the file dialog menu for output file selection. This argument
    should only ever be specified when this method is NOT being called as a result of the
    user having pressed the "Select output file" button (e.g., from the TimeStamper.run()
    method). The optional argument erase_if_empty, which is set to False by default, determines
    whether the previous output file should be cancelled if no output file is specified."""

    if file_full_path is None:

        # Get the path to the selected output file.
        file_types = (("Text files", "*.txt"), ('All files', '*.*'))

        # Get the path to the selected file.
        file_full_path = filedialog.askopenfilename(title="Select a text file", \
            initialdir=classes.template.starting_dir, filetypes=file_types)

    # Change the file path to the Windows format if we are on a Windows computer.
    if platform.startswith("win"):
        file_full_path = file_full_path.replace(posixpath_sep, ntpath_sep)

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


def button_sort_output_macro(*_):
    """This method will be executed when the "Sort output" button is pressed."""

    output_path, text_log = classes.time_stamper.output_path, classes.widgets["text_log"]

    # If the output file is valid (this should already be the case, but just double-checking)...
    if methods_output.verify_text_file(output_path, True, True):

        # Sort all the notes from the current output file.
        sorted_notes = methods_output.merge_notes([output_path])

        # Erase the current contents of the notes log and the output file.
        methods_output.print_to_text("", text_log, wipe_clean=True)
        methods_output.print_to_file("", output_path, access_mode="w+")

        # Print the sorted notes to the notes log and to the output file.
        for note in sorted_notes:
            methods_output.print_to_text(note, text_log, wipe_clean=False)
            methods_output.print_to_file(note, output_path, access_mode="a+")


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

        # Define all media file types supported by VLC.
        media_file_types = "*.3g2 *.3gp *.3gp2 *.3gpp *.amv *.asf *.avi *.bik *.bin *.divx " \
            "*.drc *.dv *.f4v *.flv *.gvi *.gxf *.iso *.m1v *.m2v *.m2t *.m2ts *.m4v *.mkv *.mov " \
            "*.mp2 *.mp2V *.mp4 *.mp4v *.mpe *.mpeg *.mpeg1 *.mpeg2 *.mpeg4 *.mpg *.mpv2 *.mts " \
            "*.mtv *.mxf *.mxg *.nsv *.nuv *.ogg *.ogm *.ogv *.ogx *.ps *.rec *.rm *.rmvb " \
            "*.rpl *.thp *.tod *.ts *.tts *.txd *.vob *.vro *.webm *.wm *.wmv *.wtv *.xesc *.3ga " \
            "*.669 *.152 *.aac *.ac3 *.adt *.adts *.aif *.aiff *.amr *.aob *.ape *.awb *.caf " \
            "*.dts *.flac *.it *.kar *.m4a *.m4b *.m4p *.m5p *.mid *.mka *.mlp *.mod *.mpa *.mp1 " \
            "*.mp2 *.mp3 *.mpc *.mpga *.mus *.oga *.ogg *oma *.opus *.qcp *.ra *.rmi *.s3m *.sid " \
            "*.spx *.thd *.tta *.voc *vqf *.w64 *.wav *.wma *.wv *.xa *.xm"

        file_types = (("Media files", media_file_types), ("All files", "*.*"))

        # Get the path to the selected file.
        file_full_path = filedialog.askopenfilename(title="Select a media file", \
            initialdir=classes.template.starting_dir, filetypes=file_types)

    # Change the file path to the Windows format if we are on a Windows computer.
    if platform.startswith("win"):
        file_full_path = file_full_path.replace(posixpath_sep, ntpath_sep)

    # Check whether or not the selected media file is valid and respond accordingly.
    methods_media.validate_media_player(file_full_path, erase_if_empty=erase_if_empty)


def button_cancel_media_macro(*_):
    """This method will be executed when the cancel media button is pressed."""

    # Enable and disable the relevant widgets for when the cancel media button is pressed.
    methods_helper.button_enable_disable_macro(classes.template["button_cancel_media"])

    # Destroy the video window if it exists.
    if "window_video" in classes.widgets.mapping \
        and classes.widgets.mapping["window_video"].winfo_exists():
        classes.widgets["window_video"].destroy()

    # Try to release the current media player.
    methods_media.attempt_media_player_release()
    classes.time_stamper.media_player = None

    # Reset and disable the widgets associated with media.
    methods_media.reset_media_widgets()
    methods_helper.toggle_widgets(classes.template["button_media_select"], False)
