#-*- coding: utf-8 -*-
"""This module contains the ScaleMacros class which stores the functions
that are executed when scales in the Time Stamper program are dragged."""

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

class ScaleMacros():
    """This class stores all of the macros that execute when scales are dragged."""

    def __init__(self, parent):
        self.parent = parent
        self.time_stamper = parent.time_stamper
        self.template = parent.template
        self.timer = parent.timer
        self.widgets = parent.widgets

    def scale_media_time_macro(self, scale_value, called_from_scroll_function=False):
        """This method will be executed when the user presses the left, middle
        or right mouse button on the media slider (but not when the user releases
        the left, middle or right mouse button from the media slider)."""

        # If a media player was successfully retrieved...
        if self.time_stamper.media_player:

            # If this method IS being called from scale_media_time_mousewheel_macro, then the
            # user is currently scrolling the media time scale, which means that the timer
            # should resume after a short delay IF media currently playing/scheduled to play.
            if called_from_scroll_function:
                self.timer.pause(play_delay=0.25)

            # If this method IS NOT being called from scale_media_time_mousewheel_macro,
            # then the user is currently moving the media time scale with mouse-clicks,
            # which means the timer should remain paused until the user releases the
            # mouse button from the scale IF media is currently playing/scheduled to play.
            else:
                self.timer.pause(play_delay=-1)

            # Update the timer to match the new position of the slider.
            self.timer.update_timer(float(scale_value))

        # If a media player was not successfully retrieved, disable all media playback settings.
        else:
            self.parent.disable_media_widgets()

    def scale_media_time_release_macro(self, *_):
        """This method will be executed when the user releases the left, middle
        or right mouse button from the media slider (but not when the user
        presses the left, middle or right mouse button on the media slider)."""

        # If the timer was previously paused when the user
        # dragged the media slider, resume the timer.
        if self.timer.temporary_pause:
            self.timer.play(playback_type="prev")

    def scale_media_time_mousewheel_macro(self, event):
        """This method gets executed when the mousewheel is moved over the media time slider."""

        scale = self.widgets["scale_media_time"]
        scale_template = self.template["scale_media_time"]

        # On Mac platforms, the registered scroll amount does not need to be divided be 120.
        event_delta = event.delta if platform.startswith("darwin") else event.delta / 120

        media = self.time_stamper.media_player.get_media()
        scroll_sensitivity = (media.get_duration() / 1000) / 180
        # Adjust the media time slider's position to reflect the mousewheel scrolling.
        scroll_amount = event_delta * float(scroll_sensitivity) * \
            (-1 if scale_template["reverse_scroll_direction"] else 1)
        scale_current_value = scale.get()

        # Set the media time slider to its adjusted position.
        new_scale_value = scale_current_value + scroll_amount
        new_scale_value = min(self.timer.get_max_time(), max(0.0, new_scale_value))
        self.scale_media_time_macro(new_scale_value, called_from_scroll_function=True)

        # Determine whether media is playing/scheduled to play.
        media_playing = self.time_stamper.media_player \
            and (self.time_stamper.media_player.is_playing() or self.timer.scheduled_id)

        # If media is currently playing/scheduled to play and the
        # timer was adjusted to the max time, pause the timer.
        max_time = self.timer.get_max_time()
        if media_playing and self.timer.get_current_seconds() >= max_time:
            self.timer.display_time(max_time, pad=2)
            self.parent["button_pause"]()

    def scale_media_volume_macro(self, volume_scale_value):
        """This method will be executed when the user presses the left,
        middle or right mouse button on the media volume slider."""

        # Convert the passed value from a string to a float.
        volume_scale_value = int(100 - float(volume_scale_value))

        # If a media player was successfully retrieved...
        if self.time_stamper.media_player:

            # Adjust the volume of the media.
            self.time_stamper.media_player.audio_set_volume(volume_scale_value)

            # Update the label that displays the current volume level.
            self.widgets["label_media_volume"]["text"] = str(volume_scale_value)

            # Determine what the new mute button image should be.
            updated_image_str_key = self.parent.updated_mute_button_image(volume_scale_value)

            # If the new mute button image does NOT match the
            # current mute button image, update the mute button image.
            button_mute = self.widgets["button_mute"]
            button_mute_image_new = self.widgets[updated_image_str_key]
            if button_mute.image != button_mute_image_new:
                button_mute.config(image=button_mute_image_new)
                button_mute.image = button_mute_image_new

        # If a media player was NOT successfully retrieved, disable all media playback settings.
        else:
            self.parent.disable_media_widgets()

    def scale_media_volume_mousewheel_macro(self, event):
        """This method gets executed when the mousewheel is moved over the media volume slider."""

        scale = self.widgets["scale_media_volume"]
        scale_template = self.template["scale_media_volume"]

        # On Mac platforms, the registered scroll amount does not need to be divided be 120.
        event_delta = event.delta if platform.startswith("darwin") else event.delta / 120

        # Adjust the volume scale's position to reflect the mousewheel scrolling.
        scroll_amount = event_delta * float(scale_template["scroll_sensitivity"]) * \
            (-1 if scale_template["reverse_scroll_direction"] else 1)
        scale_current_value = scale.get()

        # Set the media volume slider to its adjusted position.
        scale.set(scale_current_value + scroll_amount)
