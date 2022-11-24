#-*- coding: utf-8 -*-
"""This module contains the Windows class which is called
upon by the constructor of the TimeStamperTemplate class."""

from dataclasses import dataclass
from .windows_info import InfoWindows
from .windows_merge import MergeWindows

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
class Windows():
    """This class, which is called upon by the constructor of the TimeStamperTemplate class,
    should be seen as an extension of the TimeStamperTemplate class with attributes
    pertaining specifically to objects of type tkinter.Tk in the Time Stamper program."""

    def __init__(self):

        self.main = self.WindowMain()
        self.info = InfoWindows()
        self.merge = MergeWindows()

    @dataclass
    class WindowMain():
        """This class stores the attributes for the main window."""

        str_key = "window_main"

        title = "Time Stamper"
        icon_windows = "timestamp_icon.ico"
        icon_mac = "timestamp_icon.icns"

        background = None
        foreground = None

        width = 960
        height = 540

        num_columns = 19
        num_rows = 7
