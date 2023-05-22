#-*- coding: utf-8 -*-
"""This module initializes instances of classes that
will be used throughout the Time Stamper program."""

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

import classes.settings.settings
import classes.template.template
import classes.widgets.widgets
import classes.timing.timing
import classes.macros.macros
import classes.time_stamper

settings = classes.settings.settings.TimeStamperSettings()
template = classes.template.template.TimeStamperTemplate()
widgets = classes.widgets.widgets.Widgets()
timer = classes.timing.timing.TimeStamperTimer()
macros = classes.macros.macros.Macros()

time_stamper = classes.time_stamper.TimeStamper()
