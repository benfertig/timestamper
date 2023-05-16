#-*- coding: utf-8 -*-
"""This module contains the EntryMacros class which stores the functions
that are executed when an entry in the Time Stamper program is manipulated."""

from sys import platform
from tkinter import DISABLED, NORMAL

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
        self.widgets = parent.widgets

    def entry_trace_method(self, entry_text, entry_template):
        """This is a custom method that gets executed when the
        text is edited in one of several entries (hours, minutes,
        seconds, subseconds, skip backward entry, skip forward entry)."""

        max_val = entry_template["max_val"]

        if len(entry_text.get()) > 0:

            # If this entry should contain only digits...
            if entry_template["digits_only"]:

                # Remove any non-digits from the entry.
                try:
                    int(entry_text.get()[-1])
                except ValueError:
                    entry_text.set(entry_text.get()[:-1])

                # Remove any digits from the entry that put the entry over max_val.
                if len(entry_text.get()) > 0:
                    if int(entry_text.get()) > max_val:
                        entry_text.set(entry_text.get()[:-1])

        # Enable and disable the relevant buttons for when the entry's text is edited.
        for str_to_enable in entry_template["to_enable"]:
            self.widgets[str_to_enable]["state"] = NORMAL
        for str_to_disable in entry_template["to_disable"]:
            self.widgets[str_to_disable]["state"] = DISABLED

        # Save the entry's updated text in the entry's template.
        entry_template["text_loaded_value"] = entry_text.get()

    def adjust_timer_on_entry_mousewheel(self, event, entry_template):
        """This is a custom method that gets executed when the mousewheel is moved
        over one of the timer entries (hours, minutes, seconds or subseconds)."""

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
            # the media slider or timer entries but has not yet finished scrolling.
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

    #################### TIMER ENTRIES TRACE MACROS ####################

    def entry_hours_trace(self, entry_text):
        """This method gets executed when the text is edited in the hours entry."""

        self.entry_trace_method(entry_text, self.template["entry_hours"])

    def entry_minutes_trace(self, entry_text):
        """This method gets executed when the text is edited in the minutes entry."""

        self.entry_trace_method(entry_text, self.template["entry_minutes"])

    def entry_seconds_trace(self, entry_text):
        """This method gets executed when the text is edited in the seconds entry."""

        self.entry_trace_method(entry_text, self.template["entry_seconds"])

    def entry_subseconds_trace(self, entry_text):
        """This method gets executed when the text is edited in the subseconds entry."""

        self.entry_trace_method(entry_text, self.template["entry_subseconds"])

    #################### SKIP BACKWARD/FORWARD ENTRIES TRACE MACROS ####################

    def entry_skip_backward_trace(self, entry_text):
        """This method gets executed when the text is edited in the skip backward entry."""

        self.entry_trace_method(entry_text, self.template["entry_skip_backward"])

    def entry_skip_forward_trace(self, entry_text):
        """This method gets executed when the text is edited in the skip forward entry."""

        self.entry_trace_method(entry_text, self.template["entry_skip_forward"])

    #################### SETTINGS ENTRIES TRACE MACROS ####################

    def entry_pause_settings_trace(self, entry_text):
        """This method gets executed when the text is edited in the pause settings entry."""

        self.entry_trace_method(entry_text, self.template["entry_pause_settings"])

    def entry_play_settings_trace(self, entry_text):
        """This method gets executed when the text is edited in the play settings entry."""

        self.entry_trace_method(entry_text, self.template["entry_play_settings"])

    def entry_skip_backward_settings_trace(self, entry_text):
        """This method gets executed when the text is edited in the skip backward settings entry."""

        self.entry_trace_method(entry_text, self.template["entry_skip_backward_settings"])

    def entry_skip_forward_settings_trace(self, entry_text):
        """This method gets executed when the text is edited in the skip forward settings entry."""

        self.entry_trace_method(entry_text, self.template["entry_skip_forward_settings"])

    def entry_hotkey_1_settings_trace(self, entry_text):
        """This method gets executed when the text is edited in the hotkey 1 settings entry."""

        self.entry_trace_method(entry_text, self.template["entry_hotkey_1_settings"])

    def entry_hotkey_2_settings_trace(self, entry_text):
        """This method gets executed when the text is edited in the hotkey 2 settings entry."""

        self.entry_trace_method(entry_text, self.template["entry_hotkey_2_settings"])

    def entry_hotkey_3_settings_trace(self, entry_text):
        """This method gets executed when the text is edited in the hotkey 3 settings entry."""

        self.entry_trace_method(entry_text, self.template["entry_hotkey_3_settings"])

    #################### MOUSEWHEEL MACROS ####################

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
