#-*- coding: utf-8 -*-
"""This module contains the InfoButtons class which is
called upon by the constructor of the Buttons class."""

from dataclasses import dataclass
from tkinter import DISABLED, NORMAL

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
class InfoButtons():
    """This class stores the attributes for buttons associated with information."""

    def __init__(self):
        self.attribution = self.ButtonAttribution()
        self.help = self.ButtonHelp()
        self.help_left_arrow = self.ButtonHelpLeftArrow()
        self.help_right_arrow = self.ButtonHelpRightArrow()
        self.license = self.ButtonLicense()

    @dataclass
    class ButtonHelp():
        """This class stores the attributes for the help button."""

        initial_state = NORMAL

        text = "Help"
        image_file_name = None

        str_key = "button_help"

        window_str_key = "window_main"

        mac_disabled_color = "#d3d3d3"

        background = None
        foreground = None

        width = 5
        height = 1

        column = 0
        row = 5

        columnspan = 1
        rowspan = 1

        padx = (10, 0)
        pady = (8, 0)

        ipadx = None
        ipady = None

        sticky = "nsew"

        font_family = ""
        font_size = 10
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class ButtonHelpLeftArrow():
        """This class stores the attributes for the help button."""

        initial_state = DISABLED

        text = None
        image_file_name = "arrow_left.png"

        str_key = "button_help_left_arrow"

        window_str_key = "window_help"

        mac_disabled_color = "#d3d3d3"

        background = None
        foreground = None

        width = 48
        height = 48

        column = 0
        row = 1

        columnspan = 1
        rowspan = 1

        padx = None
        pady = None

        ipadx = None
        ipady = None

        sticky = "nsew"

        font_family = ""
        font_size = 10
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class ButtonHelpRightArrow():
        """This class stores the attributes for the help button."""

        initial_state = NORMAL

        text = None
        image_file_name = "arrow_right.png"

        str_key = "button_help_right_arrow"

        window_str_key = "window_help"

        mac_disabled_color = "#d3d3d3"

        background = None
        foreground = None

        width = 48
        height = 48

        column = 1
        row = 1

        columnspan = 1
        rowspan = 1

        padx = None
        pady = None

        ipadx = None
        ipady = None

        sticky = "nsew"

        font_family = ""
        font_size = 10
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class ButtonLicense():
        """This class stores the attributes for the license button."""

        initial_state = NORMAL

        text = "License"
        image_file_name = None

        str_key = "button_license"

        window_str_key = "window_main"

        mac_disabled_color = "#d3d3d3"

        background = None
        foreground = None

        width = 5
        height = 1

        column = 1
        row = 5

        columnspan = 1
        rowspan = 1

        padx = (0, 10)
        pady = (8, 0)

        ipadx = None
        ipady = None

        sticky = "nsew"

        font_family = ""
        font_size = 8
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class ButtonAttribution():
        """This class stores the attributes for the attribution button."""

        initial_state = NORMAL

        text = "Attribution"
        image_file_name = None

        str_key = "button_attribution"

        window_str_key = "window_main"

        mac_disabled_color = "#d3d3d3"

        background = None
        foreground = None

        width = 5
        height = 1

        column = 0
        row = 6

        columnspan = 2
        rowspan = 1

        padx = (10, 10)
        pady = (0, 8)

        ipadx = None
        ipady = None

        sticky = "nsew"

        font_family = ""
        font_size = 10
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0
