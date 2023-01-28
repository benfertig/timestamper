#-*- coding: utf-8 -*-
"""This module not only contains the TimeStamper class, but also, if run
in Python 3, will initialize an instance of that class and execute its
"run" function (see the very bottom of this file). Therefore, a person who
wants to run the Time Stamper program should run this file in Python 3."""

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

from dataclasses import dataclass
from classes.macros.macros import Macros
from classes.settings.settings import TimeStamperSettings
from classes.template.template import TimeStamperTemplate
from classes.timing.timing import TimeStamperTimer
from classes.widgets.widgets import Widgets


@dataclass
class TimeStamper():
    """To run the Time Stamper program, first create an instance
    of this class. Then, call this class' run() method."""

    def __init__(self):

        settings = TimeStamperSettings()

        self.timer = TimeStamperTimer(self)
        self.root = None
        self.template = TimeStamperTemplate()
        self.widgets = Widgets(self, settings, "window_main")
        self.macros = Macros(self, settings)
        self.audio_source, self.audio_player = None, None

    def run(self):
        """This method runs the Time Stamper program."""

        # Create the main window and all of its widgets.
        self.root = self.widgets.create_entire_window("window_main", self.macros)

        # Perform a check to see whether a default OUTPUT file path was provided,
        # and if so, whether that path corresponds to a TEXT file that is suitable
        # for the Time Stamper program. If this is the case, then the program
        # will change its configuration to reflect that an OUTPUT file is active.
        self.macros.validate_output_file()

        # Perform a check to see whether a default AUDIO file path was provided,
        # and if so, whether that path corresponds to an AUDIO file that is suitable
        # for the Time Stamper program. If this is the case, then the program
        # will change its configuration to reflect that an AUDIO file is active.
        self.macros.validate_audio_player()

        self.root.mainloop()


tstmpr = TimeStamper()
tstmpr.run()
