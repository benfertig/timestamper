#-*- coding: utf-8 -*-
"""This module contains methods that create Tkinter widgets."""

from sys import platform
from tkinter import DISABLED, NORMAL, HORIZONTAL, VERTICAL, END, Button, \
    Checkbutton, DoubleVar, Entry, IntVar, Label, StringVar, Scale, Spinbox, Text
from tkinter.ttk import Scale as ttk_scale
from .widgets_helper_methods import set_value, determine_widget_text, \
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


def create_button(time_stamper, button_template, button_window, macros=None):
    """This method creates a Button object for the Time Stamper program."""

    str_key = button_template["str_key"]

    # Create the Button's font.
    button_font = create_font(button_template)

    # Determine whether we should use the Button class from tkmacosx instead of tkinter.
    button_has_color = \
        button_template["background"] is not None or button_template["foreground"] is not None
    if platform.startswith("darwin") and (button_has_color or not button_template["text"]):
        button_class = MacButton
    else:
        button_class = Button

    # Determine the Button's initial state.
    is_enabled = determine_widget_attribute(button_template, \
        "initial_state", time_stamper.template, time_stamper.settings)

    # Determine what the Button's initial text should be.
    button_text = determine_widget_text(button_template, \
        time_stamper.template, time_stamper.settings)

    # Determine what the Button's image should be.
    button_image = create_image(time_stamper.template.images_dir, obj_template=button_template)

    # Determine any macros for the button.
    button_macro = macros[str_key] if str_key in macros.mapping else None
    release_macro = \
        macros[f"{str_key}_ONRELEASE"] if f"{str_key}_ONRELEASE" in macros.mapping else None

    # Create the Button object.
    button = button_class(button_window, height=button_template["height"], \
        width=button_template["width"], text=button_text, image=button_image, \
        state=NORMAL, font=button_font, background=button_template["background"], \
        foreground=button_template["foreground"])

    # If a macro for the mouse release was specified in macros.py, map the press macro
    # to the left-mouse-click and the release macro to the left-mouse-click release.
    if release_macro:
        button.bind("<Button-1>", button_macro)
        button.bind("<ButtonRelease-1>", release_macro)
    else:
        button.configure(command=button_macro)

    # Disable the button if it should initially be disabled.
    if not is_enabled:
        button["state"] = DISABLED

    # If we are on a Mac and this button is BOTH initially disabled AND an instance of the kind
    # of button whose background we would like to change when enabled/disabled, then set this
    # button's initial background color to our predefined color for disabled fields on Macs.
    if platform.startswith("darwin") and isinstance(button, MacButton) \
        and not button.cget("text") and not is_enabled:
        button["background"] = button_template["mac_disabled_color"]

    # Place the Button.
    grid_widget(button, button_template)

    # Return the button, the button's image and the button's
    # default, non-disabled (i.e., original) color.
    return button, button_image, button.cget("background")


def create_checkbutton(template, settings, checkbutton_template, checkbutton_window, macros=None):
    """This method creates a Checkbutton object for the Time Stamper program."""

    str_key = checkbutton_template["str_key"]

    # Determine the Checkbutton's initial state.
    if determine_widget_attribute(checkbutton_template, "initial_state", template, settings):
        initial_state = NORMAL
    else:
        initial_state = DISABLED

    int_var = IntVar()

    # Determine any macros for the checkbutton.
    checkbutton_macro = macros[str_key] if macros and str_key in macros.mapping else None

    # Create the Checkbutton object.
    checkbutton = Checkbutton(checkbutton_window, command=checkbutton_macro, \
        variable=int_var, state=initial_state, onvalue=1, offvalue=0)

    checkbutton.variable = int_var

    # If it is determined that the checkbutton should initially be checked, check the checkbutton.
    if determine_widget_attribute(checkbutton_template, "is_checked", template, settings):
        checkbutton.select()
        checkbutton_template["is_checked_loaded_value"] = True

    # If it is determined that the checkbutton should
    # initially be unchecked, uncheck the checkbutton.
    else:
        checkbutton_template["is_checked_loaded_value"] = False

    # Place the Checkbutton.
    grid_widget(checkbutton, checkbutton_template)

    return checkbutton


def create_entry(time_stamper, entry_template, entry_window, macros=None):
    """This method creates an Entry object for the Time Stamper program."""

    str_key = entry_template["str_key"]

    # Create the Entry's font.
    entry_font = create_font(entry_template)

    # Determine what the Entry's initial text should be.
    entry_text_str = \
        determine_widget_text(entry_template, time_stamper.template, time_stamper.settings)
    entry_text = StringVar()
    entry_text.set(entry_text_str)

    # Determine the Entry's initial state
    if determine_widget_attribute(entry_template, \
        "initial_state", time_stamper.template, time_stamper.settings):
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

    # Determine any macros for the entry.
    trace_macro = macros[f"{str_key}_TRACE"] \
        if macros and f"{str_key}_TRACE" in macros.mapping else None
    scroll_macro = macros[f"{str_key}_ONMOUSEWHEEL"] \
        if macros and f"{str_key}_ONMOUSEWHEEL" in macros.mapping else None

    # Set for a method to be executed each time the entry's text is changed
    # if it was indicated that this should be the case in macros.py.
    if trace_macro:
        entry_text.trace("w", lambda *_: trace_macro(entry_text))

    # Allow for the timer to be manipulated when the mousewheel is moved over
    # this entry if it was indicated that this should be the case in macros.py.
    if scroll_macro:

        mousewheel_strs = \
            ("<Button-4>", "<Button-5>") if platform.startswith("linux") else ("<MouseWheel>",)

        for mw_str in mousewheel_strs:
            entry.bind(mw_str, scroll_macro)

    # Load the entry's initial text into its template.
    entry_template["text_loaded_value"] = entry_text_str

    # Place the Entry.
    grid_widget(entry, entry_template)

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


def create_scale(time_stamper, scale_template, scale_window, macros=None):
    """This method creates a Scale object for the Time Stamper program."""

    str_key = scale_template["str_key"]

    # Determine the Scale's initial state.
    if determine_widget_attribute(scale_template, "initial_state", \
        time_stamper.widgets.template, time_stamper.widgets.settings):
        initial_state = NORMAL
    else:
        initial_state = DISABLED

    # Determine the Scale's orientation.
    orient = HORIZONTAL if scale_template["is_horizontal"] else VERTICAL

    double_var = DoubleVar()

    # Determine any macros for the scale.
    scale_macro = macros[str_key] if macros and str_key in macros.mapping else None
    release_macro = macros[f"{str_key}_ONRELEASE"] \
        if macros and f"{str_key}_ONRELEASE" in macros.mapping else None
    scroll_macro = macros[f"{str_key}_ONMOUSEWHEEL"] \
        if macros and f"{str_key}_ONMOUSEWHEEL" in macros.mapping else None

    # If the scale should be made using tkinter.ttk.Scale...
    if scale_template["is_ttk_scale"]:

        # Create the Scale.
        scale = ttk_scale(scale_window, variable=double_var, \
            from_=scale_template["from_"], to=scale_template["to"], \
            orient=orient, state=initial_state, command=scale_macro)

    # If the scale should be made using tkinter.Scale...
    else:

        # Create the Scale's font.
        scale_font = create_font(scale_template)

        # Create the Scale object.
        scale = Scale(scale_window, variable=double_var, \
            from_=scale_template["from_"], to=scale_template["to"], orient=orient, \
            tickinterval=scale_template["tickinterval"], font=scale_font, \
            state=initial_state, showvalue=scale_template["showvalue"], command=scale_macro)

    double_var.set(scale_template["initial_value"])
    scale.variable = double_var

    # If the left-mouse-click should function like the right-mouse-click,
    # map the left-mouse-click function to the right-mouse-click function.
    if scale_template["bind_left_click_to_right_click"]:
        scale.bind("<Button-1>", lambda event: set_value(scale, event))

    # Allow for the scale to be manipulated with the mousewheel if it was
    # indicated that this should be the case in the scale's template.
    if scroll_macro:

        mousewheel_strs = \
            ("<Button-4>", "<Button-5>") if platform.startswith("linux") else ("<MouseWheel>",)

        for mw_str in mousewheel_strs:
            scale.bind(mw_str, scroll_macro)

    # If a macro for the mouse release was specified in macros.py...
    if release_macro:

        # Map the release macro to the left-mouse-click release if it was specified in the template.
        if scale_template["run_release_macro_on_left_release"]:
            scale.bind("<ButtonRelease-1>", release_macro)

        # Map the release macro to the middle-mouse-click
        # release if it was specified in the template.
        if scale_template["run_release_macro_on_middle_release"]:
            scale.bind("<ButtonRelease-2>", release_macro)

        # Map the release macro to the right-mouse-click
        # release if it was specified in the template.
        if scale_template["run_release_macro_on_right_release"]:
            scale.bind("<ButtonRelease-3>", release_macro)

    # Place the Scale.
    grid_widget(scale, scale_template)

    return scale


def create_spinbox(template, settings, spinbox_template, spinbox_window, macros=None):
    """This method creates a Spinbox object for the Time Stamper program."""

    str_key = spinbox_template["str_key"]

    # Create the Spinbox's font.
    spinbox_font = create_font(spinbox_template)

    # Determine what the Spinbox object's initial text should be.
    spinbox_text_str = determine_widget_text(spinbox_template, template, settings)
    spinbox_text = StringVar()

    # Determine the Spinbox's initial state.
    spinbox_template_initial_state = \
        determine_widget_attribute(spinbox_template, "initial_state", template, settings)
    if spinbox_template_initial_state == "readonly":
        initial_state = "readonly"
    elif spinbox_template_initial_state:
        initial_state = NORMAL
    else:
        initial_state = DISABLED

    # Determine any macros for the spinbox.
    spinbox_macro = macros[str_key] if macros and str_key in macros.mapping else None

    # Create the Spinbox object.
    spinbox = Spinbox(spinbox_window, width=spinbox_template["width"], textvariable=spinbox_text, \
        font=spinbox_font, background=spinbox_template["background"], \
        foreground=spinbox_template["foreground"], \
        disabledbackground=spinbox_template["disabledbackground"], \
        disabledforeground=spinbox_template["disabledforeground"], \
        readonlybackground=spinbox_template["readonlybackground"], state=initial_state, \
        values=list(spinbox_template["values"]), command=spinbox_macro)

    spinbox_text.set(spinbox_text_str)

    # Allow for the spinbox to be manipulated with the mousewheel if it was
    # indicated that this should be the case in the spinbox's template.
    if spinbox_template["scroll_to_move"]:

        mousewheel_strs = \
            ("<Button-4>", "<Button-5>") if platform.startswith("linux") else ("<MouseWheel>",)

        for mw_str in mousewheel_strs:
            spinbox.bind(mw_str, \
                lambda event: spinbox.invoke("buttonup" if event.delta > 0 else "buttondown"))

    # Place the Spinbox.
    grid_widget(spinbox, spinbox_template)

    return spinbox

def create_text(template, settings, text_template, text_window):
    """This method creates a Text object for the Time Stamper program."""

    # Create the Text's font.
    text_font = create_font(text_template)

    # Determine the Text's initial state.
    if determine_widget_attribute(text_template, "initial_state", template, settings):
        initial_state = NORMAL
    else:
        initial_state = DISABLED

    # Create the Text object.
    text = Text(text_window, height=text_template["height"], \
        width=text_template["width"], font=text_font, state=initial_state)

    # Determine what the Text object's initial text should be.
    text_text = determine_widget_text(text_template, template, settings)

    # Display the Text object's text.
    text["state"] = NORMAL
    text.insert(END, text_text)
    text["state"] = initial_state

    # Place the Text.
    grid_widget(text, text_template)

    return text
