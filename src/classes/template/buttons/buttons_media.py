#-*- coding: utf-8 -*-
"""This module contains the MediaButtons class which is
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
class MediaButtons():
    """This class stores the attributes for the media buttons (pause, play, stop,
    rewind, fast-foward and record) in the Time Stamper program."""

    def __init__(self):
        self.pause = self.ButtonPause()
        self.play = self.ButtonPlay()
        self.stop = self.ButtonStop()
        self.rewind = self.ButtonRewind()
        self.fast_forward = self.ButtonFastForward()
        self.record = self.ButtonRecord()

    @dataclass
    class ButtonPause():
        """This class stores the attributes for the pause button."""

        initial_state = DISABLED

        str_key = "button_pause"

        window_str_key = "window_main"

        mac_disabled_color = "#d3d3d3"

        text = None

        image_file_name = "pause.png"
        message_file_name = None

        to_enable = ("button_play", "entry_hours", "entry_minutes", \
            "entry_seconds", "entry_subseconds")
        to_disable = ("button_pause",)

        background = None
        foreground = None

        width = 48
        height = 48

        column = 0
        row = 0

        columnspan = 1
        rowspan = 1

        padx = (5, 0)
        pady = (5, 0)

        ipadx = None
        ipady = None

        sticky = "nsew"

        font_family = ""
        font_size = 12
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class ButtonPlay():
        """This class stores the attributes for the play button."""

        initial_state = DISABLED

        text = None

        image_file_name = "play.png"
        message_file_name = None

        str_key = "button_play"

        window_str_key = "window_main"

        mac_disabled_color = "#d3d3d3"

        to_enable = ("button_pause",)
        to_disable = ("button_play", "entry_hours", "entry_minutes", \
            "entry_seconds", "entry_subseconds")

        background = None
        foreground = None

        width = 48
        height = 48

        column = 1
        row = 0

        columnspan = 1
        rowspan = 1

        padx = None
        pady = (5, 0)

        ipadx = None
        ipady = None

        sticky = "nsew"

        font_family = ""
        font_size = 12
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class ButtonStop():
        """This class stores the attributes for the stop button."""

        initial_state = DISABLED

        text = None

        image_file_name = "stop.png"
        message_file_name = None

        str_key = "button_stop"

        window_str_key = "window_main"

        mac_disabled_color = "#d3d3d3"

        print_on_press = "##### END #####"

        to_enable = ("button_record", "button_output_select", "button_merge_output_files", \
            "entry_hours", "entry_minutes", "entry_seconds", "entry_subseconds")
        to_disable = ("button_pause", "button_play", "button_stop")

        background = None
        foreground = None

        width = 48
        height = 48

        column = 2
        row = 0

        columnspan = 1
        rowspan = 1

        padx = None
        pady = (5, 0)

        ipadx = None
        ipady = None

        sticky = "nsew"

        font_family = ""
        font_size = 12
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class ButtonRewind():
        """This class stores the attributes for the rewind button."""

        initial_state = NORMAL

        text = None

        image_file_name = "rewind.png"
        message_file_name = None

        str_key = "button_rewind"

        window_str_key = "window_main"

        mac_disabled_color = "#d3d3d3"

        background = None
        foreground = None

        width = 48
        height = 48

        column = 3
        row = 0

        columnspan = 2
        rowspan = 1

        padx = None
        pady = (5, 0)

        ipadx = None
        ipady = None

        sticky = "nsew"

        font_family = ""
        font_size = 12
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class ButtonFastForward():
        """This class stores the attributes for the fast-forward button."""

        initial_state = NORMAL

        text = None

        image_file_name = "fast_forward.png"
        message_file_name = None

        str_key = "button_fast_forward"

        window_str_key = "window_main"

        mac_disabled_color = "#d3d3d3"

        background = None
        foreground = None

        width = 48
        height = 48

        column = 5
        row = 0

        columnspan = 2
        rowspan = 1

        padx = None
        pady = (5, 0)

        ipadx = None
        ipady = None

        sticky = "nsew"

        font_family = ""
        font_size = 12
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class ButtonRecord():
        """This class stores the attributes for the record button."""

        initial_state = DISABLED

        text = None

        image_file_name = "record.png"
        message_file_name = None

        str_key = "button_record"

        window_str_key = "window_main"

        mac_disabled_color = "#d3d3d3"

        print_on_press = "##### BEGIN #####"

        to_enable = ("button_pause", "button_stop")
        to_disable = ("button_record", "button_output_select", "button_merge_output_files", \
            "entry_hours", "entry_minutes", "entry_seconds", "entry_subseconds")

        background = None
        foreground = None

        width = 48
        height = 48

        column = 7
        row = 0

        columnspan = 1
        rowspan = 1

        padx = None
        pady = (5, 0)

        ipadx = None
        ipady = None

        sticky = "nsew"

        font_family = ""
        font_size = 12
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0
