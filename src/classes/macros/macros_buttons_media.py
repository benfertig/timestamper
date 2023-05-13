#-*- coding: utf-8 -*-
"""This module contains the MediaButtonMacros class which stores the functions
that are executed when a media button in the Time Stamper program is pressed."""

from sys import platform
from tkinter import RAISED, SUNKEN
from .macros_helper_methods import disable_button, \
    button_enable_disable_macro, replace_button_message_variables

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

    def non_skip_button_message(self, button_str_key):
        """This method determines whether a message should be printed when a media button
        is pressed, and, if it is determined that a message should be printed, prints that
        message to the notes log and the output file. This method gets called for any media
        button presses other than the skip backward/forward buttons, since those buttons
        potentially require some extra computation to generate their button messages."""

        # Get the button's message before replacements.
        button_message_pre_replace = self.parent.get_button_message_input(button_str_key)

        # Only print a message if there is a message associated with the button.
        if button_message_pre_replace is not None:

            # Replace any variables in the button's message.
            button_message = \
                replace_button_message_variables(button_message_pre_replace, button_str_key)

            # Print the button's message if an output file exists.
            if self.widgets["entry_output_path"].get():
                self.parent.print_timestamped_message(f"{button_message}\n")

    def button_pause_macro(self, *_):
        """This method will be executed when the pause button is pressed."""

        # Enable and disable the relevant widgets for when the pause button is pressed.
        button_enable_disable_macro(self.template["button_pause"], self.widgets)

        # Print the pause button's message if one was set in the settings.
        self.non_skip_button_message("button_pause")

        # If an audio source is loaded, the rewind and fast-forward buttons, which would
        # otherwise be activated when the pause button is pressed, should remain deactivated.
        if self.time_stamper.audio.source:
            disable_button(self.widgets["button_rewind"], \
                self.template["button_rewind"]["mac_disabled_color"])
            disable_button(self.widgets["button_fast_forward"], \
                self.template["button_fast_forward"]["mac_disabled_color"])

        # Pause the timer.
        self.timer.pause()

    def playback_press_macro(self, playback_type):
        """This method is called by button_play_press_macro, button_rewind_press_macro and
        button_fast_forward_press_macro. The functions performed by these three methods are
        very similar, so their procedures have been condensed down to a single method here, and
        different parameters are passed depending on where this method is being called from."""

        self.widgets[f"button_{playback_type}"].config(relief=SUNKEN)
        self.play_press_time = self.timer.get_current_seconds()
        self.timer.scheduled_id = self.time_stamper.root.after(250, self.timer.play, playback_type)

        return "break"

    def playback_release_macro(self, playback_type):
        """This method is called by button_play_release_macro, button_rewind_release_macro and
        button_fast_forward_release_macro. The functions performed by these three methods are
        very similar, so their procedures have been condensed down to a single method here, and
        different parameters are passed depending on where this method is being called from."""

        button_str_key = f"button_{playback_type}"
        self.widgets[button_str_key].config(relief=RAISED)

        # If the playback button HAS NOT been held long enough
        # to initiate the timer, start the timer immediately.
        if self.timer.scheduled_id:

            self.timer.scheduled_id = None

            # Enable and disable the relevant widgets for when this button is pressed.
            button_enable_disable_macro(self.template[button_str_key], self.widgets)

            # Print the button's message if one was set in the settings.
            self.non_skip_button_message(button_str_key)

            # Start the timer.
            self.timer.play(playback_type=playback_type)

        # If the play button HAS been held long enough
        # to initiate the timer, stop the timer.
        else:
            button_enable_disable_macro(self.template["button_pause"], self.widgets)
            self.timer.pause()
            self.timer.display_time(self.play_press_time)

    def button_play_press_macro(self, *_):
        """This method will be executed AS SOON AS THE PLAY BUTTON IS PRESSED
        (as opposed to waiting for the left-mouse-button to be released
        on the play button, as is the default case with other buttons)."""

        self.playback_press_macro("play")

    def button_play_release_macro(self, *_):
        """This method will be executed when the user releases
        the mouse after having clicked on the play button."""

        self.playback_release_macro("play")

        # If an audio source is loaded, the rewind and fast-forward buttons, which would
        # otherwise be activated when the play button is pressed, should remain deactivated.
        if self.time_stamper.audio.source:
            disable_button(self.widgets["button_rewind"], \
                self.template["button_rewind"]["mac_disabled_color"])
            disable_button(self.widgets["button_fast_forward"], \
                self.template["button_fast_forward"]["mac_disabled_color"])

    def button_rewind_press_macro(self, *_):
        """This method will be executed AS SOON AS THE REWIND BUTTON IS PRESSED
        (as opposed to waiting for the left-mouse-button to be released
        on the rewind button, as is the default case with other buttons)."""

        self.playback_press_macro("rewind")

    def button_rewind_release_macro(self, *_):
        """This method will be executed when the user releases
        the mouse after having clicked on the rewind button."""

        self.playback_release_macro("rewind")

    def button_fast_forward_press_macro(self, *_):
        """This method will be executed AS SOON AS THE FAST-FORWARD BUTTON IS
        PRESSED (as opposed to waiting for the left-mouse-button to be released
        on the fast-forward button, as is the default case with other buttons)."""

        self.playback_press_macro("fast_forward")

    def button_fast_forward_release_macro(self, *_):
        """This method will be executed when the user releases the
        mouse after having clicked on the fast-forward button."""

        self.playback_release_macro("fast_forward")

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
        first_timestamp = self.timer.current_time_to_timestamp()

        # Skip the timer backward/forward the specified number of seconds.
        adjust_amount = float(self.widgets[f"entry_skip_{direction}"].get())
        skip_amount = \
            self.timer.adjust_timer(adjust_amount * -1 if is_skip_backward else adjust_amount)

        # Get the timestamp after skipping backward/forward.
        new_time = self.timer.current_time_to_timestamp(include_brackets=False)

        # Get the button's message before replacements.
        button_message_pre_replace = \
            self.parent.get_button_message_input(button_str_key)

        # Only print a message if the timer skipped and
        # there is a message associated with the button.
        if skip_amount != 0 and button_message_pre_replace is not None:

            # Round the skip amount to the nearest hundreth.
            skip_amount = abs(round(skip_amount, 2))
            if skip_amount % 1 == 0:
                skip_amount = int(skip_amount)
            skip_amount = str(skip_amount)

            # Replace any variables in the button's message.
            button_message = replace_button_message_variables(button_message_pre_replace, \
                button_str_key, skip_amount=skip_amount, new_time=new_time)

            # Print the button's message if an output file exists.
            if self.widgets["entry_output_path"].get():
                self.parent.print_timestamped_message(f"{button_message}\n", first_timestamp)

    def button_skip_backward_macro(self, *_):
        """This method will be executed when the skip backward button is pressed."""

        self.skip_backward_or_forward_macro(True)

    def button_skip_forward_macro(self, *_):
        """This method will be executed when the skip forward button is pressed."""

        self.skip_backward_or_forward_macro(False)

    def button_mute_macro(self, *_):
        """This method will be executed when the mute button is pressed."""

        # If an audio player was successfully retrieved...
        if self.time_stamper.audio.player:

            # The way that the name of the current mute button image is
            # referenced changes depending on whether we are currently using a Mac.
            if platform.startswith("darwin"):
                button_mute_image_name = self.widgets["button_mute"]["image"].name
            else:
                button_mute_image_name = self.widgets["button_mute"]["image"]

            # If the volume WAS previoulsy muted...
            if button_mute_image_name == self.widgets["volume_mute.png"].name:

                # Get the value of the volume slider.
                volume_scale_value = 100 - self.widgets["scale_audio_volume"].variable.get()

                # Set the volume to the current value of the volume slider.
                self.time_stamper.audio.player.volume = volume_scale_value / 100

                # The mute button image should reflect the current value of the volume slider.
                updated_image_str_key = self.parent.updated_mute_button_image(volume_scale_value)

            # If the volume WAS NOT previously unmuted...
            else:

                # Mute the volume.
                self.time_stamper.audio.player.volume = 0.0

                # The mute button image should show that the audio is now muted.
                updated_image_str_key = "volume_mute.png"

            # Update the mute button image.
            button_mute = self.widgets["button_mute"]
            button_mute_image_new = self.widgets[updated_image_str_key]
            button_mute.config(image=button_mute_image_new)
            button_mute.image = button_mute_image_new

        # If an audio player was not successfully retrieved, disable all audio playback settings.
        else:
            self.parent.disable_audio_widgets()
