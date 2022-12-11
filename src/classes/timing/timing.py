#-*- coding: utf-8 -*-
"""This module contains the TimeStamperTimer class which allows
for keeping track of time in the Time Stamper program."""

from os.path import exists
from time import perf_counter
from pyglet.media import load, Player
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

        self.mapping = {"audio_source": None, "audio_player": None}

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

            # Only tick the timer if its current time is less than the maximum displayable time.
            if self.get_current_seconds() < 359999.99:

                # Display the current time.
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
        audio_player = self.mapping["audio_player"]
        if audio_player:
            audio_player.pause()

    def play(self):
        """This method starts the timer and is typically
        run when the play or record button is pressed."""

        # Only run the timer if the currently displayed time is less
        # than the maximum time (99 hours, 59 minutes and 59.99 seconds).
        current_time_seconds = self.get_current_seconds()
        if current_time_seconds < 359999.99:

            # Save the current raw time.
            self.start_time = perf_counter()

            # Declare the timer as running.
            self.is_running = True

            # Factor the current reading on the timer into the
            # offset for the calculation of the running time.
            self.offset = current_time_seconds

            # Begin ticking the timer.
            self.timer_tick()

        # If the timer's currently displayed time is not less
        # than the maximum displayable time, stop the timer.
        else:
            self.time_stamper.macros["button_stop"]()

        # Play the selected audio file if it exists.
        audio_file_path = self.time_stamper.widgets["entry_audio_path"].get()
        if exists(audio_file_path):

            # Load the audio source.
            audio_source = load(audio_file_path)
            self.mapping["audio_source"] = audio_source

            # Set the audio source to begin at the timer's current time.
            audio_source.seek(self.get_current_seconds())

            # Load the audio player.
            audio_player = Player()
            self.mapping["audio_player"] = audio_player
            audio_player.queue(audio_source)

            # Play the audio.
            audio_player.play()

    def adjust_timer(self, seconds_to_adjust_by):
        """This method rewinds and fast_forwards the timer. Since the rewind and fast-forward
        procedures are very similar, they have been condensed into this single method."""

        # Get the current time in seconds before adjusting the timer.
        current_time_seconds = self.get_current_seconds()

        # Figure out the amount of time to adjust the timer by, which may be less
        # than the amount of requested time because that could bring the timer below
        # the minumum time (00h 00m 00.00s) or above the maximum time (99h 59m 59.99s).
        if current_time_seconds + seconds_to_adjust_by < 0:
            seconds_to_adjust_by = -current_time_seconds
        elif current_time_seconds + seconds_to_adjust_by > 359999.99:
            seconds_to_adjust_by = 359999.99 - current_time_seconds

        # Update the timer's offset, factoring in the specified rewind/fast-forward time.
        self.offset += seconds_to_adjust_by

        # Display the updated time immediately.
        current_time_seconds += seconds_to_adjust_by
        self.display_time(current_time_seconds, pad=2)

        # Adjust the start time of the audio if it exists.
        audio_player = self.mapping["audio_player"]
        if self.is_running and audio_player and audio_player.playing:

            audio_player.pause()
            self.mapping["audio_source"].seek(self.get_current_seconds())
            audio_player.play()
