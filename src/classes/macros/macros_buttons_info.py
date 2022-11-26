#-*- coding: utf-8 -*-
"""This module contains the InfoButtonMacros class which stores the functions
that are executed when an info button in the Time Stamper program is pressed."""

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

class InfoButtonMacros():
    """This class stores all of the macros that execute when info buttons are pressed."""

    def __init__(self, template, widgets, mapping):
        self.template = template
        self.widgets = widgets
        self.mapping = mapping

    def button_help_macro(self):
        """This method will be executed when the "Help" button is pressed."""

        # Display the window containing the help message along with its relevant label.
        window_help = self.widgets.create_entire_window("window_help", \
            self.mapping, close_window_macro=self.on_close_window_help_macro)
        window_help.mainloop()

    def change_help_page(self, next_page):
        """This method is called upon by the macros for the left/right arrow buttons in
        the help page. Since the procedure for both of these buttons is nearly identical,
        we can use the same function for both buttons with only one parameter changed."""

        # Create abbreviated variable names.
        label_page_number_template = self.template.mapping["label_help_page_number"]
        page_numbers = label_page_number_template.page_numbers
        cur_page = label_page_number_template.current_page

        # Display the new page number.
        new_page = page_numbers[cur_page][1 if next_page else 0]
        label_page_number_template.current_page = new_page
        obj_page_number = self.widgets.mapping["label_help_page_number"]
        obj_page_number["text"] = str(new_page)

        # Display the new help message.
        label_help_message_template = self.template.mapping["label_help_message"]
        obj_label_help = self.widgets.mapping["label_help_message"]
        new_message = label_help_message_template.loaded_message_text[str(new_page)]
        obj_label_help["text"] = new_message

    def button_help_left_arrow_macro(self):
        """This method will be executed when the left arrow button in the help window is pressed."""
        self.change_help_page(False)

    def button_help_right_arrow_macro(self):
        """This method will be executed when the right
        arrow button in the help window is pressed."""
        self.change_help_page(True)

    def on_close_window_help_macro(self, window_help):
        """This method will be executed when the help window is closed."""

        window_help.destroy()

        # Reset the page number in the page number label template.
        label_help_page_number_template = self.template.mapping["label_help_page_number"]
        first_page_num = label_help_page_number_template.first_page
        label_help_page_number_template.current_page = first_page_num

    def button_license_macro(self):
        """This method will be executed when the License button is pressed."""

        # Display the window containing the license and
        # outside attributions along with its relevant label.
        window_license = self.widgets.create_entire_window("window_license")
        window_license.mainloop()

    def button_attribution_macro(self):
        """This method will be executed when the Attribution button is pressed."""

        window_attribution = self.widgets.create_entire_window("window_attribution")
        window_attribution.mainloop()
