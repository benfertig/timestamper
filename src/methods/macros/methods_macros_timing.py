#-*- coding: utf-8 -*-
"""This module stores some extra methods associated with the timer."""

from sys import platform
from tkinter import RAISED, SUNKEN

import classes
import methods.macros.methods_macros_helper as methods_helper
import methods.macros.methods_macros_media as methods_media
from methods.timing import methods_timing_helper

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


def playback_press_macro(playback_type):
    """This method is called by button_play_press_macro, button_rewind_press_macro and
    button_fast_forward_press_macro. The functions performed by these three methods are
    very similar, so their procedures have been condensed down to a single method here and
    different parameters are passed depending on where this method is being called from."""

    button_str_key = f"button_{playback_type}"

    # Rebind all of the playback buttons to their respective press/release macros.
    methods_helper.rebind_playback_buttons()

    # Enable and disable the relevant widgets for when this button is pressed.
    methods_helper.button_enable_disable_macro(classes.template[button_str_key])

    # Make the button appear pressed.
    classes.widgets[button_str_key].config(relief=SUNKEN)

    # Record the time that the button was pressed.
    classes.time_stamper.play_press_time = classes.timer.get_current_seconds()

    # Schedule the timer to start after a short delay (this scheduled start will be
    # cancelled if the current button is released before the delay period has ended).
    classes.timer.scheduled_id = \
        classes.time_stamper.root.after(250, classes.timer.play, playback_type)

    return "break"


def playback_release_macro(playback_type):
    """This method is called by button_play_release_macro, button_rewind_release_macro and
    button_fast_forward_release_macro. The functions performed by these three methods are
    very similar, so their procedures have been condensed down to a single method here and
    different parameters are passed depending on where this method is being called from."""

    button_str_key = f"button_{playback_type}"
    button = classes.widgets[button_str_key]
    button.config(relief=RAISED)

    # If the playback button HAS NOT been held long enough to initiate the timer...
    if classes.timer.scheduled_id:

        # Cancel the upcoming, scheduled play function.
        classes.time_stamper.root.after_cancel(classes.timer.scheduled_id)
        classes.timer.scheduled_id = None

        # Generate a timestamp using the timer's current time.
        timestamp = classes.timer.current_time_to_timestamp()

        # Unbind the button from its play/release macros temporarily.
        button.unbind("<Button-1>")
        button.unbind("<ButtonRelease-1>")

        # Start the timer.
        new_multiplier = classes.timer.play(playback_type=playback_type)

        # Return the timestamp and the timer's new speed, indicating that playback has started.
        return timestamp, new_multiplier

    # If the playback button HAS been held long enough to initiate the timer...

    # The program should behave as if the pause button was pressed (omitting button messages).
    classes.macros["button_pause"](force_suppress_message=True)

    # Reset the timer to where it was at when the current playback button was pressed.
    classes.timer.display_time(classes.time_stamper.play_press_time)

    # Return (None, None), indicating that playback has stopped.
    return None, None


def skip_backward_or_forward_macro(is_skip_backward):
    """This method contains the entire functionality for the skip backward and skip forward
    buttons. The functions performed by these two buttons are very similar, so their
    procedures have been condensed down to a single method here and different parameters
    are passed depending on whether the skip backward or skip forward button was pressed."""

    direction = "backward" if is_skip_backward else "forward"
    button_str_key = f"button_skip_{direction}"

    # Enable and disable the relevant widgets for when
    # the skip backward/forward button is pressed.
    methods_helper.button_enable_disable_macro(classes.template[button_str_key])

    # Get the timestamp before skipping backward/forward.
    timestamp = classes.timer.current_time_to_timestamp()

    # Skip the timer backward/forward the specified number of seconds.
    adjust_amount = float(classes.widgets[f"entry_skip_{direction}"].textvariable.get())
    skip_amount = \
        classes.timer.adjust_timer(adjust_amount * -1 if is_skip_backward else adjust_amount)

    # Get the time after skipping backward/forward.
    new_time = classes.timer.current_time_to_timestamp(include_brackets=False)

    # Round the skip amount to the nearest centisecond.
    skip_amount = abs(round(skip_amount, 2))
    if skip_amount % 1 == 0:
        skip_amount = int(skip_amount)

    return timestamp, skip_amount, new_time


def timer_entry_trace_method(entry_text, entry_template):
    """This method contains the entire functionality for the trace methods of the hours entry,
    the minutes entry, the seconds entry and the subseconds entry. The functions performed by
    these four methods are very similar, so their procedures have been condensed down to a single
    method here and different parameters are passed depending on which trace method was invoked."""

    # If this method was called EITHER from an automatic update of the timer because it is currently
    # running OR from the user scrolling the mousewheel over one of the timer entries, then
    # this entry's text has already been validated elsewhere, so we know that the text is valid.
    if classes.timer.is_running or classes.timer.is_being_scrolled:

        # Mark the entry's text as valid.
        entry_text_is_valid = True

        # Get the timer's current time in seconds.
        current_time_seconds = classes.timer.get_current_seconds()

    # If this method was called NEITHER from an automatic update of the timer
    # because it is currently running NOR from the user scrolling the mousewheel
    # over one of the timer entries, then this method must have been called from
    # the user having edited one of the timer entries manually, so we need to
    # ensure that the value the user entered makes the timer reflect a valid time.
    else:

        # Call the generic entry trace method to see whether the entry contains
        # any non-digits or any digits that put the entry over its maximum value.
        entry_text_is_valid = methods_helper.entry_trace_method(entry_text, entry_template)

        # Only perform further checks on the entry text if the
        # generic entry_trace_method did not detect any problems.
        if entry_text_is_valid:

            # Get the timer's current time in seconds.
            current_time_seconds = classes.timer.get_current_seconds()

            # If adding the most recently added character to the timer entry put the
            # timer over its maximum time, then the entry's current text is not valid.
            if current_time_seconds > classes.timer.get_max_time():
                entry_text_is_valid = False

    # If the user-entered text IS valid, store the entry's value for potential referencing later.
    if entry_text_is_valid:
        entry_template["previous_value"] = entry_text.get()

    # If the user-entered text IS NOT valid...
    else:

        # Set the entry's value to its previous value
        entry_text.set(entry_template["previous_value"])

        # Regenerate the timer's new time, factoring in the modified entry.
        current_time_seconds = classes.timer.get_current_seconds()

    # Update the timestamp if a fixed timestamp has not been set.
    if not classes.template["label_timestamp"]["timestamp_set"]:
        classes.timer.update_timestamp(seconds_override=current_time_seconds, truncate_to=2)

    # If a media player exists, update the position of the media time
    # slider, the displays of elapsed and remaining time and (if the media
    # file is not currently playing) the start time of the media file.
    if classes.time_stamper.media_player:
        methods_media.refresh_media_time(current_time_seconds, pad=2)

    # Store the updated value of the timer entry so that we can (potentially) revert
    # back to it should the user later enter an invalid value into this entry.
    entry_template["previous_value"] = entry_text.get()


def timer_entry_mousewheel_method(event, entry_template):
    """This method contains the entire functionality of the methods that get executed
    when the mousewheel is moved over the hours entry, the minutes entry, the seconds
    entry and the subseconds entry. The functions performed by these four methods are
    very similar, so their procedures have been condensed down to a single method here
    and different parameters are passed depending on which mousewheel method was invoked."""

    # Indicate that the timer is being scrolled.
    classes.timer.is_being_scrolled = True

    # On Mac platforms, the registered scroll amount does not need to be divided by 120.
    event_delta = event.delta if platform.startswith("darwin") else int(event.delta / 120)

    # If the timer is currently playing or is scheduled to play,
    # schedule/reschedule the timer to resume playing after a short delay.
    timer_is_playing = classes.timer.is_running or classes.timer.scheduled_id

    # Pause the timer, scheduling it to play again
    # after a short delay if it is currently running.
    classes.timer.pause(play_delay=0.25)

    # Adjust the timer according to the direction the user scrolled.
    scroll_adjustment = event_delta * float(entry_template["scroll_timer_adjustment"])
    scroll_adjustment = classes.timer.adjust_timer(scroll_adjustment, abort_if_out_of_bounds=True)

    # Pause the timer if it is playing and was adjusted to the max time.
    max_time = classes.timer.get_max_time()
    if timer_is_playing and classes.timer.get_current_seconds() >= max_time:
        classes.timer.display_time(max_time, pad=2)
        classes.macros["button_pause"]()

    # If the timer was not adjusted, ensure that the current time is displayed in its entirety.
    if scroll_adjustment == 0:
        h_m_s = classes.timer.read_timer()
        classes.timer.display_time(methods_timing_helper.h_m_s_to_seconds(*h_m_s))

    # Indicate that the timer is no longer being scrolled.
    classes.timer.is_being_scrolled = False


def skip_backward_or_forward_entry_trace_method(entry_text, is_skip_backward):
    """This method contains the entire functionality for the trace methods of the skip
    backward and skip forward entries. The functions performed by both of these methods
    are very similar, so their procedures have been condensed down to a single method
    here and different parameters are passed depending on which trace method was invoked."""

    # Store the string key and the template for the current entry.
    entry_str_key = "entry_skip_backward" if is_skip_backward else "entry_skip_forward"
    entry_template = classes.template[entry_str_key]

    # Check whether the text that the user entered into the entry is valid.
    entry_text_is_valid = methods_helper.entry_trace_method(entry_text, entry_template)

    # If the user-entered text IS valid, store the entry's value for potential referencing later.
    if entry_text_is_valid:
        entry_template["previous_value"] = entry_text.get()

    # If the user-entered text IS NOT valid, set the entry's value to its previous value.
    else:
        entry_text.set(entry_template["previous_value"])


def set_or_clear_timestamp(is_set_timestamp):
    """This method contains the entire functionality for the timestamp and clear timestamp
    buttons. The functions performed by these two buttons are very similar, so their
    procedures have been condensed down to a single method here and different parameters
    are passed depending on whether the timestamp or clear timestamp button was pressed."""

    # Make note of the fact that a timestamp has been set.
    classes.template["label_timestamp"]["timestamp_set"] = is_set_timestamp

    # Set the timestamp.
    classes.widgets["label_timestamp"]["text"] = classes.timer.current_time_to_timestamp()

    # Enable and disable the relevant buttons for when
    # the timestamp/clear timestamp button is pressed.
    methods_helper.button_enable_disable_macro(\
        classes.template["button_timestamp" if is_set_timestamp else "button_clear_timestamp"])
