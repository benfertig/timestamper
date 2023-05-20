#-*- coding: utf-8 -*-
"""This module stores the functions that are executed when
info buttons in the Time Stamper program are pressed."""

import classes
import methods.macros.methods_macros_helper as methods_helper

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


def button_help_macro(*_):
    """This method will be executed when the "Help" button is pressed."""

    # Display the window containing the help message along with its relevant label.
    if "window_help" in classes.widgets.mapping \
        and classes.widgets.mapping["window_help"].winfo_exists():

        window_help = classes.widgets.mapping["window_help"]
        window_help.lift()

    else:

        window_help = classes.widgets.create_entire_window("window_help")
        window_help.mainloop()


def button_help_left_arrow_macro(*_):
    """This method will be executed when the left arrow button in the help window is pressed."""

    methods_helper.change_help_page(False)


def button_help_right_arrow_macro(*_):
    """This method will be executed when the right
    arrow button in the help window is pressed."""

    methods_helper.change_help_page(True)


def button_license_macro(*_):
    """This method will be executed when the License button is pressed."""

    # Display the window containing the license.
    if "window_license" in classes.widgets.mapping \
        and classes.widgets.mapping["window_license"].winfo_exists():

        window_license = classes.widgets.mapping["window_license"]
        window_license.lift()

    else:

        window_license = classes.widgets.create_entire_window("window_license")
        window_license.mainloop()


def button_attribution_macro(*_):
    """This method will be executed when the Attribution button is pressed."""

    # Display the window containing the attribution.
    if "window_attribution" in classes.widgets.mapping \
        and classes.widgets.mapping["window_attribution"].winfo_exists():

        window_attribution = classes.widgets.mapping["window_attribution"]
        window_attribution.lift()

    else:

        window_attribution = classes.widgets.create_entire_window("window_attribution")
        window_attribution.mainloop()
