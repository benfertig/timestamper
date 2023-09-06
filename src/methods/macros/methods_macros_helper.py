#-*- coding: utf-8 -*-
"""This module stores some extra methods that various other macros rely on."""

from sys import platform
from tkinter import DISABLED, NORMAL, Button
import classes
import methods.macros.methods_macros_output as methods_output

if platform.startswith("darwin"):
    from tkmacosx.widget import Button as MacButton

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


def entry_trace_method(entry_text, entry_template):
    """This is a custom method that gets executed when the
    text is edited in one of several entries (hours, minutes,
    seconds, subseconds, skip backward entry, skip forward entry)."""

    if len(entry_text.get()) > 0:

        # If this entry should contain only digits...
        if entry_template["digits_only"]:

            # Remove any non-digits from the entry.
            try:
                int(entry_text.get()[-1])
            except ValueError:
                entry_text.set(entry_text.get()[:-1])

            # Remove any digits from the entry that put the entry
            # under its minimum value or over its maximum value.
            if len(entry_text.get()) > 0:

                # Define the entry's minimum value, maximum value and current value.
                min_val = entry_template["min_val"]
                max_val = entry_template["max_val"]
                entry_val = int(entry_text.get())

                # Truncate the entry's value if it is out of bounds.
                if (min_val is not None and entry_val < min_val) or \
                    (max_val is not None and entry_val > max_val):
                    entry_text.set(entry_text.get()[:-1])

    # Enable and disable the relevant buttons for when the entry's text is edited.
    for str_to_enable in entry_template["to_enable"]:
        classes.widgets[str_to_enable]["state"] = NORMAL
    for str_to_disable in entry_template["to_disable"]:
        classes.widgets[str_to_disable]["state"] = DISABLED

    # Save the entry's updated text in the entry's template.
    entry_template["text_loaded_value"] = entry_text.get()


def adjust_skip_values_on_entry_mousewheel(event, is_skip_backward):
    """This is a custom method that gets executed when the mousewheel is moved
    over the entries below the skip backward and skip forward buttons."""

    # On Mac platforms, the registered scroll amount does not need to be divided by 120.
    event_delta = event.delta if platform.startswith("darwin") else int(event.delta / 120)

    # Define the string key of the entry, the entry itself, and the template of the entry.
    entry_str_key = "entry_skip_backward" if is_skip_backward else "entry_skip_forward"
    entry = classes.widgets[entry_str_key]
    entry_template = classes.template[entry_str_key]

    # If scrolling would not put the entry under its minimum value (1)
    # or over its maximum value (99), update the value of the entry.
    new_val = int(entry.get()) + event_delta
    if entry_template["min_val"] <= new_val <= entry_template["max_val"]:
        methods_output.print_to_entry(new_val, entry, wipe_clean=True)


def change_help_page(next_page):
    """This method is called upon by the macros for the left/right arrow buttons in the
    help page. Since the procedure for both of these buttons is nearly identical, we can
    use the same function for both buttons with only one argument (next_page: boolean)."""

    # Create abbreviated variable names.
    label_page_number_template = classes.template["label_help_page_number"]
    page_numbers = label_page_number_template["page_numbers"]
    cur_page = label_page_number_template["current_page"]

    # Display the new page number.
    new_page = page_numbers[cur_page][1 if next_page else 0]
    label_page_number_template["current_page"] = new_page
    obj_page_number = classes.widgets["label_help_page_number"]
    obj_page_number["text"] = str(new_page)

    # Display the new help message.
    label_help_message_template = classes.template["label_help_message"]
    obj_label_help = classes.widgets["label_help_message"]
    new_message = label_help_message_template["loaded_message_text"][str(new_page)]
    obj_label_help["text"] = new_message


def enable_button(button, original_color=None):
    """This method enables a button. For certain buttons on Mac computers, visual modifications
    are also made to the button to make it easier to tell that the button is enabled."""

    # Enable the button.
    button["state"] = NORMAL

    # If 1) we are on a Mac, 2) the current button is a tkmacosx Button and
    # 3) the button has no text, then it will be hard to tell whether this
    # button is enabled unless we change its appearance. Therefore, the
    # tkmacosx button's background would be changed to its original color here.
    if platform.startswith("darwin") and \
        isinstance(button, MacButton) and not button.cget("text"):
        button["background"] = original_color


def disable_button(button, mac_disabled_color=None):
    """This method disables a button. For certain buttons on Mac computers, visual modifications
    are also made to the button to make it easier to tell that the button is disabled."""

    # Enable the button temporarily.
    button["state"] = NORMAL

    # If 1) we are on a Mac, 2) the current button is a tkmacosx Button and
    # 3) the button has no text, then it will be hard to tell whether this button
    # is disabled unless we change its appearance. Therefore, the tkmacosx button's
    # background would be changed to the predetermined disabled color here.
    if platform.startswith("darwin") and \
        isinstance(button, MacButton) and not button.cget("text"):
        button["background"] = mac_disabled_color

    # Disable the button.
    button["state"] = DISABLED


def button_enable_disable_macro(button_template):
    """This method, which is called upon by several button macros, will enable and
    disable the buttons associated with the string keys from the "to_enable" and
    "to_disable" attributes of a specific button from the TimeStamperTemplate class."""

    # Enable the buttons stored in the button template's "to_enable" variable.
    for str_to_enable in button_template["to_enable"]:

        original_color = classes.widgets.original_colors[str_to_enable] \
            if str_to_enable in classes.widgets.original_colors else None

        enable_button(classes.widgets[str_to_enable], original_color)

    # Disable the buttons stored in the button template's "to_disable" variable.
    for str_to_disable in button_template["to_disable"]:
        disable_button(classes.widgets[str_to_disable], button_template["mac_disabled_color"])


def toggle_widgets(widget_template, toggle_bool):
    """This method enables/disables the widgets in a template's
    to_enable_toggle and to_disable_toggle attributes."""

    # Iterate through the widget string keys in this template's "to_enable_toggle" attribute.
    if "to_enable_toggle" in widget_template:

        for str_widget in widget_template["to_enable_toggle"]:

            widget_toggle = classes.widgets[str_widget]

            # Call the custom enable_button or disable_button method if the widget is a button.
            if isinstance(widget_toggle, Button) or \
                (platform.startswith("darwin") and isinstance(widget_toggle, MacButton)):
                if toggle_bool:
                    enable_button(widget_toggle, classes.widgets.original_colors[str_widget])
                else:
                    disable_button(\
                        widget_toggle, classes.template[str_widget]["mac_disabled_color"])

            # Simply enable/disable the widget if it is not a button.
            else:
                widget_toggle["state"] = NORMAL if toggle_bool else DISABLED

    # Iterate through the widget string keys in this template's "to_disable_toggle" attribute.
    if "to_disable_toggle" in widget_template:

        for str_widget in widget_template["to_disable_toggle"]:

            widget_toggle = classes.widgets[str_widget]

            # Call the custom enable_button or disable_button method if the widget is a button.
            if isinstance(widget_toggle, Button) or \
                (platform.startswith("darwin") and isinstance(widget_toggle, MacButton)):
                if toggle_bool:
                    disable_button(\
                        widget_toggle, classes.template[str_widget]["mac_disabled_color"])
                else:
                    enable_button(widget_toggle, classes.widgets.original_colors[str_widget])

            # Simply enable/disable the widget if it is not a button.
            else:
                widget_toggle["state"] = DISABLED if toggle_bool else NORMAL


def rebind_playback_buttons():
    """This method rebinds the playback buttons (play, rewind and fast-forward)
    to their respective macros for when they are pressed/released."""

    for button_str_key in ("button_play", "button_rewind", "button_fast_forward"):
        button = classes.widgets[button_str_key]
        if not button.bind():
            button.bind("<Button-1>", classes.macros[button_str_key])
            button.bind("<ButtonRelease-1>", classes.macros[f"{button_str_key}_ONRELEASE"])


def checkbutton_enable_disable_macro(checkbutton_template):
    """This method, which is called upon by several checkbutton macros, will either
    enable (if the user has just checked the checkbutton) or disable (if the user has
    just unchecked the checkbutton) the widgets associated with the string keys from
    the "to_enable_toggle" attribute of the template associated with checkbutton_str."""

    # Store the checkbutton widget into a variable.
    checkbutton = classes.widgets[checkbutton_template["str_key"]]

    # When a checkbutton is clicked, there may be some widgets that should
    # be enabled or disabled regardless of whether that click checked or
    # unchecked the checkbutton. Enable and disable any such widgets here.
    button_enable_disable_macro(checkbutton_template)

    # If this checkbutton is checked...
    if checkbutton.variable.get() == 1:

        # Record that this checkbutton is checked in this checkbutton's template.
        checkbutton_template["is_checked_loaded_value"] = True

        # Activate the relevant widgets for when this checkbutton is checked.
        for str_to_enable in checkbutton_template["to_enable_toggle"]:
            to_enable = classes.widgets[str_to_enable]
            to_enable["state"] = NORMAL

    # If this checkbutton is unchecked...
    else:

        # Record that this checkbutton is unchecked in this checkbutton's template.
        checkbutton_template["is_checked_loaded_value"] = False

        # Deactivate the relevant widgets for when this checkbutton is unchecked.
        for str_to_disable in checkbutton_template["to_enable_toggle"]:
            to_disable = classes.widgets[str_to_disable]
            to_disable["state"] = DISABLED


def determine_widget_attribute(widget_template, attribute_str):
    """This method determines what a particular attribute (attribute_str) of a widget should
    be set to. Sometimes, a widget's attribute is stored directly in the value associated with
    a key (attribute_str) in its template. Other times, the widget's attribute is associated
    with a value stored in the settings or in another template. In either case, this method
    will locate the correct setting for an attribute and return the value of that setting."""

    state = widget_template[attribute_str]

    # Trace the linked state back to the source reference.
    while isinstance(state, dict):

        linked_dict = state["linked_dict"]
        linked_attribute = state["linked_attribute"]
        dict_to_reference = \
            classes.settings if linked_dict in classes.settings.user else classes.template
        state = dict_to_reference[linked_dict][linked_attribute]

    if isinstance(widget_template[attribute_str], dict):

        # If we should return a value that is not the linked
        # value, determine that value here and return it.
        if state and "value_if_true" in widget_template[attribute_str]:
            return widget_template[attribute_str]["value_if_true"]
        if not state and "value_if_false" in widget_template[attribute_str]:
            return widget_template[attribute_str]["value_if_false"]

    # Return the exact value of the linked state if a custom value was not set.
    return state
