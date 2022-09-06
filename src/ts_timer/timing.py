#-*- coding: utf-8 -*-
"""This module contains the Timing class, which is called upon by
the TimeStamperTimer class, and contains some helper methods for the
TimeStamperTimer that do not directly reference Tkinter widgets."""

from time import perf_counter

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


class Timing():
    """This class stores the variables of TimeStamperTimer that are not part of a Tkinter
    window. The variables in this class will be updated throughout the TimeStamper run()
    function. This can be accomplished without global variables because an instance of the
    TimeStamperTimer class is created in the main TimeStamper class before the creation of
    the root window. By creating an instance of the TimeStamperTimer class before creating
    the applicable Tkinter window, the TimeStamperTimer class will not be re-initialized on
    each iteration of the Tkinter window's "mainloop" function, so we only need to create
    the TimeStamperTimer class once, eliminating the need for global variables."""

    def __init__(self):
        """The constructor initializes variables that the timer will rely on."""

        self.is_running = False
        self.start_time = 0.0
        self.pause_time = 0.0
        self.total_pause_time = 0.0
        self.offset = 0.0
        self.reading_at_pause = 0.0

    def current_running_time(self):
        """This method returns the timer's time in seconds. This is the primary
        method that is used to retrieve the time while the timer is RUNNING."""
        return perf_counter() - self.start_time - self.total_pause_time + self.offset


    def pad_number(self, number, target_length):
        """This method puts a "0" in front of a number if that number has only 1 digit."""
        str_number = str(int(number)) if number else "0"
        str_number = "0" * (target_length - len(str_number)) + str_number
        return str_number

    def h_m_s_to_seconds(self, hours, minutes, seconds, subseconds):
        """This method converts a time in hours, minutes and seconds to a time in seconds."""
        return (hours * 3600) + (minutes * 60) + seconds + (subseconds / 100)

    def seconds_to_h_m_s(self, seconds_exact, pad=0):
        """This method converts a time in seconds to a time in hours, minutes and seconds."""

        # Convert the seconds to hours, minutes, seconds and subseconds.
        hours = seconds_exact // 3600
        seconds_exact -= (hours * 3600)
        minutes = seconds_exact // 60
        seconds_exact -= (minutes * 60)
        seconds = int(seconds_exact)
        subseconds = int((seconds_exact % 1) * 100)

        # Pad the timer's values with zeros if a pad value is passed as an argument.
        if pad > 0:
            hours = self.pad_number(hours, pad)
            minutes = self.pad_number(minutes, pad)
            seconds = self.pad_number(seconds, pad)
            subseconds = self.pad_number(subseconds, pad)

        return hours, minutes, seconds, subseconds
