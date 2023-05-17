#-*- coding: utf-8 -*-
"""This module contains the FileButtonMacros class which stores the functions
that are executed when a file button in the Time Stamper program is pressed."""

from ctypes import cdll, c_char_p
from os.path import basename, dirname, join
from tkinter import filedialog
from vlc import FILE_ptr, EventType, MediaParsedStatus, MediaPlayer
from .macros_helper_methods import merge_success_message, \
    merge_failure_message_file_not_readable, enable_button, disable_button, \
    toggle_widgets, toggle_media_buttons, merge_notes, verify_text_file
try:
    from sys import getwindowsversion
except ImportError:
    pass
finally:
    from sys import platform

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


class FileButtonMacros():
    """This class stores all of the macros that execute when file buttons are pressed."""

    def __init__(self, parent):
        self.parent = parent
        self.time_stamper = parent.time_stamper
        self.template = parent.template
        self.settings = parent.settings
        self.widgets = parent.widgets
        self.timer = parent.timer

    def validate_output_file(self, file_full_path):
        """This method will check the validity of the path that is
        currently displayed in the output path entry widget to make sure
        it corresponds to a valid text file that can be read and written to.
        This method will then edit the configuration of the program depending
        on whether or not that path corresponds to a valid text file."""

        # If the current path in the output path entry widget DOES correspond to a valid text
        # file, edit the configuration of the program to reflect that an output file is active.
        file_encoding = self.settings["output"]["file_encoding"]
        if file_full_path and verify_text_file(file_full_path, file_encoding, True, True):

            # Configure the relevant widgets to reflect that a valid output
            # file IS active (distinct from enabling/disabling widgets).
            self.parent.set_output_widgets(file_full_path)

            # Enable/disable the relevant widgets to reflect that a valid output file IS active.
            toggle_widgets(self.template["button_output_select"], True, self.template, self.widgets)

            # The rewind/fast-forward buttons should NOT be enabled when a
            # media file is loaded, even when a valid output file IS loaded.
            if self.time_stamper.media_player:
                disable_button(self.widgets["button_rewind"], \
                    self.template["button_rewind"]["mac_disabled_color"])
                disable_button(self.widgets["button_fast_forward"], \
                    self.template["button_fast_forward"]["mac_disabled_color"])

        # If the current path in the output path entry widget DOES NOT correspond
        # to a valid text file, reset and disable the relevant widgets.
        else:

            # Configure the relevant widgets to reflect that a valid output
            # file IS NOT active (distinct from enabling/disabling widgets).
            self.parent.reset_output_widgets()

            # Enable/disable the relevant widgets to reflect that a valid output file IS NOT active.
            toggle_widgets(self.template["button_output_select"], \
                False, self.template, self.widgets)

    def button_output_select_macro(self, *_, file_full_path=None):
        """This method will be executed when the "Choose output location" button is pressed."""

        if file_full_path is None:

            # Get the path to the selected output file.
            file_types = (("Text files", "*.txt"), ('All files', '*.*'))

            # Get the path to the selected file.
            file_full_path = filedialog.askopenfilename(title="Select a text file", \
                initialdir=self.template.starting_dir, filetypes=file_types)

        # Check whether or not the selected output file is valid and respond accordingly.
        self.validate_output_file(file_full_path)

    def button_merge_output_files_macro(self, *_):
        """This method will be executed when the "Merge output files" button is pressed."""

        # Call the function that will display the first window with instructions
        # on how to merge output files, passing a macro that will make the first
        # file explorer window appear when the instructions window is closed,
        # wherein the user should select all output files they would like to merge.
        window_merge_first_message = self.widgets.create_entire_window(\
            "window_merge_first_message", close_window_macro=self.on_close_window_merge_1_macro)
        window_merge_first_message.mainloop()

    def final_post_parsing_handler(self, _, file_full_path, media_player):
        """This method gets executed once VLC has both verified that the selected
        media file is valid for playback and finished parsing the media source."""

        # Re-enable all media widgets which were temporarily disabled during media file validation.
        toggle_media_buttons(True, self.widgets, self.template)
        self.parent.set_media_widgets(file_full_path, media_player)
        toggle_widgets(self.template["button_media_select"], True, self.template, self.widgets)

    def post_playing_handler(self, _, file_full_path, media_player, iteration):
        """This method gets executed once VLC's test-play of the selected media file has started."""

        # Pause the media player.
        media_player.set_pause(True)

        # If this method is being called for the first time on the selected media file, we should
        # run through the validation procedure again to give the program more time to fill out the
        # logfile, as the text we are looking for in the logfile has likely not yet been printed.
        if iteration == 1:

            self.validate_media_player(file_full_path, iteration=2)

        # If this method is being called for the second time on the selected
        # media file, we should scan the logfile to ensure that no error messages
        # were recorded that indicate this file is not suitable for VLC playback.
        else:

            # Scan the log file for a message about VLC not
            # being able to identify the audio/video codec.
            bad_codec = False
            with open(join(dirname(self.settings.user_json_path), \
                "out.log"), "r", encoding="utf-8") as log_file:

                lines = log_file.readlines()
                for line in lines:
                    if line == "VLC could not identify the audio or video codec\n":
                        bad_codec = True
                        break

            # If a message about VLC not being able to identify the audio/video codec
            # WAS found in the log file, then this file IS NOT valid for playback by
            # VLC, so we should NOT enable the widgets associated with media playback.
            if bad_codec:

                # Only re-enable the media buttons, which had been
                # disabled for the duration of media file validation.
                toggle_media_buttons(True, self.widgets, self.template)

            # If a message about VLC not being able to identify the audio/video codec
            # WAS NOT found in the log file, then this file IS valid for playback by
            # VLC, so we should change the configuration of the program to reflect this.
            else:

                # Reinitialize a MediaPlayer now that we know our media file is valid.
                media_player = MediaPlayer(file_full_path)
                media = media_player.get_media()
                events = media.event_manager()

                # Set the program to configure and enable/disable the relevant widgets to reflect
                # that a valid output file IS active once the media has finished parsing.
                events.event_attach(EventType.MediaParsedChanged, \
                    self.final_post_parsing_handler, file_full_path, media_player)

                # Parse the media.
                media.parse_with_options(1, -1)

    def post_parsing_handler(self, _, file_full_path, media_player, iteration):
        """This method gets executed when VLC's parsing of the selected media file has
        terminated. If the parsing was successful, the program will then try to briefly
        play the file to see if it is playable. If the parsing was unsuccessful, the program
        will change its configuration to reflect that a valid media file IS NOT active."""

        # Only mark that a parsed media file was generated if file_full_path IS NOT
        # blank (this is necessary because the parse will register as a success if
        # an empty string is provided as a filename) and the parsing was successful.
        if file_full_path \
            and media_player.get_media().get_parsed_status() == MediaParsedStatus.done:

            events = media_player.event_manager()
            events.event_attach(EventType.MediaPlayerPlaying, \
                self.post_playing_handler, file_full_path, media_player, iteration)

            media_player.play()

        # If a parsed media file was NOT generated...
        else:

            # Only re-enable the media buttons, which had been
            # disabled for the duration of media file validation.
            toggle_media_buttons(True, self.widgets, self.template)

    def validate_media_player(self, file_full_path, iteration=1):
        """This method will try to create a media player based on the file path provided in
        file_full_path. If a media player was successfully created, then this method will configure
        the program to reflect that a media player IS active. Otherwise, this method will configure
        the program to reflect that a media player IS NOT active. This method will still create
        an object of type vlc.MediaPlayer temporarily, even if file_full_path is an empty string,
        since the first time a MediaPlayer is initialized, VLC may raise many error messages on the
        command line. The typical end-user will not see these error messages because the command
        line will not be visible to them, but the error messages take time to generate, and this can
        introduce lag into the Time Stamper program. For this reason, we run this method as soon as
        the TimeStamper program starts (i.e., from the TimeStamper.run() method), as this will give
        the impression that the program is "booting up" (besides, the error messages themselves are
        not anything to be concerned about, as they do not appear to be program-breaking errors)."""

        media_player = MediaPlayer(file_full_path)
        media = media_player.get_media()
        events = media.event_manager()

        if iteration == 1:

            # Temporarily reset and disable all media widgets while the program attempts
            # to validate the current media file (if the current media file cannot be
            # validated, only the media buttons will be re-enabled and the remaining
            # widgets that were disabled in this block will NOT be re-enabled).
            toggle_media_buttons(False, self.widgets, self.template)
            self.parent.reset_media_widgets()
            toggle_widgets(\
                self.template["button_media_select"], False, self.template, self.widgets)

            # Set libvlc to publish its log to a location which we can reference later.
            instance = media_player.get_instance()
            fopen = cdll.msvcrt.fopen
            fopen.restype = FILE_ptr
            fopen.argtypes = (c_char_p, c_char_p)
            log_file_path = join(dirname(self.settings.user_json_path), "out.log")
            log_file = fopen(bytes(log_file_path, "utf-8"), b"w")
            instance.log_set_file(log_file)

        # Set the program to execute post_parsing_handler
        # once VLC has finished parsing the selected media.
        events.event_attach(EventType.MediaParsedChanged, \
            self.post_parsing_handler, file_full_path, media_player, iteration)

        # Attempt to parse the selected media.
        media.parse_with_options(1, -1)

    def button_media_select_macro(self, *_, file_full_path=None):
        """This method will be executed when the "Select synced media file" button is pressed.
        This method can also be called independently of pressing of the "Select synced media
        file" button (as is done in the run() method of TimeStamper in time_stamper.py). When
        calling this method from TimeStamper.run() in time_stamper.py, file_full_path is set
        to the value of TimeStamper.settings["media"]["path"]. Even if the initial media file
        validation fails on this value, it is imporant to at least attempt this initial media
        file validation (see the docstring for validate_media_player for more information)."""

        if file_full_path is None:

            # TODO: SOME POTENTIAL FUTURE AUDIO FORMATS TO INCLUDE ARE (but are not limited to):
            # *.aiff *.aac *.m4a *.ogg *.alac *.dsd *.mqa

            # TODO: RESEARCH POTENTIAL VIDEO FORMATS AS WELL:

            media_file_types = set()

            # If we are on Windows...
            if platform.startswith("win"):

                # Store the major and minor versions of the current Windows operating system.
                windows_version_major, windows_version_minor = getwindowsversion()[0:2]

                # If we are on Windows Vista or above...
                if windows_version_major >= 6:

                    media_file_types.update({"*.mp3", "*.wma"})

                    # If we are on Windows 7 or above (not Windows Vista)...
                    if not (windows_version_major == 6 and windows_version_minor == 0):
                        media_file_types.update({"*.aac", "*.adts"})

                        # If we are on Windows 10 or above (not Windows Vista or Windows 7)...
                        if windows_version_major >= 10:
                            media_file_types.update({"*.flac"})

            media_file_types.update({"*.au", "*.mp2", "*.mp3", "*.wav", "*.wma"})

            # INCLUDE "Media files" as an option in the file dialog window if ANY of
            # the media file formats mentioned in this method were determined to be
            # compatible with the user's installation of the Time Stamper program.
            if media_file_types:
                media_file_types = " ".join(sorted(media_file_types))
                file_types = (("Media files", media_file_types), ("All files", "*.*"))

            # DO NOT INCLUDE "Media files" as an option in the file dialog window if NONE
            # of the media file formats mentioned in this method were determined to
            # be compatible with the user's installation of the Time Stamper program.
            else:
                file_types = (("All files", "*.*"),)

            # Get the path to the selected file.
            file_full_path = filedialog.askopenfilename(title="Select a media file", \
                initialdir=self.template.starting_dir, filetypes=file_types)

        # Check whether or not the selected media file is valid and respond accordingly.
        self.validate_media_player(file_full_path)

    def on_close_window_merge_1_macro(self, window_merge_1):
        """This method will be executed when the FIRST window displaying
        instructions to the user on how to merge output files is closed."""

        # Destroy the window displaying the first set of merge instructions.
        window_merge_1.destroy()

        # The user will be prompted to select the files whose notes they wish to merge.
        file_types = (("Text files", "*.txt"), ('All files', '*.*'))
        files_full_paths = filedialog.askopenfilenames(title="Select output files to merge", \
            initialdir=self.template.starting_dir, filetypes=file_types)

        # Only merge the notes if at least one file was selected.
        if files_full_paths:

            # Save the specified output file encoding into an abbreviated file name.
            file_encoding = self.settings["output"]["file_encoding"]

            # Verify the validity of the text files whose notes the user would like to merge.
            invalid_file_names = []
            for file_path in files_full_paths:
                if not verify_text_file(file_path, file_encoding, True, False):
                    invalid_file_names.append(basename(file_path))

            # If the user selected any files that cannot be opened and read,
            # do not merge the notes and instead display a failure message.
            if invalid_file_names:
                label_merge_failure = self.template["label_merge_failure_file_not_readable"]
                label_merge_failure["text"] = \
                    merge_failure_message_file_not_readable(invalid_file_names)
                merge_failure_window = \
                    self.widgets.create_entire_window("window_merge_failure_file_not_readable")
                merge_failure_window.mainloop()

            # If all of the files that the user selected can
            # be opened and read, proceed with the merge.
            else:

                # Merge the notes from all of the selected files. We cannot write the merged notes
                # to a new file yet because a new file has not yet been selected. The process of
                # writing the merged notes to a new file occurs in on_close_window_merge_2_macro.
                merged_notes = merge_notes(files_full_paths, file_encoding)

                # Call the function that will display the second window with instructions on
                # how to merge output files, passing a macro that will make the second file
                # explorer window appear when the second merge instructions window is closed,
                # wherein the user should select a destination file for their merged outputs.
                merge_second_message_window = \
                    self.widgets.create_entire_window("window_merge_second_message", \
                        close_window_macro=self.on_close_window_merge_2_macro, \
                            macro_args=(merged_notes, files_full_paths,))
                merge_second_message_window.mainloop()

    def on_close_window_merge_2_macro(self, window_merge_2, merged_notes, files_full_paths):
        """This method will be executed when the SECOND window displaying
        instructions to the user on how to merge output files is closed."""

        # Destroy the window displaying the second set of merge instructions.
        window_merge_2.destroy()

        # The user will be prompted to select the file to save the merged notes to.
        file_types = (("Text files", "*.txt"), ('All files', '*.*'))
        merged_notes_path = \
            filedialog.askopenfilename(title="Select destination for merged outputs", \
            initialdir=self.template.starting_dir, filetypes=file_types)

        # Only proceed with attempting to write the merged notes to a
        # file if the user selected a file to save the merged notes to.
        if merged_notes_path:

            # Save the specified output file encoding into an abbreviated file name.
            file_encoding = self.settings["output"]["file_encoding"]

            # If the user tried to save the merged notes to a file whose notes
            # were already going to be a part of the merge, do not write the
            # merged notes to a file and instead display a failure message.
            if merged_notes_path in files_full_paths:

                merge_failure_window = \
                    self.widgets.create_entire_window("window_merge_failure_repeated_file")
                merge_failure_window.mainloop()

            # If the user tried to save the merged notes to an unreadable file, do not
            # write the merged notes to a file and instaed display a failure message.
            elif not verify_text_file(merged_notes_path, file_encoding, False, True):
                label_merge_failure = self.template["label_merge_failure_file_not_readable"]
                label_merge_failure["text"] = \
                    merge_failure_message_file_not_readable(basename(merged_notes_path))
                merge_failure_window = \
                    self.widgets.create_entire_window("window_merge_failure_file_not_readable")
                merge_failure_window.mainloop()

            # If the user chose a unique file to save the merged notes to that was NOT already
            # a part of the merge AND the chosen file is readable, proceed with the merge.
            else:

                # Write the merged notes to the requested file.
                with open(merged_notes_path, "a+", encoding=file_encoding) as out:
                    for note in merged_notes:
                        out.write(note)

                # Display a message stating that the notes were successfully merged.
                label_merge_success = self.template["label_merge_success"]
                label_merge_success["text"] = merge_success_message(basename(merged_notes_path))
                merge_success_window = \
                    self.widgets.create_entire_window("window_merge_success")
                merge_success_window.mainloop()
