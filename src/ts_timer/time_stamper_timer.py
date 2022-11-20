#-*- coding: utf-8 -*-
"""This module contains the TimeStamperTimer class which allows
for keeping track of time in the Time Stamper program."""

from time import perf_counter
from tkinter import DISABLED, END, NORMAL
from .timing import Timing

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
    Once an instance of the TimeStamper class from the module time_stamper_class
    is created, its constructor will create an instance of this TimeStamperTimer
    class, passing itself to the TimeStamperTimer constructor."""

    def __init__(self, time_stamper):
        """The __init__ method of TimeStamperTimer takes one argument
        (time_stamper) which should be an object of type TimeStamper."""

        self.time_stamper = time_stamper
        self.timing = Timing()

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

    def print_to_field(self, field, to_print):
        """This method displays the text stored in the argument to_print to the argument field."""

        # Determine whether the field is enabled.
        was_enabled = field["state"] == NORMAL

        # Print the passed information to the field.
        field["state"] = NORMAL
        field.delete(0, END)
        field.insert(0, to_print)

        # Disable field if is was disabled to begin with.
        if not was_enabled:
            field["state"] = DISABLED

    def display_time(self, hours, minutes, seconds, subseconds):
        """This method displays the time passed to it as
        arguments to the timer fields of self.time_stamper."""

        # Print the hours, minutes, seconds and subseconds to their relevant Tkinter entries.
        self.print_to_field(self.time_stamper.time_fields.hours_field, hours)
        self.print_to_field(self.time_stamper.time_fields.minutes_field, minutes)
        self.print_to_field(self.time_stamper.time_fields.seconds_field, seconds)
        self.print_to_field(self.time_stamper.time_fields.subseconds_field, subseconds)

        # If a timestamp has not been set, make the timestamp label reflect the current time.
        if not self.time_stamper.template.timestamp_set:
            label_timestamp_template = self.time_stamper.template.fields.labels.timestamp
            obj_mapping = self.time_stamper.macros.object_mapping
            obj_timestamp = obj_mapping[label_timestamp_template.str_key]
            obj_timestamp["text"] = f"[{hours}:{minutes}:{seconds}.{subseconds}]"

    def update_timer(self, seconds_to_add=0):
        """This method refreshes the timer, but the refreshed time that this method returns
        still needs to be converted to hours, minutes and seconds and displayed using
        the "display_time" method. The optional argument "seconds_to_add "will add to/subtract
        from the timer the specified amount of seconds. If a positive number is passed,
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
                macro_mapping = self.time_stamper.macros.button_macros.mapping
                button_stop_str_key = self.time_stamper.template.fields.buttons.media.stop.str_key
                macro_mapping[button_stop_str_key]()

    def pause(self):
        """This method pauses the timer and is typically run when the pause button is pressed."""

        # Declare the timer as not running.
        self.timing.is_running = False

    def play(self):
        """This method resumes (unpauses) the timer and is
        typically run when the play button is pressed."""

        # Only run the timer if the currently displayed time is less
        # than the maximum time (99 hours, 59 minutes and 59.99 seconds).
        disp_hours, disp_minutes, disp_seconds, disp_subseconds = self.read_current_time()
        if self.timing.h_m_s_to_seconds(disp_hours, disp_minutes, \
            disp_seconds, disp_subseconds) < 359999.99:

            # Save the raw time that the timer was started
            self.timing.start_time = perf_counter()

            # Declare the timer as running.
            self.timing.is_running = True

            # Read the timer's current time from the time fields.
            disp_hours, disp_minutes, disp_seconds, disp_subseconds = self.read_current_time()

            # It is possible that the user edited the timer's values by hand while
            # the timer was paused. If this is the case, factor the difference between
            # the reading of the timer when it resumed and the reading of the timer
            # when it was paused into future calculations of the timer's running time.
            self.timing.offset = self.timing.h_m_s_to_seconds(disp_hours, \
                disp_minutes, disp_seconds, disp_subseconds)

            # Begin ticking the timer.
            self.timer_tick()

        # If the timer's currently displayed time is not less
        # than the maximum displayable time, stop the timer.
        else:
            macro_mapping = self.time_stamper.macros.button_macros.mapping
            button_stop_str_key = self.time_stamper.template.fields.buttons.media.stop.str_key
            macro_mapping[button_stop_str_key]()

    def stop(self):
        """This method stops the timer and is typically
        run when the stop button is pressed."""

        # To stop the timer, simply reset all variables responsible for keeping track of the time.
        self.timing = Timing()

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

        # The record method, in its current form, serves
        # merely as a wrapper for the play method.
        self.play()
