#-*- coding: utf-8 -*-
"""This module stores the functions that are executed when
text widgets in the Time Stamper program are manipulated."""

import classes
import methods.macros.methods_macros_output as methods_output

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


def text_current_note_return_key_macro(*_):
    """This macro will be executed when the return key is pressed
    while the user has selected the current note Text widget."""

    # Behave exactly as though the "Save note" button
    # was pressed, but only if an output file exists.
    if classes.time_stamper.output_path:
        classes.macros["button_save_note"]()
        #classes.macros["button_cancel_note"]()
        classes.time_stamper.root.after(1, methods_output.print_to_text, \
            "", classes.widgets["text_current_note"], True)
