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
        self.temporary_pause = False

    def scale_media_time_macro(self, scale_value, called_from_scroll_function=False):
        """This method will be executed when the user presses the left, middle
        or right mouse button on the media slider (but not when the user releases
        the left, middle or right mouse button from the media slider)."""

        # If a media player was successfully retrieved...
        if self.time_stamper.media_player:

            # If there is an existing scheduled play function and this method is not being called
            # as a result of the user scrolling the media time slider with the mousewheel, this
            # effectively means that the user was scrolling the media time slider prior to clicking
            # on it. Neglecting to cancel the scheduled play function would then potentially play
            # the media before the user releases the mouse button from the media time slider, so the
            # existing scheduled play function should be cancelled and the timer should be paused.
            if self.timer.scheduled_id and not called_from_scroll_function:
                self.time_stamper.root.after_cancel(self.timer.scheduled_id)
                self.timer.scheduled_id = None
                self.timer.pause(reset_multiplier=False)
                self.temporary_pause = True

            # Pause the timer.
            if self.timer.is_running:
                self.timer.pause(reset_multiplier=False)
                self.temporary_pause = True

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
        if self.temporary_pause:
            self.temporary_pause = False
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

        # Determine whether media is playing/scheduled to play.
        media_playing = self.time_stamper.media_player \
            and (self.time_stamper.media_player.is_playing() or self.timer.scheduled_id)

        # If there is media currently playing/scheduled to play,
        # schedule the media to resume playing after a short delay.
        if media_playing:

            # Pause the timer without resetting the multiplier.
            self.timer.pause(reset_multiplier=False)

            # If there is an existing scheduled play function, then it should be
            # cancelled, as this effectively means that the user was already scrolling
            # the media slider or timer entries but has not yet finished scrolling.
            if self.timer.scheduled_id:
                self.time_stamper.root.after_cancel(self.timer.scheduled_id)

            # Schedule the timer to play after the specified delay.
            self.timer.scheduled_id = \
                self.time_stamper.root.after(250, self.timer.play, "prev")

        # Set the media time slider to its adjusted position.
        new_scale_value = scale_current_value + scroll_amount
        new_scale_value = min(self.timer.get_max_time(), max(0.0, new_scale_value))
        self.scale_media_time_macro(new_scale_value, called_from_scroll_function=True)

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
