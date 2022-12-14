#-*- coding: utf-8 -*-
"""This module contains the TimeStamperTimer class which allows
for keeping track of time in the Time Stamper program."""

from time import perf_counter
from pyglet.media import Player
from .timing_helper_methods import print_to_field, pad_number, \
    h_m_s_to_timestamp, h_m_s_to_seconds, seconds_to_h_m_s

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
    """This class runs a timer with pause, resume, rewind and fast-forward
    features. Once an instance of the TimeStamper class from the module
    time_stamper is created, its constructor will create an instance of this
    TimeStamperTimer class, passing itself to the TimeStamperTimer constructor."""

    def __init__(self, time_stamper):

        self.time_stamper = time_stamper

        self.timestamp_set = False
        self.is_running = False
        self.start_time = 0.0
        self.offset = 0.0

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

    def current_time_to_timestamp(self):
        """This method converts the currently diplayed time to a timestamp."""

        return h_m_s_to_timestamp(*self.read_timer(raw=True))

    def display_time(self, time_in_seconds, pad=0):
        """This method, after converting the provided time in seconds to hours, minutes,
        seconds and subseconds, will display this time to timer fields of self.time_stamper."""

        # Convert the provided time in seconds to hours, minutes, seconds and subseconds.
        h_m_s = seconds_to_h_m_s(time_in_seconds, pad)

        # Print the hours, minutes, seconds and subseconds to their relevant Tkinter entries.
        print_to_field(self.time_stamper.widgets["entry_hours"], h_m_s[0])
        print_to_field(self.time_stamper.widgets["entry_minutes"], h_m_s[1])
        print_to_field(self.time_stamper.widgets["entry_seconds"], h_m_s[2])
        print_to_field(self.time_stamper.widgets["entry_subseconds"], h_m_s[3])

        # If a timestamp has not been set, make the timestamp label reflect the current time.
        if not self.timestamp_set:
            obj_timestamp = self.time_stamper.widgets["label_timestamp"]
            obj_timestamp["text"] = h_m_s_to_timestamp(*h_m_s)

    def timer_tick(self):
        """This method runs continuously while the timer is running to update the current time."""

        # Only tick the timer if it is currently running.
        if self.is_running:

            # Store the audio player and the audio source into variables.
            audio_player = self.time_stamper.audio_player
            audio_source = self.time_stamper.audio_source

            # Only tick the timer if its current time is less than the maximum time.
            max_time = \
                min(359999.99, round(audio_source.duration, 2)) if audio_player else 359999.99
            if self.get_current_seconds() < max_time:

                # If audio is playing, sync the timer with the the audio player.
                if audio_player and audio_player.playing:
                    internal_time = audio_player.time

                # If audio is not playing, set the timer using perf_counter().
                else:
                    internal_time = perf_counter() - self.start_time + self.offset

                self.display_time(internal_time, pad=2)

                # After a very short delay, tick the timer again.
                self.time_stamper.root.after(2, self.timer_tick)

            # If the timer's currently displayed time is not less
            # than the maximum displayable time, stop the timer.
            else:
                self.time_stamper.macros["button_stop"]()

    def pause(self):
        """This method halts the timer and is typically
        run when the pause or stop button is pressed."""

        # Declare the timer as not running.
        self.is_running = False

        # Pause the audio if it exists.
        if self.time_stamper.audio_player:
            self.time_stamper.audio_player.pause()

    def play(self):
        """This method starts the timer and is typically
        run when the play or record button is pressed."""

        # Store the audio player, the audio source, and
        # the duration of the audio source into variables.
        audio_source = self.time_stamper.audio_source
        audio_player = self.time_stamper.audio_player

        # Get the timer's current time in seconds.
        current_time_seconds = self.get_current_seconds()

        # Only start the timer if the currently displayed time is less than the maximum time,
        # which is either 99h 59m 59.99s (if an audio source is not loaded) or the minumum
        # of 99h 59m 59.99s and the duration of the audio source (if an audio source is loaded).
        max_time = min(359999.99, round(audio_source.duration, 2)) if audio_player else 359999.99
        if current_time_seconds < max_time:

            # Save the current raw time.
            self.start_time = perf_counter()

            # Declare the timer as running.
            self.is_running = True

            # Factor the current reading on the timer into the
            # offset for the calculation of the running time.
            self.offset = current_time_seconds

            # Play the selected audio file if it exists.
            if audio_player:

                # Refresh the audio player.
                self.time_stamper.audio_player = audio_player = Player()
                audio_player.queue(audio_source)

                # Set the audio player to begin at the timer's current time.
                audio_player.seek(current_time_seconds)

                # Play the audio.
                audio_player.play()

            # Begin ticking the timer.
            self.timer_tick()

        # If the timer's currently displayed time is not less
        # than the maximum displayable time, stop the timer.
        else:
            self.time_stamper.macros["button_stop"]()

    def adjust_timer(self, seconds_to_adjust_by):
        """This method rewinds/fast_forwards the timer and is typically run when the
        rewind or fast-forward button is pressed. Since the rewind and fast-forward
        procedures are very similar, they have been condensed into this single method."""

        if seconds_to_adjust_by != 0:

            # Store the audio player, the audio source, and
            # the duration of the audio source into variables.
            audio_player = self.time_stamper.audio_player
            audio_source = self.time_stamper.audio_source

            # Get the current time in seconds before adjusting the timer.
            current_time_seconds = self.get_current_seconds()

            # If the requested adjustment WOULD BRING the timer0
            # below the minimum displayable time (00h 00m 00.00s)...
            if current_time_seconds + seconds_to_adjust_by < 0:

                # Reduce the adjustment so that it brings the timer to the minimum time.
                seconds_to_adjust_by = -current_time_seconds

            # If the requested adjustment WOULD NOT BRING the timer below the
            # minimum displayable time (00h 00m 00.00s), we need to check whether
            # the requested adjustment would bring the timer over the maximum time.
            else:

                # The maximum time is either the maximum time displayable by the
                # timer (99h 59m 59.99s) or the duration of the audio source. If an
                # audio source is loaded, figure out which of these is shorter and
                # set that to the maximum time. If an audio source is not loaded,
                # set the maximum time to the maxmimum time displayable by the timer.
                max_time = \
                    min(359999.99, round(audio_source.duration, 2)) if audio_player else 359999.99

                # IF the requested adjustment would have previously brought
                # the timer over the maximum time, reduce the adjustment
                # amount so that it brings the timer to the maximum time.
                if current_time_seconds + seconds_to_adjust_by > max_time:
                    seconds_to_adjust_by = max_time - current_time_seconds

            # Update the timer's time.
            current_time_seconds += seconds_to_adjust_by
            self.display_time(current_time_seconds, pad=2)
            self.offset += seconds_to_adjust_by

            # Adjust the start time of the audio if it exists.
            audio_playing = audio_player and audio_player.playing
            if self.is_running and audio_playing:

                # Pause the audio player.
                audio_player.pause()

                # Refresh the audio player.
                self.time_stamper.audio_player = audio_player = Player()
                audio_player.queue(audio_source)

                # Adjust the start time of the audio.
                audio_player.seek(current_time_seconds)

                # Play the audio.
                audio_player.play()

        return seconds_to_adjust_by
