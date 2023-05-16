#-*- coding: utf-8 -*-
"""This module contains the TimeStamper class. In order to run the Time Stamper program, a user
should create an instance of this TimeStamper class and then call that instance's "run" function."""

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

from sys import platform
from tkinter import Button, Menu
from .macros.macros import Macros
from .settings.settings import TimeStamperSettings
from .template.template import TimeStamperTemplate
from .timing.timing import TimeStamperTimer
from .widgets.widgets import Widgets


class TimeStamper():
    """To run the Time Stamper program, first create an instance
    of this class. Then, call this class' run() method."""

    def __init__(self):

        self.settings = TimeStamperSettings()
        self.timer = TimeStamperTimer(self)
        self.root = None
        self.template = TimeStamperTemplate()
        self.widgets = Widgets(self, "window_main")
        self.macros = Macros(self)
        self.media_player = None

    def remove_func(self, root):
        """This method is used as the command for the Tkinter "Button"
        which, when placed, will remove the menu bar submenus from
        Mac computers while the Time Stamper program is running."""

        root.config(menu=Menu(root))

    def remove_mac_menu_bar_submenus(self, root):
        """This method removes the menu bar submenus from Mac computers while
        the Time Stamper program is running. The only argument that needs
        to be provided is the Time Stamper program's root window."""

        # Initialize the menu bar for the root window.
        menubar = Menu(root)
        root.config(menu=menubar)

        # Create the "button" which, once placed, will remove the menu bar submenus.
        remove_button = Button(root, text="Remove", \
            command=lambda _: self.remove_func(root))

        # "Grid" the "button" that will remove the menu bar submenus (although
        # this "button" will neither be visible nor take up any space).
        remove_button.grid_forget()

    def run(self):
        """This method runs the Time Stamper program."""

        # Create the main window and all of its widgets.
        self.root = self.widgets.create_entire_window("window_main", self.macros)

        # If we are on a Mac, remove all of the submenus from the menu bar.
        if platform.startswith("darwin"):
            self.remove_mac_menu_bar_submenus(self.root)

        # Perform a check to see whether a default OUTPUT file path was provided,
        # and if so, whether that path corresponds to a TEXT file that is suitable
        # for the Time Stamper program. If this is the case, then the program
        # will change its configuration to reflect that an OUTPUT file is active.
        self.macros["button_output_select"](file_full_path=self.settings["output"]["path"])

        # Perform a check to see whether a default MEDIA file path was provided,
        # and if so, whether that path corresponds to a MEDIA file that is suitable
        # for the Time Stamper program. If this is the case, then the program
        # will change its configuration to reflect that a MEDIA file is active.
        self.macros["button_media_select"](file_full_path=self.settings["media"]["path"])

        self.root.mainloop()
