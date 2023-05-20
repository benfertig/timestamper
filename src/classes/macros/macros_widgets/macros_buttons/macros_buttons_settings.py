#-*- coding: utf-8 -*-
"""This module stores the functions that are executed when
settings buttons in the Time Stamper program are pressed."""

from tkinter import DISABLED, NORMAL

import classes
import methods.macros.methods_macros_helper as methods_helper
import methods.macros.methods_macros_settings as methods_settings

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


def button_settings_macro(*_):
    "This method will be executed when the settings button is pressed."

    # Display the settings window.
    if "window_settings" in classes.widgets.mapping \
        and classes.widgets.mapping["window_settings"].winfo_exists():

        window_settings = classes.widgets.mapping["window_settings"]
        window_settings.lift()

    else:

        window_settings = classes.widgets.create_entire_window("window_settings")

        # If the current settings are the same as the default
        # settings, disable the "Reset to default" button.
        if classes.settings.user == classes.settings.default:
            classes.widgets["button_reset_to_default"]["state"] = DISABLED

        window_settings.mainloop()


def button_reset_to_default_macro(*_):
    """This method will be executed when the "Reset to
    default" button in the settings window is pressed."""

    # Save the current user settings.
    settings_user_temp = classes.settings.user.copy()

    # Temporarily reset the current settings to their defaults.
    classes.settings.user = classes.settings.default

    # Reset the values of all of the widgets in the settings window.
    methods_settings.refresh_settings_window_values()

    # If resetting to the default settings DID NOT CHANGE any settings in the
    # settings window, disable the "Cancel changes" and "Save settings" button.
    if classes.settings.user == settings_user_temp:
        classes.widgets["button_cancel_changes"]["state"] = DISABLED
        classes.widgets["button_save_settings"]["state"] = DISABLED

    # If resetting to the default settings CHANGED any settings in the
    # settings window, enable the "Cancel changes" and "Save settings" button.
    else:
        classes.widgets["button_cancel_changes"]["state"] = NORMAL
        classes.widgets["button_save_settings"]["state"] = NORMAL

    # Set the settings back to the values they were at before this method began
    # (because we do not want to change the actual settings stored in
    # settings.user unless the user presses the "Save settings" button, and we
    # only changed settings.user back to the default settings temporarily so that
    # the settings window could be recreated with the default settings filled in).
    classes.settings.user = settings_user_temp

    # Enable and disable the relevant widgets for when the "Reset to default" button is pressed.
    methods_helper.button_enable_disable_macro(classes.template["button_reset_to_default"])


def button_cancel_changes_macro(*_):
    """This method will be executed when the "Cancel
    changes" button in the settings window is pressed."""

    # Reset the values of all of the widgets in the settings window.
    methods_settings.refresh_settings_window_values()

    # Disable the "Save settings" button.
    classes.widgets["button_save_settings"]["state"] = DISABLED

    # If the current settings are the same as the default
    # settings, disable the "Reset to default" button.
    if classes.settings.user == classes.settings.default:
        classes.widgets["button_reset_to_default"]["state"] = DISABLED

    # Enable and disable the relevant widgets for when the "Cancel changes" button is pressed.
    methods_helper.button_enable_disable_macro(classes.template["button_cancel_changes"])


def button_save_settings_macro(*_):
    """This method will be executed when the "Save
    settings" button in the settings window is pressed."""

    # Update the settings to reflect the currently entered values in the settings window.
    classes.settings.user = methods_settings.copy_entered_settings_to_dict()

    # Write the changed settings to settings_user.json.
    classes.settings.dump_dict_to_json(\
        classes.settings.user, classes.settings.user_json_path, indent=4)

    # Enable and disable the relevant widgets for when the "Save settings" button is pressed.
    methods_helper.button_enable_disable_macro(classes.template["button_save_settings"])
