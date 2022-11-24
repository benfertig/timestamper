"""This module contains the MergeWindows class which is
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
class MergeWindows():
    """This class stores the templates of all windows that are
    associated with the program's "Merge output files" function."""

    def __init__(self):
        self.first_message = self.WindowMergeOutputFilesFirstMessage()
        self.second_message = self.WindowMergeOutputFilesSecondMessage()
        self.success = self.WindowMergeOutputFilesSuccess()
        self.failure = self.WindowMergeOutputFilesFailure()

    @dataclass
    class WindowMergeOutputFilesFirstMessage():
        """This class stores the attributes for the window that displays
        the first instruction to the user on how to merge output files."""

        str_key = "window_merge_first_message"

        title = "Step 1: Select files to merge"
        icon_windows = "timestamp_icon.ico"
        icon_mac = "timestamp_icon.icns"

        background = None
        foreground = None

        width = None
        height = None

        num_columns = 1
        num_rows = 1

    @dataclass
    class WindowMergeOutputFilesSecondMessage():
        """This class stores the attributes for the window that displays
        the second instruction to the user on how to merge output files."""

        str_key = "window_merge_second_message"

        title = "Step 2: Store merge"
        icon_windows = "timestamp_icon.ico"
        icon_mac = "timestamp_icon.icns"

        background = None
        foreground = None

        width = None
        height = None

        num_columns = 1
        num_rows = 1

    @dataclass
    class WindowMergeOutputFilesSuccess():
        """This class stores the attributes for the window that
        displays the message notifying the user that the program
        successfully merged the selected output files."""

        str_key = "window_merge_success"

        title = "Merge success"
        icon_windows = "timestamp_icon.ico"
        icon_mac = "timestamp_icon.icns"

        background = None
        foreground = None

        width = None
        height = None

        num_columns = 1
        num_rows = 1

    @dataclass
    class WindowMergeOutputFilesFailure():
        """This class stores the attributes for the window that displays
        the message stating that the program failed to merge output files
        (due to the fact that the user tried to send the merged notes to
        a file whose notes would have already been part of the merge)."""

        str_key = "window_merge_failure"

        title = "Merge failure"
        icon_windows = "timestamp_icon.ico"
        icon_mac = "timestamp_icon.icns"

        background = None
        foreground = None

        width = None
        height = None

        num_columns = 1
        num_rows = 1
