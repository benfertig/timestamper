#-*- coding: utf-8 -*-
"""This module contains the Macros class which serves as a container for all methods
that are executed when any button, checkbutton, or scale in the Time Stamper program is
manipulated. The actual macros are stored in submodules (all of which are imported below)."""

from dataclasses import dataclass

import classes.macros.macros_widgets.macros_checkbuttons as check
import classes.macros.macros_widgets.macros_comboboxes as comboboxes
import classes.macros.macros_widgets.macros_entries as entries
import classes.macros.macros_widgets.macros_scales as scales
import classes.macros.macros_widgets.macros_spinboxes as spinboxes
import classes.macros.macros_widgets.macros_texts as texts
import classes.macros.macros_widgets.macros_windows as windows

import classes.macros.macros_widgets.macros_buttons.macros_buttons_file as file
import classes.macros.macros_widgets.macros_buttons.macros_buttons_info as info
import classes.macros.macros_widgets.macros_buttons.macros_buttons_media as media
import classes.macros.macros_widgets.macros_buttons.macros_buttons_note as note
import classes.macros.macros_widgets.macros_buttons.macros_buttons_settings as settings
import classes.macros.macros_widgets.macros_buttons.macros_buttons_timestamping as timestamping

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
    """This class is a container class for all of the macros in the Time Stamper program.
    The macro for any widget can be accessed through the Macros.mapping attribute. For
    example, to access the pause button's macro, reference Macros.mapping["button_pause"]."""

    def __getitem__(self, item):
        return self.mapping[item]

    def __init__(self):

        # Map the widgets to their macros.
        self.mapping = {

            # Checkbuttons
            "checkbutton_pause_settings": check.checkbutton_pause_settings_macro,
            "checkbutton_play_settings": check.checkbutton_play_settings_macro,
            "checkbutton_rewind_settings": check.checkbutton_rewind_settings_macro,
            "checkbutton_fast_forward_settings": check.checkbutton_fast_forward_settings_macro,
            "checkbutton_skip_backward_settings": check.checkbutton_skip_backward_settings_macro,
            "checkbutton_skip_forward_settings": check.checkbutton_skip_forward_settings_macro,
            "checkbutton_always_include_hours_in_timestamp_settings": \
                check.checkbutton_always_include_hours_in_timestamp_settings_macro,

            # Comboboxes
            "combobox_round_timestamp_settings": comboboxes.combobox_round_timestamp_settings_macro,
            "combobox_round_timestamp_settings_ONMOUSEWHEEL": \
                comboboxes.combobox_round_timestamp_settings_mousewheel_macro,

            # Entries
            "entry_hours_TRACE": entries.entry_hours_trace,
            "entry_hours_ONMOUSEWHEEL": entries.entry_hours_mousewheel_macro,
            "entry_minutes_TRACE": entries.entry_minutes_trace,
            "entry_minutes_ONMOUSEWHEEL": entries.entry_minutes_mousewheel_macro,
            "entry_seconds_TRACE": entries.entry_seconds_trace,
            "entry_seconds_ONMOUSEWHEEL": entries.entry_seconds_mousewheel_macro,
            "entry_subseconds_TRACE": entries.entry_subseconds_trace,
            "entry_subseconds_ONMOUSEWHEEL": entries.entry_subseconds_mousewheel_macro,
            "entry_skip_backward_TRACE": entries.entry_skip_backward_trace,
            "entry_skip_backward_ONMOUSEWHEEL": entries.entry_skip_backward_mousewheel_macro,
            "entry_skip_forward_TRACE": entries.entry_skip_forward_trace,
            "entry_skip_forward_ONMOUSEWHEEL": entries.entry_skip_forward_mousewheel_macro,
            "entry_pause_settings_TRACE": entries.entry_pause_settings_trace,
            "entry_play_settings_TRACE": entries.entry_play_settings_trace,
            "entry_rewind_settings_TRACE": entries.entry_rewind_settings_trace,
            "entry_fast_forward_settings_TRACE": entries.entry_fast_forward_settings_trace,
            "entry_skip_backward_settings_TRACE": entries.entry_skip_backward_settings_trace,
            "entry_skip_forward_settings_TRACE": entries.entry_skip_forward_settings_trace,
            "entry_hotkey_1_settings_TRACE": entries.entry_hotkey_1_settings_trace,
            "entry_hotkey_2_settings_TRACE": entries.entry_hotkey_2_settings_trace,
            "entry_hotkey_3_settings_TRACE": entries.entry_hotkey_3_settings_trace,

            # Scales
            "scale_media_time": scales.scale_media_time_macro,
            "scale_media_time_ONRELEASE": scales.scale_media_time_release_macro,
            "scale_media_time_ONMOUSEWHEEL": scales.scale_media_time_mousewheel_macro,
            "scale_media_volume": scales.scale_media_volume_macro,
            "scale_media_volume_ONMOUSEWHEEL": scales.scale_media_volume_mousewheel_macro,

            # Spinboxes
            "spinbox_rewind": spinboxes.spinbox_rewind_macro,
            "spinbox_rewind_ONMOUSEWHEEL": spinboxes.spinbox_rewind_mousehweel_macro,
            "spinbox_fast_forward": spinboxes.spinbox_fast_forward_macro,
            "spinbox_fast_forward_ONMOUSEWHEEL": spinboxes.spinbox_fast_forward_mousehweel_macro,

            # Texts
            "text_current_note_ONRETURN": texts.text_current_note_return_key_macro,

            # Windows
            "window_video_ONCLOSE": windows.on_close_window_video_macro,
            "window_help_ONCLOSE": windows.on_close_window_help_macro,

            # File buttons
            "button_output_select": file.button_output_select_macro,
            "button_reconcile_timestamps": file.button_reconcile_timestamps_macro,
            "button_sort_output": file.button_sort_output_macro,
            "button_cancel_output": file.button_cancel_output_macro,
            "button_media_select": file.button_media_select_macro,
            "button_cancel_media": file.button_cancel_media_macro,

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
