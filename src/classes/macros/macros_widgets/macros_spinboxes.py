#-*- coding: utf-8 -*-
"""This module stores the functions that are executed when
spinboxes in the Time Stamper program are manipulated."""

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


def spinbox_rewind_macro():
    """This method will be executed when the user clicks the up/down arrow on the rewind spinbox."""

    # Only rewind the timer at the newly selected speed if we are ALREADY rewinding.
    if classes.timer.multiplier < 0.0:

        # Get the current speed of the timer.
        prev_multiplier = classes.timer.multiplier

        # Rewind the timer at the speed specified in the rewind spinbox.
        new_multiplier = classes.timer.play(playback_type="rewind")

        # Only attempt to print a message if scrolling the rewind spinbox modified the rewind speed.
        if prev_multiplier != new_multiplier:

            # Modify the representation of the rewind speed.
            if new_multiplier % 1 == 0:
                rewind_speed = abs(int(new_multiplier))
            else:
                rewind_speed = abs(round(new_multiplier, 2))

            # Attempt to print the rewind button message.
            methods_output.attempt_button_message("button_rewind", speed=str(rewind_speed))


def spinbox_fast_forward_macro():
    """This method will be executed when the user clicks
    the up/down arrow on the fast-forward spinbox."""

    # Only fast-forward the timer at the newly selected speed if we are ALREADY fast-forwarding.
    if classes.timer.multiplier != 1.0 and classes.timer.multiplier > 0.0:

        # Get the current speed of the timer.
        prev_multiplier = classes.timer.multiplier

        # Fast-forward the timer at the speed specified in the fast-forward spinbox.
        new_multiplier = classes.timer.play(playback_type="fast_forward")

        # Only attempt to print a message if scrolling the
        # fast-forward spinbox modified the fast-forward speed.
        if prev_multiplier != new_multiplier:

            # Modify the representation of the fast-forward speed.
            if new_multiplier % 1 == 0:
                fast_forward_speed = abs(int(new_multiplier))
            else:
                fast_forward_speed = abs(round(new_multiplier, 2))

            # Attempt to print the fast-forward button message.
            methods_output.attempt_button_message(\
                "button_fast_forward", speed=str(fast_forward_speed))
