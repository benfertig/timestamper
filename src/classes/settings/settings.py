#-*- coding: utf-8 -*-
"""This module contains the TimeStamperSettings class which contains all of
the attributes that can be edited by the user in the Time Stamper program."""

from dataclasses import dataclass
from json import dump, load
from json.decoder import JSONDecodeError
from os import mkdir, sep
from os.path import dirname, exists, expanduser, join
from sys import platform

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

        # Save the version of the Time Stamper program that this source code corresponds to.
        program_version_number = "0.3.0"

        # Save the path to settings_default.json.
        self.default_json_path = join(f"{dirname(__file__)}{sep}", "settings_default.json")

        # Load the default settings from settings_default.json.
        self.default = self.load_json(self.default_json_path)

        # Get the folder that settings_user.json should be saved to.
        user_settings_folder = self.get_settings_folder(version_number=program_version_number)

        # Create the user settings directory if it does not exist.
        dir_so_far = ""
        for isolated_dir_name in user_settings_folder.split(sep):
            dir_so_far = join(f"{dir_so_far}{sep}", isolated_dir_name)
            if not exists(dir_so_far):
                mkdir(dir_so_far)

        # Define the full path to settings_user.json.
        self.user_json_path = join(f"{user_settings_folder}{sep}", "settings_user.json")

        # Retrieve the current user settings if they exist.
        user_settings = self.check_current_user_settings(self.user_json_path)

        # If the current user settings DO NOT exist, copy them from the default
        # settings and write the default settings to settings_user.json.
        if user_settings is None:
            self.user = self.default.copy()
            self.dump_dict_to_json(self.default, self.user_json_path, indent=4)

        # If the current user settings DO exist, reference these settings directly.
        else:
            self.user = user_settings

    def __getitem__(self, item):
        return self.user[item]

    def load_json(self, json_path):
        """This method loads a JSON file into a dictionary and returns that dictionary."""

        with open(json_path, encoding="utf-8") as json_file:
            return load(json_file)

    def dump_dict_to_json(self, dict_to_dump, json_path, indent=4):
        """This method dumps the contents of a dictionary to a JSON file."""

        with open(json_path, "w", encoding="utf-8") as json_file:
            dump(dict_to_dump, json_file, indent=indent)

    def get_settings_folder(self, version_number=""):
        """This method returns the folder that settings_user.json should be
        saved to. This folder varies based on the current operating system."""

        # If we are on Windows, search for the settings_user.json within %APPDATA%.
        if platform.startswith("win"):
            return join(f"{expanduser('~')}{sep}", f"Documents{sep}",
                f"Time Stamper{sep}", f"{version_number}{sep}")

        # If we are on a Mac, search for settings_user.json within Library/Preferences
        if platform.startswith("darwin"):
            return join(f"{expanduser('~')}{sep}", f"Library{sep}", \
                f"Preferences{sep}", f"Time Stamper{sep}", f"{version_number}{sep}")

        # TODO: In the future, add a settings folder for Linux computers.
        return join(f"{dirname(__file__)}{sep}", f"{version_number}{sep}")

    def check_settings_structures_match(self, dict_1, dict_2):
        """This method does not check whether two dictionaries are identical, but rather, whether
        the outer keys and inner keys of two dictionaries are identical (disregarding values)."""

        # Return False if the keys of dict_1 and dict_2 are not the same.
        if dict_1.keys() != dict_2.keys():
            return False

        # If the outer keys of the two dictionaries are the
        # same, iterate through the key-value pairs of dict_1.
        for dict_1_key, dict_1_value in dict_1.items():

            # The current key for dict_2 is the same as the current key for
            # dict_1 (we know this because this section of code is unreachable
            # unless the outer keys for both dictionaries are identical), but
            # the value corresponding to the current key in dict_2 may differ
            # from that of dict_1, so we store the current value from dict_2 here.
            dict_2_value = dict_2[dict_1_key]

            # Save the types of the current values from both dictionaries.
            dict_1_value_type = type(dict_1_value)
            dict_2_value_type = type(dict_2_value)

            # Return False if the type of the current value
            # from both dictionaries is not the same.
            if dict_1_value_type != dict_2_value_type:
                return False

            # Return False if the current value from both dictionaries
            # is another dictionary but their keys are not the same.
            if dict_2_value_type == dict and dict_1_value.keys() != dict_2_value.keys():
                return False

        # Return True if dict_1 is analogous with dict_2.
        return True

    def check_current_user_settings(self, user_json_path):
        """This method returns a dictionary corresponding to the user settings
        IF settings_user.json exists at the provided location (user_json_path)
        AND the data hierarchy of settings_user.json matches that of
        settings_default.json. Otherwise, this method returns None."""

        # If the user settings JSON exists...
        if exists(user_json_path):

            # Try loading settings_user.json.
            try:
                user_settings = self.load_json(user_json_path)

            # If settings_user.json could not be loaded, return None.
            except JSONDecodeError:
                return None

            # If settings_user.json was successfully loaded into a dictionary...

            # If the data hierarchy of the loaded user settings MATCHES
            # that of the default settings, return the loaded user settings.
            if self.check_settings_structures_match(user_settings, self.default):
                return user_settings

            # If the data hierarchy of the loaded user settings DOES
            # NOT MATCH that of the default settings, return None.
            return None

        # If settings_user.json does not exist at the expected location, return None.
        return None
