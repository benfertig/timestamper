#-*- coding: utf-8 -*-
"""This module contains the Labels class which is called upon by
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
class Labels():
    """This module, which is called upon by the constructor of the Fields class,
    should be seen as an extension of the TimeStamperTemplate class, with attributes
    pertaining specifically to objects of type tkinter.Label in the Time Stamper program."""

    def __init__(self):

        self.str_key = "labels"

        # Map the label templates to their string keys.
        cur_dir = dirname(__file__)
        mapping = {}
        with open(join(cur_dir, "labels_info.json"), encoding="utf-8") as labels_info_json:
            mapping.update(load(labels_info_json))
        with open(join(cur_dir, "labels_merge.json"), encoding="utf-8") as labels_merge_json:
            mapping.update(load(labels_merge_json))
        with open(join(cur_dir, "labels_timer.json"), encoding="utf-8") as labels_timer_json:
            mapping.update(load(labels_timer_json))
        with open(join(cur_dir, "labels_other.json"), encoding="utf-8") as labels_other_json:
            mapping.update(load(labels_other_json))
        self.mapping = mapping

        # Map the label templates to the windows that they appear in.
        self.template_window_mapping = {
            "window_main":
                (mapping["label_h"], mapping["label_m"], mapping["label_dot"],
                mapping["label_s"], mapping["label_output_path"],
                mapping["label_rewind_sec"], mapping["label_fast_forward_sec"],
                mapping["label_timestamp"]),
            "window_help":
                (mapping["label_help_image"], mapping["label_help_message"],
                mapping["label_help_page_number"]),
            "window_license":
                (mapping["label_license"],),
            "window_merge_first_message" :
                (mapping["label_merge_first_message"],),
            "window_merge_second_message" :
                (mapping["label_merge_second_message"],),
            "window_merge_success" :
                (mapping["label_merge_success"],),
            "window_merge_failure" :
                (mapping["label_merge_failure"],)
        }
