#-*- coding: utf-8 -*-
"""This module contains the Text class which is
called upon by the constructor of the Fields class."""

from dataclasses import dataclass
from tkinter import NORMAL, DISABLED

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
class Texts():
    """This module, which is called upon by the constructor of the Fields class,
    should be seen as an extension of the TimeStamperTemplate class, with attributes
    pertaining specifically to objects of type tkinter.Text in the Time Stamper program."""

    def __init__(self):

        self.str_key = "texts"

        self.log = self.TextLog()
        self.current_note = self.TextCurrentNote()
        self.attribution = self.TextAttribution()

        # Map the text templates to the windows that they appear in.
        self.template_window_mapping = {
            "window_main":
                (self.log, self.current_note),
            "window_attribution":
                (self.attribution,)
        }

    @dataclass
    class TextLog():
        """This class stores the attributes for the text
        box where the user's past notes are displayed."""

        text = ""

        initial_state = DISABLED

        str_key = "text_log"

        window_str_key = "window_main"

        width = 105
        height = 14

        column = 0
        row = 2

        columnspan = 20
        rowspan = 1

        padx = (5, 5)
        pady = None

        ipadx = None
        ipady = 33

        sticky = "nsew"

        font_family = ""
        font_size = 12
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class TextCurrentNote():
        """This class stores the attributes for the text
        box where the user's current note is displayed."""

        text = ""

        initial_state = NORMAL

        str_key = "text_current_note"

        window_str_key = "window_main"

        width = 93
        height = 3

        column = 2
        row = 3

        columnspan = 18
        rowspan = 2

        padx = (0, 5)
        pady = (6, 0)

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
    class TextAttribution():
        """This class stores the attributes for the text box in the "Attribution" window."""

        attr_msg_file_name = "messages/attribution.txt"
        attr_msg_encoding = "utf-8"
        text = ""

        with open(attr_msg_file_name, "r", encoding=attr_msg_encoding) as attr_msg:
            text = attr_msg.read()

        initial_state = DISABLED

        str_key = "text_attribution"

        window_str_key = "window_attribution"

        width = 107
        height = 30

        column = 1
        row = 1

        columnspan = 1
        rowspan = 1

        padx = (5, 5)
        pady = (5, 5)

        ipadx = None
        ipady = None

        sticky = "nsew"

        font_family = ""
        font_size = 12
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0
