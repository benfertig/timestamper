#-*- coding: utf-8 -*-
"""This module contains the InfoButtonMacros class which stores the functions
that are executed when an info button in the Time Stamper program is pressed."""

from tkinter import DISABLED, NORMAL

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

        label_page_number_template = self.template.mapping["label_help_page_number"]
        page_numbers = label_page_number_template.page_numbers
        cur_page = label_page_number_template.current_page_number

        if page_numbers[cur_page][1 if next_page else 0] is not None:

            # Display the new page number.
            new_page = page_numbers[cur_page][1 if next_page else 0]
            label_page_number_template.current_page_number = new_page
            obj_page_number = self.widgets.mapping["label_help_page_number"]
            obj_page_number["text"] = str(new_page)

            # Display the new help message.
            label_help_message_template = self.template.mapping["label_help_message"]
            obj_label_help = self.widgets.mapping["label_help_message"]
            new_message = label_help_message_template.help_data[str(new_page)]
            label_help_message_template.text = new_message
            obj_label_help["text"] = new_message

            # Disable the left arrow button if we are at the first help page.
            obj_button_help_left_arrow = self.widgets.mapping["button_help_left_arrow"]
            if page_numbers[new_page][0] is None:
                obj_button_help_left_arrow["state"] = DISABLED
            else:
                obj_button_help_left_arrow["state"] = NORMAL

            # Disable the right arrow button if we are at the last help page.
            obj_button_help_right_arrow = self.widgets.mapping["button_help_right_arrow"]
            if page_numbers[new_page][1] is None:
                obj_button_help_right_arrow["state"] = DISABLED
            else:
                obj_button_help_right_arrow["state"] = NORMAL

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

        # Reset the page number in the page numbe label template.
        label_page_number_template = self.template.mapping["label_help_page_number"]
        first_page_num = label_page_number_template.first_page
        label_page_number_template.current_page_number = first_page_num

        # Reset the help message in the help message label template.
        label_help_message_template = self.template.mapping["label_help_message"]
        help_data = label_help_message_template.help_data
        label_help_message_template.text = help_data[str(first_page_num)]

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
