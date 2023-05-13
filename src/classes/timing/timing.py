#-*- coding: utf-8 -*-
"""This module contains the TimeStamperTimer class which allows
for keeping track of time in the Time Stamper program."""

from math import ceil
from time import perf_counter
from tkinter import DISABLED
from pyglet.media import Player
from .timing_helper_methods import confirm_audio, \
    make_playback_button_images_visible, pulse_button_image, print_to_entry, pad_number, \
    h_m_s_to_timestamp, h_m_s_to_seconds, seconds_to_h_m_s, seconds_to_timestamp

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
        self.start_time = 0.0
        self.offset = 0.0
        self.multiplier = 0.0

        self.scheduled_id = None

    def get_max_time(self):
        """This method returns the timer's current maximum time in seconds. Typically, the
        maximum time will be 359999.99 seconds unless an audio file is loaded, in which case
        the maximum time will be the minimum of 359999.99 and the duration of the audio source."""

        if self.time_stamper.audio.source:
            return min(359999.99, round(self.time_stamper.audio.source.duration, 2))

        return 359999.99

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

    def display_time(self, new_time, pad=2):
        """This method, after converting the provided time in seconds to hours, minutes,
        seconds and subseconds, will display this time to timer fields of self.time_stamper."""

        # Convert the provided time in seconds to hours, minutes, seconds and subseconds.
        h_m_s = seconds_to_h_m_s(new_time, pad=pad)

        # Print the hours, minutes, seconds and subseconds to their relevant Tkinter entries.
        for i, time_field in enumerate(("hours", "minutes", "seconds", "subseconds")):

            current_timer_entry = self.time_stamper.widgets[f"entry_{time_field}"]

            # Only update the value in the timer entry if the
            # updated value is not equal to the current value.
            if h_m_s[i] != current_timer_entry.get():
                print_to_entry(h_m_s[i], current_timer_entry)

        # If a timestamp has not been set, make the timestamp label reflect the current time.
        if not self.timestamp_set:
            obj_timestamp = self.time_stamper.widgets["label_timestamp"]
            obj_timestamp["text"] = h_m_s_to_timestamp(*h_m_s)

        # If an audio player exists, update the position of the audio
        # slider as well as the displays of elapsed and remaining time.
        if self.time_stamper.audio.player:

            audio_duration = min(359999.99, self.time_stamper.audio.source.duration)

            # Update the audio slider.
            self.time_stamper.widgets["scale_audio_time"].variable.set(new_time)

            # Update the elapsed time.
            audio_elapsed_to_timestamp = h_m_s_to_timestamp(*h_m_s[:3], include_brackets=False)
            label_audio_elapsed = self.time_stamper.widgets["label_audio_elapsed"]
            label_audio_elapsed["text"] = audio_elapsed_to_timestamp

            # Update the remaining time.
            audio_seconds_remaining = max(0.0, audio_duration - new_time)
            audio_remaining_to_timestamp = seconds_to_timestamp(audio_seconds_remaining, \
                pad=pad, include_subseconds=False, include_brackets=False)
            label_audio_remaining = self.time_stamper.widgets["label_audio_remaining"]
            label_audio_remaining["text"] = audio_remaining_to_timestamp

    def update_audio(self, new_time):
        """This method adjusts the start time of the current audio
        source to new_time and then plays that audio source."""

        if self.is_running:

            # Pause the audio player.
            self.time_stamper.audio.player.pause()

            # Refresh the audio player.
            self.time_stamper.audio.player.delete()
            self.time_stamper.audio.player = Player()
            self.time_stamper.audio.player.queue(self.time_stamper.audio.source)

            # Adjust the start time of the audio.
            self.time_stamper.audio.player.seek(new_time)

            # If the volume is currently muted, set the audio player's volume to zero.
            if self.time_stamper.widgets["button_mute"].image == \
                self.time_stamper.widgets["volume_mute.png"]:
                self.time_stamper.audio.player.volume = 0.0

            # If the volume is not currently muted, set the audio
            # player's volume to the value of the volume slider.
            else:
                self.time_stamper.audio.player.volume = \
                    (100 - self.time_stamper.widgets["scale_audio_volume"].variable.get()) / 100

            # Play the audio.
            self.time_stamper.audio.player.play()

    def attempt_audio_playback(self, start_time):
        """If an audio player can be initialized with the current information provided in
        the Time Stamper program, then this method will begin playing the audio from the
        time specified by start_time. Otherwise, no audio will begin playing and the
        widgets that are only relevant to audio playback will be cleared and/or disabled."""

        # Retrieve the audio source and the audio player if they can be retrieved.
        entry_audio_path = self.time_stamper.widgets["entry_audio_path"]
        self.time_stamper.audio.source, self.time_stamper.audio.player = confirm_audio(\
            self.time_stamper.audio.source, self.time_stamper.audio.player, entry_audio_path)

        # Play the selected audio player if it WAS successfully retrieved.
        if self.time_stamper.audio.player:
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
                self.time_stamper.audio.player and self.time_stamper.audio.player.playing
            if audio_playing:
                internal_time = self.time_stamper.audio.player.time

            # If audio is not playing, set the timer using perf_counter().
            else:
                internal_time = self.offset + ((perf_counter() - self.start_time) * self.multiplier)

            # Only tick the timer if its current time is less than the maximum time.
            if internal_time < self.get_max_time() or self.multiplier < 0.0:

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
                    next_hundreth_second = \
                        (int(internal_time * 100) + int(self.multiplier > 0.0)) / 100
                    seconds_to_next_tick = abs(next_hundreth_second - internal_time)

                    # Convert the number of seconds to the next hundreth of a second to
                    # the number of thousandth-seconds to the next hundreth of a second.
                    thousandth_seconds_to_next_tick = max(seconds_to_next_tick, .001) * 1000

                    # Consider the time dilation from rewinding/fast-forwarding when calculating
                    # the number of thousandth-seconds to the next hundreth of a second.
                    thousandth_seconds_to_next_tick = \
                        ceil(thousandth_seconds_to_next_tick * abs(1 / self.multiplier))

                    # After the next hundreth second has elapsed, tick the timer again.
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
                self.display_time(self.get_max_time(), pad=2)
                self.time_stamper.macros["button_pause"]()

    def pause(self, play_delay=None, reset_multiplier=True):
        """This method halts the timer and is typically run when the pause button is pressed,
        when the audio slider is dragged/scrolled and audio is playing or when the timer entries
        are scrolled. An optional argument play_delay, which is set to None by default,
        determines the amount of time after which the timer should resume. A value for play_delay
        should only ever be passed when this method is called from adjust_timer_on_entry_mousewheel
        or custom_scale_on_mousewheel in widgets_helper_methods.py and the timer is already
        playing. An optional argument, reset_multiplier (which is set to True by default),
        determines whether the timer's multiplier should be reset to 0.0 (the typical value
        of the multiplier when the timer is paused). This argument should only ever be set
        to False from the adjust_timer_on_entry_mousewheel method and, in certain
        cases, from the custom_scale_on_mousewheel methods in widgets_helper_methods.py
        (i.e., whenever the user scrolls on the audio time slider or timer entries)."""

        # Reset the multiplier if it was indicated that this should be done.
        if reset_multiplier:
            self.multiplier = 0.0

        # Only pause the timer if it is currently running.
        if self.is_running:

            # Declare the timer as not running.
            self.is_running = False

            # The images for the play, rewind and fast-forward buttons
            # should no longer be invisible if any of them currently are.
            make_playback_button_images_visible(self.time_stamper.widgets)

            # Pause the audio if it exists.
            if self.time_stamper.audio.player:
                self.time_stamper.audio.player.pause()

        # If the timer should resume playing after a delay...
        if play_delay:

            # If there is an existing scheduled play function, then it should be
            # cancelled, as this effectively means that the user was already scrolling
            # the audio slider or timer entries but has not yet finished scrolling.
            if self.scheduled_id:
                self.time_stamper.root.after_cancel(self.scheduled_id)

            # Schedule the timer to play after the specified delay.
            new_multiplier = 1.0 if reset_multiplier else self.multiplier
            self.scheduled_id = \
                self.time_stamper.root.after(int(play_delay * 1000), self.play, new_multiplier)

    def play(self, set_multiplier_to=1.0):
        """This method starts the timer and is typically run when the play, rewind or fast-forward
        buttons are pressed. An optional argument, set_multiplier_to (which is set to 1.0 by
        default), determines the speed of the timer. This argument should only ever be altered
        from the rewind_or_fast_forward method in macros_helper_methods.py (i.e., whenever
        the user presses the rewind or fast-forward buttons, but not the play button)."""

        self.scheduled_id = None

        if not self.is_running:

            # Declare the timer as running.
            self.is_running = True

            # Set the multiplier to the value of the argument set_multiplier_to.
            self.multiplier = set_multiplier_to

            # The images for the play, rewind and fast-forward buttons
            # should no longer be invisible if any of them currently are.
            make_playback_button_images_visible(self.time_stamper.widgets)

            # Get the timer's current time in seconds.
            current_time_seconds = self.get_current_seconds()

            # Save the current raw time.
            self.start_time = perf_counter()

            # Factor the current reading on the timer into the
            # offset for the calculation of the running time.
            self.offset = current_time_seconds

            # Try to play the specified audio file if one has been specified.
            self.attempt_audio_playback(current_time_seconds)

            # Begin ticking the timer.
            self.timer_tick(self.multiplier)

    def adjust_timer(self, seconds_to_adjust_by, abort_if_out_of_bounds=False):
        """This method skips the timer backward and forward and is typically run when
        the skip backward or skip forward button is pressed or when the user scrolls
        the mousewheel while the cursor is hovering over one of the timer entries. This
        method takes one optional argument, abort_if_out_of_bounds, which is set to False
        by default. When abort_if_out_of_bounds is set to True, this method will not adjust
        the timer if the passed adjustment amount would put the timer below 0 or above the
        maximum time (as can be the case when the user scrolls the timer entries with the
        mousewheel). When abort_if_out_of_bounds is set to False, this method will reduce
        the passed adjustment amount to put the timer at either 0 or its maximum time if the
        passed adjustment amount would have otherwise put the timer under 0 or over its maximum
        time (as is the case when the user presses the skip backward or skip forward buttons)."""

        if seconds_to_adjust_by != 0:

            current_time_seconds = self.get_current_seconds()

            # If the requested adjustment WOULD BRING the
            # timer below the minimum time (00h 00m 00.00s)...
            if current_time_seconds + seconds_to_adjust_by < 0:

                # If abort_if_out_of_bounds is True, we should not adjust the timer.
                if abort_if_out_of_bounds:
                    return 0

                # If abort_if_out_of_bounds is False, reduce the
                # adjustment so that it brings the timer to 0.
                seconds_to_adjust_by = -current_time_seconds

            # If the requested adjustment WOULD NOT BRING the
            # timer below the minimum time (00h 00m 00.00s)...
            else:

                # IF the requested adjustment WOULD BRING the timer OVER the maximum time...
                if current_time_seconds + seconds_to_adjust_by > self.get_max_time():

                    # If abort_if_out_of_bounds is True, we should not adjust the timer.
                    if abort_if_out_of_bounds:
                        return 0

                    # If abort_if_out_of_bounds is False, reduce the adjustment
                    # amount so that it brings the timer TO the maximum time
                    seconds_to_adjust_by = self.get_max_time() - current_time_seconds

            # Update the timer's time.
            current_time_seconds += seconds_to_adjust_by
            self.update_timer(current_time_seconds)

        return seconds_to_adjust_by
