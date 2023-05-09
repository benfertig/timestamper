#-*- coding: utf-8 -*-
"""This module contains the SpinboxMacros class which stores the functions
that are executed when spinboxes in the Time Stamper program are manipulated."""

from .macros_helper_methods import rewind_or_fast_forward

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


class SpinboxMacros():
    """This class stores all of the macros that execute when spinboxes are manipulated."""

    def __init__(self, parent):
        self.template = parent.template
        self.timer = parent.timer
        self.widgets = parent.widgets

    def spinbox_rewind_macro(self):
        """This method will be executed when the user
        clicks the up/down arrow on the rewind spinbox."""

        # Only rewind the timer at the newly selected speed if we are ALREADY rewinding.
        if self.timer.multiplier < 0.0:

            # Retrieve the speed at which we should rewind from the rewind spinbox.
            spinbox_val = self.widgets["spinbox_rewind"].get()
            multiplier_str = self.template["spinbox_rewind"]["values"][spinbox_val]

            # Rewind the timer at the specified speed.
            rewind_or_fast_forward(multiplier_str, True, self.timer)

    def spinbox_fast_forward_macro(self):
        """This method will be executed when the user clicks
        the up/down arrow on the fast-forward spinbox."""

        # Only fast-forward the timer at the newly selected speed if we are ALREADY fast-forwarding.
        if self.timer.multiplier != 1.0 and self.timer.multiplier > 0.0:

            # Retrieve the speed at which we should fast-forward from the fast-forward spinbox.
            spinbox_val = self.widgets["spinbox_fast_forward"].get()
            multiplier_str = self.template["spinbox_fast_forward"]["values"][spinbox_val]

            # Fast-forward the timer at the specified speed.
            rewind_or_fast_forward(multiplier_str, False, self.timer)
