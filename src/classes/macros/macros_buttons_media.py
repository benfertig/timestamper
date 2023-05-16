#-*- coding: utf-8 -*-
"""This module contains the MediaButtonMacros class which stores the functions
that are executed when a media button in the Time Stamper program is pressed."""

from sys import platform
from tkinter import RAISED, SUNKEN
from .macros_helper_methods import button_enable_disable_macro, replace_button_message_variables

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


class MediaButtonMacros():
    """This class stores all of the macros that execute when media buttons are pressed."""

    def __init__(self, parent):

        self.parent = parent
        self.time_stamper = parent.time_stamper
        self.template = parent.template
        self.settings = parent.settings
        self.widgets = parent.widgets
        self.timer = parent.timer

        self.play_press_time = 0.0

    def attempt_button_message(self, button_str_key, timestamp=None, **user_variables):
        """This method determines whether a message should be printed when a media
        button is pressed, and, if it is determined that a message should be
        printed, prints that message to the notes log and the output file."""

        # Only attempt to print the button's message if there is an output path.
        if self.widgets["entry_output_path"].get():

            # Get the button's message before replacements.
            button_message_pre_replace = self.parent.get_button_message_input(button_str_key)

            # Only attempt to print a message if there is a message associated with the button.
            if button_message_pre_replace is not None:

                # Generate a timestamp if one was not provided.
                if timestamp is None:
                    timestamp = self.timer.current_time_to_timestamp()

                # Replace any variables in the button's message.
                button_message = replace_button_message_variables(\
                    button_message_pre_replace, **user_variables)

                # Print the button's message.
                self.parent.print_timestamped_message(f"{button_message}\n", timestamp)

    def button_pause_macro(self, *_, force_suppress_message=False):
        """This method will be executed when the pause button is pressed."""

        # Enable and disable the relevant widgets for when the pause button is pressed.
        button_enable_disable_macro(self.template["button_pause"], self.widgets)

        # Only attempt to print a button message if the
        # button message should not be force overridden.
        if not force_suppress_message:
            self.attempt_button_message("button_pause")

        # Pause the timer.
        self.timer.pause()

    def playback_press_macro(self, playback_type):
        """This method is called by button_play_press_macro, button_rewind_press_macro and
        button_fast_forward_press_macro. The functions performed by these three methods are
        very similar, so their procedures have been condensed down to a single method here, and
        different parameters are passed depending on where this method is being called from."""

        button_str_key = f"button_{playback_type}"

        # Enable and disable the relevant widgets for when this button is pressed.
        button_enable_disable_macro(self.template[button_str_key], self.widgets)

        # Make the button appear pressed.
        self.widgets[button_str_key].config(relief=SUNKEN)

        # Record the time that the button was pressed.
        self.play_press_time = self.timer.get_current_seconds()

        # Schedule the timer to start after a short delay (this scheduled start will be
        # cancelled if the current button is released before the delay period has ended).
        self.timer.scheduled_id = self.time_stamper.root.after(250, self.timer.play, playback_type)

        return "break"

    def button_play_press_macro(self, *_):
        """This method will be executed AS SOON AS THE LEFT-MOUSE-BUTTON IS PRESSED
        ON THE PLAY BUTTON (as opposed to waiting for the left-mouse-button to be
        released on the play button, as is the default case with other buttons)."""

        self.playback_press_macro("play")

    def button_rewind_press_macro(self, *_):
        """This method will be executed AS SOON AS THE LEFT-MOUSE-BUTTON IS PRESSED
        ON THE REWIND BUTTON (as opposed to waiting for the left-mouse-button to be
        released on the rewind button, as is the default case with other buttons)."""

        self.playback_press_macro("rewind")

    def button_fast_forward_press_macro(self, *_):
        """This method will be executed AS SOON AS THE LEFT-MOUSE-BUTTON IS PRESSED ON
        THE FAST-FORWARD BUTTON (as opposed to waiting for the left-mouse-button to be
        released on the fast-forward button, as is the default case with other buttons)."""

        self.playback_press_macro("fast_forward")

    def playback_release_macro(self, playback_type):
        """This method is called by button_play_release_macro, button_rewind_release_macro and
        button_fast_forward_release_macro. The functions performed by these three methods are
        very similar, so their procedures have been condensed down to a single method here, and
        different parameters are passed depending on where this method is being called from."""

        button_str_key = f"button_{playback_type}"
        self.widgets[button_str_key].config(relief=RAISED)

        # If the playback button HAS NOT been held long enough to initiate the timer...
        if self.timer.scheduled_id:

            # Get the current timestamp.
            timestamp = self.timer.current_time_to_timestamp()

            # Start the timer.
            self.timer.play(playback_type=playback_type)

            # Return the timestamp, indicating that playback has started.
            return timestamp

        # If the playback button HAS been held long enough to initiate the timer...

        # The program should behave as if the pause button was pressed (omitting button messages).
        self.button_pause_macro(force_suppress_message=True)

        # Reset the timer to where it was at when the current playback button was pressed.
        self.timer.display_time(self.play_press_time)

        # Return None, indicating that playback has stopped.
        return None

    def button_play_release_macro(self, *_, force_suppress_message=False):
        """This method will be executed when the user releases
        the mouse after having clicked on the play button."""

        timestamp = self.playback_release_macro("play")

        # Only attempt to print a button message if the timer started as a result
        # of this method and the button message should not be force overridden.
        if timestamp and not force_suppress_message:
            self.attempt_button_message("button_play", timestamp=timestamp)

    def button_rewind_release_macro(self, *_, force_suppress_message=False):
        """This method will be executed when the user releases
        the mouse after having clicked on the rewind button."""

        timestamp = self.playback_release_macro("rewind")

        # Only attempt to print a button message if the timer started as a result
        # of this method and the button message should not be force overridden.
        if timestamp and not force_suppress_message:
            self.attempt_button_message("button_rewind", timestamp=timestamp)

    def button_fast_forward_release_macro(self, *_, force_suppress_message=False):
        """This method will be executed when the user releases the
        mouse after having clicked on the fast-forward button."""

        timestamp = self.playback_release_macro("fast_forward")

        # Only attempt to print a button message if the timer started as a result
        # of this method and the button message should not be force overridden.
        if timestamp and not force_suppress_message:
            self.attempt_button_message("button_fast_forward", timestamp=timestamp)

    def skip_backward_or_forward_macro(self, is_skip_backward):
        """This method contains the entire functionality for the skip backward and skip forward
        buttons. The functions performed by these two buttons are very similar, so their
        procedures have been condensed down to a single method here, and different parameters
        are passed depending on whether the skip backward or skip forward button was pressed."""

        direction = "backward" if is_skip_backward else "forward"
        button_str_key = f"button_skip_{direction}"

        # Enable and disable the relevant widgets for when
        # the skip backward/forward button is pressed.
        button_enable_disable_macro(self.template[button_str_key], self.widgets)

        # Get the timestamp before skipping backward/forward.
        timestamp = self.timer.current_time_to_timestamp()

        # Skip the timer backward/forward the specified number of seconds.
        adjust_amount = float(self.widgets[f"entry_skip_{direction}"].get())
        skip_amount = \
            self.timer.adjust_timer(adjust_amount * -1 if is_skip_backward else adjust_amount)

        # Get the time after skipping backward/forward.
        new_time = self.timer.current_time_to_timestamp(include_brackets=False)

        # Round the skip amount to the nearest hundreth.
        skip_amount = abs(round(skip_amount, 2))
        if skip_amount % 1 == 0:
            skip_amount = int(skip_amount)

        return timestamp, skip_amount, new_time

    def button_skip_backward_macro(self, *_):
        """This method will be executed when the skip backward button is pressed."""

        # Attempt to skip the timer backward.
        timestamp, skip_amount, new_time = self.skip_backward_or_forward_macro(True)

        # Only attempt to print a button message if the timer skipped as a result of this method.
        if skip_amount != 0:
            self.attempt_button_message("button_skip_backward", \
                timestamp=timestamp, amount=str(skip_amount), dest=new_time)

    def button_skip_forward_macro(self, *_):
        """This method will be executed when the skip forward button is pressed."""

        # Attempt to skip the timer forward.
        timestamp, skip_amount, new_time = self.skip_backward_or_forward_macro(False)

        # Only attempt to print a button message if the timer skipped as a result of this method.
        if skip_amount != 0:
            self.attempt_button_message("button_skip_forward", \
                timestamp=timestamp, amount=str(skip_amount), dest=new_time)

    def button_mute_macro(self, *_):
        """This method will be executed when the mute button is pressed."""

        # If a media player was successfully retrieved...
        if self.time_stamper.media_player:

            # The way that the name of the current mute button image is
            # referenced changes depending on whether we are currently using a Mac.
            if platform.startswith("darwin"):
                button_mute_image_name = self.widgets["button_mute"]["image"].name
            else:
                button_mute_image_name = self.widgets["button_mute"]["image"]

            # If the volume WAS previoulsy muted...
            if button_mute_image_name == self.widgets["volume_mute.png"].name:

                # Get the value of the volume slider.
                volume_scale_value = int(100 - self.widgets["scale_media_volume"].variable.get())

                # Set the volume to the current value of the volume slider.
                self.time_stamper.media_player.audio_set_volume(volume_scale_value)

                # The mute button image should reflect the current value of the volume slider.
                updated_image_str_key = self.parent.updated_mute_button_image(volume_scale_value)

            # If the volume WAS NOT previously unmuted...
            else:

                # Mute the volume.
                self.time_stamper.media_player.audio_set_volume(0)

                # The mute button image should show that the media is now muted.
                updated_image_str_key = "volume_mute.png"

            # Update the mute button image.
            button_mute = self.widgets["button_mute"]
            button_mute_image_new = self.widgets[updated_image_str_key]
            button_mute.config(image=button_mute_image_new)
            button_mute.image = button_mute_image_new

        # If a media player was not successfully retrieved, disable all media playback settings.
        else:
            self.parent.disable_media_widgets()
