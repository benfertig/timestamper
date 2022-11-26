"""This module contains the LabelsInfo class which
is called upon by the constructor of the Labels class."""

from dataclasses import dataclass
from json import load

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
class InfoLabels():
    """This class contains subclasses storing attributes of Tkinter
    labels that provide information about the program to the user."""

    def __init__(self):
        self.help_image = self.LabelHelpImage()
        self.help_message = self.LabelHelpMessage()
        self.help_page_number = self.LabelHelpPageNumber()
        self.license_message = self.LabelLicenseMessage()

    @dataclass
    class LabelHelpImage():
        """This class stores the attributes for the label
        that displays the image in the help window."""

        text = None

        str_key = "label_help_image"
        window_str_key = "window_help"

        image_file_name = "timestamper_window_labeled.png"
        message_file_name = None

        background = None
        foreground = None

        wraplength = None

        justify = "left"

        width = None
        height = None

        column = 0
        row = 0

        columnspan = 2
        rowspan = 1

        padx = None
        pady = None

        ipadx = None
        ipady = None

        sticky = "nw"

        font_family = ""
        font_size = 12
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class LabelHelpPageNumber():
        """This class stores the attributes for the label that
        displays the current page number in the help window."""

        page_numbers = {1: (18, 2), 2: (1, 3), 3: (2, 4), 4: (3, 4.1), 4.1: (4, 5),
                            5: (4.1, 5.1), 5.1: (5, 6), 6: (5.1, 7), 7: (6, 8), 8: (7, 9),
                            9: (8, 10), 10: (9, 11), 11: (10, 11.1), 11.1: (11, 11.2),
                            11.2: (11.1, 12), 12: (11.2, 13), 13: (12, 14), 14: (13, 15),
                            15: (14, 16), 16: (15, 17), 17: (16, 18), 18: (17, 1)}

        current_page = 1
        first_page = 1
        last_page = 18

        text = str(first_page)

        str_key = "label_help_page_number"
        window_str_key = "window_help"

        image_file_name = None
        message_file_name = None

        background = None
        foreground = None

        wraplength = None

        justify = "center"

        width = None
        height = None

        column = 0
        row = 2

        columnspan = 2
        rowspan = 1

        padx = None
        pady = None

        ipadx = None
        ipady = None

        sticky = "n"

        font_family = ""
        font_size = 14
        font_weight = "bold"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class LabelHelpMessage():
        """This class stores the attributes for the label
        that displays the message the help window."""

        text = None

        str_key = "label_help_message"
        window_str_key = "window_help"

        image_file_name = None
        message_file_name = "help_messages.json"
        message_file_encoding = "utf-8"
        json_first_message_key = "1"
        loaded_message_text = None

        background = None
        foreground = None

        wraplength = 960

        justify = "left"

        width = None
        height = None

        column = 0
        row = 3

        columnspan = 2
        rowspan = 1

        padx = None
        pady = None

        ipadx = None
        ipady = None

        sticky = "w"

        font_family = ""
        font_size = 12
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class LabelLicenseMessage():
        """This class stores the attributes for the label that displays
        the license in a new window when the "License" button is pressed."""

        text = None

        str_key = "label_license"
        window_str_key = "window_license"

        image_file_name = None
        message_file_name = "license_notice.txt"
        message_file_encoding = "utf-8"
        loaded_message_text = None

        background = None
        foreground = None

        wraplength = None

        justify = "left"

        width = None
        height = None

        column = 0
        row = 0

        columnspan = 1
        rowspan = 1

        padx = None
        pady = None

        ipadx = None
        ipady = None

        sticky = "nw"

        font_family = ""
        font_size = 12
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0
