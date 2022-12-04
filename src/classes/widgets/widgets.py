#-*- coding: utf-8 -*-
"""This module contains the Widgetsclass which contains methods that create various Tkinter widgets
as well as a mapping of widgets to their string keys. This allows for easy reference of widgets.
Also see the "widgets_helper_methods.py" module for additional methods associated with widgets."""

from .widgets_helper_methods import entry_value_limit, create_window, \
    create_image, create_button, create_entry, create_label, create_text

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


class Widgets():
    """This class stores methods that create various Tkinter widgets based on
    templates. Widgets can be referenced based on their string keys. For example,
    to access the pause button, one would reference Widgets.mapping["button_pause"]."""

    def __init__(self, template_mapping, images_dir, messages_dir, main_window_str):

        self.template_mapping = template_mapping
        self.images_dir = images_dir
        self.messages_dir = messages_dir
        self.main_window_str = main_window_str

        self.mapping = {}
        self.original_colors = {}

    def create_entire_window(self, window_str, button_macro_mapping=None, \
        close_window_macro=None, macro_args=()):
        """This method creates an entire window with all of its widgets. For
        this method to work properly, the widget templates must already be mapped
        to the window's string key in the "template_window_mapping" dictionaries
        in "buttons.py", "entries.py", "labels.py" and "texts.py"."""

        # Create the window.
        window_template = self.template_mapping[window_str]
        self.mapping[window_template["str_key"]] = \
            create_window(window_template, self.main_window_str, self.images_dir)

        # Create the buttons.
        button_mapping = self.template_mapping["buttons"]
        if button_macro_mapping is not None and window_str in button_mapping:
            button_window_templates = button_mapping[window_str]
            self.create_images(button_window_templates)
            self.create_buttons(button_window_templates, button_macro_mapping)

        # Create the entries.
        entry_mapping = self.template_mapping["entries"]
        if window_str in entry_mapping:
            entry_window_templates = entry_mapping[window_str]
            self.create_entries(entry_window_templates, entry_value_limit)

        # Create the labels.
        label_mapping = self.template_mapping["labels"]
        if window_str in label_mapping:
            label_window_templates = label_mapping[window_str]
            self.create_images(label_window_templates)
            self.create_labels(label_window_templates)

        # Create the texts.
        text_mapping = self.template_mapping["texts"]
        if window_str in text_mapping:
            text_window_templates = text_mapping[window_str]
            self.create_texts(text_window_templates)

        window = self.mapping[window_str]

        # If a function should be executed when this new window is closed, set that function here.
        if close_window_macro:
            macro_args = (window,) + macro_args
            window.protocol("WM_DELETE_WINDOW", lambda: close_window_macro(*macro_args))

        # Return the window object.
        return window

    def create_images(self, widget_templates):
        """This method creates all of the images specified by the templates in
        widget_templates, searching for images in the directory provided by images_dir."""

        images = {}

        for w_template in widget_templates:
            image = create_image(w_template, self.images_dir)
            self.mapping[w_template["image_file_name"]] = image
            images[w_template["image_file_name"]] = image

        return images

    def create_buttons(self, button_templates, button_macro_mapping):
        """This method creates all of the buttons specified by the templates in
        button_templates, searching for images in the directory provided by images_dir."""

        buttons = {}

        for b_template in button_templates:

            # Retrieve the window and image objects for the current button.
            button_window = self.mapping[b_template["window_str_key"]]
            button_image = self.mapping[b_template["image_file_name"]]

            # Retrieve the macro for the current button.
            button_macro = button_macro_mapping[b_template["str_key"]]

            # Create the button.
            button, button_orig_color = create_button(b_template, \
                button_window, button_macro, self.messages_dir, button_image)

            # Map the Button object's initial background to the Button's string key so that the
            # Button's background can be reset to this color upon reactivation (currently, this
            # change applies only to Buttons from the tkmacosx class with images but no text,
            # since there is no easy way to tell whether these buttons are activated, so we change
            # the button's color upon activation/deactivation as a visual aid to the user). Even
            # when we pass None as the argument for "background" in the Button's constructor, the
            # background is set to a specific color, so we should save the explicit background
            # color because we will need to reference this color if we want to revert to it later.
            self.original_colors[b_template["str_key"]] = button_orig_color

            # Map the Button object to the Button's string
            # key so that the Macros class can reference it.
            self.mapping[b_template["str_key"]] = button

            buttons[b_template["str_key"]] = button

        return buttons

    def create_entries(self, entry_templates, e_v_limit):
        """This method creates all of the entries specified by the templates in entry_templates."""

        entries = {}

        for e_template in entry_templates:

            # Retrieve the window and image objects for the current entry.
            entry_window = self.mapping[e_template["window_str_key"]]

            # Create the entry.
            entry = create_entry(e_template, entry_window, e_v_limit, self.messages_dir)

            # Map the Entry object to the Entry's string key
            # so that the Macros class can reference it.
            self.mapping[e_template["str_key"]] = entry

            entries[e_template["str_key"]] = entry

        return entries

    def create_labels(self, label_templates):
        """This method creates all of the labels specified by the templates in label_templates."""

        labels = {}

        for l_template in label_templates:

            # Retrieve the window and image objects for the current label.
            label_window = self.mapping[l_template["window_str_key"]]
            label_image = self.mapping[l_template["image_file_name"]]

            # Create the label.
            label = create_label(l_template, label_window, self.messages_dir, label_image)

            # Map the Label object to the Label's string
            # key so that the Macros class can reference it.
            self.mapping[l_template["str_key"]] = label

            labels[l_template["str_key"]] = label

        return labels

    def create_texts(self, text_templates):
        """This method creates all of the texts specified by the templates in text_templates."""

        texts = {}

        for t_template in text_templates:

            # Retrieve the window and image objects for the current text.
            text_window = self.mapping[t_template["window_str_key"]]

            # Create the text.
            text = create_text(t_template, text_window, self.messages_dir)

            # Map the Text object to the Text's string key
            # so that the Macros class can reference it.
            self.mapping[t_template["str_key"]] = text

            texts[t_template["str_key"]] = text

        return texts
