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

    def __init__(self, template):
        """This constructor initializes the Time Stamper template (which stores
        all of the attributes for objects in the the Time Stamper program), the
        macros (which store all of the macros for buttons in the Time Stamper
        program) and the timer (which runs the timer for the Time Stamper program)."""

        self.root = None
        self.template = template
        self.time_fields = self.TimeFields()
        self.widget_creators = WidgetCreators(template.mapping, template.images_dir, "window_main")
        self.timer = TimeStamperTimer(self)
        self.macros = Macros(template, self.widget_creators, self.timer)

    def store_time_fields(self, entries_mapping):
        """This method stores the widgets that display the timer's current
        time, which will be referenced by the TimeStamperTimer class"""

        self.time_fields.hours_field = entries_mapping["entry_hours"]
        self.time_fields.minutes_field = entries_mapping["entry_minutes"]
        self.time_fields.seconds_field = entries_mapping["entry_seconds"]
        self.time_fields.subseconds_field = entries_mapping["entry_subseconds"]

    def stop_macro_wrapper(self):
        """This method is a wrapper for the stop macro."""
        self.macros.button.mapping["button_stop"]()

    def run(self):
        """This method runs the Time Stamper program."""

        self.root = self.widget_creators.create_entire_window("window_main", \
            self.macros.button.mapping)

        # Store the entries containing the hours, minutes, seconds and subseconds
        # so that the TimeStamperTimer class can reference them later.
        self.store_time_fields(self.widget_creators.mapping)

        # Map the timer to the WidgetCreators mapping so that the macros can reference it.
        self.widget_creators.mapping["time_stamper_timer"] = self.timer

        self.root.mainloop()
