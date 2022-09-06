#-*- coding: utf-8 -*-
"""This module contains the Label class which is
called upon by the constructor of the Fields class."""

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
class Labels():
    """This module, which is called upon by the constructor of the Fields class,
    should be seen as an extension of the TimeStamperTemplate class, with attributes
    pertaining specifically to objects of type tkinter.Label in the Time Stamper program."""

    def __init__(self):

        self.timer = self.TimerLabels()
        self.output_path = self.LabelOutputPath()
        self.rewind_sec = self.LabelRewindSec()
        self.fast_forward_sec = self.LabelFastForwardSec()
        self.timestamp = self.LabelTimestamp()

        self.separate_windows = self.LabelsSeparateWindows()

        # Do not include any labels from the LabelsSeparateWindows class in
        # self.all_templates because self.all_templates is only meant to store the
        # templates for objects that we would like to create immediately when the
        # program starts. Any objects that are part of separate windows will only be
        # created when the user performs an action that triggers that window's creation.
        self.all_templates = (
            self.timer.hrs, self.timer.min, self.timer.dot, self.timer.sec, \
            self.output_path, self.rewind_sec, self.fast_forward_sec, self.timestamp
        )

    @dataclass
    class TimerLabels():
        """This class contains subclasses storing attributes of Tkinter labels
        pertaining specifically to the timer in the Time Stamper program."""

        def __init__(self):

            self.hrs = self.LabelHrs()
            self.min = self.LabelMin()
            self.dot = self.LabelDot()
            self.sec = self.LabelSec()

        @dataclass
        class LabelHrs():
            """This class stores the attributes for the
            label (by default "h") of the timer's hour field."""

            text = "h"

            str_key = "label_hrs"

            background = None
            foreground = None

            wraplength = None

            justify = "left"

            width = 1
            height = 1

            column = 12
            row = 5

            columnspan = 1
            rowspan = 2

            padx = None
            pady = (7, 0)

            ipadx = None
            ipady = None

            sticky = "nw"

            font_family = ""
            font_size = 30
            font_weight = "normal"
            font_slant = "roman"
            font_underline = 0
            font_overstrike = 0

        @dataclass
        class LabelMin():
            """This class stores the attributes for the
            label (by default "m") of the timer's minutes field."""

            text = "m"

            str_key = "label_min"

            background = None
            foreground = None

            wraplength = None

            justify = "left"

            width = 1
            height = 1

            column = 14
            row = 5

            columnspan = 1
            rowspan = 2

            padx = 2
            pady = (7, 0)

            ipadx = None
            ipady = None

            sticky = "nw"

            font_family = ""
            font_size = 30
            font_weight = "normal"
            font_slant = "roman"
            font_underline = 0
            font_overstrike = 0

        @dataclass
        class LabelDot():
            """This class stores the attributes for the label
            (by default ".") displayed before timer's subseconds field."""

            text = "."

            str_key = "label_dot"

            background = None
            foreground = None

            wraplength = None

            justify = "left"

            width = 1
            height = 1

            column = 16
            row = 5

            columnspan = 1
            rowspan = 2

            padx = None
            pady = (7, 0)

            ipadx = None
            ipady = None

            sticky = "nw"

            font_family = ""
            font_size = 30
            font_weight = "normal"
            font_slant = "roman"
            font_underline = 0
            font_overstrike = 0

        @dataclass
        class LabelSec():
            """This class stores the attributes for the label
            (by default "s") of the timer's seconds field."""

            text = "s"

            str_key = "label_s"

            background = None
            foreground = None

            wraplength = None

            justify = "left"

            width = 1
            height = 1

            column = 18
            row = 5

            columnspan = 1
            rowspan = 2

            padx = None
            pady = (7, 0)

            ipadx = None
            ipady = None

            sticky = "nw"

            font_family = ""
            font_size = 30
            font_weight = "normal"
            font_slant = "roman"
            font_underline = 0
            font_overstrike = 0

    @dataclass
    class LabelsSeparateWindows():
        """This class contains subclasses storing attributes of Tkinter labels pertaining
        specifically to windows other than the main window in the Time Stamper program."""

        def __init__(self):
            self.help_message = self.LabelHelpMessage()
            self.license_message = self.LabelLicenseMessage()
            self.merge_output_files_first_message = self.LabelMergeOutputFilesFirstMessage()
            self.merge_output_files_second_message = self.LabelMergeOutputFilesSecondMessage()
            self.merge_output_files_success = self.LabelMergeOutputFilesSuccess()
            self.merge_output_files_failure = self.LabelMergeOutputFilesFailure()

        @dataclass
        class LabelHelpMessage():
            """This class stores the attributes for the label that displays
            instructions to the user when they press the help button."""

            text = \
                "Time Stamper by Benjamin Fertig (2022)\n\n" \
                "To make notes, you must first select an output file.\n" \
                "Press the \"Choose output location\" button and select an output file.\n" \
                "You should choose a file that ends in \".txt\".\n" \
                "If you do not have an output file, you should create one.\n\n" \
                "If you have multiple output files whose notes you would like to merge and sort\n" \
                "based on their timestamps, click the \"Merge output files\" " \
                "button, then select all of the\n" \
                "output files containing timestamped notes you would like to " \
                "merge, and then click \"Open\"\n" \
                "(you can select multiple files using ctrl+click " \
                "on Windows or command+click on Macs).\n" \
                "You will then be prompted to select another file. " \
                "This is where your merged notes will be saved to.\n" \
                "Once you select a file to save your merged " \
                "notes to, your notes will be merged.\n\n" \
                "As long as the timer is not running, you can manually " \
                "edit the time in the bottom-right corner.\n" \
                "The next time you press play or record, the " \
                "timer will start at the time you entered.\n\n" \
                "The current timestamp is displayed to the left " \
                "of the input box at the bottom of the window.\n" \
                "A timestamp of \"[—:—:—.—]\" indicates that no timestamp is set.\n" \
                "When no timestamp is set, any notes you save will " \
                "be timestamped with the timer's current time.\n\n" \
                "To set a timestamp, press the timestamp button " \
                "(to the right of the record button).\n" \
                "All subsequent notes will be saved with the " \
                "time that you pressed the timestamp button " \
                "(until you clear the timestamp or set a new one).\n" \
                "To clear a timestamp, press the \"Clear timestamp\" button.\n\n" \
                "To save a note, type it into the text box at the bottom of " \
                "the screen and then click on the \"Save note\" button.\n" \
                "To cancel a note, press the \"Cancel note\" button.\n" \
                "Both the \"Cancel note\" and \"Save note\" " \
                "buttons will clear the input text box.\n\n" \
                "The pause and play buttons will pause and resume the timer.\n\n" \
                "The stop button will stop the timer and also " \
                "allow you to select a new output file.\n\n" \
                "The rewind and fast-forward buttons will " \
                "rewind/fast-forward the timer the amount of seconds " \
                "that you specified directly below the buttons."

            background = None
            foreground = None

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
                "Contact: github.cqrde@simplelogin.com\n\n" \
                "Please visit this program's GitHub repository for a full list of attributions:\n" \
                "https://github.com/benfertig/timestamper"

            background = None
            foreground = None

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

        @dataclass
        class LabelMergeOutputFilesFirstMessage():
            """This class stores the attributes for the label that displays
            the first instruction to the user on how to merge output files."""

            text = \
                "On the next screen, select all of the Time Stamper\n" \
                "output files whose notes you would like to merge.\n" \
                "You can select multiple files using ctrl+click\n" \
                "(or command+click on Macs).\n\n" \
                "Close this window to proceed."

            background = None
            foreground = None

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

        @dataclass
        class LabelMergeOutputFilesSecondMessage():
            """This class stores the attributes for the label that displays the
            second instruction to the user on how to merge output files."""

            text = \
                "Next, select the file where the merged notes\n" \
                "should be saved to (just a single file this time).\n" \
                "This should be a \".txt\" file.\n" \
                "You can create a new \".txt\" file in the next\n" \
                "window if you do not have one already.\n\n" \
                "Close this window to proceed."

            background = None
            foreground = None

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

        @dataclass
        class LabelMergeOutputFilesSuccess():
            """This class stores the attributes for the label that displays the message
            notifying the user that the program successfully merged the selected output files."""

            text = \
                "MERGE SUCCESS\n\n" \
                "Close this window to proceed."

            background = None
            foreground = None

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


        @dataclass
        class LabelMergeOutputFilesFailure():
            """This class stores the attributes for the label that displays
            the message stating that the program failed to merge output files
            (due to the fact that the user tried to send the merged notes to
            a file whose notes would have already been part of the merge)."""

            text = \
                "MERGE FAILED:\n" \
                "You cannot save merged notes to a file\n" \
                "whose notes are already a part of the merge.\n" \
                "Please try again.\n\n" \
                "Close this window to proceed."

            background = None
            foreground = None

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

    @dataclass
    class LabelOutputPath():
        """This class stores the attributes for the label
        displaying the path to the current output file."""

        display_path_prefix = "Saving notes to: "

        text = "-----PLEASE SELECT AN OUTPUT FILE-----"

        str_key = "label_output_path"

        background = None
        foreground = None

        wraplength = 550

        justify = "left"

        width = None
        height = 1

        column = 9
        row = 0

        columnspan = 9
        rowspan = 1

        padx = None
        pady = None

        ipadx = None
        ipady = None

        sticky = "sw"

        font_family = ""
        font_size = 10
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class LabelRewindSec():
        """This class stores the attributes for the label (by default "sec") of
        the entry where the desired number of seconds to rewind is entered."""

        text = "sec"

        str_key = "label_rewind_sec"

        background = None
        foreground = None

        wraplength = None

        justify = "left"

        width = 3
        height = 1

        column = 4
        row = 1

        columnspan = 1
        rowspan = 1

        padx = None
        pady = None

        ipadx = None
        ipady = None

        sticky = "nw"

        font_family = ""
        font_size = 11
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class LabelFastForwardSec():
        """This class stores the attributes for the label (by default "sec") of the
        entry where the desired number of seconds to fast-forward is entered."""

        text = "sec"

        str_key = "label_fast_forward_sec"

        background = None
        foreground = None

        wraplength = None

        justify = "left"

        width = 3
        height = 1

        column = 6
        row = 1

        columnspan = 1
        rowspan = 1

        padx = None
        pady = None

        ipadx = None
        ipady = None

        sticky = "nw"

        font_family = ""
        font_size = 11
        font_weight = "normal"
        font_slant = "roman"
        font_underline = 0
        font_overstrike = 0

    @dataclass
    class LabelTimestamp():
        """This class stores the attributes for the
        label displaying the current timestamp."""

        text = "[—:—:—.—]"

        str_key = "label_timestamp"

        background = None
        foreground = None

        wraplength = None

        justify = "center"

        width = None
        height = None

        column = 0
        row = 3

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
