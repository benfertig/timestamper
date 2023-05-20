#-*- coding: utf-8 -*-
"""This module stores the functions that are executed when
media buttons in the Time Stamper program are pressed."""

from sys import platform

import classes
import methods.macros.methods_macros_helper as methods_helper
import methods.macros.methods_macros_media as methods_media
import methods.macros.methods_macros_output as methods_output
import methods.macros.methods_macros_timing as methods_timing

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


def button_pause_macro(*_, force_suppress_message=False):
    """This method will be executed when the pause button is pressed."""

    # Enable and disable the relevant widgets for when the pause button is pressed.
    methods_helper.button_enable_disable_macro(classes.template["button_pause"])

    # Only attempt to print a button message if the
    # button message should not be force overridden.
    if not force_suppress_message:
        methods_output.attempt_button_message("button_pause")

    # Pause the timer.
    classes.timer.pause()


def button_play_press_macro(*_):
    """This method will be executed AS SOON AS THE LEFT-MOUSE-BUTTON IS PRESSED
    ON THE PLAY BUTTON (as opposed to waiting for the left-mouse-button to be
    released on the play button, as is the default case with other buttons)."""

    methods_timing.playback_press_macro("play")


def button_rewind_press_macro(*_):
    """This method will be executed AS SOON AS THE LEFT-MOUSE-BUTTON IS PRESSED
    ON THE REWIND BUTTON (as opposed to waiting for the left-mouse-button to be
    released on the rewind button, as is the default case with other buttons)."""

    methods_timing.playback_press_macro("rewind")


def button_fast_forward_press_macro(*_):
    """This method will be executed AS SOON AS THE LEFT-MOUSE-BUTTON IS PRESSED ON
    THE FAST-FORWARD BUTTON (as opposed to waiting for the left-mouse-button to be
    released on the fast-forward button, as is the default case with other buttons)."""

    methods_timing.playback_press_macro("fast_forward")


def button_play_release_macro(*_, force_suppress_message=False):
    """This method will be executed when the user releases
    the mouse after having clicked on the play button."""

    timestamp = methods_timing.playback_release_macro("play")

    # Only attempt to print a button message if the timer started as a result
    # of this method and the button message should not be force overridden.
    if timestamp and not force_suppress_message:
        methods_output.attempt_button_message("button_play", timestamp=timestamp)


def button_rewind_release_macro(*_, force_suppress_message=False):
    """This method will be executed when the user releases
    the mouse after having clicked on the rewind button."""

    timestamp = methods_timing.playback_release_macro("rewind")

    # Only attempt to print a button message if the timer started as a result
    # of this method and the button message should not be force overridden.
    if timestamp and not force_suppress_message:
        methods_output.attempt_button_message("button_rewind", timestamp=timestamp)


def button_fast_forward_release_macro(*_, force_suppress_message=False):
    """This method will be executed when the user releases the
    mouse after having clicked on the fast-forward button."""

    timestamp = methods_timing.playback_release_macro("fast_forward")

    # Only attempt to print a button message if the timer started as a result
    # of this method and the button message should not be force overridden.
    if timestamp and not force_suppress_message:
        methods_output.attempt_button_message("button_fast_forward", timestamp=timestamp)


def button_skip_backward_macro(*_):
    """This method will be executed when the skip backward button is pressed."""

    # Attempt to skip the timer backward.
    timestamp, skip_amount, new_time = methods_timing.skip_backward_or_forward_macro(True)

    # Only attempt to print a button message if the timer skipped as a result of this method.
    if skip_amount != 0:
        methods_output.attempt_button_message("button_skip_backward", \
            timestamp=timestamp, amount=str(skip_amount), dest=new_time)


def button_skip_forward_macro(*_):
    """This method will be executed when the skip forward button is pressed."""

    # Attempt to skip the timer forward.
    timestamp, skip_amount, new_time = methods_timing.skip_backward_or_forward_macro(False)

    # Only attempt to print a button message if the timer skipped as a result of this method.
    if skip_amount != 0:
        methods_output.attempt_button_message("button_skip_forward", \
            timestamp=timestamp, amount=str(skip_amount), dest=new_time)


def button_mute_macro(*_):
    """This method will be executed when the mute button is pressed."""

    # If a media player was successfully retrieved...
    if classes.media_player:

        # The way that the name of the current mute button image is
        # referenced changes depending on whether we are currently using a Mac.
        if platform.startswith("darwin"):
            button_mute_image_name = classes.widgets["button_mute"]["image"].name
        else:
            button_mute_image_name = classes.widgets["button_mute"]["image"]

        # If the volume WAS previoulsy muted...
        if button_mute_image_name == classes.widgets["volume_mute.png"].name:

            # Get the value of the volume slider.
            volume_scale_value = int(100 - classes.widgets["scale_media_volume"].variable.get())

            # Set the volume to the current value of the volume slider.
            classes.media_player.audio_set_volume(volume_scale_value)

            # The mute button image should reflect the current value of the volume slider.
            updated_image_str_key = methods_media.updated_mute_button_image(volume_scale_value)

        # If the volume WAS NOT previously unmuted...
        else:

            # Mute the volume.
            classes.media_player.audio_set_volume(0)

            # The mute button image should show that the media is now muted.
            updated_image_str_key = "volume_mute.png"

        # Update the mute button image.
        button_mute = classes.widgets["button_mute"]
        button_mute_image_new = classes.widgets[updated_image_str_key]
        button_mute.config(image=button_mute_image_new)
        button_mute.image = button_mute_image_new

    # If a media player was not successfully retrieved, disable all media playback settings.
    else:
        methods_media.reset_media_widgets()
        methods_helper.toggle_widgets(classes.template["button_media_select"], False)
