#-*- coding: utf-8 -*-
"""This module contains the TimeStamper class. In order to run the Time Stamper program, a user
should create an instance of this TimeStamper class and then call that instance's "run" function."""

from sys import platform
from tkinter import Button, Menu
from vlc import MediaPlayer

import classes

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
    """To run the Time Stamper program, first create an instance
    of this class. Then, call this class' run() method."""

    def __init__(self):
        self.root = None
        self.output_path = ""
        self.media_player = MediaPlayer()
        self.log_file = None
        self.play_press_time = 0.0

    def remove_func(self):
        """This method is used as the command for the Tkinter "Button"
        which, when placed, will remove the menu bar submenus from
        Mac computers while the Time Stamper program is running."""

        self.root.config(menu=Menu(self.root))

    def remove_mac_menu_bar_submenus(self):
        """This method removes the menu bar submenus from Mac
        computers while the Time Stamper program is running."""

        # Initialize the menu bar for the root window.
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        # Create the "button" which, once placed, will remove the menu bar submenus.
        remove_button = Button(self.root, text="Remove", command = self.remove_func)

        # "Grid" the "button" that will remove the menu bar submenus (although
        # this "button" will neither be visible nor take up any space).
        remove_button.grid_forget()

    def run(self):
        """This method runs the Time Stamper program."""

        # Create the main window and all of its widgets.
        self.root = classes.widgets.create_entire_window("window_main", is_main_window=True)

        # Ensure that the initial timestamp format matches user specifications.
        classes.timer.update_timestamp(truncate_to=2)

        # If we are on a Mac, remove all of the submenus from the menu bar.
        if platform.startswith("darwin"):
            self.remove_mac_menu_bar_submenus()

        # Perform a check to see whether a default OUTPUT file path was provided, and
        # if so, whether that path corresponds to a TEXT file that is suitable for the
        # Time Stamper program. If this is the case, then the program will change its
        # configuration to reflect that an OUTPUT file IS active. Otherwise, the program
        # will change its configuration to reflect that an OUTPUT file IS NOT active.
        classes.macros["button_output_select"](\
            file_full_path=classes.settings["output"]["path"], erase_if_empty=True)

        # Perform a check to see whether a default MEDIA file path was provided, and
        # if so, whether that path corresponds to a MEDIA file that is suitable for the
        # Time Stamper program. If this is the case, then the program will change its
        # configuration to reflect that a MEDIA file IS active. Otherwise, the program
        # will change its configuration to reflect that a MEDIA file IS NOT active.
        classes.macros["button_media_select"](\
            file_full_path=classes.settings["media"]["path"], erase_if_empty=True)

        self.root.mainloop()
