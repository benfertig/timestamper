#-*- coding: utf-8 -*-
"""This module contains the Macros class which serves as a container for all methods
that are executed when any button, checkbutton, or scale in the Time Stamper program is
manipulated. The actual macros are stored in submodules (all of which are imported below)."""

from dataclasses import dataclass
from ntpath import sep as ntpath_sep
from posixpath import sep as posixpath_sep
from sys import platform
from tkinter import DISABLED, NORMAL, END
from vlc import  MediaPlayer
from .macros_checkbuttons import CheckbuttonMacros
from .macros_entries import EntryMacros
from .macros_scales import ScaleMacros
from .macros_spinboxes import SpinboxMacros
from .macros_buttons_file import FileButtonMacros
from .macros_buttons_info import InfoButtonMacros
from .macros_buttons_media import MediaButtonMacros
from .macros_buttons_note import NoteButtonMacros
from .macros_buttons_settings import SettingsButtonMacros
from .macros_buttons_timestamping import TimestampingButtonMacros
from .macros_helper_methods import toggle_widgets, print_to_entry, \
    print_to_text, print_to_file, copy_text_file_to_text_widget

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


@dataclass
class Macros():
    """This class is a container class for all of the button macros in the Time Stamper program.
    The macro for any button can be accessed through the Macros.mapping attribute. For
    example, to access the pause button's macro, reference Macros.mapping["button_pause"]."""

    def __getitem__(self, item):
        return self.mapping[item]

    def __init__(self, time_stamper):

        self.time_stamper = time_stamper
        self.template = time_stamper.template
        self.settings = time_stamper.settings
        self.widgets = time_stamper.widgets
        self.timer = time_stamper.timer

        check = CheckbuttonMacros(self)
        entries = EntryMacros(self)
        scales = ScaleMacros(self)
        spinboxes = SpinboxMacros(self)

        file = FileButtonMacros(self)
        info = InfoButtonMacros(self)
        media = MediaButtonMacros(self)
        note = NoteButtonMacros(self)
        settings = SettingsButtonMacros(self)
        timestamping = TimestampingButtonMacros(self)

        # Map the widgets to their macros.
        self.mapping = {

            # Checkbuttons
            "checkbutton_pause_settings": check.checkbutton_pause_settings_macro,
            "checkbutton_play_settings": check.checkbutton_play_settings_macro,
            "checkbutton_skip_backward_settings": check.checkbutton_skip_backward_settings_macro,
            "checkbutton_skip_forward_settings": check.checkbutton_skip_forward_settings_macro,

            # Entries
            "entry_hours_TRACE": entries.entry_hours_trace,
            "entry_minutes_TRACE": entries.entry_minutes_trace,
            "entry_seconds_TRACE": entries.entry_seconds_trace,
            "entry_subseconds_TRACE": entries.entry_subseconds_trace,
            "entry_skip_backward_TRACE": entries.entry_skip_backward_trace,
            "entry_skip_forward_TRACE": entries.entry_skip_forward_trace,
            "entry_pause_settings_TRACE": entries.entry_pause_settings_trace,
            "entry_play_settings_TRACE": entries.entry_play_settings_trace,
            "entry_skip_backward_settings_TRACE": entries.entry_skip_backward_settings_trace,
            "entry_skip_forward_settings_TRACE": entries.entry_skip_forward_settings_trace,
            "entry_hotkey_1_settings_TRACE": entries.entry_hotkey_1_settings_trace,
            "entry_hotkey_2_settings_TRACE": entries.entry_hotkey_2_settings_trace,
            "entry_hotkey_3_settings_TRACE": entries.entry_hotkey_3_settings_trace,
            "entry_hours_ONMOUSEWHEEL": entries.entry_hours_mousewheel_macro,
            "entry_minutes_ONMOUSEWHEEL": entries.entry_minutes_mousewheel_macro,
            "entry_seconds_ONMOUSEWHEEL": entries.entry_seconds_mousewheel_macro,
            "entry_subseconds_ONMOUSEWHEEL": entries.entry_subseconds_mousewheel_macro,

            # Scales
            "scale_media_time": scales.scale_media_time_macro,
            "scale_media_time_ONRELEASE": scales.scale_media_time_release_macro,
            "scale_media_time_ONMOUSEWHEEL": scales.scale_media_time_mousewheel_macro,
            "scale_media_volume": scales.scale_media_volume_macro,
            "scale_media_volume_ONMOUSEWHEEL": scales.scale_media_volume_mousewheel_macro,

            # Spinboxes
            "spinbox_rewind": spinboxes.spinbox_rewind_macro,
            "spinbox_fast_forward": spinboxes.spinbox_fast_forward_macro,

            # File buttons
            "button_output_select": file.button_output_select_macro,
            "button_merge_output_files": file.button_merge_output_files_macro,
            "button_media_select": file.button_media_select_macro,

            # Info buttons
            "button_help": info.button_help_macro,
            "button_help_left_arrow": info.button_help_left_arrow_macro,
            "button_help_right_arrow": info.button_help_right_arrow_macro,
            "button_license": info.button_license_macro,
            "button_attribution": info.button_attribution_macro,

            # Media buttons
            "button_pause": media.button_pause_macro,
            "button_play": media.button_play_press_macro,
            "button_play_ONRELEASE": media.button_play_release_macro,
            "button_rewind": media.button_rewind_press_macro,
            "button_rewind_ONRELEASE": media.button_rewind_release_macro,
            "button_fast_forward": media.button_fast_forward_press_macro,
            "button_fast_forward_ONRELEASE": media.button_fast_forward_release_macro,
            "button_skip_backward": media.button_skip_backward_macro,
            "button_skip_forward": media.button_skip_forward_macro,
            "button_mute": media.button_mute_macro,

            # Note buttons
            "button_hotkey_1": note.button_hotkey_1_macro,
            "button_hotkey_2": note.button_hotkey_2_macro,
            "button_hotkey_3": note.button_hotkey_3_macro,
            "button_cancel_note": note.button_cancel_note_macro,
            "button_save_note": note.button_save_note_macro,

            # Settings buttons
            "button_settings": settings.button_settings_macro,
            "button_reset_to_default": settings.button_reset_to_default_macro,
            "button_cancel_changes": settings.button_cancel_changes_macro,
            "button_save_settings": settings.button_save_settings_macro,

            # Timestamping buttons
            "button_timestamp": timestamping.button_timestamp_macro,
            "button_clear_timestamp": timestamping.button_clear_timestamp_macro

        }

    def print_timestamped_message(self, message, timestamp=None):
        """This method takes a message, timestamps it, and then prints that timestamped
        message to the notes log and the output file (if no timestamp is provided,
        then a timestamp will be generated using the timer's current time)."""

        # Get the current output path from the output path entry widget.
        output_path = self.widgets["entry_output_path"].get()

        # If no timestamp was provided, set the timestamp to the timer's current time.
        if timestamp is None:
            timestamp = self.timer.current_time_to_timestamp()

        # Generate the complete message that should be printed, including the timestamp.
        to_print = f"{timestamp} {message}"

        # Print the message passed in the argument "message" along with
        # the current timestamp to the notes log and the output file.
        print_to_text(to_print, self.widgets["text_log"])
        print_to_file(to_print, output_path, self.settings["output"]["file_encoding"])

    def get_button_message_input(self, button_str_key):
        """This method, which is called upon by several button macros, uses a button's
        template to determine whether a message should be printed when the button is pressed.
        If this method determines that a message should be printed when the button is pressed,
        then this method will return that message. Otherwise, this method will return None.
        Keep in mind that this method does not substitute potential variables (e.g., $amount
        and $dest for the skip backward and skip forward messages) in the returned message. Any
        variable substitution will need to be performed on the string returned by this method."""

        button_template = self.template[button_str_key]

        # Determine whether a potential message exists for this button.
        if "print_on_press" in button_template:

            should_print = True
            print_on_press_val = button_template["print_on_press"]

            # If the text that gets printed when this button is
            # pressed is based on attributes stored elsewhere.
            if isinstance(print_on_press_val, dict):

                print_on_press_dict = print_on_press_val
                linked_dict_str = print_on_press_dict["linked_dict"]

                # Determine whether this button's message information
                # is stored in the settings or in the template.
                if linked_dict_str in self.settings.user:
                    linked_dict = self.settings[linked_dict_str]
                else:
                    linked_dict = self.template[linked_dict_str]

                # Determine the button's message.
                print_message_key = print_on_press_dict["print_message_attribute"]
                print_on_press_val = linked_dict[print_message_key]

                # Determine whether the button's associated message should be printed.
                if "print_bool_attribute" in print_on_press_dict:
                    print_bool_key = print_on_press_dict["print_bool_attribute"]
                    should_print = linked_dict[print_bool_key]

            # If it is determined that this button's message should be printed, return its message.
            if should_print:
                return print_on_press_val

        # If it was determined that nothing should be
        # printed when this button is pressed, return None.
        return None

    def set_output_widgets(self, file_full_path):
        """This method alters all of the relevant widgets in the Time Stamper program to
        indicate that a valid output file IS currently active. Note that this method does
        not handle the actual enabling/disabling of widgets associated with an output file."""

        # Change the text of the label that appears above the file
        # path entry widget to indicate that a file has been selected.
        if isinstance(self.template["label_output_path"]["text"], dict):
            self.widgets["label_output_path"]["text"] = \
                self.template["label_output_path"]["text"]["value_if_true"]

        # Change the file path to the Windows format if we are on a Windows computer.
        if platform.startswith("win"):
            file_full_path = file_full_path.replace(posixpath_sep, ntpath_sep)

        # Print the file path to the entry widget.
        print_to_entry(file_full_path, self.widgets["entry_output_path"], wipe_clean=True)

        # Any text already in the output file should be printed to the notes log.
        file_encoding = self.settings["output"]["file_encoding"]
        copy_text_file_to_text_widget(file_full_path, file_encoding, self.widgets["text_log"])

    def reset_output_widgets(self):
        """This method alters all of the relevant widgets in the Time Stamper program to
        indicate that a valid output file IS NOT currently active. Note that this method does
        not handle the actual enabling/disabling of widgets associated with an output file."""

        # Set the text of the label that displays above the output path entry widget
        # to the value that should be displayed when no output file is active.
        self.widgets["label_output_path"]["text"] = \
            self.template["label_output_path"]["text"]["value_if_false"]

        # Clear the entry displaying the output path.
        print_to_entry("", self.widgets["entry_output_path"], wipe_clean=True)

        # Clear the text displaying the notes log.
        print_to_text("", self.widgets["text_log"], wipe_clean=True)

    def set_media_widgets(self, file_full_path, media):
        """This method alters all of the relevant widgets in the Time Stamper program to
        indicate that a valid media file IS currently active. Note that this method does
        not handle the actual enabling/disabling of widgets associated with a media file."""

        # Change the text of the label that appears above the file
        # path entry widget to indicate that a file has been selected.
        if isinstance(self.template["label_media_path"]["text"], dict):
            self.widgets["label_media_path"]["text"] = \
                self.template["label_media_path"]["text"]["value_if_true"]

        # Change the file path to the Windows format if we are on a Windows computer.
        if platform.startswith("win"):
            file_full_path = file_full_path.replace(posixpath_sep, ntpath_sep)

        # Print the file path to the entry widget.
        print_to_entry(file_full_path, self.widgets["entry_media_path"], wipe_clean=True)

        # Load the media into a VLC MediaPlayer and save the
        # MediaPlayer as an attribute of the TimeStamper class.
        self.time_stamper.media_player = MediaPlayer()
        self.time_stamper.media_player.set_media(media)

        # Make the range of the media slider equal to the minimum
        # of 359999.99 and the duration of the media player.
        self.widgets["scale_media_time"]["to"] = self.timer.get_max_time()

        # Reset the timer and the media slider.
        self.timer.display_time(0.0, pad=2)

    def reset_media_widgets(self):
        """This method alters all of the relevant widgets in the Time Stamper program to
        indicate that a valid media file IS NOT currently active. Note that this method does
        not handle the actual enabling/disabling of widgets associated with a media file."""

        entry_media_path = self.widgets["entry_media_path"]

        # Erase the Time Stamper program's media player.
        self.time_stamper.media_player = None

        # Clear the entry displaying the media path.
        entry_media_path["state"] = NORMAL
        entry_media_path.delete(0, END)
        entry_media_path["state"] = DISABLED

        # Reset the media slider.
        scale_media_time = self.widgets["scale_media_time"]
        scale_media_time.variable.set(self.template["scale_media_time"]["initial_value"])

        # Reset the volume slider.
        scale_media_volume = self.widgets["scale_media_volume"]
        scale_media_volume.variable.set(100 - float(self.template["label_media_volume"]["text"]))

        # Reset the volume label.
        self.widgets["label_media_volume"]["text"] = self.template["label_media_volume"]["text"]

        # Reset the elapsed/remaining time labels.
        self.widgets["label_media_elapsed"]["text"] = \
            self.template["label_media_elapsed"]["text"]
        self.widgets["label_media_remaining"]["text"] = \
            self.template["label_media_remaining"]["text"]

        # Reset the mute button image.
        button_mute = self.widgets["button_mute"]
        button_mute_image_new = self.widgets["volume_high.png"]
        button_mute.config(image=button_mute_image_new)
        button_mute.image = button_mute_image_new

    def updated_mute_button_image(self, volume_scale_value):
        """Assuming that the volume is not muted, this method returns the
        string corresponding to the PhotoImage object from self.widgets.mapping
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
