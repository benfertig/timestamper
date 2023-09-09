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
