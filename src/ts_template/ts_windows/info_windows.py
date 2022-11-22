"""This module contains the InfoWindows class which is
called upon by the constructor of the Windows class."""

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
class InfoWindows():
    """This class stores the templates of all windows that are associated
    with providing information about the program to the user."""

    def __init__(self):
        self.help = self.WindowHelp()
        self.license = self.WindowLicense()
        self.attribution = self.WindowAttribution()

    @dataclass
    class WindowHelp():
        """This class stores the attributes for the help window."""

        str_key = "window_help"

        title = "Help"
        icon_windows = "timestamp_icon.ico"
        icon_mac = "timestamp_icon.icns"

        background = None
        foreground = None

        num_columns = 1
        num_rows = 1

    @dataclass
    class WindowLicense():
        """This class stores the attributes for the license window."""

        str_key = "window_license"

        title = "License"
        icon_windows = "timestamp_icon.ico"
        icon_mac = "timestamp_icon.icns"

        background = None
        foreground = None

        num_columns = 1
        num_rows = 1

    @dataclass
    class WindowAttribution():
        """This class stores the attributes for the attribution window."""

        str_key = "window_attribution"

        title = "Attribution"
        icon_windows = "timestamp_icon.ico"
        icon_mac = "timestamp_icon.icns"

        background = None
        foreground = None

        num_columns = 1
        num_rows = 1
