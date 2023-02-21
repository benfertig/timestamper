#-*- coding: utf-8 -*-
"""This module contains the ScaleMacros class which stores the functions
that are executed when scales in the Time Stamper program are dragged."""

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

class ScaleMacros():
    """This class stores all of the macros that execute when scales are dragged."""

    def __init__(self, parent):
        self.parent = parent
        self.time_stamper = parent.time_stamper
        self.template = parent.template
        self.widgets = parent.widgets
        self.timer = parent.timer

    def scale_audio_time_macro(self, scale_value):
        """This method will be executed when the user presses the left, middle
        or right mouse button on the audio slider (but not when the user releases
        the left, middle or right mouse button from the audio slider)."""

        # If an audio player was successfully retrieved...
        if self.time_stamper.audio_player:

            # Pause the timer.
            self.timer.pause(temporary_pause=True)

            # Update the timer to match the new position of the slider.
            new_time = float(scale_value) * self.time_stamper.audio_source.duration
            self.timer.update_timer(new_time)

        # If audio player was not successfully retrieved, disable all audio playback settings.
        else:
            self.parent.disable_audio_widgets()

    def scale_audio_time_release_macro(self, *_):
        """This method will be executed when the user releases the left, middle
        or right mouse button from the audio slider (but not when the user
        presses the left, middle or right mouse button on the audio slider)."""

        # If the timer was previously paused when the user
        # dragged the audio slider, resume the timer.
        if self.timer.temporary_pause:
            self.timer.play()

    def scale_audio_volume_macro(self, volume_scale_value):
        """This method will be executed when the user presses the left,
        middle or right mouse button on the audio volume slider."""

        # Convert the passed value from a string to a float.
        volume_scale_value = 100 - float(volume_scale_value)

        # If an audio player was successfully retrieved...
        if self.time_stamper.audio_player:

            # Adjust the volume of the audio.
            self.time_stamper.audio_player.volume = volume_scale_value / 100

            # Update the label that displays the current volume level.
            self.widgets["label_audio_volume"]["text"] = str(int(volume_scale_value))

            # Determine what the new mute button image should be.
            updated_image_str_key = self.parent.updated_mute_button_image(volume_scale_value)

            # If the new mute button image does NOT match the
            # current mute button image, update the mute button image.
            button_mute = self.widgets["button_mute"]
            button_mute_image_new = self.widgets[updated_image_str_key]
            if button_mute.image != button_mute_image_new:
                button_mute.config(image=button_mute_image_new)
                button_mute.image = button_mute_image_new

        # If an audio player was NOT successfully retrieved, disable all audio playback settings.
        else:
            self.parent.disable_audio_widgets()
