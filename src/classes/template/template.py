#-*- coding: utf-8 -*-
"""This module contains the TimeStamperTemplate class which contains all
of the custom attributes for all of the objects called upon in the
TimeStamper run() method (the method that runs the Time Stamper program)."""

from collections import defaultdict
from dataclasses import dataclass
import sys
from os import getcwd, scandir
from os.path import abspath, basename, dirname, isdir, join
from glob import glob
from json import load

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


def resource_path():
    """This method gets the absolute path to the resource."""

    try:
        res_path = sys._MEIPASS
    except AttributeError:
        res_path = abspath(".")

    return res_path


@dataclass
class TimeStamperTemplate():
    """
    This class does not store the Time Stamper objects themselves, but rather, stores all of
    the attributes for all of the Time Stamper objects in an organized way. This serves two
    purposes:

        1) People will be able to locate and/or make changes
           to the attributes of Time Stamper objects quickly.

        2) The amount of code that needs to be written in other modules is reduced. For example,
           in the main "time_stamper" class, all objects that are of the same type (Buttons,
           Labels, Entries, Texts, etc.) are placed by running a loop, where for each object
           template "x_template", the row, column, initial state, etc. of its corresponding
           object x can be retrieved by referencing template.mapping["x_template"]["row"],
           template.mapping["x_template"]["column"], and
           template.mapping["x_template"]["initial_state"] among other attributes.

    To edit the attributes of ANY widget in the Time Stamper program, edit the JSON
    files inside of the subdirectories that this file (template.py) is located in.
    """

    def __init__(self):

        self.output_file_encoding = "utf-8"
        self.output_path = None
        self.starting_dir = getcwd()
        self.images_dir = join(resource_path(), "images")
        self.messages_dir = join(resource_path(), "messages")

        self.mapping = {}

        # Iterate through the subitems of the directory that template.py is in.
        for inner_dir in scandir(dirname(__file__)):
            inner_dir_name = basename(inner_dir)

            # If the current subitem of this file's directory is also
            # a directory and that directory is not __pychache__...
            if isdir(inner_dir) and inner_dir_name != "__pycache__":

                self.mapping[inner_dir_name] = defaultdict(list)
                jsons = set(glob(join(inner_dir, "*.json")))

                # Get the default template values from the "default" JSON file.
                default_json_path = join(inner_dir, f"{inner_dir_name}_default.json")
                jsons.remove(default_json_path)
                with open(default_json_path, encoding="utf-8") as default_json_file:
                    default_mapping = load(default_json_file)

                # Iterate through all of the JSON files in the current subdirectory.
                for json_file_path in jsons:
                    with open(json_file_path, encoding="utf-8") as json_file:
                        json_to_dict = load(json_file)

                        # Iterate through all of the entries in the current JSON file.
                        for widget_str_key, widget_template in json_to_dict.items():

                            # If the current template does not contain an attribute that the
                            # "default" template does contain, set the value of that attribute
                            # for the current template to the value from the "default" template.
                            for default_attribute, default_value in default_mapping.items():
                                if default_attribute not in widget_template:
                                    widget_template[default_attribute] = default_value

                            # Map the widget templates in the "mapping" dictionary.
                            self.mapping[widget_str_key] = widget_template
                            window_str_key = widget_template["window_str_key"]
                            self.mapping[inner_dir_name][window_str_key].append(widget_template)
