#-*- coding: utf-8 -*-
"""This module contains the Widgets class which contains methods associated with
various Tkinter widgets as well as a mapping of widgets to their string keys. This
allows for easy reference of widgets. Also see the "widgets_creation_methods.py" and
"widgets_helper_methods.py" modules for additional methods associated with widgets."""

from .widgets_creation_methods import create_button, \
    create_checkbutton, create_entry, create_label, create_text
from .widgets_helper_methods import create_window, determine_widget_text

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
    """This class contains methods associated with various Tkinter widgets as
    well as a mapping of widgets to their string keys. Widgets can be referenced
    based on their string keys. For example, to access the pause button, one would
    reference Widgets["button_pause"]. Also see the "widgets_creation_methods.py" and
    "widgets_helper_methods.py" modules for additional methods associated with widgets."""

    def __init__(self, template, settings, timer, main_window_str):

        self.template = template
        self.settings = settings
        self.main_window_str = main_window_str
        self.original_colors = {}
        self.determine_widget_text = determine_widget_text

        self.mapping = {"time_stamper_timer": timer}

    def __getitem__(self, item):
        return self.mapping[item]

    def create_widgets(self, window_str, macros=None):
        """This method creates all of the widgets that are meant
        to appear in the window indicated by window_str."""

        widget_window = self[window_str]

        # Create the buttons.
        for w_template in self.template["buttons"][window_str]:
            widget_macro = macros[w_template["str_key"]] \
                if w_template["str_key"] in macros.mapping else None
            widget, widget_image, button_orig_color = \
                create_button(self.template, self.settings, w_template, widget_window, widget_macro)
            self.original_colors[w_template["str_key"]] = button_orig_color
            if widget_image:
                self.mapping[w_template["image_file_name"]] = widget_image
            self.mapping[w_template["str_key"]] = widget

        # Create the checkbuttons.
        for w_template in self.template["checkbuttons"][window_str]:
            widget_macro = macros[w_template["str_key"]] \
                if w_template["str_key"] in macros.mapping else None
            widget = create_checkbutton(self.template, \
                self.settings, w_template, widget_window, widget_macro)
            self.mapping[w_template["str_key"]] = widget

        # Create the entries.
        for w_template in self.template["entries"][window_str]:
            widget = create_entry(self.template, self.settings, w_template, widget_window, self)
            self.mapping[w_template["str_key"]] = widget

        # Create the labels.
        for w_template in self.template["labels"][window_str]:
            widget, widget_image = \
                create_label(self.template, self.settings, w_template, widget_window)
            if widget_image:
                self.mapping[w_template["image_file_name"]] = widget_image
            self.mapping[w_template["str_key"]] = widget

        # Create the texts.
        for w_template in self.template["texts"][window_str]:
            widget = create_text(self.template, self.settings, w_template, widget_window)
            self.mapping[w_template["str_key"]] = widget

    def clear_all_window_widgets(self, window_str):
        """This method destroys all of the widgets within a window (but not the window itself)."""

        for widget_type in ("buttons", "checkbuttons", "entries", "labels", "texts"):
            for widget_template in self.template[widget_type][window_str]:
                widget_str_key = widget_template["str_key"]
                self.mapping[widget_str_key].destroy()

    def refresh_window(self, window_str, macros=None):
        """This method reloads all of the widgets in a window without
        destroying the current window or creating a new one."""

        # Destroy all of the widgets in the current window.
        self.clear_all_window_widgets(window_str)

        # Recreate all of the current window's widgets.
        self.create_widgets(window_str, macros)

    def create_entire_window(self, window_str, macros=None, close_window_macro=None, macro_args=()):
        """This method creates an entire window with all of its widgets
        based on the string key for a particular window (window_str_key)."""

        # If the window already exists, simply bring it to the front instead of recreating it.
        if window_str in self.mapping and self.mapping[window_str].winfo_exists():

            window = self.mapping[window_str]
            window.lift()

        else:

            # Create the window.
            window_template = self.template[window_str]
            window = create_window(window_template, self.main_window_str, self.template.images_dir)
            self.mapping[window_str] = window

            # Create the widgets that should appear in the current window.
            self.create_widgets(window_str, macros)

            # If a function should be executed when this
            # new window is closed, set that function here.
            if close_window_macro:
                macro_args = (window,) + macro_args
                window.protocol("WM_DELETE_WINDOW", lambda: close_window_macro(*macro_args))

        # Return the window object.
        return window
