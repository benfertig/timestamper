#-*- coding: utf-8 -*-
"""This module contains the TimeStamperTimer class which allows
for keeping track of time in the Time Stamper program."""

from time import perf_counter
from tkinter import DISABLED, END, NORMAL

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
    """This class runs a timer with pause, resume, rewind and fast-forward features.
    Once the objects for the root window and the fields displaying the timer's current time
    are created, they should be passed to this class through the pass_objects method."""

    class Timing():
        """This class stores the variables that are not part of a Tkinter window. The
        variables in this class will be updated throughout the TimeStamper run() function.
        This can be accomplished wiothout global variables because an instance of the
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

    def __init__(self, time_stamper):
        """The __init__ method of TimeStamperTimer takes one argument
        (time_stamper) which should be an object of type TimeStamper."""

        self.time_stamper = time_stamper
        self.timing = self.Timing()

    def read_current_time(self, raw=False):
        """This method reads in and returns the current time from the time fields. This
        is the primary method that is used to retrieve the time while the timer is PAUSED.
        This method takes one optional argument, raw, which is set to False by default.
        When raw is True, the returned values will be three strings representing the timer's
        current time in hours, minutes and seconds (padded with 0's if necessary). When raw
        is False, the returned values will be the same as the values that are returned when
        raw is True, but the values will be converted to integers before being returned."""

        ################
        # If raw is True
        ################
        if raw:

            # Return the time from the time fields as it should appear on the timer.
            hours = self.timing.pad_number(self.time_stamper.time_fields.hours_field.get(), 2)
            minutes = self.timing.pad_number(self.time_stamper.time_fields.minutes_field.get(), 2)
            seconds = self.timing.pad_number(self.time_stamper.time_fields.seconds_field.get(), 2)
            subseconds = \
                self.timing.pad_number(self.time_stamper.time_fields.subseconds_field.get(), 2)
            return hours, minutes, seconds, subseconds

        #################
        # If raw is False
        #################

        # Get the current time from the time fields.
        hours = self.time_stamper.time_fields.hours_field.get()
        minutes = self.time_stamper.time_fields.minutes_field.get()
        seconds = self.time_stamper.time_fields.seconds_field.get()
        subseconds = self.time_stamper.time_fields.subseconds_field.get()

        # Convert the numbers from the time fields to integers before returning them.
        hours = int(hours) if hours else 0
        minutes = int(minutes) if minutes else 0
        seconds = int(seconds) if seconds else 0
        subseconds = int(subseconds) if subseconds else 0

        return hours, minutes, seconds, subseconds

    def current_time_to_timestamp(self):
        """This method converts the currently diplayed time to a timestamp."""
        hours, minutes, seconds, subseconds = self.read_current_time(raw=True)
        return f"[{hours}:{minutes}:{seconds}.{subseconds}]"

    def display_time(self, hours, minutes, seconds, subseconds):
        """This method displays the time passed to it as
        arguments to the timer fields of self.time_stamper."""

        # Determine whether the time fields are enabled.
        was_enabled = self.time_stamper.time_fields.hours_field["state"] == NORMAL

        # Display the hours time.
        self.time_stamper.time_fields.hours_field["state"] = NORMAL
        self.time_stamper.time_fields.hours_field.delete(0, END)
        self.time_stamper.time_fields.hours_field.insert(0, hours)

        # Display the minutes time.
        self.time_stamper.time_fields.minutes_field["state"] = NORMAL
        self.time_stamper.time_fields.minutes_field.delete(0, END)
        self.time_stamper.time_fields.minutes_field.insert(0, minutes)

        # Display the seconds time.
        self.time_stamper.time_fields.seconds_field["state"] = NORMAL
        self.time_stamper.time_fields.seconds_field.delete(0, END)
        self.time_stamper.time_fields.seconds_field.insert(0, seconds)

        # Display the subseconds time.
        self.time_stamper.time_fields.subseconds_field["state"] = NORMAL
        self.time_stamper.time_fields.subseconds_field.delete(0, END)
        self.time_stamper.time_fields.subseconds_field.insert(0, subseconds)

        # Disable the time fields if they were disabled to begin with.
        if not was_enabled:
            self.time_stamper.time_fields.hours_field["state"] = DISABLED
            self.time_stamper.time_fields.minutes_field["state"] = DISABLED
            self.time_stamper.time_fields.seconds_field["state"] = DISABLED
            self.time_stamper.time_fields.subseconds_field["state"] = DISABLED

    def update_timer(self, seconds_to_add=0):
        """This method refreshes the timer. The optional argument seconds_to_add will add
        to/subtract from the timer the specified amount of seconds. If a positive number is passed,
        seconds will be added. If a negative number is passed, seconds will be subtracted."""

        # If the timer is running, calculate the current time by using the time module.
        if self.timing.is_running:
            current_time_seconds = self.timing.current_running_time()
            return current_time_seconds

        # If the timer is not running calculate the current
        # time by retrieving it from the time fields.
        hours, minutes, seconds, subseconds = self.read_current_time()
        current_time_seconds = self.timing.h_m_s_to_seconds(hours, minutes, seconds, subseconds)

        # Increase or decrease the current time if a number of seconds is supplied as an argument.
        current_time_seconds += seconds_to_add

        # Return the updated time.
        return current_time_seconds

    def timer_tick(self):
        """This method runs continuously while the
        timer is running to update the current time."""

        # Only tick the timer if it is currently running.
        if self.timing.is_running:

            # Only tick the timer if it is less than the maximum displayable time.
            disp_hours, disp_minutes, disp_seconds, disp_subseconds = self.read_current_time()
            if self.timing.h_m_s_to_seconds(disp_hours, disp_minutes, \
                disp_seconds, disp_subseconds) < 359999.99:

                # Refresh the current time (in seconds) and retrieve it.
                current_time_seconds = self.update_timer()

                # Convert the current time (in seconds) to hours, minutes, seconds and subseconds.
                hours, minutes, seconds, subseconds = \
                    self.timing.seconds_to_h_m_s(current_time_seconds, pad=2)

                # Display the current time.
                self.display_time(hours, minutes, seconds, subseconds)

                # Tick the timer again.
                self.time_stamper.root.after(5, self.timer_tick)

            # If the timer's currently displayed time is not less
            # than the maximum displayable time, stop the timer.
            else:
                macro_mapping = self.time_stamper.macros.macro_mapping
                button_stop_str_key = self.time_stamper.shell.fields.buttons.media.stop.str_key
                macro_mapping[button_stop_str_key]()

    def pause(self):
        """This method pauses the timer and is typically run when the pause button is pressed."""

        # Declare the timer as not running.
        self.timing.is_running = False

        # Record the raw time of pause.
        self.timing.pause_time = perf_counter()

        # Get the current time from the time fields.
        disp_hours, disp_minutes, disp_seconds, disp_subseconds = self.read_current_time()

        # Save the currently displayed time as the timer's reading at pause.
        self.timing.reading_at_pause = \
            self.timing.h_m_s_to_seconds(disp_hours, disp_minutes, disp_seconds, disp_subseconds)

    def play(self):
        """This method resumes (unpauses) the timer and is
        typically run when the play button is pressed."""

        # Only run the timer if the currently displayed time is less
        # than the maximum time (99 hours, 59 minutes and 59.99 seconds).
        disp_hours, disp_minutes, disp_seconds, disp_subseconds = self.read_current_time()
        if self.timing.h_m_s_to_seconds(disp_hours, disp_minutes, \
            disp_seconds, disp_subseconds) < 359999.99:

            # Declare the timer as running.
            self.timing.is_running = True

            # Calculate the amount of raw time that the timer has spent paused.
            self.timing.total_pause_time += (perf_counter() - self.timing.pause_time)

            # Read the timer's current time from the time fields.
            disp_hours, disp_minutes, disp_seconds, disp_subseconds = self.read_current_time()

            # It is possible that the user edited the timer's values by hand while
            # the timer was paused. If this is the case, factor the difference between
            # the reading of the timer when it resumed and the reading of the timer
            # when it was paused into future calculations of the timer's running time.
            self.timing.offset += (self.timing.h_m_s_to_seconds(disp_hours, \
                disp_minutes, disp_seconds, disp_subseconds) - self.timing.reading_at_pause)

            # Begin ticking the timer.
            self.timer_tick()

        # If the timer's currently displayed time is not less
        # than the maximum displayable time, stop the timer.
        else:
            macro_mapping = self.time_stamper.macros.macro_mapping
            button_stop_str_key = self.time_stamper.shell.fields.buttons.media.stop.str_key
            macro_mapping[button_stop_str_key]()

    def stop(self):
        """This method stops the timer and is typically
        run when the stop button is pressed."""

        # To stop the timer, simply reset all variables responsible for keeping track of the time.
        self.timing = self.Timing()

    def rewind(self, seconds_to_rewind):
        """This method rewinds the timer and is typically run when the rewind button is pressed.
        The timer will rewind the amount of seconds provided in the argument seconds_to_rewind,
        which is is typically retrieved from the input field below the rewind button."""

        # Get the current time in seconds before rewinding
        if self.timing.is_running:

            # If the timer is running, calculate the current time by using the time module.
            current_time_seconds = self.timing.current_running_time()

        else:

            # If the timer is not running calculate the current
            # time by retrieving it from the time fields.
            hours, minutes, seconds, subseconds = self.read_current_time()
            current_time_seconds = self.timing.h_m_s_to_seconds(hours, minutes, seconds, subseconds)

        # Figure out the amount of time to rewind, which may be less than the
        # amount of requested time because that could bring the timer below 0.
        if current_time_seconds - seconds_to_rewind < 0:
            seconds_to_rewind = current_time_seconds
        current_time_seconds -= seconds_to_rewind

        # Subtract the rewound amount of time from the timer
        if self.timing.is_running:
            self.timing.offset -= seconds_to_rewind

        current_time_seconds = self.update_timer(-seconds_to_rewind)

        # Display the updated time immediately
        hours, minutes, seconds, subseconds = \
            self.timing.seconds_to_h_m_s(current_time_seconds, pad=2)
        self.display_time(hours, minutes, seconds, subseconds)

    def fast_forward(self, seconds_to_fast_forward):
        """This method fast-forwards the timer and is typically run when the
        fast-forward button is pressed. The timer will fast-forward the amount
        of seconds provided in the argument seconds_to_fast_forward, which
        is typically retrieved from the input field below the fast-forward button."""

        # Get the current time in seconds before fast-forwarding
        if self.timing.is_running:

            # If the timer is running, calculate the current time by using the time module.
            current_time_seconds = self.timing.current_running_time()

        else:

            # If the timer is not running calculate the current
            # time by retrieving it from the time fields.
            hours, minutes, seconds, subseconds = self.read_current_time()
            current_time_seconds = \
                self.timing.h_m_s_to_seconds(hours, minutes, seconds, subseconds)

        # Figure out the amount of time to fast-forward, which may
        # be less than the amount of time requested because that could
        # bring the timer over the maximum time that it can display (99:59:59.99).
        if current_time_seconds + seconds_to_fast_forward > 359999.99:
            seconds_to_fast_forward = 359999.999 - current_time_seconds
        current_time_seconds += seconds_to_fast_forward

        # Add the fast forward time to the timer.
        if self.timing.is_running:
            self.timing.offset += seconds_to_fast_forward

        # Refresh the timer with the amount of requested fast-forward seconds factored in.
        current_time_seconds = self.update_timer(seconds_to_fast_forward)

        # Display the updated time immediately.
        hours, minutes, seconds, subseconds = \
            self.timing.seconds_to_h_m_s(current_time_seconds, pad=2)
        self.display_time(hours, minutes, seconds, subseconds)

    def record(self):
        """This method initially starts the timer and is
        typically run when the record button is pressed."""

        # Only run the timer if the currently displayed time is less
        # than the maximum time (99 hours, 59 minutes and 59.99 seconds).
        disp_hours, disp_minutes, disp_seconds, disp_subseconds = self.read_current_time()
        if self.timing.h_m_s_to_seconds(disp_hours, disp_minutes, \
            disp_seconds, disp_subseconds) < 359999.99:

            # Save the raw time as the timer's start time.
            self.timing.start_time = perf_counter()

            # Calculate the timer's initial offset by retrieving the timer's
            # initial time from the time fields so that this can be
            # factored into future calculations of the timer's running time.
            disp_hours, disp_minutes, disp_seconds, disp_subseconds = self.read_current_time()
            self.timing.offset += self.timing.h_m_s_to_seconds(\
                disp_hours, disp_minutes, disp_seconds, disp_subseconds)

            # Declare the timer as running.
            self.timing.is_running = True

            # Begin ticking the timer.
            self.timer_tick()

        # If the timer's currently displayed time is not less
        # than the maximum displayable time, stop the timer.
        else:
            macro_mapping = self.time_stamper.macros.macro_mapping
            button_stop_str_key = self.time_stamper.shell.fields.buttons.media.stop.str_key
            macro_mapping[button_stop_str_key]()
