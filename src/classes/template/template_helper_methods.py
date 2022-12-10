#-*- coding: utf-8 -*-
"""This module contains helper methods for the TimeStamperTemplate class in template.py."""

from collections import defaultdict
from glob import glob
from os import scandir
from os.path import abspath, basename, isdir, join
from json import load
import sys

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


def get_default_json_path(json_dir):
    """This method locates the default JSON file for a
    folder and returns the path to that JSON file."""

    json_dir_name = basename(json_dir)
    default_json_path = join(json_dir, f"{json_dir_name}_default.json")
    return default_json_path

def json_to_dict(json_path):
    """This method loads the contents of a JSON file (whose path is
    specified by json_path) into a dictionary and returns that dictionary."""

    with open(json_path, encoding="utf-8") as json_file:
        mapping = load(json_file)
        return mapping


def get_json_dict_mapping(json_dict, default_mapping):
    """This method takes a JSON file that has already been loaded into a dictionary (json_dict),
    adds the contents of that dictionary to a mapping, and then returns that mapping. The
    default_mapping argument should be a dictionary containing key-value pairs that should
    be added to "mapping" whenever the corresponding key is not present in json_dict."""

    mapping = {}

    # Iterate through all of the entries in the current JSON file.
    for widget_str_key, widget_template in json_dict.items():

        # If the current template does not contain an attribute that the
        # "default" template does contain, set the value of that attribute
        # for the current template to the value from the "default" template.
        for default_attribute, default_value in default_mapping.items():
            if default_attribute not in widget_template:
                widget_template[default_attribute] = default_value

        # Map the widget templates in the "mapping" dictionary.
        mapping[widget_str_key] = widget_template

    return mapping


def map_all_templates(templates_dir):
    """This method loads the contents of all JSON files from all subdirectories of
    this file's current directory into the "mapping" attribute of this class."""

    mapping = {}

    # Iterate through the subitems of the directory that template.py is in.
    for inner_dir in scandir(templates_dir):

        # Store the name of the base directory
        # of the path to the current subitem.
        inner_dir_name = basename(inner_dir)

        # If the current subitem of templates_dir is also a
        # directory and that directory is not __pychache__...
        if isdir(inner_dir) and inner_dir_name != "__pycache__":

            # Find the default JSON file of the current
            # subdirectory and load it into a dictionary.
            default_json_path = get_default_json_path(inner_dir)
            default_mapping = json_to_dict(default_json_path)

            # Initialize an empty dictionary which will store the mapping of
            # all the widgets whose type is indicated by the name of the current
            # subdirectory (e.g., "buttons", "checkbuttons", "labels", etc.).
            mapping[inner_dir_name] = defaultdict(list)
            inner_json_paths = set(glob(join(inner_dir, "*.json")))

            # Do not include the current directory's "default" JSON file in the main
            # mapping (although we will still rely on the "default" JSON file to set
            # the values for attributes that are not stored in the other JSON files).
            inner_json_paths.discard(default_json_path)

            # Iterate through the paths to all of the JSON files in the current subdirectory.
            for json_path in inner_json_paths:

                # Retrieve the mapping from the current JSON file, falling back
                # on the values from the "default" JSON file when there is
                # no value for a specific attribute in the current JSON file.
                json_dict = json_to_dict(json_path)
                cur_json_mapping = get_json_dict_mapping(json_dict, default_mapping)

                # Map the key-value pairs from the current JSON file to "mapping".
                for widget_str_key, widget_template in cur_json_mapping.items():
                    mapping[widget_str_key] = widget_template
                    window_str_key = widget_template["window_str_key"]
                    mapping[inner_dir_name][window_str_key].append(widget_template)

    return mapping
