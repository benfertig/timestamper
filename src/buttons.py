#-*- coding: utf-8 -*-
"""This module contains the Button class which is
called upon by the constructor of the Fields class."""

from dataclasses import dataclass
from os import path
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
class Buttons():
    """This class, which is called upon by the constructor of the Fields class,
    should be seen as an extension of the TimeStamperShell class with attributes
    pertaining specifically to objects of type tkinter.Button in the Time Stamper program."""

    def __init__(self):

        self.media = self.MediaButtons()
        self.other = self.OtherButtons()

        # Save all of the shells in a list
        self.all_shells = (
            self.media.pause, self.media.play, self.media.stop, self.media.rewind, \
            self.media.fast_forward, self.media.record, self.media.timestamp, \
            self.other.output_select, self.other.merge_output_files, self.other.clear_timestamp, \
            self.other.help, self.other.license, self.other.cancel_note, self.other.save_note
        )

    @dataclass
    class MediaButtons():
        """This class stores the attributes for the media buttons (pause, play, stop,
        rewind, fast-foward, record and timestamp) in the Time Stamper program."""

        def __init__(self):
            self.pause = self.ButtonPause()
            self.play = self.ButtonPlay()
            self.stop = self.ButtonStop()
            self.rewind = self.ButtonRewind()
            self.fast_forward = self.ButtonFastForward()
            self.record = self.ButtonRecord()
            self.timestamp = self.ButtonTimestamp()

        @dataclass
        class ButtonPause():
            """This class stores the attributes for the pause button."""

            initial_state = DISABLED

            str_key = "button_pause"

            text = None
            image_file_name = "pause.png"

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

            str_key = "button_play"

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

            str_key = "button_stop"

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

            str_key = "button_rewind"

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

            str_key = "button_fast_forward"

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

            str_key = "button_record"

            print_on_press = "##### BEGIN #####"

            to_enable = ("button_pause", "button_stop", "button_timestamp")
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

        @dataclass
        class ButtonTimestamp():
            """This class stores the attributes for the timestamp button."""

            initial_state = NORMAL

            text = None
            image_file_name = "timestamp.png"

            str_key = "button_timestamp"

            to_enable = ()
            to_disable = ()

            background = None
            foreground = None

            width = 48
            height = 48

            column = 8
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
    class OtherButtons():
        """This class stores the attributes the non-media buttons (output select,
        help, cancel note and save note) in the Time Stamper program."""

        def __init__(self):
            self.output_select = self.ButtonOutputSelect()
            self.merge_output_files = self.ButtonMergeOutputFiles()
            self.help = self.ButtonHelp()
            self.license = self.ButtonLicense()
            self.cancel_note = self.ButtonCancelNote()
            self.save_note = self.ButtonSaveNote()
            self.clear_timestamp = self.ButtonClearTimestamp()

        @dataclass
        class ButtonOutputSelect():
            """This class stores the attributes for the output file selection button."""

            initial_state = NORMAL

            text = "Choose output location"
            image_file_name = None

            str_key = "button_output_select"

            image_file_name = None

            starting_dir = path.abspath(path.join(path.dirname( __file__ ), ".."))

            background = None
            foreground = None

            width = None
            height = 1

            column = 9
            row = 0

            columnspan = 1
            rowspan = 1

            padx = None
            pady = (5, 26)

            ipadx = None
            ipady = None

            sticky = "nsew"

            to_enable_toggle = ("button_record", "button_save_note")

            font_family = ""
            font_size = 10
            font_weight = "normal"
            font_slant = "roman"
            font_underline = 0
            font_overstrike = 0

        @dataclass
        class ButtonMergeOutputFiles():
            """This class stores the attributes for the merge output files button."""

            initial_state = NORMAL

            text = "Merge output files"
            image_file_name = None

            str_key = "button_merge_output_files"

            image_file_name = None

            starting_dir = path.abspath(path.join(path.dirname( __file__ ), ".."))

            background = None
            foreground = None

            width = None
            height = 1

            column = 10
            row = 0

            columnspan = 1
            rowspan = 1

            padx = None
            pady = (5, 26)

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
        class ButtonClearTimestamp():
            """This class stores the attributes for the clear timestamp button."""

            initial_state = NORMAL

            text = "Clear timestamp"
            image_file_name = None

            str_key = "button_clear_timestamp"

            background = None
            foreground = None

            width = None
            height = 1

            column = 0
            row = 4

            columnspan = 2
            rowspan = 1

            padx = (11, 11)
            pady = (7, 7)

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
        class ButtonHelp():
            """This class stores the attributes for the help button."""

            initial_state = NORMAL

            text = "Help"
            image_file_name = None

            str_key = "button_help"

            background = None
            foreground = None

            width = 5
            height = 1

            column = 0
            row = 5

            columnspan = 2
            rowspan = 1

            padx = (11, 11)
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
        class ButtonLicense():
            """This class stores the attributes for the license button."""

            initial_state = NORMAL

            text = "License/Credit"
            image_file_name = None

            str_key = "button_license"

            background = None
            foreground = None

            width = 5
            height = 1

            column = 0
            row = 6

            columnspan = 2
            rowspan = 1

            padx = (11, 11)
            pady = (0, 8)

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
        class ButtonCancelNote():
            """This class stores the attributes for the cancel note button."""

            initial_state = NORMAL

            text = "Cancel note"
            image_file_name = None

            str_key = "button_cancel_note"

            to_enable = ("button_timestamp",)
            to_disable = ()

            background = "#E06666"
            foreground = None

            width = 12
            height = 1

            column = 2
            row = 5

            columnspan = 7
            rowspan = 2

            padx = (14, 7)
            pady = (8, 8)

            ipadx = None
            ipady = None

            sticky = "nsew"

            font_family = ""
            font_size = 19
            font_weight = "normal"
            font_slant = "roman"
            font_underline = 0
            font_overstrike = 0

        @dataclass
        class ButtonSaveNote():
            """This class stores the attributes for the save note button."""

            initial_state = DISABLED

            text = "Save note"

            str_key = "button_save_note"

            image_file_name = None

            to_enable = ("button_timestamp",)
            to_disable = ()

            background = "#93C47D"
            foreground = None

            width = 12
            height = 1

            column = 9
            row = 5

            columnspan = 2
            rowspan = 2

            padx = (7, 14)
            pady = (8, 8)

            ipadx = None
            ipady = None

            sticky = "nsew"

            font_family = ""
            font_size = 19
            font_weight = "normal"
            font_slant = "roman"
            font_underline = 0
            font_overstrike = 0
