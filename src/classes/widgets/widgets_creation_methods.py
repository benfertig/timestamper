#-*- coding: utf-8 -*-
"""This module contains methods that create Tkinter widgets."""

from sys import platform
from tkinter import DISABLED, NORMAL, HORIZONTAL, VERTICAL, END, Button, \
    Checkbutton, DoubleVar, Entry, IntVar, Label, StringVar, Scale, Text
from tkinter.ttk import Scale as ttk_scale
from .widgets_helper_methods import entry_helper_method, determine_widget_text, \
    determine_widget_attribute, create_font, grid_widget, create_image

if platform.startswith("darwin"):
    from tkmacosx import Button as MacButton

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


def set_value(scale, event):
    """This method binds a scale's left-mouse-click event to its right-mouse-click event."""

    scale.event_generate("<Button-3>", x=event.x, y=event.y)
    return "break"


def create_button(template, settings, button_template, button_window, button_macro):
    """This method creates a Button object for the Time Stamper program."""

    # Create the Button's font.
    button_font = create_font(button_template)

    # Determine whether we should use the Button class from tkmacosx instead of tkinter.
    button_background = button_template["background"]
    button_foreground = button_template["foreground"]
    button_has_color = button_background is not None or button_foreground is not None
    if platform.startswith("darwin") and (button_has_color or not button_template["text"]):
        button_class = MacButton
    else:
        button_class = Button

    # Determine the Button's initial state.
    if determine_widget_attribute(button_template, "initial_state", template, settings):
        initial_state = NORMAL
    else:
        initial_state = DISABLED

    # Determine what the Button's initial text should be.
    button_text = determine_widget_text(button_template, template, settings)

    # Determine what the Button's image should be.
    button_image = create_image(template.images_dir, obj_template=button_template)

    # Create the Button object.
    button = button_class(button_window, height=button_template["height"], \
        width=button_template["width"], text=button_text, image=button_image, \
        state=initial_state, font=button_font, background=button_background, \
        foreground=button_foreground, command=button_macro)

    # Place the Button.
    grid_widget(button, button_template)

    # If we are on a Mac and this button is BOTH initially disabled AND an instance of the kind
    # of button whose background we would like to change when enabled/disabled, then set this
    # button's initial background color to our predefined color for disabled fields on Macs.
    if platform.startswith("darwin") and isinstance(button, MacButton) \
        and not button.cget("text") and button["state"] == DISABLED:
        button["background"] = button_template["mac_disabled_color"]

    return button, button_image, button.cget("background")


def create_checkbutton(template, settings, \
    checkbutton_template, checkbutton_window, checkbutton_macro):
    """This method creates a Checkbutton object for the Time Stamper program."""

    # Determine the Checkbutton's initial state.
    if determine_widget_attribute(checkbutton_template, "initial_state", template, settings):
        initial_state = NORMAL
    else:
        initial_state = DISABLED

    int_var = IntVar()

    # Create the Checkbutton object.
    checkbutton = Checkbutton(checkbutton_window, command=checkbutton_macro, \
        variable=int_var, state=initial_state, onvalue=1, offvalue=0)

    checkbutton.variable = int_var

    # Place the Checkbutton.
    grid_widget(checkbutton, checkbutton_template)

    # Determine whether the checkbutton should initially be checked or unchecked.
    if determine_widget_attribute(checkbutton_template, "is_checked", template, settings):
        checkbutton.select()
        checkbutton_template["is_checked_loaded_value"] = True
    else:
        checkbutton_template["is_checked_loaded_value"] = False

    return checkbutton


def create_entry(template, settings, entry_template, entry_window, widgets):
    """This method creates an Entry object for the Time Stamper program."""

    # Create the Entry's font.
    entry_font = create_font(entry_template)

    # Determine what the Entry's initial text should be.
    entry_text_str = determine_widget_text(entry_template, template, settings)
    entry_text = StringVar()
    entry_text.set(entry_text_str)

    # Determine the Entry's initial state
    if determine_widget_attribute(entry_template, "initial_state", template, settings):
        initial_state = NORMAL
    else:
        initial_state = DISABLED

    # Create the Entry object.
    entry = Entry(\
        entry_window, width=entry_template["width"], textvariable=entry_text, font=entry_font, \
        background=entry_template["background"], foreground=entry_template["foreground"], \
        disabledbackground=entry_template["disabledbackground"], \
        disabledforeground=entry_template["disabledforeground"],
        state=initial_state)

    # Place the Entry.
    grid_widget(entry, entry_template)

    # Set the Entry input restrictions.
    entry_text.trace("w", lambda *_: entry_helper_method(entry_text, entry_template, widgets))

    # Load the entry's initial text into its template.
    entry_template["text_loaded_value"] = entry_text_str

    return entry


def create_label(template, settings, label_template, label_window):
    """This method creates a Label object for the Time Stamper program."""

    # Create the Label's font.
    label_font = create_font(label_template)

    # Determine what the Label's initial text should be.
    label_text = determine_widget_text(label_template, template, settings)

    # Determine what the label's image should be.
    label_image = create_image(template.images_dir, obj_template=label_template)

    # Create the Label object.
    label = Label(label_window, height=label_template["height"], \
        width=label_template["width"], background=label_template["background"], \
        foreground=label_template["foreground"], text=label_text, \
        image=label_image, font=label_font, highlightthickness=0, \
        wraplength=label_template["wraplength"], justify=label_template["justify"])

    # Place the Label.
    grid_widget(label, label_template)

    return label, label_image


def create_scale(widgets, scale_template, scale_window, scale_command=None, release_command=None):
    """This method creates a Scale object for the Time Stamper program."""

    # Determine the Scale's initial state.
    if determine_widget_attribute(scale_template, \
        "initial_state", widgets.template, widgets.settings):
        initial_state = NORMAL
    else:
        initial_state = DISABLED

    # Determine the Scale's orientation.
    orient = HORIZONTAL if scale_template["is_horizontal"] else VERTICAL

    double_var = DoubleVar()

    # If the scale should be made using tkinter.ttk.Scale...
    if scale_template["is_ttk_scale"]:

        # Create the Scale.
        scale = ttk_scale(scale_window, variable=double_var, \
            from_=scale_template["from_"], to=scale_template["to"], \
            orient=orient, state=initial_state, command=scale_command)

    # If the scale should be made using tkinter.Scale...
    else:

        # Create the Scale's font.
        scale_font = create_font(scale_template)

        # Create the Scale object.
        scale = Scale(scale_window, variable=double_var, \
            from_=scale_template["from_"], to=scale_template["to"], orient=orient, \
            tickinterval=scale_template["tickinterval"], font=scale_font, \
            state=initial_state, showvalue=scale_template["showvalue"], command=scale_command)

    initial_value = determine_widget_attribute(scale_template, \
        "initial_value", widgets.template, widgets.settings)

    double_var.set(initial_value)
    scale.variable = double_var

    # If the left-mouse-click should function like the right-mouse-click,
    # map the left-mouse-click function to the right-mouse-click function.
    if scale_template["bind_left_click_to_right_click"]:
        scale.bind("<Button-1>", lambda event: set_value(scale, event))

    # If a macro for the mouse release was specified in macros.py...
    if release_command:

        # Map the release macro to the left-mouse-click if it was specified in the template.
        if scale_template["run_release_macro_on_left_release"]:
            scale.bind("<ButtonRelease-1>", release_command)

        # Map the release macro to the middle-mouse-click if it was specified in the template.
        if scale_template["run_release_macro_on_middle_release"]:
            scale.bind("<ButtonRelease-2>", release_command)

        # Map the release macro to the right-mouse-click if it was specified in the template.
        if scale_template["run_release_macro_on_right_release"]:
            scale.bind("<ButtonRelease-3>", release_command)

    # Place the Scale.
    grid_widget(scale, scale_template)

    return scale


def create_text(template, settings, text_template, text_window):
    """This method creates a Text object for the Time Stamper program."""

    # Create the Text's font.
    text_font = create_font(text_template)

    # Determine the Text's initial state
    if determine_widget_attribute(text_template, "initial_state", template, settings):
        initial_state = NORMAL
    else:
        initial_state = DISABLED

    # Create the Text object.
    text = Text(text_window, height=text_template["height"], \
        width=text_template["width"], font=text_font, state=initial_state)

    # Determine what the text object's initial text should be.
    text_text = determine_widget_text(text_template, template, settings)

    # Display the Text object's text.
    text["state"] = NORMAL
    text.insert(END, text_text)
    text["state"] = initial_state

    # Place the Text.
    grid_widget(text, text_template)

    return text
