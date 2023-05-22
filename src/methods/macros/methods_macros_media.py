#-*- coding: utf-8 -*-
"""This module stores some extra methods associated with media."""

from ctypes import cdll, c_char_p
from ntpath import sep as ntpath_sep
from posixpath import sep as posixpath_sep
from os import remove
from os.path import dirname, isfile, join
from sys import platform
from tkinter import DISABLED, NORMAL, END

from vlc import FILE_ptr, EventType, MediaParsedStatus, MediaPlayer

import classes
import methods.macros.methods_macros_helper as methods_helper
import methods.macros.methods_macros_output as methods_output

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


def updated_mute_button_image(volume_scale_value):
    """Assuming that the volume is not muted, this method returns the
    string corresponding to the PhotoImage object from widgets.mapping
    that best matches the current value of the volume slider."""

    # If the volume is at zero, return "volume_zero.png".
    if volume_scale_value == 0.0:
        return "volume_zero.png"

    # If the volume is between 0 and 33.3, return "volume_low.png".
    if 0 < volume_scale_value < 100 * (1 / 3):
        return "volume_low.png"

    # If the volume is between 33.3 and 66.6, return "volume_medium.png".
    if 100 * (1 / 3) <= volume_scale_value < 100 * (2 / 3):
        return "volume_medium.png"

    # If the volume is between 66.6 and 100 return "volume_high.png".
    return "volume_high.png"


def create_video_window(media_player):
    """This method creates a video window for
    media_player (an object of type vlc.MediaPlayer)."""

    # Destroy any video windows that have previously been created.
    if "window_video" in classes.widgets.mapping \
        and classes.widgets.mapping["window_video"].winfo_exists():
        classes.widgets["window_video"].destroy()

    # Create the video window.
    classes.widgets.create_entire_window("window_video")

    # Set the window for media_player to the newly created window.

    # TODO: set_hwnd likely needs to be replaced with
    # set_nsobject on Mac and set_xwindow on Linux.
    if platform.startswith("win"):
        media_player.set_hwnd(classes.widgets["window_video"].winfo_id())
    elif platform.startswith("darwin"):
        media_player.set_nsobject(classes.widgets["window_video"].winfo_id())
    else:
        media_player.set_xwindow(classes.widgets["window_video"].winfo_id())

    media_player.set_fullscreen(False)
    media_player.video_set_scale(0)


def toggle_media_buttons(to_enable):
    """This method toggles the media buttons and the media select
    button (enables if to_enable is True, disables otherwise)."""

    button_strs = ("button_pause", "button_play", "button_rewind", "button_fast_forward", \
        "button_skip_backward", "button_skip_forward", "button_media_select")
    if to_enable:
        for button_str_key in button_strs:

            original_color = classes.widgets.original_colors[button_str_key] \
                if button_str_key in classes.widgets.original_colors else None

            methods_helper.enable_button(classes.widgets[button_str_key], original_color)

    else:
        for button_str_key in button_strs:

            methods_helper.disable_button(classes.widgets[button_str_key], \
                classes.template[button_str_key]["mac_disabled_color"])


def set_media_widgets(file_full_path):
    """This method alters all of the relevant widgets in the Time Stamper program to
    indicate that a valid media file IS currently active. Note that this method does
    not handle the actual enabling/disabling of widgets associated with a media file."""

    # Change the text of the label that appears above the file
    # path entry widget to indicate that a file has been selected.
    if isinstance(classes.template["label_media_path"]["text"], dict):

        classes.widgets["label_media_path"]["text"] = \
            classes.template["label_media_path"]["text"]["value_if_true"]

    # Change the file path to the Windows format if we are on a Windows computer.
    if platform.startswith("win"):
        file_full_path = file_full_path.replace(posixpath_sep, ntpath_sep)

    # Print the file path to the entry widget.
    methods_output.print_to_entry(\
        file_full_path, classes.widgets["entry_media_path"], wipe_clean=True)

    # Make the range of the media slider equal to the minimum
    # of 359999.99 and the duration of the media player.
    classes.widgets["scale_media_time"]["to"] = classes.timer.get_max_time()

    # Reset the timer and the media slider.
    classes.timer.display_time(0.0, pad=2)


def reset_media_widgets():
    """This method alters all of the relevant widgets in the Time Stamper program to
    indicate that a valid media file IS NOT currently active. Note that this method does
    not handle the actual enabling/disabling of widgets associated with a media file."""

    entry_media_path = classes.widgets["entry_media_path"]

    # Clear the entry displaying the media path.
    entry_media_path["state"] = NORMAL
    entry_media_path.delete(0, END)
    entry_media_path["state"] = DISABLED

    # Reset the media slider.
    scale_media_time = classes.widgets["scale_media_time"]
    scale_media_time.variable.set(classes.template["scale_media_time"]["initial_value"])

    # Reset the volume slider.
    scale_media_volume = classes.widgets["scale_media_volume"]
    scale_media_volume.variable.set(100 - float(classes.template["label_media_volume"]["text"]))

    # Reset the volume label.
    classes.widgets["label_media_volume"]["text"] = classes.template["label_media_volume"]["text"]

    # Reset the elapsed/remaining time labels.
    classes.widgets["label_media_elapsed"]["text"] = classes.template["label_media_elapsed"]["text"]
    classes.widgets["label_media_remaining"]["text"] = \
        classes.template["label_media_remaining"]["text"]

    # Reset the mute button image.
    button_mute = classes.widgets["button_mute"]
    button_mute_image_new = classes.widgets["volume_high.png"]
    button_mute.config(image=button_mute_image_new)
    button_mute.image = button_mute_image_new


def final_media_handler(file_full_path, media_player):
    """This is the final method involved in the media file validation procedure. This method
    enables and configures all widgets relevant to media playback. If this method determines
    that the selected media file is not a video file, it will destroy the video window."""

    # Re-enable all media widgets which were temporarily disabled during media file validation.
    toggle_media_buttons(True)

    # Save the MediaPlayer as an attribute of the TimeStamper class.
    classes.time_stamper.media_player = media_player

    # Configure and enable the widgets associated with media.
    set_media_widgets(file_full_path)
    methods_helper.toggle_widgets(classes.template["button_media_select"], True)

    # If the selected media file is not a video, destroy the video window if it exists.
    if not media_player.has_vout() and ("window_video" in classes.widgets.mapping \
        and classes.widgets.mapping["window_video"].winfo_exists()):

        classes.widgets["window_video"].destroy()

    # Close the logfile.
    instance = media_player.get_instance()
    instance.log_unset()
    cdll.msvcrt.fclose(classes.time_stamper.log_file)


def second_post_playing_handler(file_full_path, media_player):
    """This method gets executed once the selected media has both been completely
    verified as valid and has been playing for approximately one millisecond."""

    # Pause the media.
    media_player.set_pause(True)

    # Reset the media back to its start time.
    media_player.set_time(0)

    # Wait for a longer period, after which the program will be able
    # to confirm whether the media has any video output streams.
    classes.time_stamper.root.after(500, final_media_handler, file_full_path, media_player)


def second_post_parsing_handler( _, file_full_path, media_player):
    """This method gets executed once VLC has both verified that the selected
    media file is valid for playback and finished parsing the media source."""

    # Play the media.
    media_player.play()

    # Allow the media to play for a very brief period (~1 millisecond) before proceeding.
    classes.time_stamper.root.after(1, second_post_playing_handler, file_full_path, media_player)


def first_post_playing_handler(_, file_full_path, media_player, iteration):
    """If VLC has successfully parsed the selected media file, then this
    method will get executed once the state of the media player switches
    to vlc.State.Playing. This method will then examine the libvlc logfiles
    to determine whether the selected file is valid for playback in VLC."""

    # Pause the media player.
    media_player.set_pause(True)

    # If this method is being called for the first time on the selected media file, we should
    # run through the validation procedure again to give the program more time to fill out the
    # logfile, as the text we are looking for in the logfile has likely not yet been printed.
    if iteration == 1:

        validate_media_player(file_full_path, iteration=2)

    # If this method is being called for the second time on the selected
    # media file, we should scan the logfile to ensure that no error messages
    # were recorded that indicate this file is not suitable for VLC playback.
    else:

        # Scan the log file for a message about VLC not
        # being able to identify the audio/video codec.
        bad_codec = False
        with open(join(dirname(classes.settings.user_json_path), \
            "out.log"), "r", encoding="utf-8") as log_file:

            lines = log_file.readlines()
            for line in lines:
                if line == "VLC could not identify the audio or video codec\n":
                    bad_codec = True
                    break

        # If a message about VLC not being able to identify the audio/video codec
        # WAS found in the log file, then this file IS NOT valid for playback by
        # VLC, so we should NOT enable the widgets associated with media playback.
        if bad_codec:

            # Destroy the video window if it exists.
            if "window_video" in classes.widgets.mapping \
                and classes.widgets.mapping["window_video"].winfo_exists():

                classes.widgets["window_video"].destroy()

            # Re-enable the media buttons, which had been
            # disabled for the duration of media file validation.
            toggle_media_buttons(True)

            # Close the logfile.
            instance = media_player.get_instance()
            instance.log_unset()
            cdll.msvcrt.fclose(classes.time_stamper.log_file)

        # If a message about VLC not being able to identify the audio/video codec
        # WAS NOT found in the log file, then this file IS valid for playback by
        # VLC, so we should change the configuration of the program to reflect this.
        else:

            # Reinitialize a MediaPlayer now that we know our media file is valid.
            media_player = MediaPlayer(file_full_path)
            create_video_window(media_player)
            media = media_player.get_media()
            events = media.event_manager()

            # Set the program to configure and enable/disable the relevant widgets to reflect
            # that a valid output file IS active once the media has finished parsing.
            events.event_attach(EventType.MediaParsedChanged, \
                second_post_parsing_handler, file_full_path, media_player)

            # Parse the media.
            media.parse_with_options(1, -1)


def first_post_parsing_handler(_, file_full_path, media_player, iteration):
    """This method gets executed when VLC's parsing of the selected media
    file has terminated. If the parsing was successful, the program will then
    try to play the media. If the parsing was unsuccessful, the program will
    change its configuration to reflect that a valid media file IS NOT active."""

    # If a parsed media file WAS generated...
    if media_player.get_media().get_parsed_status() == MediaParsedStatus.done:

        # Attach an event handler for when the media starts playing.
        events = media_player.event_manager()
        events.event_attach(EventType.MediaPlayerPlaying, \
            first_post_playing_handler, file_full_path, media_player, iteration)

        # Play the media.
        media_player.play()

    # If a parsed media file WAS NOT generated...
    else:

        # Only re-enable the media buttons, which had been
        # disabled for the duration of media file validation.
        toggle_media_buttons(True)

        # Close the logfile.
        instance = media_player.get_instance()
        instance.log_unset()
        cdll.msvcrt.fclose(classes.time_stamper.log_file)


def validate_media_player(file_full_path, iteration=1):
    """This method will try to create a media player based on the file path provided
    in file_full_path. If a media player was successfully created, then this method
    will configure the program to reflect that a media player IS active. Otherwise, this
    method will configure the program to reflect that a media player IS NOT active."""

    # Destroy the video window if it exists.
    if "window_video" in classes.widgets.mapping and \
        classes.widgets.mapping["window_video"].winfo_exists():

        classes.widgets["window_video"].destroy()

    if file_full_path:

        # Create a new media player using the selected media file.
        media_player = MediaPlayer(file_full_path)

        # Create a window for the media player (which will potentially
        # get destroyed later if it is discovered that the selected
        # media file is either invalid or does not contain any video).
        create_video_window(media_player)

        # Get the vlc.Media object associated with the new media player.
        media = media_player.get_media()

        # Get the event manager associated with the media.
        events = media.event_manager()

        if iteration == 1:

            # Temporarily reset and disable all media widgets while the program attempts
            # to validate the current media file (if the current media file cannot be
            # validated, only the media buttons will be re-enabled and the remaining
            # widgets that were disabled in this code block will NOT be re-enabled).
            toggle_media_buttons(False)
            classes.time_stamper.media_player = None
            reset_media_widgets()
            methods_helper.toggle_widgets(classes.template["button_media_select"], False)

            # Delete the logfile if it exists.
            log_file_path = join(dirname(classes.settings.user_json_path), "out.log")
            if isfile(log_file_path):
                remove(log_file_path)

            # Set libvlc to publish its log to a location which we can reference later.
            instance = media_player.get_instance()
            fopen = cdll.msvcrt.fopen
            fopen.restype = FILE_ptr
            fopen.argtypes = (c_char_p, c_char_p)
            classes.time_stamper.log_file = fopen(bytes(log_file_path, "utf-8"), b"w")
            instance.log_set_file(classes.time_stamper.log_file)

        # Set the program to execute first_post_parsing_handler
        # once VLC has finished parsing the selected media.
        events.event_attach(EventType.MediaParsedChanged, \
            first_post_parsing_handler, file_full_path, media_player, iteration)

        # Attempt to parse the selected media.
        media.parse_with_options(1, -1)

    # If no media file was selected, no media will be loaded.
    else:

        # Stop the Time Stamper program's media player if it exists.
        if isinstance(classes.time_stamper.media_player, MediaPlayer):
            classes.time_stamper.media_player.stop()

        # Erase the Time Stamper program's media player.
        classes.time_stamper.media_player = None

        # Reset and disable the widgets associated with media.
        reset_media_widgets()
        methods_helper.toggle_widgets(classes.template["button_media_select"], False)
