#-*- coding: utf-8 -*-
"""This module contains the Buttons class which is called upon by
the constructor of the Fields class (which is found in template.py)"""

from dataclasses import dataclass
from json import load
from os.path import dirname, join

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
class Buttons():
    """This class, which is called upon by the constructor of the Fields class, should
    be seen as an extension of the TimeStamperTemplate class with attributes pertaining
    specifically to objects of type tkinter.Button in the Time Stamper program."""

    def __init__(self):

        self.str_key = "buttons"

        # Map the button templates to their string keys.
        mapping = {}
        cur_dir = dirname(__file__)
        with open(join(cur_dir, "buttons_file.json"), encoding="utf-8") as buttons_file_json:
            mapping.update(load(buttons_file_json))
        with open(join(cur_dir, "buttons_info.json"), encoding="utf-8") as buttons_info_json:
            mapping.update(load(buttons_info_json))
        with open(join(cur_dir, "buttons_media.json"), encoding="utf-8") as buttons_media_json:
            mapping.update(load(buttons_media_json))
        with open(join(cur_dir, "buttons_note.json"), encoding="utf-8") as buttons_note_json:
            mapping.update(load(buttons_note_json))
        with open(join(cur_dir, "buttons_timestamping.json"), encoding="utf-8") as btns_tstmp_json:
            mapping.update(load(btns_tstmp_json))
        self.mapping = mapping

        # Map the button templates to the windows that they appear in.
        self.template_window_mapping = {
            "window_main":
                (mapping["button_pause"], mapping["button_play"], mapping["button_stop"],
                mapping["button_rewind"], mapping["button_fast_forward"],
                mapping["button_record"], mapping["button_output_select"],
                mapping["button_merge_output_files"], mapping["button_timestamp"],
                mapping["button_clear_timestamp"], mapping["button_help"],
                mapping["button_license"], mapping["button_attribution"],
                mapping["button_cancel_note"], mapping["button_save_note"]),
            "window_help":
                (mapping["button_help_left_arrow"], mapping["button_help_right_arrow"])
        }
