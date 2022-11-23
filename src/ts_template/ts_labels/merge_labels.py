"""This module contains the MergeLabels class which
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
class MergeLabels():
    """This class stores the templates of all labels
    associated with the "Merge output files" function."""

    def __init__(self):
        self.first_message = self.LabelMergeOutputFilesFirstMessage()
        self.second_message = self.LabelMergeOutputFilesSecondMessage()
        self.success = self.LabelMergeOutputFilesSuccess()
        self.failure = self.LabelMergeOutputFilesFailure()

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

        str_key = "label_merge_first_message"
        window_str_key = "window_merge_first_message"

        image_file_name = None

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
    class LabelMergeOutputFilesSecondMessage():
        """This class stores the attributes for the label that displays the
        second instruction to the user on how to merge output files."""

        text = \
            "Next, select the file where the merged notes\n" \
            "should be saved to (just a single file this time).\n" \
            "This should be a \".txt\" file.\n\n" \
            "Close this window to proceed."

        str_key = "label_merge_second_message"
        window_str_key = "window_merge_second_message"

        image_file_name = None

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

        str_key = "label_merge_success"
        window_str_key = "window_merge_success"

        image_file_name = None

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
    class LabelMergeOutputFilesFailure():
        """This class stores the attributes for the label that displays
        the message stating that the program failed to merge output files
        (due to the fact that the user tried to send the merged notes to
        a file whose notes would have already been part of the merge)."""

        text = \
            "MERGE FAILED\n\n" \
            "You cannot save merged notes to a file\n" \
            "whose notes are already a part of the merge.\n" \
            "Please try again.\n\n" \
            "Close this window to proceed."

        str_key = "label_merge_failure"
        window_str_key = "window_merge_failure"

        image_file_name = None

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
