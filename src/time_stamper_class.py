#-*- coding: utf-8 -*-
"""This module contains the TimeStamper class which runs the Time Stamper program."""

from dataclasses import dataclass
from ts_macros.macros import Macros
from ts_timer.time_stamper_timer import TimeStamperTimer
from widget_creators import WidgetCreators

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


class TimeStamper():
    """This class runs the Time Stamper program."""

    @dataclass
    class TimeFields():
        """This class stores the fields where the time is displayed in the Time Stamper program."""

        hours_field = None
        minutes_field = None
        seconds_field = None
        subseconds_field = None

    @dataclass
    class StoredTkObjects():
        """While it typically suffices to assert instances of the Tkinter objects in the main
        Time Stamper window without storing them in variables, there are some Tkinter objects
        (namely entries and images) which need to be stored in variables because they need to be
        accessed later. The variables storing those objects will be contained in this class."""

        entries = None
        images = None

    def __init__(self, template):
        """This constructor initializes the Time Stamper template (which stores
        all of the attributes for objects in the the Time Stamper program), the
        macros (which store all of the macros for buttons in the Time Stamper
        program) and the timer (which runs the timer for the Time Stamper program)."""

        self.root = None
        self.template = template

        self.widget_creators = WidgetCreators(self.root, self.template)
        self.macros = \
            Macros(self.template, self.widget_creators, WidgetCreators(None, self.template))

        self.timer = TimeStamperTimer(self)
        self.stored_tk_objs = self.StoredTkObjects()
        self.time_fields = self.TimeFields()

    def create_window(self):
        """This method creates the main window, and is merely a wrapper
        for the create_window function from the WidgetCreators class."""

        return self.widget_creators.create_window()

    def create_buttons(self):
        """This method creates all of the buttons in the main window of the Time Stamper program."""

        button_templates = self.template.mapping["buttons"].main_window_templates
        button_str_mapping = {btn.str_key: btn for btn in button_templates}
        self.stored_tk_objs.images = {str_key: self.widget_creators.create_tk_image(btn) \
            for str_key, btn in button_str_mapping.items()}
        assert [self.widget_creators.create_button(button_str_mapping[str_key], self.macros, img) \
            for str_key, img in self.stored_tk_objs.images.items()]

    def create_entries(self):
        """This method creates all of the entries in the main window of the Time Stamper program."""

        entry_templates = self.template.mapping["entries"].main_window_templates
        self.stored_tk_objs.entries = {sh.str_key: \
            self.widget_creators.create_entry(sh, self.macros) for sh in entry_templates}

    def create_labels(self):
        """This method creates all of the labels in the main window of the Time Stamper program."""

        label_templates = self.template.mapping["labels"].main_window_templates
        assert [self.widget_creators.create_label(sh, self.macros) for sh in label_templates]

    def create_texts(self):
        """This method creates all of the texts in the main window of the Time Stamper program."""

        text_templates = self.template.mapping["texts"].main_window_templates
        assert [self.widget_creators.create_text(sh, self.macros) for sh in text_templates]

    def run(self):
        """This method runs the Time Stamper program."""

        # Create the window, buttons, entries, labels and texts.
        self.root = self.create_window()
        self.create_buttons()
        self.create_entries()
        self.create_labels()
        self.create_texts()

        entries_mapping = self.stored_tk_objs.entries

        # Pass the entries containing the hours, minutes, seconds and subseconds to the timer.
        self.time_fields.hours_field = entries_mapping["entry_hours"]
        self.time_fields.minutes_field = entries_mapping["entry_minutes"]
        self.time_fields.seconds_field = entries_mapping["entry_seconds"]
        self.time_fields.subseconds_field = entries_mapping["entry_subseconds"]

        # Map the timer to the timer's string key so that the Macros class can reference it.
        self.macros.button.object_mapping["time_stamper_timer"] = self.timer

        self.root.mainloop()
