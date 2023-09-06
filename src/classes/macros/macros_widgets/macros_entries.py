#-*- coding: utf-8 -*-
"""This module stores the functions that are executed when
entries in the Time Stamper program are manipulated."""

import classes
import methods.macros.methods_macros_helper as methods_helper
import methods.macros.methods_macros_timing as methods_timing

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

#################### TIMER ENTRIES MACROS ####################


def entry_hours_trace(entry_text):
    """This method gets executed when the text is edited in the hours entry."""

    methods_helper.entry_trace_method(entry_text, classes.template["entry_hours"])


def entry_hours_mousewheel_macro(event):
    """This method gets executed when the mousewheel is moved over the hours entry."""

    methods_timing.adjust_timer_on_entry_mousewheel(event, classes.template["entry_hours"])


def entry_minutes_trace(entry_text):
    """This method gets executed when the text is edited in the minutes entry."""

    methods_helper.entry_trace_method(entry_text, classes.template["entry_minutes"])


def entry_minutes_mousewheel_macro(event):
    """This method gets executed when the mousewheel is moved over the minutes entry."""

    methods_timing.adjust_timer_on_entry_mousewheel(event, classes.template["entry_minutes"])


def entry_seconds_trace(entry_text):
    """This method gets executed when the text is edited in the seconds entry."""

    methods_helper.entry_trace_method(entry_text, classes.template["entry_seconds"])


def entry_seconds_mousewheel_macro(event):
    """This method gets executed when the mousewheel is moved over the seconds entry."""

    methods_timing.adjust_timer_on_entry_mousewheel(event, classes.template["entry_seconds"])


def entry_subseconds_trace(entry_text):
    """This method gets executed when the text is edited in the subseconds entry."""

    methods_helper.entry_trace_method(entry_text, classes.template["entry_subseconds"])


def entry_subseconds_mousewheel_macro(event):
    """This method gets executed when the mousewheel is moved over the subseconds entry."""

    methods_timing.adjust_timer_on_entry_mousewheel(event, classes.template["entry_subseconds"])


#################### SKIP BACKWARD/FORWARD ENTRIES MACROS ####################


def entry_skip_backward_trace(entry_text):
    """This method gets executed when the text is edited in the skip backward entry."""

    methods_helper.entry_trace_method(entry_text, classes.template["entry_skip_backward"])


def entry_skip_backward_mousewheel_macro(event):
    """This method gets executed when the mousewheel is moved over the skip backward entry."""

    methods_helper.adjust_skip_values_on_entry_mousewheel(event, True)


def entry_skip_forward_trace(entry_text):
    """This method gets executed when the text is edited in the skip forward entry."""

    methods_helper.entry_trace_method(entry_text, classes.template["entry_skip_forward"])


def entry_skip_forward_mousewheel_macro(event):
    """This method gets executed when the mousewheel is moved over the skip forward entry."""

    methods_helper.adjust_skip_values_on_entry_mousewheel(event, False)


#################### SETTINGS ENTRIES MACROS ####################


def entry_pause_settings_trace(entry_text):
    """This method gets executed when the text is edited in the pause settings entry."""

    methods_helper.entry_trace_method(entry_text, classes.template["entry_pause_settings"])


def entry_play_settings_trace(entry_text):
    """This method gets executed when the text is edited in the play settings entry."""

    methods_helper.entry_trace_method(entry_text, classes.template["entry_play_settings"])


def entry_rewind_settings_trace(entry_text):
    """This method gets executed when the text is edited in the rewind settings entry."""

    methods_helper.entry_trace_method(entry_text, classes.template["entry_rewind_settings"])


def entry_fast_forward_settings_trace(entry_text):
    """This method gets executed when the text is edited in the fast-forward settings entry."""

    methods_helper.entry_trace_method(entry_text, classes.template["entry_fast_forward_settings"])


def entry_skip_backward_settings_trace(entry_text):
    """This method gets executed when the text is edited in the skip backward settings entry."""

    methods_helper.entry_trace_method(entry_text, classes.template["entry_skip_backward_settings"])


def entry_skip_forward_settings_trace(entry_text):
    """This method gets executed when the text is edited in the skip forward settings entry."""

    methods_helper.entry_trace_method(entry_text, classes.template["entry_skip_forward_settings"])


def entry_hotkey_1_settings_trace(entry_text):
    """This method gets executed when the text is edited in the hotkey 1 settings entry."""

    methods_helper.entry_trace_method(entry_text, classes.template["entry_hotkey_1_settings"])


def entry_hotkey_2_settings_trace(entry_text):
    """This method gets executed when the text is edited in the hotkey 2 settings entry."""

    methods_helper.entry_trace_method(entry_text, classes.template["entry_hotkey_2_settings"])


def entry_hotkey_3_settings_trace(entry_text):
    """This method gets executed when the text is edited in the hotkey 3 settings entry."""

    methods_helper.entry_trace_method(entry_text, classes.template["entry_hotkey_3_settings"])
