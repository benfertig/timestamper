#-*- coding: utf-8 -*-
"""This module contains the EntryMacros class which stores the functions
that are executed when an entry in the Time Stamper program is manipulated."""

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


class EntryMacros():
    """This class stores all of the macros that execute when entries are manipulated."""

    def __init__(self, parent):
        self.parent = parent
        self.time_stamper = parent.time_stamper
        self.template = parent.template
        self.timer = parent.timer

    def adjust_timer_on_entry_mousewheel(self, event, entry_template):
        """This is a custom event method that gets executed when the mousewheel is
        moved over one of the timer entries (hours, minutes, seconds or subseconds)."""

        # On Mac platforms, the registered scroll amount does not need to be divided by 120.
        event_delta = event.delta if platform.startswith("darwin") else int(event.delta / 120)

        # If the timer is currently playing or is scheduled to play,
        # schedule/reschedule the timer to resume playing after a short delay.
        timer_is_playing = self.timer.is_running or self.timer.scheduled_id
        if timer_is_playing:

            # Pause the timer without resetting the multiplier.
            self.timer.pause(reset_multiplier=False)

            # If there is an existing scheduled play function, then it should be
            # cancelled, as this effectively means that the user was already scrolling
            # the audio slider or timer entries but has not yet finished scrolling.
            if self.timer.scheduled_id:
                self.time_stamper.root.after_cancel(self.timer.scheduled_id)

            # Schedule the timer to play after the specified delay.
            self.timer.scheduled_id = \
                self.time_stamper.root.after(250, self.timer.play, "prev")

        # Adjust the timer according to the direction the user scrolled.
        scroll_timer_adjustment = event_delta * float(entry_template["scroll_timer_adjustment"])
        self.timer.adjust_timer(scroll_timer_adjustment, abort_if_out_of_bounds=True)

        # Pause the timer if it is playing and was adjusted to the max time.
        max_time = self.timer.get_max_time()
        if timer_is_playing and self.timer.get_current_seconds() >= max_time:
            self.timer.display_time(max_time, pad=2)
            self.parent["button_pause"]()

    def entry_hours_mousewheel_macro(self, event):
        """This method that gets executed when the mousewheel is moved over the hours entry."""

        self.adjust_timer_on_entry_mousewheel(event, self.template["entry_hours"])

    def entry_minutes_mousewheel_macro(self, event):
        """This method that gets executed when the mousewheel is moved over the minutes entry."""

        self.adjust_timer_on_entry_mousewheel(event, self.template["entry_minutes"])

    def entry_seconds_mousewheel_macro(self, event):
        """This method that gets executed when the mousewheel is moved over the seconds entry."""

        self.adjust_timer_on_entry_mousewheel(event, self.template["entry_seconds"])

    def entry_subseconds_mousewheel_macro(self, event):
        """This method that gets executed when the mousewheel is moved over the subseconds entry."""

        self.adjust_timer_on_entry_mousewheel(event, self.template["entry_subseconds"])
