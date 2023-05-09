#-*- coding: utf-8 -*-
"""This module contains helper methods for the TimeStamperTimer class
that do not directly rely on class variables of TimeStamperTimer."""

from tkinter import NORMAL, END
from pyglet.media import load, Player
from pyglet.media.codecs.wave import WAVEDecodeException

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


def confirm_audio(audio_source, audio_player, entry_audio_path):
    """This method checks whether an audio player can be initialized with the
    current information provided in the Time Stamper program. If an audio player
    can be loaded, then a tuple containing the appropriate audio source and
    audio player is returned. Otherwise, the tuple (None, None) is returned."""

    # Return the audio player if it exists.
    if audio_player:
        return audio_source, audio_player

    # Retrieve the current text from the audio path Entry widget.
    audio_path = entry_audio_path.get()

    # If there is no audio player and also no audio path, return
    # None in place of both the audio source and the audio player.
    if not audio_path:
        return None, None

    # Try to load the audio source specified in the audio path entry.
    try:
        audio_source = load(audio_path)

    # If the audio source specified in the audio path entry was not successfully
    # loaded, return None in place of both the audio source and the audio player.
    except (FileNotFoundError, WAVEDecodeException):
        return None, None

    # If the audio source specified in the audio path entry was successfully
    # loaded, return the audio source and a freshly initialized audio player.
    return audio_source, Player()


def make_playback_button_images_visible(widgets):
    """This method makes the images for the play, rewind and fast-forward buttons visible."""

    for button_name, image_name in (("button_play", "play.png"), \
        ("button_rewind", "rewind.png"), ("button_fast_forward", "fast_forward.png")):
        widgets[button_name].config(image=widgets[image_name])
        widgets[button_name].image = widgets[image_name]


def pulse_button_image(internal_time, multiplier, widgets):
    """This method, which is called by the timer_tick method from the TimeStamperTimer
    class in timing.py, will potentially make the image of one of the media buttons
    visible/invisible depending on the reading of the timer. This provides visual feedback
    to the user about which timer function is currently executing (play, rewind or
    fast-forward) as well as the relative speed at which the timer is progressing."""

    # If the timer is moving at 1X SPEECD (i.e., the play button was pressed),
    # we will potentially be manipulating the image of the play button.
    if multiplier == 1.0:
        button_to_edit = widgets["button_play"]
        button_default_image = widgets["play.png"]

    # If we are REWINDING, we will potentially be
    # manipulating the image of the rewind button.
    elif multiplier < 0.0:
        button_to_edit = widgets["button_rewind"]
        button_default_image = widgets["rewind.png"]

    # If we are FAST-FORWARDING, we will potentially be
    # manipulating the image of the fast-forward button.
    else:
        button_to_edit = widgets["button_fast_forward"]
        button_default_image = widgets["fast_forward.png"]

    closest_second_lower = internal_time - int(internal_time) < 0.5
    button_blank_image = widgets["blank.png"]
    new_button_image = None

    # If the nearest second to the current time is LOWER than the current
    # time, make the image of the rewind/fast-forward button VISIBLE.
    if closest_second_lower and button_to_edit.image == button_blank_image:
        new_button_image = button_default_image

    # If the nearest second to the current time is HIGHER than the current
    # time, make the image of the rewind/fast-forward button INVISIBLE.
    elif not closest_second_lower \
        and button_to_edit.image == button_default_image:
        new_button_image = button_blank_image

    # Update the image of the rewind/fast-forward button only if
    # its current image does not match the image it should have.
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


def h_m_s_to_timestamp(hours, minutes, seconds, subseconds):
    """This method converts a time in hours, minutes, seconds and subseconds to a
    timestamp with the following format: [hours:minutes:seconds:subseconds]."""

    return f"[{hours}:{minutes}:{seconds}.{subseconds}]"


def h_m_s_to_seconds(hours, minutes, seconds, subseconds):
    """This method converts a time in hours, minutes,
    seconds and subseconds to a time in seconds."""

    return (hours * 3600) + (minutes * 60) + seconds + (subseconds / 100)


def seconds_to_h_m_s(seconds_exact, pad=0):
    """This method converts a time in seconds to a time in hours, minutes, seconds and
    subseconds. The optional integer argument pad, which is set to zero by default, provides
    the length to which the returned hours, minutes, seconds and subseconds should be padded."""

    # Convert the seconds to hours, minutes, seconds and subseconds.
    hours = int(seconds_exact // 3600)
    seconds_exact = round(seconds_exact - (hours * 3600), 2)
    minutes = int(seconds_exact // 60)
    seconds_exact = round(seconds_exact - (minutes * 60), 2)
    seconds = int(seconds_exact)
    seconds_exact = round((seconds_exact % 1) * 100, 0)
    subseconds = int(seconds_exact)

    # Pad the timer's values with zeros if a pad value is passed as an argument.
    if pad > 0:
        hours = pad_number(hours, pad, True)
        minutes = pad_number(minutes, pad, True)
        seconds = pad_number(seconds, pad, True)
        subseconds = pad_number(subseconds, pad, True)

    return str(hours), str(minutes), str(seconds), str(subseconds)
