#-*- coding: utf-8 -*-
"""This module contains helper methods for the TimeStamperTimer class
that do not directly rely on class variables of TimeStamperTimer."""

from fractions import Fraction
from tkinter import NORMAL, END

import classes

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


def attempt_media_player_release():
    """This method tries to release the current media player. If this method
    is unable to release the current media player, then nothing will happen."""

    try:
        classes.time_stamper.media_player.release()
    except (AttributeError, OSError):
        pass


def make_playback_button_images_visible():
    """This method makes the images for the play, rewind and fast-forward buttons visible."""

    for button_name, image_name in (("button_play", "play.png"), \
        ("button_rewind", "rewind.png"), ("button_fast_forward", "fast_forward.png")):

        classes.widgets[button_name].config(image=classes.widgets[image_name])
        classes.widgets[button_name].image = classes.widgets[image_name]


def get_new_multiplier(playback_type):
    """This method returns a value based on the argument playback_type. If playback_type is "play",
    this method will return 1.0. If playback_type is "rewind" or "fast_forward", this method will
    return a float based on the current value in the rewind or fast-forward spinboxes, respectively.
    If playback_type is not "play", "rewind" or "fast_forward", this method will raise an error."""

    # Set the multiplier based on the value of playback_type.
    if playback_type == "play":
        return 1.0

    if playback_type == "rewind":
        is_rewind, spinbox_str_key = True, "spinbox_rewind"
    elif playback_type == "fast_forward":
        is_rewind, spinbox_str_key = False, "spinbox_fast_forward"
    else:
        raise ValueError("Argument playback_type must be either",
                        "\"play\", \"rewind\" or \"fast_forward\".")

    spinbox_val = classes.widgets[spinbox_str_key].get()
    multiplier_str = classes.template[spinbox_str_key]["values"][spinbox_val]
    return float(Fraction(multiplier_str)) * (-1 if is_rewind else 1)


def determine_new_play_button_image(subseconds):
    """This method determines whether the current image of the play button should
    be changed, and if so, what it should be changed to. If it is determined that the
    image of the play button should not be changed, this method will return None."""

    button_play = classes.widgets["button_play"]
    button_default_image = classes.widgets["play.png"]
    button_blank_image = classes.widgets["blank.png"]

    # If we are on the 1st half of the current second, the image
    # of the play button should be set to its default image.
    if 0 <= subseconds < 50:
        return None if button_play.image == button_default_image else button_default_image

    # If we are on the 2nd half of the current second,
    # the image of play button should be blank.
    return None if button_play.image == button_blank_image else button_blank_image


def determine_new_rewind_button_image(multiplier, subseconds):
    """This method determines whether the current image of the rewind button should
    be changed, and if so, what it should be changed to. If it is determined that the
    image of the rewind button should not be changed, this method will return None."""

    rewind_button = classes.widgets["button_rewind"]
    button_half_image = classes.widgets["rewind_half.png"]
    button_default_image = classes.widgets["rewind.png"]
    button_blank_image = classes.widgets["blank.png"]

    # IF WE ARE REWINDING AT A SPEED SLOWER THAN 1X...
    if abs(multiplier) < 1.0:

        # If we are on the 3rd third of the current second, the image
        # of the rewind button should be set to its default image.
        if 67 <= subseconds < 100:
            return None if rewind_button.image == button_default_image else button_default_image

        # If we are on the 2nd third of the current second,
        # the image of rewind button should be blank.
        if 33 <= subseconds < 67:
            return None if rewind_button.image == button_blank_image else button_blank_image

        # If we are on the 1st third of the current second, the image of
        # the rewind button should depict half of what it normally depicts.
        return None if rewind_button.image == button_half_image else button_half_image

    # IF WE ARE REWINDING AT A SPEED FASTER THAN 1X...

    # If we are on the 2nd half of the current second, the image
    # of rewind button should be set to its default image.
    if 50 <= subseconds < 100:
        return None if rewind_button.image == button_default_image else button_default_image

    # If we are on the 1st half of the current second,
    # the image of rewind button should be blank.
    return None if rewind_button.image == button_blank_image else button_blank_image


def determine_new_fast_forward_button_image(multiplier, subseconds):
    """This method determines whether the current image of the fast-forward button should
    be changed, and if so, what it should be changed to. If it is determined that the
    image of the fast-forward button should not be changed, this method will return None."""

    button_fast_forward = classes.widgets["button_fast_forward"]
    button_half_image = classes.widgets["fast_forward_half.png"]
    button_default_image = classes.widgets["fast_forward.png"]
    button_blank_image = classes.widgets["blank.png"]

    # IF WE ARE "FAST"-FORWARDING AT A SPEED SLOWER THAN 1X...
    if abs(multiplier) < 1.0:

        # If we are on the 1st third of the current second, the image of
        # the fast-forward button should be set to its default image.
        if 0 <= subseconds < 33:
            return None if button_fast_forward.image == button_default_image \
                else button_default_image

        # If we are on the 2nd third of the current second,
        # the image of fast-forward button should be blank.
        if 33 <= subseconds < 67:
            return None if button_fast_forward.image == button_blank_image else button_blank_image

        # If we are on the 3rd third of the current second, the image of the
        # fast-forward button should depict half of what it normally depicts.
        return None if button_fast_forward.image == button_half_image else button_half_image

    # IF WE ARE FAST-FORWARDING AT A SPEED FASTER THAN 1X...

    # If we are on the 1st half of the current second, the image
    # of fast-forward button should be set to its default image.
    if 0 <= subseconds < 50:
        return None if button_fast_forward.image == button_default_image else button_default_image

    # If we are on the 2nd half of the current second,
    # the image of fast-forward button should be blank.
    return None if button_fast_forward.image == button_blank_image else button_blank_image


def pulse_button_image(subseconds, multiplier):
    """This method, which is called by the timer_tick method from the TimeStamperTimer
    class in timing.py, will potentially make the image of one of the media buttons
    visible/invisible depending on the reading of the timer. This provides visual feedback
    to the user about which timer function is currently executing (play, rewind or
    fast-forward) as well as the relative speed at which the timer is progressing."""

    # If the timer is moving at 1X SPEED (i.e., the play button was pressed),
    # we will potentially be manipulating the image of the play button.
    if multiplier == 1.0:
        button_to_edit = classes.widgets["button_play"]
        new_button_image = determine_new_play_button_image(subseconds)

    # If we are REWINDING, we will potentially be
    # manipulating the image of the rewind button.
    elif multiplier < 0.0:
        button_to_edit = classes.widgets["button_rewind"]
        new_button_image = determine_new_rewind_button_image(multiplier, subseconds)

    # If we are FAST-FORWARDING, we will potentially be
    # manipulating the image of the fast-forward button.
    else:
        button_to_edit = classes.widgets["button_fast_forward"]
        new_button_image = determine_new_fast_forward_button_image(multiplier, subseconds)

    # Update the image of the play/rewind/fast-forward button only
    # if its current image does not match the image it should have.
    if new_button_image is not None:
        button_to_edit.config(image=new_button_image)
        button_to_edit.image = new_button_image


def print_to_entry(to_print, entry_obj, wipe_clean=True):
    """This method prints the value stored in to_print to the entry widget entry_obj. An optional
    argument wipe_clean, which is set to True by default, determines whether any text currently
    displayed in the entry widget should be removed before the new text is displayed."""

    initial_state = entry_obj["state"]
    entry_obj["state"] = NORMAL
    if wipe_clean:
        entry_obj.delete(0, END)
    entry_obj.insert(END, to_print)
    entry_obj["state"] = initial_state


def pad_number(number, target_length, pad_before):
    """This method pads a number to target_length with leading zeros (if
    pad_before is set to True) or trailing zeros (if pad_before is set to False)."""

    str_number = str(number) if number else "0"
    zeros_to_add = "0" * (target_length - len(str_number))
    if pad_before:
        return zeros_to_add + str_number
    return str_number + zeros_to_add


def h_m_s_to_seconds(hours=0, minutes=0, seconds=0, subseconds=0):
    """This method converts a time in hours, minutes,
    seconds and subseconds to a time in seconds."""

    return (hours * 3600) + (minutes * 60) + seconds + (subseconds / 100)


def h_m_s_to_timestamp(hours=None, minutes=None, \
    seconds=None, subseconds=None, include_brackets=True):
    """This method converts a time in hours, minutes, seconds and subseconds to a timestamp. All
    arguments are optional. However, at the very least, seconds will always be included in the
    timestamp (and set to "00" if they were not provided). If the hours were provided, but not the
    minutes, then the minutes will be set to "00" and will also be included in the timestamp. This
    method DOES NOT pad or truncate any passed values or perform any check to determine whether the
    passed values are valid. It is therefore the responsibility of the function that calls this
    method to ensure that the values passed to this method (which would preferably be strings) are
    already formatted in the desired way. The optional argument include_brackets, which is set to
    True by default, determines whether the returned string will be enclosed in square brackets."""

    # If brackets were requested, add the opening bracket.
    timestamp = "[" if include_brackets else ""

    # If the hours were provided, include the hours.
    if hours:
        timestamp = f"{timestamp}{hours}:"

    # If the minutes should be included...
    if minutes or hours:

        # If the hours were included and the minutes should also be included...
        if hours:

            # If the hours AND the minutes were provided, add the minutes to the timestamp.
            if minutes:
                timestamp = f"{timestamp}{minutes}"

            # If the hours were provided, but NOT the minutes, set the
            # minutes to "00" and then add the minutes to the timestamp.
            else:
                minutes = "00"
                timestamp = f"{timestamp}00"

        # If the minutes, but NOT the hours, should be included, just add the minutes.
        else:
            timestamp = f"{timestamp}{minutes}"

    # If the minutes were included, add a colon before adding the seconds.
    if minutes:
        timestamp = f"{timestamp}:"

    # If the seconds were included, add the seconds to the timestamp. Otherwise, add "00" in place
    # of the seconds (seconds are the only thing that get included in the timestamp no matter what).
    timestamp = f"{timestamp}{seconds if seconds else '00'}"

    # If the subseconds were included, add the subseconds to the timestamp.
    if subseconds:
        timestamp = f"{timestamp}.{subseconds}"

    # If brackets were requested, add the closing bracket. Otherwise, add nothing.
    return f"{timestamp}]" if include_brackets else timestamp


def seconds_to_h_m_s(seconds_exact, pad=0, include_subseconds=True):
    """This method converts a time in seconds to a time in hours, minutes, seconds and
    subseconds. The optional integer argument pad, which is set to zero by default, provides
    the length to which the returned hours, minutes, seconds and subseconds should be padded."""

    # Convert the seconds to hours, minutes, seconds and subseconds.
    hours = int(seconds_exact // 3600)
    seconds_exact = round(seconds_exact - (hours * 3600), 2)
    minutes = int(seconds_exact // 60)
    seconds_exact = round(seconds_exact - (minutes * 60), 2)
    seconds = int(seconds_exact)
    if include_subseconds:
        seconds_exact = round((seconds_exact % 1) * 100, 0)
        subseconds = int(seconds_exact)

    # Pad the timer's values with zeros if a pad value is passed as an argument.
    if pad > 0:
        hours = pad_number(hours, pad, True)
        minutes = pad_number(minutes, pad, True)
        seconds = pad_number(seconds, pad, True)
        if include_subseconds:
            subseconds = pad_number(subseconds, pad, True)

    if include_subseconds:
        return [str(hours), str(minutes), str(seconds), str(subseconds)]

    return [str(hours), str(minutes), str(seconds)]


def seconds_to_timestamp(seconds, pad=0, force_include_hours=True, \
    include_subseconds=True, include_brackets=True):
    """This method converts a time in seconds to a timestamp with
    the following format: [hours:minutes:seconds:subseconds]"""

    # Convert the seconds into hours, minutes, seconds and (potentially) subseconds.
    h_m_s = seconds_to_h_m_s(seconds, pad=pad, include_subseconds=include_subseconds)

    # If the time is under one hour and it was specified that the
    # inclusion of hours should not be forced, omit the hours.
    if seconds < 3600 and not force_include_hours:
        h_m_s[0] = None

    # Convert the time to a timestamp and return it.
    return h_m_s_to_timestamp(*h_m_s, include_brackets=include_brackets)


def timestamp_to_h_m_s(timestamp, pad=0, pad_subseconds=False):
    """This method takes a timetsamp and converts it to a time in hours, minutes, seconds and
    subseconds. The returned value is a list of the form [hours, minutes, seconds, subseconds].
    Any of those four values which were not detected in the timestamp will be equal to None."""

    hours, minutes, seconds, subseconds = None, None, None, None

    # Split the provided timestamp.
    timestamp_split = timestamp.split(":")

    # Remove the first and last brackets if they exist.
    if timestamp_split[0] and timestamp_split[0][0] == "[":
        timestamp_split[0] = timestamp_split[0][1:]
    if timestamp_split[-1] and timestamp_split[-1][-1] == "]":
        timestamp_split[-1] = timestamp_split[-1][:-1]

    # If minutes were included in the timestamp...
    if len(timestamp_split) > 1:

        # If hours AND minutes were included in the timestamp...
        if len(timestamp_split) > 2:
            hours = timestamp_split[0] if timestamp_split[0] else None
            minutes = timestamp_split[1] if timestamp_split[1] else None

        # If minutes, but NOT hours, were included in the timestamp...
        else:
            minutes = timestamp_split[0] if timestamp_split[0] else None

    # If subseconds WERE included in the timestamp...
    seconds_split = timestamp_split[-1].split(".")
    if len(seconds_split) == 2:

        # Store the subseconds.
        subseconds = seconds_split[1] if seconds_split[1] else None

        # Update the split timestamp.
        timestamp_split[-1] = seconds_split[0]
        timestamp_split.append(seconds_split[1])

        # Pad the subseconds if necessary.
        if pad and pad_subseconds:
            subseconds = pad_number(subseconds, pad, False)

    # Store the seconds.
    seconds = seconds_split[0] if seconds_split[0] else None

    # Ensure that the timestamp contains only values that can be interpreted as numbers
    # and that those numbers are not longer than two characters long. If this is not the
    # case for any values in the timestamp, then this method will return None, as the
    # timestamp will not be convertible into hours, minutes, seconds and subseconds.
    for denom in timestamp_split:
        if len(denom) > 2:
            return None
        if denom != "":
            try:
                int(denom)
            except ValueError:
                return None

    # Pad all of the time values if padding was requested (besides subseconds, which
    # were padded earlier if it was determined that they should have been padded).
    if pad:
        hours = pad_number(hours, pad, True) if hours else hours
        minutes = pad_number(minutes, pad, True) if minutes else minutes
        seconds = pad_number(seconds, pad, True) if seconds else seconds

    return [hours, minutes, seconds, subseconds]
