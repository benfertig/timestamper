#-*- coding: utf-8 -*-
"""This module contains the Button class which is
called upon by the constructor of the Fields class."""

from dataclasses import dataclass
from .media_buttons import MediaButtons
from .other_buttons import OtherButtons

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
class Buttons():
    """This class, which is called upon by the constructor of the Fields class, should
    be seen as an extension of the TimeStamperTemplate class with attributes pertaining
    specifically to objects of type tkinter.Button in the Time Stamper program."""

    def __init__(self):

        self.media = MediaButtons()
        self.other = OtherButtons()

        # Save all of the templates in a list
        self.all_templates = (
            self.media.pause, self.media.play, self.media.stop, self.media.rewind, \
            self.media.fast_forward, self.media.record, self.media.timestamp, \
            self.other.output_select, self.other.merge_output_files,
            self.other.clear_timestamp, self.other.help, self.other.license, \
            self.other.cancel_note, self.other.save_note
        )
