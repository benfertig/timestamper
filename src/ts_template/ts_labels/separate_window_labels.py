#-*- coding: utf-8 -*-
"""This module contains the SeparateWindowLabels class which
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
class SeparateWindowLabels():
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
            "The current timestamp will be synchronized with the timer until you\n" \
            "press the timestamp button (located directly below the timestamp).\n" \
            "When you press the timestamp button, the timestamp will be set to the\n" \
            "exact reading that the timer was at when you pressed the button.\n\n" \
            "To clear a timestamp, press the clear timestamp button " \
            "(located to the right of the timestamp button).\n" \
            "Doing so will unfreeze the timestamp reading, resynchronizing it with the timer.\n\n" \
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
            "You can select one file OR you can select multiple\n" \
            "files using ctrl+click (or command+click on Macs).\n\n" \
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
            "This should be a \".txt\" file.\n\n" \
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

        def success_message(self, merged_output_file_name):
            """This method returns the message stating that the merging
            of the output files was a success, inserting the name of the
            file storing the merged notes at the appropriate place."""

            return "MERGE SUCCESS\n\n" \
                "Your merged notes have been saved in:\n" \
                f"\"{merged_output_file_name}\".\n\n" \
                "Close this window to proceed."

        text = ""

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
