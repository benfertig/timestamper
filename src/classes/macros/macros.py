#-*- coding: utf-8 -*-
"""This module contains the Macros class which serves as a container for all
methods that are executed when any button in the Time Stamper program is pressed.
The actual macros are stored in submodules (all of which are imported below)."""

from dataclasses import dataclass
from .macros_checkbuttons import CheckbuttonMacros
from .macros_buttons_file import FileButtonMacros
from .macros_buttons_info import InfoButtonMacros
from .macros_buttons_media import MediaButtonMacros
from .macros_buttons_note import NoteButtonMacros
from .macros_buttons_settings import SettingsButtonMacros
from .macros_buttons_timestamping import TimestampingButtonMacros

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

    def __init__(self, template, settings, widgets, timer):

        check = CheckbuttonMacros(template, widgets)
        file = FileButtonMacros(template, settings, widgets)
        info = InfoButtonMacros(template, widgets, self)
        media = MediaButtonMacros(template, settings, widgets, timer)
        note = NoteButtonMacros(settings, widgets)
        settings = SettingsButtonMacros(template, settings, widgets, self)
        timestamping = TimestampingButtonMacros(template, widgets, timer)

        # Map buttons to their macros.
        self.mapping = { \

            # Checkbuttons
            "checkbutton_pause_settings": check.checkbutton_pause_settings_macro,
            "checkbutton_play_settings": check.checkbutton_play_settings_macro,
            "checkbutton_stop_settings": check.checkbutton_stop_settings_macro,
            "checkbutton_rewind_settings": check.checkbutton_rewind_settings_macro,
            "checkbutton_fast_forward_settings": check.checkbutton_fast_forward_settings_macro,
            "checkbutton_record_settings": check.checkbutton_record_settings_macro,

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

            # Note buttons
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
