#-*- coding: utf-8 -*-
"""This module contains the MediaButtonMacros class which stores the functions
that are executed when a media button in the Time Stamper program is pressed."""

from sys import platform
from .macros_helper_methods import disable_button, \
    button_enable_disable_macro, rewind_or_fast_forward, skip_backward_or_forward

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

    def media_button_macro(self, button_str_key, entry_str_key=None, is_skip_backward=True):
        """This method is called on by the macros for the pause, play, skip backward,
        and skip forward buttons. Since similar processes are executed for all
        of these buttons, their shared procedures have been condensed down to
        this method, where the arguments specific to each button can be passed."""

        button_template = self.template[button_str_key]

        # Enable and disable the relevant widgets for when this button is pressed.
        button_enable_disable_macro(button_template, self.widgets)

        # Get the timestamp before skipping backward/forward.
        first_timestamp = self.timer.current_time_to_timestamp()

        seconds_to_adjust_by = None

        # If there is an entry associated with this button, then that means
        # we are either skipping backward or forward, so we should skip backward
        # or forward the amount of seconds indicated by the relevant entry.
        if entry_str_key:

            # Skip the timer backward/forward the specified number of seconds.
            adjustment_input = self.widgets[entry_str_key].get()
            seconds_to_adjust_by = skip_backward_or_forward(adjustment_input, \
                is_skip_backward, self.timer.adjust_timer)

            # Get the timestamp after skipping backward/forward.
            second_timestamp = self.timer.current_time_to_timestamp(include_brackets=False)

        # If the user has set a message to be printed
        # when this button is pressed, retrieve that message.
        button_message = self.parent.get_button_message_input(button_str_key)

        # Only print a message for this button if:
        #     1) a message was specified for this button
        #     AND
        #     2) the skip backward/forward amount was not zero seconds (this
        #        condition does not apply if the user pressed a media button
        #        that was not the skip backrward or skip forward button).
        if button_message is not None and seconds_to_adjust_by != 0:

            # If there is an entry associated with this button, then that means we
            # are either skipping backward or skipping forward and we potentially need
            # to swap the user's input for the button's message with other values.
            if entry_str_key:

                # We may need to print the exact number of seconds that the
                # user skipped backward/forward by. Manipulate the displayed
                # adjustment amount to make it as readable as possible here.
                seconds_to_adjust_by = abs(round(seconds_to_adjust_by, 2))
                if seconds_to_adjust_by % 1 == 0:
                    seconds_to_adjust_by = int(seconds_to_adjust_by)
                seconds_to_adjust_by = str(seconds_to_adjust_by)

                # Replace any variables in the button message with their corresponding values.
                button_message = button_message.replace("$amount", seconds_to_adjust_by)
                button_message = button_message.replace("$dest", second_timestamp)

            # Print the button's message, along with the current
            # timestamp, to the notes log and the output file.
            self.parent.print_timestamped_message(f"{button_message}\n", first_timestamp)

    def button_pause_macro(self):
        """This method will be executed when the pause button is pressed."""

        self.media_button_macro("button_pause")

        # If an audio source is loaded, the rewind and fast-forward buttons, which would
        # otherwise be activated when the pause button is pressed, should remain deactivated.
        if self.time_stamper.audio_source:
            disable_button(self.widgets["button_rewind"], \
                self.template["button_rewind"]["mac_disabled_color"])
            disable_button(self.widgets["button_fast_forward"], \
                self.template["button_fast_forward"]["mac_disabled_color"])

        # Pause the timer.
        self.timer.pause()

    def button_play_macro(self):
        """This method will be executed when the play button is pressed."""

        self.media_button_macro("button_play")

        # If an audio source is loaded, the rewind and fast-forward buttons, which would
        # otherwise be activated when the play button is pressed, should remain deactivated.
        if self.time_stamper.audio_source:
            disable_button(self.widgets["button_rewind"], \
                self.template["button_rewind"]["mac_disabled_color"])
            disable_button(self.widgets["button_fast_forward"], \
                self.template["button_fast_forward"]["mac_disabled_color"])

        # Start the timer.
        self.timer.play()

    def button_rewind_macro(self):
        """This method will be executed when the rewind button is pressed."""

        # Enable and disable the relevant buttons for when the rewind button is pressed.
        button_enable_disable_macro(self.template["button_rewind"], self.widgets)

        # Retrieve the speed at which we should rewind from the rewind spinbox.
        spinbox_val = self.widgets["spinbox_rewind"].get()
        multiplier_str = self.template["spinbox_rewind"]["values"][spinbox_val]

        # Rewind the timer at the specified speed.
        rewind_or_fast_forward(multiplier_str, True, self.timer)

    def button_fast_forward_macro(self):
        """This method will be executed when the fast-forward button is pressed."""

        # Enable and disable the relevant buttons for when the fast-forward button is pressed.
        button_enable_disable_macro(self.template["button_fast_forward"], self.widgets)

        # Retrieve the speed at which we should fast-forward from the fast-forward spinbox.
        spinbox_val = self.widgets["spinbox_fast_forward"].get()
        multiplier_str = self.template["spinbox_fast_forward"]["values"][spinbox_val]

        # Fast-forward the timer at the specified speed.
        rewind_or_fast_forward(multiplier_str, False, self.timer)

    def button_skip_backward_macro(self):
        """This method will be executed when the skip backward button is pressed."""

        self.media_button_macro("button_skip_backward", \
            "entry_skip_backward", is_skip_backward=True)

    def button_skip_forward_macro(self):
        """This method will be executed when the skip forward button is pressed."""

        self.media_button_macro("button_skip_forward", "entry_skip_forward", is_skip_backward=False)

    def button_mute_macro(self):
        """This method will be executed when the mute button is pressed."""

        # If an audio player was successfully retrieved...
        if self.time_stamper.audio_player:

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
                self.time_stamper.audio_player.volume = volume_scale_value / 100

                # The mute button image should reflect the current value of the volume slider.
                updated_image_str_key = self.parent.updated_mute_button_image(volume_scale_value)

            # If the volume WAS NOT previously unmuted...
            else:

                # Mute the volume.
                self.time_stamper.audio_player.volume = 0.0

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
