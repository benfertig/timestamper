#-*- coding: utf-8 -*-
"""This module contains the TimeStamperTemplate class which contains all
of the custom attributes for all of the objects called upon in the
TimeStamper run() method (the method that runs the Time Stamper program)."""

from dataclasses import dataclass
import sys
from os import path
from .ts_buttons.buttons import Buttons
from .ts_entries.entries import Entries
from .ts_labels.labels import Labels
from .ts_texts.texts import Texts
from .ts_windows.windows import Windows

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


def resource_path():
    """This method gets the absolute path to the resource."""

    try:
        res_path = sys._MEIPASS
    except AttributeError:
        res_path = path.abspath(".")

    return res_path


@dataclass
class TimeStamperTemplate():
    """
    This class does not store the TimeStamper objects themselves, but rather stores all of
    the attributes for all of the TimeStamper objects in an organized way. This serves two
    purposes:

        1) People will be able to locate and/or make changes to attributes quickly.

        2) The amount of code that needs to be written in other modules is reduced.
           For example, in the main TimeStamper class, all objects that are of
           the same type (Buttons, Labels, Entries, Texts, etc.) are placed by
           running a loop, where for each object template x_template, the position,
           dimensions, initial state, etc. of its corresponding object x can be
           retrieved by referencing x_template.x_coord, x_template.y_coord, x_template.width,
           x_template.height and x_template.initial_state among other attributes.
    """

    def __init__(self):

        self.output_file_encoding = "utf-8"
        self.images_dir = path.join(resource_path(), "ts_images", "program_images")

        self.mapping = self.map_template_objects_to_string_keys()

    @dataclass
    class Fields():
        """This class, which is called upon by the constructor of the TimeStamperTemplate
        class, should be seen as an extension of the TimeStamperTemplate class with attributes
        pertaining specifically to interactable objects in the Time Stamper program."""

        def __init__(self):
            self.buttons = Buttons()
            self.entries = Entries()
            self.labels = Labels()
            self.texts = Texts()

    @dataclass
    class Timer():
        """This class, which is called upon by the constructor of the TimeStamperTemplate
        class, should be seen as an extension of the TimeStamperTemplate class with
        attributes pertaining specifically to the timer in the Time Stamper program."""

        def __init__(self):
            self.str_key = "time_stamper_timer"
            self.window_str_key = "window_main"

    def map_template_objects_to_string_keys(self):
        """This method creates a mapping of all templates
        to their string keys and returns that mapping."""

        fields = self.Fields()
        buttons = fields.buttons
        entries = fields.entries
        labels = fields.labels
        texts = fields.texts
        timer = self.Timer()
        windows = Windows()

        # In a list, store all of the templates so that, immediately afterwards, we can use
        # a dict comprehension to map the template objects to their string keys ("str_key").
        all_templates = ( \

        ####################
        # Buttons
        ####################

            # Outer Buttons() template class
            buttons,

            # File buttons
            buttons.file.output_select, buttons.file.merge_output_files,

            # Info buttons
            buttons.info.attribution, buttons.info.license,
            buttons.info.help, buttons.info.help_left_arrow, buttons.info.help_right_arrow,

            # Media buttons
            buttons.media.pause,  buttons.media.play, buttons.media.stop,
            buttons.media.rewind, buttons.media.fast_forward, buttons.media.record,

            # Note buttons
            buttons.notes.cancel_note, buttons.notes.save_note,

            # Timestamping buttons
            buttons.timestamping.timestamp, buttons.timestamping.clear_timestamp,

        ####################
        # Entries
        ####################

            # Outer Entries() template class
            entries,

            # Timer entries
            entries.timer.num_hours,  entries.timer.num_minutes,
            entries.timer.num_seconds, entries.timer.num_subseconds,

            # Other entries
            entries.other.rewind, entries.other.fast_forward,

        ####################
        # Labels
        ####################

            # Outer Labels() template class
            labels,

            # Timer labels
            labels.timer.hrs, labels.timer.min, labels.timer.dot, labels.timer.sec,

            # Info labels
            labels.info.help_image, labels.info.help_message,
            labels.info.help_page_number, labels.info.license_message,

            # Merge labels
            labels.merge.first_message,  labels.merge.second_message,
            labels.merge.success, labels.merge.failure,

            # Other labels
            labels.other.output_path, labels.other.rewind_sec,
            labels.other.fast_forward_sec, labels.other.timestamp,

        ####################
        # Texts
        ####################

            # Outer Texts() template class
            texts,

            # There are currently only three text widgets.
            texts.log, texts.current_note, texts.attribution,

        ####################
        # Texts
        ####################

            timer,

        ####################
        # Windows
        ####################

            # Main window
            windows.main,

            # Info windows
            windows.info.attribution, windows.info.help, windows.info.license,

            # Windows associated with the "Merge output files" function
            windows.merge.first_message, windows.merge.second_message,
            windows.merge.success, windows.merge.failure

        )

        # Map the template objects to their string keys ("str_key") so that the template objects
        # can be easily accessed elsewhere in the program. For example, to reference the pause
        # button template, one should reference TimeStamperTemplate.mapping["button_pause"].
        return {template_obj.str_key: template_obj for template_obj in all_templates}
