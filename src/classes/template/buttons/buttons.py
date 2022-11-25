#-*- coding: utf-8 -*-
"""This module contains the Button class which is
called upon by the constructor of the Fields class."""

from dataclasses import dataclass
from .buttons_file import FileButtons
from .buttons_info import InfoButtons
from .buttons_media import MediaButtons
from .buttons_note import NoteButtons
from .buttons_timestamping import TimestampingButtons

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

        self.str_key = "buttons"

        self.file = FileButtons()
        self.info = InfoButtons()
        self.media = MediaButtons()
        self.notes = NoteButtons()
        self.timestamping = TimestampingButtons()

        # Map the button templates to the windows that they appear in.
        self.template_window_mapping = {
            "window_main":
                (self.media.pause, self.media.play, self.media.stop, self.media.rewind,
                self.media.fast_forward, self.media.record, self.file.output_select,
                self.file.merge_output_files, self.timestamping.timestamp,
                self.timestamping.clear_timestamp, self.info.help, self.info.license,
                self.info.attribution, self.notes.cancel_note, self.notes.save_note),
            "window_help":
                (self.info.help_left_arrow, self.info.help_right_arrow)
        }
