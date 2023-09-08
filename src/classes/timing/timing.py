#-*- coding: utf-8 -*-
"""This module contains the TimeStamperTimer class which allows
for keeping track of time in the Time Stamper program."""

from math import ceil
from time import perf_counter
from vlc import State

import classes
import methods.timing.methods_timing_helper as methods_helper

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
    """This class runs a timer with pause, resume, rewind,
    fast-forward, skip backward and skip forward features."""

    def __init__(self):

        self.is_running = False
        self.temporary_pause = False
        self.start_time = 0.0
        self.offset = 0.0
        self.multiplier = 0.0

        self.scheduled_id = None

    def get_max_time(self):
        """This method returns the timer's current maximum time in seconds. Typically, the
        maximum time will be 359999.99 seconds unless a media player is loaded, in which case
        the maximum time will be the minimum of 359999.99 and the duration of the media player."""

        if classes.time_stamper.media_player:
            media = classes.time_stamper.media_player.get_media()
            return min(359999.99, round(media.get_duration() / 1000, 2))

        return 359999.99

    def read_timer(self, raw=False):
        """This method reads in and returns the current time from the time fields. This method
        takes one optional argument, raw, which is set to False by default. When raw is True,
        the returned values will be four strings representing the timer's current time in
        hours, minutes, seconds and subseconds (padded with 0's if necessary). When raw is
        False, the returned values will be the same as the values that are returned when
        raw is True, but the values will be converted to integers before being returned."""

        # Get the current values from the timer's time fields.
        hours = classes.widgets["entry_hours"].get()
        minutes = classes.widgets["entry_minutes"].get()
        seconds = classes.widgets["entry_seconds"].get()
        subseconds = classes.widgets["entry_subseconds"].get()

        # The timer's values may need to be padded if they contain user-entered numbers.
        hours = methods_helper.pad_number(hours, 2, True)
        minutes = methods_helper.pad_number(minutes, 2, True)
        seconds = methods_helper.pad_number(seconds, 2, True)
        subseconds = methods_helper.pad_number(subseconds, 2, False)

        # If raw is True, return the time from the time fields as it should appear on the timer.
        if raw:
            return [hours, minutes, seconds, subseconds]

        # If raw is False, convert the numbers from the
        # time fields to integers before returning them.
        return [int(hours), int(minutes), int(seconds), int(subseconds)]

    def get_current_seconds(self):
        """This method returns the timer's current time in seconds."""

        return methods_helper.h_m_s_to_seconds(*self.read_timer())

    def current_time_to_timestamp(self, force_include_hours=True, \
        round_to="centisecond", include_brackets=True):
        """This method converts the currently diplayed time to a timestamp."""

        # Get the timer reading from the time fields.
        h_m_s = self.read_timer(raw=True)

        # Exclude the hours if the time is less than one hour and force_include_hours is False.
        if int(h_m_s[0]) < 1 and not force_include_hours:
            h_m_s[0] = None

        # Round the timestamp to the specified increment.
        if round_to == "decisecond":
            h_m_s[3] = str(int(h_m_s[3]) // 10)
        elif round_to == "second":
            h_m_s[3] = None
        elif round_to != "centisecond":
            raise ValueError("Argument round_to must be either",
                            "\"second\", \"decisecond\" or \"centisecond\".")

        return methods_helper.h_m_s_to_timestamp(*h_m_s, include_brackets=include_brackets)

    def display_time(self, new_time, pad=2):
        """This method, after converting the provided time in seconds to hours, minutes,
        seconds and subseconds, will display this time to timer fields of self.time_stamper."""

        # Determine whether hours should be forced to be included in the timestamp.
        force_timestamp_hours = classes.settings["always_include_hours_in_timestamp"]["is_enabled"]

        # Convert the provided time in seconds to hours, minutes, seconds and subseconds.
        h_m_s = methods_helper.seconds_to_h_m_s(new_time, pad=pad)

        # Print the hours, minutes, seconds and subseconds to their relevant Tkinter entries.
        for i, time_field in enumerate(("hours", "minutes", "seconds", "subseconds")):

            current_timer_entry = classes.widgets[f"entry_{time_field}"]

            # Only update the value in the timer entry if the
            # updated value is not equal to the current value.
            if h_m_s[i] != current_timer_entry.get():
                methods_helper.print_to_entry(h_m_s[i], current_timer_entry)

        # Omit the hours from the timestamp if the time is less than one hour and the user
        # set hours to be omitted from the timestamp when the time is less than one hour.
        if new_time < 3600 and not force_timestamp_hours:
            h_m_s[0] = None

        # For the timestamp, either round down the subseconds, omit the subseconds or leave
        # the subseconds unaltered depending on what the user specified in the settings.
        timestamp_rounding = classes.settings["round_timestamp"]["round_to_last"]
        if timestamp_rounding == "decisecond":
            h_m_s[3] = str(int(h_m_s[3]) % 10)
        elif timestamp_rounding == "second":
            h_m_s[3] = None

        # If a timestamp has not been set, make the timestamp label reflect the current time.
        if not classes.template["label_timestamp"]["timestamp_set"]:

            obj_timestamp = classes.widgets["label_timestamp"]
            obj_timestamp["text"] = methods_helper.h_m_s_to_timestamp(*h_m_s)

        # If a media player exists, update the position of the media time
        # slider as well as the displays of elapsed and remaining time.
        if classes.time_stamper.media_player:

            # Update the start time of the media if it is not playing.
            if not classes.time_stamper.media_player.is_playing():
                classes.time_stamper.media_player.set_time(int(new_time * 1000))

            # Update the media time slider.
            classes.widgets["scale_media_time"].variable.set(new_time)

            # Update the elapsed time.
            media_elapsed_to_timestamp = \
                methods_helper.h_m_s_to_timestamp(*h_m_s[:3], include_brackets=False)
            classes.widgets["label_media_elapsed"]["text"] = media_elapsed_to_timestamp

            # Update the remaining time.
            media_seconds_remaining = max(0.0, self.get_max_time() - new_time)
            media_remaining_to_timestamp = methods_helper.seconds_to_timestamp(\
                media_seconds_remaining, pad=pad, force_include_hours=force_timestamp_hours, \
                include_subseconds=False, include_brackets=False)
            classes.widgets["label_media_remaining"]["text"] = media_remaining_to_timestamp

    def update_media(self, new_time):
        """This method adjusts the start time of the current media
        player to new_time and then plays that media player."""

        if self.is_running:

            # Pause the media player.
            classes.time_stamper.media_player.set_pause(True)

            # If the current media player has not played before or the
            # current media player has ended, adjust the media start time.
            if classes.time_stamper.media_player.get_time() == -1 \
                or classes.time_stamper.media_player.get_state() == State.Ended:

                media = classes.time_stamper.media_player.get_media()
                media.add_option(f"start-time={new_time}")
                classes.time_stamper.media_player.set_media(media)

            # If the current media player has played before and has
            # not ended, adjust the media player using set_time.
            else:
                classes.time_stamper.media_player.set_time(int(new_time * 1000))

            # If the volume is currently muted, set the media player's volume to zero.
            if classes.widgets["button_mute"].image == classes.widgets["volume_mute.png"]:
                classes.time_stamper.media_player.audio_set_volume(0)

            # If the volume is not currently muted, set the media
            # player's volume to the value of the volume slider.
            else:
                new_vol = int(100 - classes.widgets["scale_media_volume"].variable.get())
                classes.time_stamper.media_player.audio_set_volume(new_vol)

            # Play the media.
            classes.time_stamper.media_player.play()

    def update_timer(self, new_time):
        """This method updates the timer to the new time passed
        in new_time (which should be a time in seconds)."""

        # Find the time we are adjusting FROM.
        prev_time = self.get_current_seconds()

        # Set the new offset.
        self.offset += (new_time - prev_time)

        # Display the new time.
        self.display_time(new_time, pad=2)

        # Play the current media file if one is loaded.
        if classes.time_stamper.media_player:
            self.update_media(new_time)

    def timer_tick(self, prev_multiplier):
        """This method runs continuously while the timer is running to update the current time."""

        # Only tick the timer if it is currently running.
        if self.is_running and self.multiplier != 0.0:

            internal_time = self.offset + ((perf_counter() - self.start_time) * self.multiplier)

            # Only tick the timer if its current time is less than the maximum time.
            if internal_time < self.get_max_time() or self.multiplier < 0.0:

                # Only tick the timer if the precise internal time
                # is greater than 0 or if a media file is loaded.
                media_playing = classes.time_stamper.media_player \
                    and classes.time_stamper.media_player.is_playing()

                if internal_time > 0.0 or media_playing:

                    # Display the updated time.
                    self.display_time(internal_time, pad=2)

                    # Potentially, make the image of either the play, rewind
                    # or fast-forward button either visible or invisible.
                    subseconds = int(classes.widgets["entry_subseconds"].get())
                    methods_helper.pulse_button_image(subseconds, self.multiplier)

                    # Calculate the number of seconds to the next centisecond.
                    next_centisecond = \
                        (int(internal_time * 100) + int(self.multiplier > 0.0)) / 100
                    seconds_to_next_tick = abs(next_centisecond - internal_time)

                    # Convert the number of seconds to the next centisecond
                    # the number of milliseconds to the next centisecond.
                    milliseconds_to_next_tick = max(seconds_to_next_tick, .001) * 1000

                    # Consider the time dilation from rewinding/fast-forwarding when
                    # calculating the number of milliseconds to the next centisecond.
                    milliseconds_to_next_tick = \
                        ceil(milliseconds_to_next_tick * abs(1 / self.multiplier))

                    # After the next centisecond has elapsed, tick the timer again.
                    if self.multiplier == prev_multiplier:
                        classes.time_stamper.root.after(\
                            milliseconds_to_next_tick, self.timer_tick, self.multiplier)

                # If the timer's currently displayed time is greater than 0, pause the timer.
                else:

                    self.display_time(0.0, pad=2)
                    classes.macros.mapping["button_pause"]()

            # If the timer's currently displayed time is not less
            # than the maximum displayable time, pause the timer.
            else:
                self.display_time(self.get_max_time(), pad=2)
                classes.macros.mapping["button_pause"]()

    def pause(self, play_delay=None):
        """This method halts the timer and is typically run when the pause button is
        pressed, when the media time slider is dragged/scrolled and media is playing
        or when the timer entries are scrolled. An optional argument, play_delay (which
        is set to None by default), determines the amount of time after which the timer
        should resume once it is paused. This argument should only ever be set to a value
        other than None from the scale_media_time_macro and adjust_timer_on_entry_mousewheel
        methods in widgets_helper_methods.py (i.e., whenever the user manipulates the
        media time scale or timer entries). Note that play_delay only has an effect if
        this method is called when the timer is already running or is scheduled to run."""

        # Only pause the timer if it is currently running/scheduled to run.
        if self.is_running or self.scheduled_id:

            # If a play delay was provided, initiate a temporary pause.
            if play_delay:

                # Record that the timer is only being paused temporarily.
                self.temporary_pause = True

                # If there is an existing scheduled play function, then it should be
                # cancelled, as this effectively means that the user was previously scrolling
                # the media slider or timer entries but has not yet finished editing the time.
                if self.scheduled_id:
                    classes.time_stamper.root.after_cancel(self.scheduled_id)

                # If a positive play delay was provided, schedule
                # the timer to play after the play delay.
                if play_delay > 0:
                    self.scheduled_id = \
                        classes.time_stamper.root.after(int(play_delay * 1000), self.play, "prev")

                # If a positive play delay was not provided, this effectively means
                # that the user edited the media time scale by clicking on it instead of
                # scrolling it, so instead of scheduling the timer to play, keep the timer
                # paused until the user releases the mouse button from the media time scale.
                else:
                    self.scheduled_id = None

            # If no play delay was provided, the timer should stay paused
            # until the user performs an action that resumes the timer
            # (i.e., pressing the play, rewind or fast-forward button).
            else:
                self.multiplier = 0.0

            # Declare the timer as not running.
            self.is_running = False

            # The images for the play, rewind and fast-forward buttons
            # should no longer be invisible if any of them currently are.
            methods_helper.make_playback_button_images_visible()

            # Pause the media if it exists.
            if classes.time_stamper.media_player:
                classes.time_stamper.media_player.set_pause(True)

    def play(self, playback_type="play"):
        """This method starts the timer and is typically run when the play, rewind or
        fast-forward buttons are pressed. An optional argument, playback_type (which is
        set to "play" by default), determines the speed of the timer. If playback_type is
        set to "play", the timer's multiplier will be set to 1.0. If playback_type is set
        to "rewind" or "fast_forward", the timer's multiplier will be determined by the
        current value in the rewind or fast-forward spinboxes, respectively. If playback_type
        is set to "prev", the timer's multiplier will not be altered from its current value."""

        self.scheduled_id = None
        self.temporary_pause = False

        # Determine the new multiplier.
        if playback_type == "prev":
            new_multiplier = self.multiplier
        else:
            new_multiplier = methods_helper.get_new_multiplier(playback_type)

        # Only play the timer if it is not already running
        # at the speed we would like to set it to.
        if not self.is_running or new_multiplier != self.multiplier:

            # Pause the timer if it is currently running.
            self.pause()

            # Declare the timer as running.
            self.is_running = True

            # Set the new multiplier.
            self.multiplier = new_multiplier

            # The images for the play, rewind and fast-forward buttons
            # should no longer be invisible if any of them currently are.
            methods_helper.make_playback_button_images_visible()

            # Get the timer's current time in seconds.
            current_time_seconds = self.get_current_seconds()

            # Play the current media file if one is loaded and we are not rewinding.
            if classes.time_stamper.media_player and new_multiplier > 0.0:
                classes.time_stamper.media_player.set_rate(new_multiplier)
                self.update_media(current_time_seconds)

            # Save the current raw time.
            self.start_time = perf_counter()

            # Factor the current reading on the timer into the
            # offset for the calculation of the running time.
            self.offset = current_time_seconds

            # Begin ticking the timer.
            self.timer_tick(self.multiplier)

        # Return the rate at which the timer is now playing.
        return new_multiplier


    def adjust_timer(self, seconds_to_adjust_by, abort_if_out_of_bounds=False):
        """This method skips the timer backward and forward and is typically run when
        the skip backward or skip forward button is pressed or when the user scrolls
        the mousewheel while the cursor is hovering over one of the timer entries. This
        method takes one optional argument, abort_if_out_of_bounds, which is set to False
        by default. When abort_if_out_of_bounds is set to True, this method will not adjust
        the timer if the passed adjustment amount would put the timer below 0 or above the
        maximum time (as can be the case when the user scrolls the timer entries with the
        mousewheel). When abort_if_out_of_bounds is set to False, this method will reduce
        the passed adjustment amount to put the timer at either 0 or its maximum time if the
        passed adjustment amount would have otherwise put the timer below 0 or above its maximum
        time (as is the case when the user presses the skip backward or skip forward buttons)."""

        if seconds_to_adjust_by != 0:

            current_time_seconds = self.get_current_seconds()

            # If the requested adjustment WOULD BRING the
            # timer below the minimum time (00h 00m 00.00s)...
            if current_time_seconds + seconds_to_adjust_by < 0:

                # If abort_if_out_of_bounds is True, we should not adjust the timer.
                if abort_if_out_of_bounds:
                    return 0

                # If abort_if_out_of_bounds is False, reduce the
                # adjustment so that it brings the timer to 0.
                seconds_to_adjust_by = -current_time_seconds

            # If the requested adjustment WOULD NOT BRING the
            # timer below the minimum time (00h 00m 00.00s)...
            else:

                # IF the requested adjustment WOULD BRING the timer OVER the maximum time...
                if current_time_seconds + seconds_to_adjust_by > self.get_max_time():

                    # If abort_if_out_of_bounds is True, we should not adjust the timer.
                    if abort_if_out_of_bounds:
                        return 0

                    # If abort_if_out_of_bounds is False, reduce the adjustment
                    # amount so that it brings the timer TO the maximum time
                    seconds_to_adjust_by = self.get_max_time() - current_time_seconds

            # Update the timer's time.
            current_time_seconds += seconds_to_adjust_by
            self.update_timer(current_time_seconds)

        return seconds_to_adjust_by
