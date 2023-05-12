#-*- coding: utf-8 -*-
"""This module contains additional methods that the widgets module relies on."""

from json import load as json_load
from os.path import join, splitext
from sys import platform
from tkinter import DISABLED, NORMAL, END, font, Grid, PhotoImage, Tk, Toplevel

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


def pad_number(number, target_length, pad_before):
    """This method pads a number to target_length with leading zeros (if
    pad_before is set to True) or trailing zeros (if pad_before is set to False)."""

    str_number = str(number) if number else "0"
    zeros_to_add = "0" * (target_length - len(str_number))
    if pad_before:
        return zeros_to_add + str_number
    return str_number + zeros_to_add


def set_value(scale, event):
    """This method can be bound to a button press on a Scale widget, making it so that the
    result of pressing that button while the cursor is hovering over that scale will mimic the
    result of clicking the right mouse button while the cursor is hovering over that scale."""

    scale.event_generate("<Button-3>", x=event.x, y=event.y)
    return "break"


def adjust_timer_on_entry_mousewheel(event, time_stamper, entry_template):
    """This is a custom event method that gets executed when the mousewheel is
    moved over one of the timer entries (hours, minutes, seconds or subseconds)."""

    # On Mac platforms, the registered scroll amount does not need to be divided by 120.
    event_delta = event.delta if platform.startswith("darwin") else int(event.delta / 120)

    # If there is audio currently playing, schedule
    # the audio to resume playing after a short delay.
    if time_stamper.timer.multiplier or time_stamper.timer.scheduled_id:
        time_stamper.timer.pause(play_delay=0.25)

    # Adjust the timer according to the direction the user scrolled.
    scroll_timer_adjustment = event_delta * float(entry_template["scroll_timer_adjustment"])
    time_stamper.timer.adjust_timer(scroll_timer_adjustment, abort_if_out_of_bounds=True)

def custom_scale_on_mousewheel(scale, event, scale_template, time_stamper):
    """This is a custom event method that gets executed when
    the mousewheel is moved while the cursor is on a Scale."""

    # On Mac platforms, the registered scroll amount does not need to be divided be 120.
    event_delta = event.delta if platform.startswith("darwin") else event.delta / 120

    # Adjust the scale's position to reflect the mousewheel scrolling.
    scroll_amount = event_delta * float(scale_template["scroll_sensitivity"]) * \
        (-1 if scale_template["reverse_scroll_direction"] else 1)
    scale_current_value = scale.get()

    # If we are manipulating the audio time slider and there is audio currently
    # playing, schedule the audio to resume playing after a short delay.
    if scale_template["str_key"] == "scale_audio_time" and time_stamper.audio_player \
        and (time_stamper.audio_player.playing or time_stamper.timer.scheduled_id):
        time_stamper.timer.pause(play_delay=0.25)

    # Set the audio time slider to its adjusted position.
    scale.set(scale_current_value + scroll_amount)

def entry_helper_method(entry_text, entry_template, widgets):
    """This method will be executed every time an entry's text is manipulated."""

    max_val = entry_template["max_val"]

    if len(entry_text.get()) > 0:

        # If this entry should contain only digits...
        if entry_template["digits_only"]:

            # Remove any non-digits from the entry.
            try:
                int(entry_text.get()[-1])
            except ValueError:
                entry_text.set(entry_text.get()[:-1])

            # Remove any digits from the entry that put the entry over max_val.
            if len(entry_text.get()) > 0:
                if int(entry_text.get()) > max_val:
                    entry_text.set(entry_text.get()[:-1])

    # Enable and disable the relevant buttons for when the entry's text is edited.
    for str_to_enable in entry_template["to_enable"]:
        widgets[str_to_enable]["state"] = NORMAL
    for str_to_disable in entry_template["to_disable"]:
        widgets[str_to_disable]["state"] = DISABLED

    # Save the entry's updated text in the entry's template.
    entry_template["text_loaded_value"] = entry_text.get()


def determine_widget_text(widget_template, template, settings):
    """There are different ways that a widget's text can be set. The widget's text can be
    stored in a file, in its template's "text" key, or be referenced from a setting or another
    template. This method determines where to find the widget's text and returns that text."""

    # If there is a file associated with this widget,
    # determine the widget's initial text using that file.
    if widget_template["message_file_name"] is not None:

        # If there is both a non-empty "message_file_name" as well as a non-empty "text"
        # attribute for this widget template, then we must decide which of these values
        # to set the widget's text to. In such cases, this program defaults to the
        # "message_file_name" attribute, instead of the "text" attribute. However, it is
        # not consistent with this program's expectations to have a non-empty value for both
        # "message_file_name" and "text" (at most, only one of these attributes should be
        # non-empty), so a warning message will be printed to the terminal if this is the case.
        # The reason that this program does not expect both "message_file_name" and "text" to
        # be non-empty is because "text" will be ignored if "message_file_name" is non-empty,
        # which may cause confusion for the programmer as it may lead them to wonder why their
        # custom entered value for "text" is not displaying in the Time Stamper program under
        # a circumstance where they also have a non-empty value for "message_file_name".
        if widget_template["text"] is not None:
            print(f"\nWARNING for template \"{widget_template['str_key']}\":\n" \
                "A template's \"text\" and \"message_file_name\" attributes should "\
                "not both be set to non-None values simultaneously. The \"message_file_name\" " \
                "attribute takes precedence, so the text for the widget based on this template " \
                "will be generated using the information stored in " \
                f"\"{widget_template['message_file_name']}\", as opposed to the information " \
                "stored in this template's \"text\" attribute " \
                f"(i.e., \"{widget_template['text']}\").\n")

        # Open the file containing the widget's text.
        message_file_loc = join(template.messages_dir, widget_template["message_file_name"])
        message_encoding = widget_template["message_file_encoding"]
        with open(message_file_loc, "r", encoding=message_encoding) as message_file:

            # If the file associated with the widget's initial text IS a JSON file, set the
            # widget's initial text to the value (from the JSON) that is paired with the
            # key (from the JSON) that is asssociated with the widget's initial message.
            if splitext(message_file_loc)[1] == ".json":
                json_text = json_load(message_file)
                widget_template["loaded_message_text"] = json_text
                widget_text = json_text[widget_template["json_first_message_key"]]
                return widget_text

            # If the file associated with the widget's initial text IS NOT a JSON
            # file, set the widget's initial text to the exact reading of the file.
            widget_text = message_file.read()
            widget_template["loaded_message_text"] = widget_text
            return widget_text

    # If this widget's initial text is conditional on another
    # attribute, retrieve the value of the linked attribute.
    elif isinstance(widget_template["text"], dict):

        widget_text = determine_widget_attribute(widget_template, "text", template, settings)
        return widget_text if widget_text else ""

    # If there is no file associated with this widget and this widget's text
    # is not conditional on another attribute, set this widget's initial text
    # to its template's "text" attribute (unless the "text" attribute is None,
    # in which case you would set the widget's initial text to an empty string).
    else:
        return "" if widget_template["text"] is None else widget_template["text"]


def determine_widget_attribute(widget_template, attribute_str, template, settings):
    """This method determines what a particular attribute (indicated by "state") of a widget
    should be set to. Sometimes, a widget's attribute is stored directly in the value associated
    with a key ("state") in its template. Other times, the widget's attribute is associated
    with a value stored in the settings or in another template. In either case, this method
    will locate the correct setting for an attribute and return the value of that setting."""

    state = widget_template[attribute_str]

    # Trace the linked state back to the source reference.
    while isinstance(state, dict):

        linked_dict = state["linked_dict"]
        linked_attribute = state["linked_attribute"]
        dict_to_reference = settings if linked_dict in settings.user else template
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


def create_font(widget_template):
    """This method creates a widget's font based on its template."""

    # Tkinter text shows up a bit smaller on Mac computers compared to Windows
    # computers. We compensate for this by making text a bit larger on Macs.
    font_size = widget_template["font_size"] + 2 \
        if platform.startswith("darwin") else widget_template["font_size"]

    return font.Font(family=widget_template["font_family"], \
        size=font_size, weight=widget_template["font_weight"], \
        slant=widget_template["font_slant"], \
        underline=widget_template["font_underline"], \
        overstrike=widget_template["font_overstrike"])


def grid_widget(widget, widget_template):
    """This method grids a widget based on its template."""

    widget.grid(column=widget_template["column"], row=widget_template["row"], \
        columnspan=widget_template["columnspan"], rowspan=widget_template["rowspan"], \
        padx=widget_template["padx"], pady=widget_template["pady"], \
        ipadx=widget_template["ipadx"], ipady=widget_template["ipady"], \
        sticky=widget_template["sticky"])


def create_window(window_template, main_window_str, images_dir):
    """This method creates the main window for the Time Stamper program."""

    # If we are creating the main window, it should be an instance of tkinter.Tk.
    # Otherwise, the window should be an instance of tkinter.Toplevel.
    if window_template["str_key"] == main_window_str:
        window = Tk()
    else:
        window = Toplevel()

    # Set the title, dimensions, background and foreground of the window.
    window.title(window_template["title"])
    if window_template["width"] is not None and window_template["height"] is not None:
        window.geometry(f"{window_template['width']}x{window_template['height']}")
    window["background"] = window_template["background"]
    window["foreground"] = window_template["foreground"]

    # If we are on a Mac, the window icon needs to be a .icns file.
    # On Windows, the window icon needs to be a .ico file.
    if platform.startswith("darwin"):
        icon_file_name = window_template["icon_mac"]
    else:
        icon_file_name = window_template["icon_windows"]

    # Set the main window icon.
    window.iconbitmap(join(images_dir, icon_file_name))

    # Configure the main window's columns.
    for col_num in range(window_template["num_columns"]):
        col_weights = window_template["column_weights"]
        col_weight = int(col_weights[str(col_num)]) if str(col_num) in col_weights else 1
        Grid.columnconfigure(window, col_num, weight=col_weight)

    # Configure the main window's rows.
    for row_num in range(window_template["num_rows"]):
        row_weights = window_template["row_weights"]
        row_weight = int(row_weights[str(row_num)]) if str(row_num) in row_weights else 1
        Grid.rowconfigure(window, row_num, weight=row_weight)

    return window


def create_image(images_dir, obj_template=None, image_file_name=None):
    """This method creates an image object for the Time Stamper program."""

    # If an image file name was passed, return a new PhotoImage from the corresponding image file.
    if image_file_name is not None:
        return PhotoImage(file=join(images_dir, image_file_name))

    # If there is no image file name but there is an object template, return
    # an image only if an image file name was specified in the object template.
    if obj_template is not None \
        and "image_file_name" in obj_template and obj_template["image_file_name"]:
        return PhotoImage(file=join(images_dir, obj_template["image_file_name"]))

    # If there was neither a passed image file name nor an image
    # file name associated with the object template, return None.
    return None
