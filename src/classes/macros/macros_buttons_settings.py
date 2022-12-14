#-*- coding: utf-8 -*-
"""This module contains the SettingsButtonMacros class which stores the functions
that are executed when a settings button in the Time Stamper program is pressed."""

from tkinter import DISABLED, NORMAL
from .macros_helper_methods import button_enable_disable_macro

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


class SettingsButtonMacros():
    """This class stores all of the macros that execute when settings buttons are pressed."""

    def __init__(self, parent):
        self.parent = parent
        self.template = parent.template
        self.settings = parent.settings
        self.widgets = parent.widgets

    def copy_entered_settings_to_dict(self):
        """This method copies the currently entered settings in the settings window to a dictionary
        and returns that dictionary. The structure of the returned dictionary will be identical
        to TimeStamperSettings.user and can therefore be substituted 1-to-1 for this dictionary."""

        # Copy the current settings.
        settings_copy = self.settings.user.copy()

        # Iterate through all the widgets containing information
        # which should be used to update the settings.
        for settings_widget_template in self.template["settings"]:

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

    def button_settings_macro(self):
        "This method will be executed when the settings button is pressed."

        # Display the settings window.
        if "window_settings" in self.widgets.mapping \
            and self.widgets.mapping["window_settings"].winfo_exists():

            window_settings = self.widgets.mapping["window_settings"]
            window_settings.lift()

        else:

            window_settings = self.widgets.create_entire_window("window_settings", self.parent)

            # If the current settings are the same as the default
            # settings, disable the "Reset to default" button.
            if self.settings.user == self.settings.default:
                self.widgets["button_reset_to_default"]["state"] = DISABLED

            window_settings.mainloop()

    def button_reset_to_default_macro(self):
        """This method will be executed when the "Reset to
        default" button in the settings window is pressed."""

        # Save the current user settings.
        settings_user_temp = self.settings.user.copy()

        # Temporarily reset the current settings to their defaults.
        self.settings.user = self.settings.default

        # Reset all of the widgets in the settings window.
        self.widgets.refresh_window("window_settings", self.parent)

        # If resetting to the default settings DID NOT CHANGE any settings in the
        # settings window, disable the "Cancel changes" and "Save settings" button.
        if self.settings.user == settings_user_temp:
            self.widgets["button_cancel_changes"]["state"] = DISABLED
            self.widgets["button_save_settings"]["state"] = DISABLED

        # If resetting to the default settings CHANGED any settings in the
        # settings window, enable the "Cancel changes" and "Save settings" button.
        else:
            self.widgets["button_cancel_changes"]["state"] = NORMAL
            self.widgets["button_save_settings"]["state"] = NORMAL

        # Set the settings back to the values they were at before this method began
        # (because we do not want to change the actual settings stored in
        # self.settings.user unless the user presses the "Save settings" button, and we
        # only changed self.settings.user back to the default settings temporarily so that
        # the settings window could be recreated with the default settings filled in).
        self.settings.user = settings_user_temp

        # Enable and disable the relevant widgets for when the "Reset to default" button is pressed.
        button_enable_disable_macro(self.template["button_reset_to_default"], self.widgets)

    def button_cancel_changes_macro(self):
        """This method will be executed when the "Cancel
        changes" button in the settings window is pressed."""

        # Refresh all of the widgets in the settings window.
        self.widgets.refresh_window("window_settings", self.parent)

        # If the current settings are the same as the default
        # settings, disable the "Reset to default" button.
        if self.settings.user == self.settings.default:
            self.widgets["button_reset_to_default"]["state"] = DISABLED

        # Enable and disable the relevant widgets for when the "Cancel changes" button is pressed.
        button_enable_disable_macro(self.template["button_cancel_changes"], self.widgets)

    def button_save_settings_macro(self):
        """This method will be executed when the "Save
        settings" button in the settings window is pressed."""

        # Update the settings to reflect the currently entered values in the settings window.
        self.settings.user = self.copy_entered_settings_to_dict()

        # Write the changed settings to settings_user.json.
        self.settings.dump_dict_to_json(self.settings.user, self.settings.user_json_path, indent=4)

        # Enable and disable the relevant widgets for when the "Save settings" button is pressed.
        button_enable_disable_macro(self.template["button_save_settings"], self.widgets)
