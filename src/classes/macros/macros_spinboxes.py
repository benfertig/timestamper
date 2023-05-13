#-*- coding: utf-8 -*-
"""This module contains the SpinboxMacros class which stores the functions
that are executed when spinboxes in the Time Stamper program are manipulated."""

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

            # Rewind the timer at the speed specified in the rewind spinbox.
            self.timer.play(playback_type="rewind")

    def spinbox_fast_forward_macro(self):
        """This method will be executed when the user clicks
        the up/down arrow on the fast-forward spinbox."""

        # Only fast-forward the timer at the newly selected speed if we are ALREADY fast-forwarding.
        if self.timer.multiplier != 1.0 and self.timer.multiplier > 0.0:

            # Rewind the timer at the speed specified in the fast-forward spinbox.
            self.timer.play(playback_type="fast_forward")
