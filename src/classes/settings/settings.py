#-*- coding: utf-8 -*-
"""This module contains the TimeStamperSettings class which contains all of
the attributes that can be edited by the user in the Time Stamper program."""

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
class TimeStamperSettings():
    """This class stores all of the settings that can be
    edited by the user in the Time Stamper program."""

    def __init__(self):

        cur_dir = dirname(__file__)

        self.changes_made = False

        # Save the paths to the default settings and user settings JSONs.
        self.default_json_path = join(cur_dir, "settings_default.json")
        self.user_json_path = join(cur_dir, "settings_user.json")

        # Load the default settings and the user settings from their JSONs.
        self.default = self.load_json(self.default_json_path)
        self.user = self.load_json(self.user_json_path)

        # Store the string keys of the widgets into which the user can enter their custom settings.
        self.widgets_to_reference = [

            # Checkbuttons
            "checkbutton_pause_settings", "checkbutton_play_settings",
            "checkbutton_stop_settings", "checkbutton_rewind_settings",
            "checkbutton_fast_forward_settings", "checkbutton_record_settings",

            # Entries
            "entry_pause_settings", "entry_play_settings", "entry_stop_settings",
            "entry_rewind_settings", "entry_fast_forward_settings", "entry_record_settings"

        ]

    def __getitem__(self, item):
        return self.user[item]

    def load_json(self, json_path):
        """This method loads a JSON file into a dictionary and returns that dictionary."""

        with open(json_path, encoding="utf-8") as json_file:
            return load(json_file)
