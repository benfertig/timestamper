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

    def __init__(self):

        settings = TimeStamperSettings()
        timer = TimeStamperTimer(self)

        self.root = None
        self.template = TimeStamperTemplate()
        self.widgets = Widgets(self.template, settings, timer, "window_main")
        self.macros = Macros(self, settings, timer)
        self.audio_source, self.audio_player = None, None

    def run(self):
        """This method runs the Time Stamper program."""

        # Create the main window and all of its widgets.
        self.root = self.widgets.create_entire_window("window_main", self.macros)
        self.root.mainloop()
