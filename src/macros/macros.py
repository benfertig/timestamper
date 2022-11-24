#-*- coding: utf-8 -*-
"""This module contains the Macros class which serves as a container for all methods
that are executed when any button in the Time Stamper program is pressed. The actual
macros are stored in submodules, namely macros_buttons_file.py, macros_buttons_info.py,
macros_buttons_media.py, macros_buttons_note.py and macros_buttons_timestamping.py."""

from dataclasses import dataclass
from .macros_buttons_file import FileButtonMacros
from .macros_buttons_info import InfoButtonMacros
from .macros_buttons_media import MediaButtonMacros
from .macros_buttons_note import NoteButtonMacros
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

    def __init__(self, template, widgets, timer):

        self.file = FileButtonMacros(template, widgets)
        self.info = InfoButtonMacros(template, widgets, None)
        self.media = MediaButtonMacros(template, widgets, timer)
        self.note = NoteButtonMacros(template, widgets)
        self.timestamping = TimestampingButtonMacros(template, widgets, timer)

        self.widgets = widgets

        # Map buttons to their macros.
        self.mapping = { \

            # File buttons
            "button_output_select": self.file.button_output_select_macro,
            "button_merge_output_files": self.file.button_merge_output_files_macro,

            # Info buttons
            "button_help": self.info.button_help_macro,
            "button_help_left_arrow": self.info.button_help_left_arrow_macro,
            "button_help_right_arrow": self.info.button_help_right_arrow_macro,
            "button_license": self.info.button_license_macro,
            "button_attribution": self.info.button_attribution_macro,

            # Media buttons
            "button_pause": self.media.button_pause_macro,
            "button_play": self.media.button_play_macro,
            "button_stop": self.media.button_stop_macro,
            "button_rewind": self.media.button_rewind_macro,
            "button_fast_forward": self.media.button_fast_forward_macro,
            "button_record": self.media.button_record_macro,

            # Note buttons
            "button_cancel_note": self.note.button_cancel_note_macro,
            "button_save_note": self.note.button_save_note_macro,

            # Timestamping buttons
            "button_timestamp": self.timestamping.button_timestamp_macro,
            "button_clear_timestamp": self.timestamping.button_clear_timestamp_macro

        }

        self.info.mapping = self.mapping
