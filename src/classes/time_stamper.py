#-*- coding: utf-8 -*-
"""This module contains the TimeStamper class which runs the Time Stamper program."""

from dataclasses import dataclass
from .macros.macros import Macros
from .settings.settings import TimeStamperSettings
from .template.template import TimeStamperTemplate
from .timing.timing import TimeStamperTimer
from .widgets.widgets import Widgets

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


@dataclass
class TimeStamper():
    """This class runs the Time Stamper program."""

    @dataclass
    class TimeFields():
        """This class stores the fields where the time is displayed in the Time Stamper program."""

        hours_field = None
        minutes_field = None
        seconds_field = None
        subseconds_field = None

    def __init__(self):

        self.root = None
        self.template = TimeStamperTemplate()
        settings = TimeStamperSettings()
        self.time_fields = self.TimeFields()
        self.timer = TimeStamperTimer(self)
        self.widgets = Widgets(self.template, settings, self.timer, "window_main")
        self.macros = Macros(self.template, settings, self.widgets, self.timer)

    def run(self):
        """This method runs the Time Stamper program."""

        # Create the main window and all of its widgets.
        self.root = self.widgets.create_entire_window("window_main", self.macros)

        self.root.mainloop()
