#-*- coding: utf-8 -*-
"""This module contains the Macros class which serves as a container for all
methods that are executed when any button in the Time Stamper program is pressed.
The actual macros are stored in submodules (all of which are imported below)."""

from dataclasses import dataclass
from tkinter import DISABLED, NORMAL, END
from pyglet.media import load, Player
from pyglet.media.codecs.wave import WAVEDecodeException
from .macros_checkbuttons import CheckbuttonMacros
from .macros_scales import ScaleMacros
from .macros_buttons_file import FileButtonMacros
from .macros_buttons_info import InfoButtonMacros
from .macros_buttons_media import MediaButtonMacros
from .macros_buttons_note import NoteButtonMacros
from .macros_buttons_settings import SettingsButtonMacros
from .macros_buttons_timestamping import TimestampingButtonMacros
from .macros_helper_methods import disable_button, print_to_text, print_to_file

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

    def __init__(self, time_stamper, settings):

        self.time_stamper = time_stamper
        self.template = time_stamper.template
        self.settings = settings
        self.widgets = time_stamper.widgets
        self.timer = time_stamper.timer

        check = CheckbuttonMacros(self)
        scales = ScaleMacros(self)
        file = FileButtonMacros(self)
        info = InfoButtonMacros(self)
        media = MediaButtonMacros(self)
        note = NoteButtonMacros(self)
        settings = SettingsButtonMacros(self)
        timestamping = TimestampingButtonMacros(self)

        # Map buttons to their macros.
        self.mapping = {

            # Checkbuttons
            "checkbutton_pause_settings": check.checkbutton_pause_settings_macro,
            "checkbutton_play_settings": check.checkbutton_play_settings_macro,
            "checkbutton_stop_settings": check.checkbutton_stop_settings_macro,
            "checkbutton_rewind_settings": check.checkbutton_rewind_settings_macro,
            "checkbutton_fast_forward_settings": check.checkbutton_fast_forward_settings_macro,
            "checkbutton_record_settings": check.checkbutton_record_settings_macro,

            # Scales
            "scale_audio_time": scales.scale_audio_time_macro,
            "scale_audio_time_ONRELEASE": scales.scale_audio_time_release_macro,
            "scale_audio_volume": scales.scale_audio_volume_macro,

            # File buttons
            "button_output_select": file.button_output_select_macro,
            "button_merge_output_files": file.button_merge_output_files_macro,
            "button_audio_select": file.button_audio_select_macro,

            # Info buttons
            "button_help": info.button_help_macro,
            "button_help_left_arrow": info.button_help_left_arrow_macro,
            "button_help_right_arrow": info.button_help_right_arrow_macro,
            "button_license": info.button_license_macro,
            "button_attribution": info.button_attribution_macro,

            # Media buttons
            "button_pause": media.button_pause_macro,
            "button_play": media.button_play_macro,
            "button_stop": media.button_stop_macro,
            "button_rewind": media.button_rewind_macro,
            "button_fast_forward": media.button_fast_forward_macro,
            "button_record": media.button_record_macro,
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
        """This method takes a message, timestamps it, and then prints that
        timestamped message to the notes log and the output file. If no timestamp is
        provided, a timestamp will be generated using the timer's current time."""

        if timestamp is None:
            timestamp = self.timer.current_time_to_timestamp()

        to_print = f"{timestamp} {message}"

        # Get the current output path from the output path entry widget.
        output_path = self.widgets["entry_output_path"].get()

        # Print the button's message, along with the current
        # timestamp, to the notes log and the output file.
        print_to_text(to_print, self.widgets["text_log"])
        print_to_file(to_print, output_path, self.settings["output"]["file_encoding"])

    def get_button_message_input(self, button_str_key):
        """This method, which is called upon by several button macros, uses a button's
        template to determine whether a message should be printed when the button is pressed.
        If this method determines that a message should be printed when the button is pressed,
        then this method will return that message. Otherwise, this method will return None.
        Keep in mind that this method does not substitute potential variables (e.g., $amount
        and $dest for the rewind and fast-forward messages) in the returned message. Any
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

        return None

    def validate_audio_player(self):
        """If an audio player is already loaded into the Time Stamper program, this
        method will return that audio player. Otherwise, this method will attempt to
        create an audio player with the information the user has provided. If an audio
        player is successfully created, this method will return that audio player. Otherwise,
        this method will clear the text displayed in the audio path entry and return None."""

        # If an audio player is already loaded, return that audio player.
        if self.time_stamper.audio_player:
            return self.time_stamper.audio_player

        # Try to load the audio source.
        try:
            entry_audio_path = self.widgets["entry_audio_path"]
            audio_path = entry_audio_path.get()
            self.time_stamper.audio_source = load(audio_path)

        # If the audio source fails to load, return None in place of an audio player
        except (FileNotFoundError, WAVEDecodeException):
            return None

        # If the audio source loaded successfully, create a new audio player.
        else:
            return Player()

    def disable_audio_widgets(self):
        """This method alters all of the widgets in the Time Stamper program that are
        associated with audio playback to indicate that no audio source is available."""

        entry_audio_path = self.widgets["entry_audio_path"]

        # Clear the entry displaying the audio path.
        entry_audio_path["state"] = NORMAL
        entry_audio_path.delete(0, END)
        entry_audio_path["state"] = DISABLED

        # Reset and disable the audio slider.
        scale_audio_time = self.widgets["scale_audio_time"]
        scale_audio_time.variable.set(self.template["scale_audio_time"]["initial_value"])
        scale_audio_time["state"] = DISABLED

        # Reset and disable the volume slider.
        scale_audio_volume = self.widgets["scale_audio_volume"]
        scale_audio_volume.variable.set(self.template["label_audio_volume"]["text"])
        scale_audio_volume["state"] = DISABLED

        # Reset the volume label.
        self.widgets["label_audio_volume"]["text"] = self.template["label_audio_volume"]["text"]

        # Reset the elapsed/remaining time labels.
        self.widgets["label_audio_elapsed"]["text"] = \
            self.template["label_audio_elapsed"]["text"]
        self.widgets["label_audio_remaining"]["text"] = \
            self.template["label_audio_remaining"]["text"]

        # Disable the mute button.
        disable_button(self.widgets["button_mute"], \
            self.template["button_mute"]["mac_disabled_color"])

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

        # If the volume is between 0 and 66.6, return "volume_medium.png".
        if 100 * (1 / 3) <= volume_scale_value < 100 * (2/3):
            return "volume_medium.png"

        # If the volume is between 66.6 and 100, set the
        # picture of the mute button to "volume_high.png".
        return "volume_high.png"
