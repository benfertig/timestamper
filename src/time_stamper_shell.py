#-*- coding: utf-8 -*-
"""This module contains the TimeStamperShell class which contains all
of the custom attributes for all of the objects called upon in the
TimeStamper run() method (the method that runs the Time Stamper program)."""

from dataclasses import dataclass
from os import path
from buttons import Buttons
from entries import Entries
from labels import Labels
from texts import Texts

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
class TimeStamperShell():
    """
    This class does not store the TimeStamper objects themselves, but rather stores all of
    the attributes for all of the TimeStamper objects in an organized way. This serves two
    purposes:

        1) People will be able to locate and/or make changes to attributes quickly.

        2) The amount of code that needs to be written in other modules is reduced.
           For example, in the main TimeStamper class, all objects that are of
           the same type (Buttons, Labels, Entries, Texts, etc.) are placed by
           running a loop, where for each object shell x_shell, the position,
           dimensions, initial state, etc. of its corresponding object x can be
           retrieved by referencing x_shell.x_coord, x_shell.y_coord, x_shell.width,
           x_shell.height and x_shell.initial_state among other attributes.
    """

    def __init__(self):

        self.timer = self.Timer()
        self.windows = self.Windows()
        self.path = self.Path()
        self.output_file = self.OutputFile()
        self.fields = self.Fields()

    @dataclass
    class Fields():
        """This class, which is called upon by the constructor of the TimeStamperShell
        class, should be seen as an extension of the TimeStamperShell class with attributes
        pertaining specifically to interactable objects in the Time Stamper program."""

        def __init__(self):
            self.buttons = Buttons()
            self.entries = Entries()
            self.labels = Labels()
            self.texts = Texts()

    @dataclass
    class Windows():
        """This class, which is called upon by the constructor of the TimeStamperShell class,
        should be seen as an extension of the TimeStamperShell class with attributes
        pertaining specifically to objects of type tkinter.Tk in the Time Stamper program."""

        def __init__(self):
            self.main = self.WindowMain()
            self.help = self.WindowHelp()
            self.license = self.WindowLicense()
            self.merge_output_files_first_message = self.WindowMergeOutputFilesFirstMessage()
            self.merge_output_files_second_message = self.WindowMergeOutputFilesSecondMessage()
            self.merge_output_files_success = self.WindowMergeOutputFilesSuccess()
            self.merge_output_files_failure = self.WindowMergeOutputFilesFailure()

        @dataclass
        class WindowMain():
            """This class stores the attributes for the main window."""

            title = "Time Stamper"
            icon = "timestamp_icon.ico"

            background = None
            foreground = None

            width = 960
            height = 540

            num_columns = 19
            num_rows = 7

        @dataclass
        class WindowHelp():
            """This class stores the attributes for the help window."""

            title = "Help"
            icon = "timestamp_icon.ico"

            background = None
            foreground = None

            num_columns = 1
            num_rows = 1

        @dataclass
        class WindowLicense():
            """This class stores the attributes for the license window."""

            title = "License"
            icon = "timestamp_icon.ico"

            background = None
            foreground = None

            num_columns = 1
            num_rows = 1

        @dataclass
        class WindowMergeOutputFilesFirstMessage():
            """This class stores the attributes for the window that displays
            the first instruction to the user on how to merge output files."""

            title = "Step 1: Select files to merge"
            icon = "timestamp_icon.ico"

            background = None
            foreground = None

            num_columns = 1
            num_rows = 1

        @dataclass
        class WindowMergeOutputFilesSecondMessage():
            """This class stores the attributes for the window that displays
            the second instruction to the user on how to merge output files."""

            title = "Step 2: Store merge"
            icon = "timestamp_icon.ico"

            background = None
            foreground = None

            num_columns = 1
            num_rows = 1

        @dataclass
        class WindowMergeOutputFilesSuccess():
            """This class stores the attributes for the window that displays the message
            notifying the user that the program successfully merged the selected output files."""

            title = "Merge success"
            icon = "timestamp_icon.ico"

            background = None
            foreground = None

            num_columns = 1
            num_rows = 1

        @dataclass
        class WindowMergeOutputFilesFailure():
            """This class stores the attributes for the window that displays
            the message stating that the program failed to merge output files
            (due to the fact that the user tried to send the merged notes to
            a file whose notes would have already been part of the merge)."""

            title = "Merge failure"
            icon = "timestamp_icon.ico"

            background = None
            foreground = None

            num_columns = 1
            num_rows = 1

    @dataclass
    class Path():
        """This class stores the attributes for file paths."""

        current_dir = path.abspath(path.dirname(__file__))
        images_dir = path.abspath(path.join(current_dir, "..", "images"))

    @dataclass
    class OutputFile():
        """This class stores the attributes for the output file."""

        encoding = "utf-8"

    @dataclass
    class Timer():
        """This class stores the attributes for timer."""

        str_key = "time_stamper_timer"
