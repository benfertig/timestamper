"""This module contains the LabelsInfo class which
is called upon by the constructor of the Labels class."""

from dataclasses import dataclass

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
        self.help_message = self.LabelHelpMessage()
        self.license_message = self.LabelLicenseMessage()

    @dataclass
    class LabelHelpMessage():
        """This class stores the attributes for the label that displays
        instructions to the user when they press the help button."""

        help_message_file_name = "help_message.txt"
        help_message_encoding = "utf-8"
        text = ""

        with open(help_message_file_name, "r", encoding=help_message_encoding) as help_message:
            text = help_message.read()

        str_key = "label_help"

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

    @dataclass
    class LabelLicenseMessage():
        """This class stores the attributes for the label that displays
        the license in a new window when the \"License\" button is pressed."""

        text = \
            "Time Stamper: Run a timer and write automatically timestamped notes.\n" \
            "Copyright (C) 2022 Benjamin Fertig\n\n" \
            "This program is free software: you can redistribute it and/or modify\n" \
            "it under the terms of the GNU General Public License as published by\n" \
            "the Free Software Foundation, either version 3 of the License, or\n" \
            "(at your option) any later version.\n\n" \
            "This program is distributed in the hope that it will be useful,\n" \
            "but WITHOUT ANY WARRANTY; without even the implied warranty of\n" \
            "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n" \
            "GNU General Public License for more details.\n" \
            "You should have received a copy of the GNU General Public License\n" \
            "along with this program.  If not, see <https://www.gnu.org/licenses/>.\n\n" \
            "Contact: github.cqrde@simplelogin.com"

        str_key = "label_license"

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
