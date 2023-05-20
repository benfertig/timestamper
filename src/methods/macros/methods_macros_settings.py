#-*- coding: utf-8 -*-
"""This module stores some extra methods associated with settings."""

from tkinter import DISABLED, NORMAL

import classes
import methods.macros.methods_macros_helper as methods_helper
import methods.macros.methods_macros_output as methods_output

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


def copy_entered_settings_to_dict():
    """This method copies the currently entered settings in the settings window to a dictionary
    and returns that dictionary. The structure of the returned dictionary will be identical
    to TimeStamperSettings.user and can therefore be substituted 1-to-1 for this dictionary."""

    # Copy the current settings.
    settings_copy = classes.settings.user.copy()

    # Iterate through all the widgets containing information
    # which should be used to update the settings.
    for settings_widget_template in classes.template["settings"]:

        # Find the dictionary containing the information
        template_linking_info = settings_widget_template["linked_setting"]

        # Get the value from the template that should be copied into the settings.
        template_attribute_str = template_linking_info["attribute_to_copy"]
        template_value_to_copy = settings_widget_template[template_attribute_str]

        # Find the OUTER key for the settings attribute that should be changed.
        linked_settings_dict_str = template_linking_info["linked_dict"]
        linked_settings_dict = settings_copy[linked_settings_dict_str]

        # Find the INNER key for the settings attribute that should be changed.
        linked_attribute_str = template_linking_info["linked_attribute"]

        # Change the setting.
        linked_settings_dict[linked_attribute_str] = template_value_to_copy

    return settings_copy


def refresh_settings_window_values():
    """This method forces the values that appear in the
    settings window to be updated to match settings.user."""

    # Loop through all of the checkbuttons in the settings window.
    for checkbutton_template in classes.template["checkbuttons"]["window_settings"]:

        # Retrieve the checkbutton widget associated with
        # the current checkbutton template's string key.
        checkbutton_obj = classes.widgets[checkbutton_template["str_key"]]

        # If it is determined that the checkbutton should
        # initially be checked, check the checkbutton.
        if methods_helper.determine_widget_attribute(checkbutton_template, "is_checked"):

            checkbutton_obj.select()
            checkbutton_template["is_checked_loaded_value"] = True

        # If it is determined that the checkbutton should
        # initially be unchecked, uncheck the checkbutton.
        else:
            checkbutton_obj.deselect()
            checkbutton_template["is_checked_loaded_value"] = False

    # Loop through all of the entries in the settings window.
    for entry_template in classes.template["entries"]["window_settings"]:

        # Retrieve the entry widget associated with the current entry template's string key.
        entry_obj = classes.widgets[entry_template["str_key"]]

        # If it is determined that the entry should initially be enabled, enable the entry.
        if methods_helper.determine_widget_attribute(entry_template, "initial_state"):
            entry_obj["state"] = NORMAL

        # If it is determined that the entry should initially be disabled, disable the entry.
        else:
            entry_obj["state"] = DISABLED

        # Determine what the text of the entry should be set to.
        entry_text = methods_helper.determine_widget_attribute(entry_template, "text")

        # Set the text value of the current entry to the previously determined value.
        methods_output.print_to_entry(entry_text, entry_obj, wipe_clean=True)
