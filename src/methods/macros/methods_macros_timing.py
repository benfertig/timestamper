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
    adjust_amount = float(classes.widgets[f"entry_skip_{direction}"].get())
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

    # Call the generic entry trace method, removing any non-digits
    # or any digits that put the entry over its maximum value.
    methods_helper.entry_trace_method(entry_text, entry_template)

    # Generate a list of timer values that will be passed to h_m_s_to_seconds. All timer entry
    # values will be retrieved using entry.get() except for the timer value that is currently
    # being edited, which will be retrieved using entry_text.get(). This is necessary due to
    # the limitations of Tkinter. At this point in the program, we have successfully truncated
    # only the textvariable of the current entry and not the .get() value of the entry itself.
    # It is unclear to me why this is the case, although it seems that the entry's .get() method
    # accurately reflects the true updated text of the entry shortly after this method terminates.
    h_m_s = [entry_text.get() if f"entry_{denom}" == entry_template["str_key"] \
             else classes.widgets[f"entry_{denom}"].get() \
             for denom in ("hours", "minutes", "seconds", "subseconds")]

    # Get the timer's current time in seconds (factoring in the potentially modified entry).
    current_time_seconds = methods_timing_helper.h_m_s_to_seconds(*h_m_s)

    # If adding the most recently added character to the
    # timer entry put the timer over its maximum time...
    if current_time_seconds > classes.timer.get_max_time():

        # Set the value of the entry to its current value, but with the last character removed.
        entry_text.set(entry_text.get()[:-1])

        # Generate the timer values using the same strategy outlined
        # earlier in this method (see long comment several lines above).
        h_m_s = [entry_text.get() if f"entry_{denom}" == entry_template["str_key"] \
                else classes.widgets[f"entry_{denom}"].get() \
                for denom in ("hours", "minutes", "seconds", "subseconds")]

        # Regenerate the timer's new time, factoring in the removed character.
        current_time_seconds = methods_timing_helper.h_m_s_to_seconds(*h_m_s)

    # Update the timestamp if a fixed timestamp has not been set.
    if not classes.template["label_timestamp"]["timestamp_set"]:
        classes.timer.update_timestamp(seconds_override=current_time_seconds, truncate_to=2)

    # If a media player exists, update the position of the media time
    # slider, the displays of elapsed and remaining time and (if the media
    # file is not currently playing) the start time of the media file.
    if classes.time_stamper.media_player:
        methods_media.refresh_media_time(current_time_seconds, pad=2)


def timer_entry_mousewheel_method(event, entry_template):
    """This method contains the entire functionality of the methods that get executed
    when the mousewheel is moved over the hours entry, the minutes entry, the seconds
    entry and the subseconds entry. The functions performed by these four methods are
    very similar, so their procedures have been condensed down to a single method here
    and different parameters are passed depending on which mousewheel method was invoked."""

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
