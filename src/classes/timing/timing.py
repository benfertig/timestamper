#-*- coding: utf-8 -*-
"""This module contains the TimeStamperTimer class which allows
for keeping track of time in the Time Stamper program."""

from math import ceil
from time import perf_counter
from tkinter import DISABLED
from pyglet.media import Player
from .timing_helper_methods import confirm_audio, \
    make_playback_button_images_visible, pulse_button_image, print_to_entry, \
    pad_number, h_m_s_to_timestamp, h_m_s_to_seconds, seconds_to_h_m_s

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


class TimeStamperTimer():
    """This class runs a timer with pause, resume, skip backward and skip
    forward features. Once an instance of the TimeStamper class from the module
    time_stamper is created, its constructor will create an instance of this
    TimeStamperTimer class, passing itself to the TimeStamperTimer constructor."""

    def __init__(self, time_stamper):

        self.time_stamper = time_stamper

        self.timestamp_set = False
        self.is_running = False
        self.temporary_pause = False
        self.start_time = 0.0
        self.offset = 0.0
        self.multiplier = 1.0

    def read_timer(self, raw=False):
        """This method reads in and returns the current time from the time fields. This method
        takes one optional argument, raw, which is set to False by default. When raw is True,
        the returned values will be four strings representing the timer's current time in
        hours, minutes, seconds and subseconds (padded with 0's if necessary). When raw is
        False, the returned values will be the same as the values that are returned when
        raw is True, but the values will be converted to integers before being returned."""

        # Get the current values from the timer's time fields.
        hours = self.time_stamper.widgets["entry_hours"].get()
        minutes = self.time_stamper.widgets["entry_minutes"].get()
        seconds = self.time_stamper.widgets["entry_seconds"].get()
        subseconds = self.time_stamper.widgets["entry_subseconds"].get()

        # The timer's values may need to be padded if they contain user-entered numbers.
        if not self.is_running:
            hours = pad_number(hours, 2, True)
            minutes = pad_number(minutes, 2, True)
            seconds = pad_number(seconds, 2, True)
            subseconds = pad_number(subseconds, 2, False)

        # If raw is True, return the time from the time fields as it should appear on the timer.
        if raw:
            return hours, minutes, seconds, subseconds

        # If raw is False, convert the numbers from the
        # time fields to integers before returning them.
        return int(hours), int(minutes), int(seconds), int(subseconds)

    def get_current_seconds(self):
        """This method returns the timer's current time in seconds."""

        return h_m_s_to_seconds(*self.read_timer())

    def current_time_to_timestamp(self, include_brackets=True):
        """This method converts the currently diplayed time to a timestamp."""

        return h_m_s_to_timestamp(*self.read_timer(raw=True), include_brackets)

    def display_time(self, new_time, pad=0):
        """This method, after converting the provided time in seconds to hours, minutes,
        seconds and subseconds, will display this time to timer fields of self.time_stamper."""

        # Convert the provided time in seconds to hours, minutes, seconds and subseconds.
        h_m_s = seconds_to_h_m_s(new_time, pad)

        # Print the hours, minutes, seconds and subseconds to their relevant Tkinter entries.
        for i, time_field in enumerate(("hours", "minutes", "seconds", "subseconds")):
            print_to_entry(h_m_s[i], self.time_stamper.widgets[f"entry_{time_field}"])

        # If a timestamp has not been set, make the timestamp label reflect the current time.
        if not self.timestamp_set:
            obj_timestamp = self.time_stamper.widgets["label_timestamp"]
            obj_timestamp["text"] = h_m_s_to_timestamp(*h_m_s)

        # If an audio player exists, update the position of the audio
        # slider as well as the displays of elapsed and remaining time.
        if self.time_stamper.audio_player:

            audio_duration = self.time_stamper.audio_source.duration

            # Update the audio slider.
            self.time_stamper.widgets["scale_audio_time"].variable.set(new_time)

            # Update the elapsed time.
            label_audio_elapsed = self.time_stamper.widgets["label_audio_elapsed"]
            label_audio_elapsed["text"] = f"{h_m_s[0]}:{h_m_s[1]}:{h_m_s[2]}"

            # Update the remaining time.
            h_m_s_remaining = seconds_to_h_m_s(audio_duration - new_time, pad)
            label_audio_remaining = self.time_stamper.widgets["label_audio_remaining"]
            label_audio_remaining["text"] = \
                f"{h_m_s_remaining[0]}:{h_m_s_remaining[1]}:{h_m_s_remaining[2]}"

    def update_audio(self, new_time):
        """This method adjusts the start time of the current audio
        source to new_time and then plays that audio source."""

        if self.is_running:

            # Pause the audio player.
            self.time_stamper.audio_player.pause()

            # Refresh the audio player.
            self.time_stamper.audio_player.delete()
            self.time_stamper.audio_player = Player()
            self.time_stamper.audio_player.queue(self.time_stamper.audio_source)

            # Adjust the start time of the audio.
            self.time_stamper.audio_player.seek(new_time)

            # If the volume is currently muted, set the audio player's volume to zero.
            if self.time_stamper.widgets["button_mute"].image == \
                self.time_stamper.widgets["volume_mute.png"]:
                self.time_stamper.audio_player.volume = 0.0

            # If the volume is not currently muted, set the audio
            # player's volume to the value of the volume slider.
            else:
                self.time_stamper.audio_player.volume = \
                    (100 - self.time_stamper.widgets["scale_audio_volume"].variable.get()) / 100

            # Play the audio.
            self.time_stamper.audio_player.play()

    def attempt_audio_playback(self, start_time):
        """If an audio player can be initialized with the current information provided in
        the Time Stamper program, then this method will begin playing the audio from the
        time specified by start_time. Otherwise, no audio will begin playing and the
        widgets that are only relevant to audio playback will be cleared and/or disabled."""

        # Retrieve the audio source and the audio player if they can be retrieved.
        entry_audio_path = self.time_stamper.widgets["entry_audio_path"]
        self.time_stamper.audio_source, self.time_stamper.audio_player = confirm_audio(\
            self.time_stamper.audio_source, self.time_stamper.audio_player, entry_audio_path)

        # Play the selected audio player if it WAS successfully retrieved.
        if self.time_stamper.audio_player:
            self.update_audio(start_time)

        # Clear the audio path and disable the audio slider
        # if an audio player WAS NOT successfully retrieved.
        else:
            print_to_entry("", entry_audio_path)
            self.time_stamper.widgets["scale_audio_time"]["state"] = DISABLED

    def update_timer(self, new_time):
        """This method updates the timer to the new time passed
        in new_time (which should be a time in seconds)."""

        # Find the time we are adjusting FROM.
        prev_time = self.get_current_seconds()

        # Set the new offset.
        self.offset += (new_time - prev_time)

        # Display the new time.
        self.display_time(new_time, pad=2)

        # Try to play the specified audio file if one has been specified.
        self.attempt_audio_playback(new_time)

    def timer_tick(self, prev_multiplier):
        """This method runs continuously while the timer is running to update the current time."""

        # Only tick the timer if it is currently running.
        if self.is_running:

            # If audio is playing, sync the timer with the the audio player.
            audio_playing = \
                self.time_stamper.audio_player and self.time_stamper.audio_player.playing
            if audio_playing:
                internal_time = self.time_stamper.audio_player.time

            # If audio is not playing, set the timer using perf_counter().
            else:
                internal_time = self.offset + ((perf_counter() - self.start_time) * self.multiplier)

            # Determine the maximum time displayable by the timer.
            max_time = min(359999.99, round(self.time_stamper.audio_source.duration, 2)) \
                if self.time_stamper.audio_player else 359999.99

            # Only tick the timer if its current time is less than the maximum time.
            if internal_time < max_time or self.multiplier < 0.0:

                # Only tick the timer if the precise internal time
                # is greater than 0 or if an audio file is loaded.
                if internal_time > 0.0 or audio_playing:

                    # Display the updated time.
                    self.display_time(internal_time, pad=2)

                    # Potentially, make the image of either the play, rewind
                    # or fast-forward button either visible or invisible.
                    subseconds = int(self.time_stamper.widgets["entry_subseconds"].get())
                    pulse_button_image(subseconds, self.multiplier, self.time_stamper.widgets)

                    # Calculate the number of seconds to the next hundreth of a second.
                    seconds_to_next_tick = ((int(internal_time * 100) + 1) / 100) - internal_time

                    # Convert the number of seconds to the next hundreth of a second to
                    # the number of thousandth-seconds to the next hundreth of a second.
                    thousandth_seconds_to_next_tick = ceil(max(seconds_to_next_tick, .001) * 1000)

                    # Consider the time dilation from rewinding/fast-forwarding when calculating
                    # the number of thousandth-seconds to the next hundreth of a second.
                    thousandth_seconds_to_next_tick *= ceil(abs(1 / self.multiplier))

                    # After a very short delay, tick the timer again.
                    if self.multiplier == prev_multiplier:
                        self.time_stamper.root.after(thousandth_seconds_to_next_tick, \
                            self.timer_tick, self.multiplier)

                # If the timer's currently displayed time is greater than 0, pause the timer.
                else:

                    self.display_time(0.0, pad=2)
                    self.time_stamper.macros["button_pause"]()

            # If the timer's currently displayed time is not less
            # than the maximum displayable time, pause the timer.
            else:
                self.display_time(max_time, pad=2)
                self.time_stamper.macros["button_pause"]()

    def pause(self, temporary_pause=False):
        """This method halts the timer and is typically run when the pause button is
        pressed or when the audio slider is dragged. An optional argument temporary_pause,
        which is set to False by default, is only ever set to True if this method is called
        from scale_audio_time_left_mouse_press in widgets_helper_methods.py and if the
        timer was previously unpaused. When the audio slider is then released (i.e., when
        scale_audio_time_left_mouse_release from widgets_helper_methods.py is called),
        then the timer will immediately resume if temporary_pause was set to True."""

        # Only pause the timer if it is currently running.
        if self.is_running:

            # Declare the timer as not running.
            self.is_running = False

            # We are no longer rewinding or fast-forwarding, so the multiplier should be reset.
            self.multiplier = 1.0

            # The images for the play, rewind and fast-forward buttons
            # should no longer be invisible if any of them currently are.
            make_playback_button_images_visible(self.time_stamper.widgets)

            # If this method is being called from scale_audio_time_left_mouse_press, then
            # indicate that the timer should be resumed when the audio slider is released.
            if temporary_pause:
                self.temporary_pause = True

            # Pause the audio if it exists.
            if self.time_stamper.audio_player:
                self.time_stamper.audio_player.pause()

    def play(self, reset_multiplier=True):
        """This method starts the timer and is typically run when the play, rewind or
        fast-forward buttons are pressed. An optional argument, reset_multiplier (which
        is set to True by default), determines whether the timer should be reset to 1x
        speed. This argument should only ever be set to False when this method is called
        from the rewind_or_fast_forward method in macros_helper_methods.py (i.e., whenever
        the user presses the rewind or fast-forward buttons, but not the play button)."""

        # The timer is no longer paused, so self.temporary_pause should be set to False.
        self.temporary_pause = False

        # If we arenot rewinding or fast-forwarding, then the multiplier should be set to 1.0.
        if reset_multiplier:
            self.multiplier = 1.0

        # The images for the play, rewind and fast-forward buttons
        # should no longer be invisible if any of them currently are.
        make_playback_button_images_visible(self.time_stamper.widgets)

        # Get the timer's current time in seconds.
        current_time_seconds = self.get_current_seconds()

        # Save the current raw time.
        self.start_time = perf_counter()

        # Declare the timer as running.
        self.is_running = True

        # Factor the current reading on the timer into the
        # offset for the calculation of the running time.
        self.offset = current_time_seconds

        # Try to play the specified audio file if one has been specified.
        self.attempt_audio_playback(current_time_seconds)

        # Begin ticking the timer.
        self.timer_tick(self.multiplier)

    def adjust_timer(self, seconds_to_adjust_by):
        """This method skipes the timer backward and forward and is typically run when the
        skip backward or skip forward button is pressed. Since the skip backward and skip
        forward procedures are very similar, they have been condensed into this single method."""

        if seconds_to_adjust_by != 0:

            current_time_seconds = self.get_current_seconds()

            # If the requested adjustment WOULD BRING the timer below
            # the minimum time (00h 00m 00.00s), reduce the adjustment
            # so that it brings the timer to the minimum time.
            if current_time_seconds + seconds_to_adjust_by < 0:
                seconds_to_adjust_by = -current_time_seconds

            # If the requested adjustment WOULD NOT BRING the
            # timer below the minimum time (00h 00m 00.00s)...
            else:

                # The maximum time is either the maximum time displayable by the
                # timer (99h 59m 59.99s) or the duration of the audio source. If an
                # audio source is loaded, figure out which of these is shorter and
                # set that to the maximum time. If an audio source is not loaded,
                # set the maximum time to the maxmimum time displayable by the timer.
                max_time = min(359999.99, round(self.time_stamper.audio_source.duration, 2)) \
                    if self.time_stamper.audio_player else 359999.99

                # IF the requested adjustment would have previously brought
                # the timer OVER the maximum time, reduce the adjustment
                # amount so that it brings the timer TO the maximum time.
                if current_time_seconds + seconds_to_adjust_by > max_time:
                    seconds_to_adjust_by = max_time - current_time_seconds

            # Update the timer's time.
            current_time_seconds += seconds_to_adjust_by
            self.update_timer(current_time_seconds)

        return seconds_to_adjust_by
