# Time Stamper <br />
Run a timer and write automatically timestamped notes.<br />

**If you just want to run the *Time Stamper* program, [download the latest release here](https://github.com/benfertig/timestamper/releases/).**<br />

If you would like to run and build this program from the source code, check out the instructions for:
* [Running/building from source on Windows](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_windows.md)
* [Running/building from source on Mac](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_mac.md)

## Usage Instructions
![extra_files/help_images/timestamper_window_labeled_webimage.png](https://github.com/benfertig/timestamper/blob/main/extra_files/help_images/timestamper_window_labeled_webimage.png?raw=true)

### 1 - Pause button
![extra_files/help_images/button_pause.png](https://github.com/benfertig/timestamper/blob/main/extra_files/help_images/button_pause.png?raw=true)
* This button pauses the timer. You must have already selected an output file (see 7) and begun recording (see 6) to be able to press the pause button.

### 2 - Play button
![extra_files/help_images/button_play.png](https://github.com/benfertig/timestamper/blob/main/extra_files/help_images/button_play.png?raw=true)
* This button resumes the timer (see 18). You must already be paused (see 1) to be able to press the play button.

### 3 - Stop button
![extra_files/help_images/button_stop.png](https://github.com/benfertig/timestamper/blob/main/extra_files/help_images/button_stop.png?raw=true)
* This button stops the timer (see 18). Pressing the stop button will also record a new note, timestamped with the timer's current time, indicating that the user has finished entering notes, as well as allow the user to select a different output file (see 7). After you have pressed the stop button, you cannot enter new notes until you have pressed the record button (see 6) again.

### 4 - Rewind button
![extra_files/help_images/button_rewind.png](https://github.com/benfertig/timestamper/blob/main/extra_files/help_images/button_rewind.png?raw=true)
* This button rewinds the timer (see 18) the number of seconds specified in the rewind amount field (see 4.1).

### 4.1 - Rewind amount
![extra_files/help_images/rewind_fast_forward_seconds.png](https://github.com/benfertig/timestamper/blob/main/extra_files/help_images/rewind_fast_forward_seconds.png?raw=true)
* This is where you should enter the number of seconds you would like the timer (see 18) to rewind when you press the rewind button (see 4).

### 5 - Fast-forward button
![extra_files/help_images/button_fast_forward.png](https://github.com/benfertig/timestamper/blob/main/extra_files/help_images/button_fast_forward.png?raw=true)
* This button fast-forwards the timer (see 18) the number of seconds specified in the fast-forward amount field (see 5.1).

### 5.1 - Fast-forward amount
![extra_files/help_images/rewind_fast_forward_seconds.png](https://github.com/benfertig/timestamper/blob/main/extra_files/help_images/rewind_fast_forward_seconds.png?raw=true)
* This is where you should enter the number of seconds you would like the timer (see 18) to fast-forward when you press the fast-forward button (see 5).

### 6 - Record button
![extra_files/help_images/button_record.png](https://github.com/benfertig/timestamper/blob/main/extra_files/help_images/button_record.png?raw=true)
* This button starts the timer (see 18). Pressing the record button will also record a new note, timestamped with the current time on the timer (see 18), indicating that the user has begun entering notes. You cannot press the record button until you have selected an output file (see 7).

### 7 - Output select button
![extra_files/help_images/button_output_select.png](https://github.com/benfertig/timestamper/blob/main/extra_files/help_images/button_output_select.png?raw=true)
* Press this button to open a new file dialog window in which you can select an output file to save your notes to. Output file names normally end in ".txt". You must have selected an output file to be able to enter notes.

### 8 - Merge output files button
![extra_files/help_images/button_merge_output_files.png](https://github.com/benfertig/timestamper/blob/main/extra_files/help_images/button_merge_output_files.png?raw=true)
* If you have multiple output files whose notes you would like to merge and sort based on their timestamps, press this button. You will first be prompted to select the output files whose notes you would like to merge. Then, you will be prompted to select the file you would like to save the merged notes to.

### 9 - Output path
* If an output file is currently selected, the path to that file will be displayed here. For example:</br>
![extra_files/help_images/label_output_path_selected.png](https://github.com/benfertig/timestamper/blob/main/extra_files/help_images/label_output_path_selected.png?raw=true)
* If an output file is not currently selected, a message prompting the user to select an output file will be displayed here. For example:</br>
![extra_files/help_images/label_output_path_default.png](https://github.com/benfertig/timestamper/blob/main/extra_files/help_images/label_output_path_default.png?raw=true)
* If you have not selected an output file, you cannot write notes. To select an output file, press the output select button (see 7).

### 10 - Notes log
* All past notes will be displayed here. This area cannot be edited by the user.

### 11 - Timestamp
![extra_files/help_images/label_timestamp.png](https://github.com/benfertig/timestamper/blob/main/extra_files/help_images/label_timestamp.png?raw=true)
* This displays the current timestamp. The value displayed here will be added to the beginning of your next note. To freeze the current timestamp and set it to the current value on the timer (see 18), press the timestamp button (see 11.1). To unfreeze the current timestamp and resynchronize it with the timer, press the clear timestamp button (see 11.2).

### 11.1 - Timestamp button
![extra_files/help_images/button_timestamp.png](https://github.com/benfertig/timestamper/blob/main/extra_files/help_images/button_timestamp.png?raw=true)
* Press this button to freeze the timestamp (see 11), setting it to the value currently displayed on the timer (see 18). The timestamp button does NOT stop the timer.

### 11.2 - Clear timestamp button
![extra_files/help_images/button_clear_timestamp.png](https://github.com/benfertig/timestamper/blob/main/extra_files/help_images/button_clear_timestamp.png?raw=true)
* Press this button to unfreeze the timestamp (see 11), resynchronizing it with the timer (see 18).

### 12 - Help button
![extra_files/help_images/button_help.png](https://github.com/benfertig/timestamper/blob/main/extra_files/help_images/button_help.png?raw=true)
* Press this button for instructions on how to use this program (which you probably won't have any need for, considering you are already reading this).

### 13 - License button
![extra_files/help_images/button_license.png](https://github.com/benfertig/timestamper/blob/main/extra_files/help_images/button_license.png?raw=true)
* Press this button to view this program's licensing information. A copy of the entire license can be found **[here](https://www.gnu.org/licenses/gpl-3.0.en.html)**.

### 14 - Attribution button
![extra_files/help_images/button_attribution.png](https://github.com/benfertig/timestamper/blob/main/extra_files/help_images/button_attribution.png?raw=true)
* Press this button to view attribution for the outside sources that were used to help create this program, which can also be found **[at the bottom of this README](https://github.com/benfertig/timestamper/blob/main/README.md#attribution)**.

### 15 - Current note
* This is the area where the user should type their current note. Pressing the "Cancel note" button (see 16) will clear this area. Pressing the "Save note" button (see 17) will clear this area AND record BOTH the previously entered text AS WELL AS the current timestamp (see 11) in the current output file (see 9) as well as in the notes log (see 10).

### 16 - Cancel note button
![extra_files/help_images/button_cancel_note.png](https://github.com/benfertig/timestamper/blob/main/extra_files/help_images/button_cancel_note.png?raw=true)
* Press this button to clear the "Current note" box (see 15) WITHOUT RECORDING THE TIMESTAMP (see 11) OR CURRENT NOTE in the notes log (see 10) or in the current output file (see 9).

### 17 - Save note button
![extra_files/help_images/button_save_note.png](https://github.com/benfertig/timestamper/blob/main/extra_files/help_images/button_save_note.png?raw=true)
* Press this button to clear the "Current note" box (see 15) AND RECORD THE TIMESTAMP (see 11) ALONG WITH THE CURRENT NOTE in the notes log (see 10) and in the current output file (see 9). You must have selected an output file (see 7) to be able to press this button.

### 18 - Timer
![extra_files/help_images/timer.png](https://github.com/benfertig/timestamper/blob/main/extra_files/help_images/timer.png?raw=true)
* This area displays the timer's current time. As long as the timer is not running, the user can edit these values. For example:</br>
![extra_files/help_images/timer_edited.png](https://github.com/benfertig/timestamper/blob/main/extra_files/help_images/timer_edited.png?raw=true)
* The minimum time supported by the timer is 00h 00m 00.00s.
* The maximum time supported by the timer is 99h 59m 59.99s.

## Attribution
### Visuals
* #### Images
    * *Flaticon*<br />
        * Images
            * <a href="https://www.flaticon.com/free-icons/timestamp" title="timestamp icons">Timestamp icons created by Freepik - Flaticon</a>
                * Specifically, [this image](https://www.flaticon.com/free-icon/timestamp_1674929?term=timestamp&page=1&position=4&page=1&position=4&related_id=1674929&origin=tag) and [this image](https://www.flaticon.com/free-icon/timestamp_1674827?term=timestamp&related_id=1674827) were used.
            * <a href="https://www.flaticon.com/free-icons/forbidden" title="forbidden icons">Forbidden icons created by prettycons - Flaticon</a>
                * Specifically, [this image was used](https://www.flaticon.com/free-icon/forbidden_2001386?related_id=2001386).
        * License
            * The *Timestamp* and *Forbidden* images from *Flaticon* are licensed under the *Flaticon License* ([see section 8 of the Freepik Company Terms of Use](https://www.freepikcompany.com/legal#nav-flaticon)).

    * [*Iconfinder*](https://www.iconfinder.com/)<br />
        * The [*Ionicons*](https://www.iconfinder.com/iconsets/ionicons) pack was used.
            * Specifically, the following images were used:
                * [Pause icon](https://www.iconfinder.com/icons/211871/pause_icon)
                * [Play icon](https://www.iconfinder.com/icons/211801/play_icon)
                * [Stop icon](https://www.iconfinder.com/icons/211931/stop_icon)
                * [Rewind icon](https://www.iconfinder.com/icons/211816/rewind_icon)
                * [Fastforward icon](https://www.iconfinder.com/icons/211741/fastforward_icon)
                * [Record icon](https://www.iconfinder.com/icons/211881/record_icon)
                * [Gear icon](https://www.iconfinder.com/icons/211751/gear_icon)
                * [Volume, mute icon](https://www.iconfinder.com/icons/211942/volume_mute_icon)
                * [Volume, low icon](https://www.iconfinder.com/icons/211845/volume_low_icon)
                * [Volume, low icon](https://www.iconfinder.com/icons/211940/volume_low_icon)
                * [Volume, medium icon](https://www.iconfinder.com/icons/211941/volume_medium_icon)
                * [High, volume icon](https://www.iconfinder.com/icons/211939/high_volume_icon)
                * [A, left, arrow icon ](https://www.iconfinder.com/icons/211616/a_left_arrow_icon)
                * [A, right, arrow icon](https://www.iconfinder.com/icons/211619/a_right_arrow_icon)
        * License
            * The *Ionicions* pack from *Iconfinder* is licensed under the [MIT License](https://opensource.org/licenses/MIT).

* #### Image conversion
    * [*FreeConvert*](https://www.freeconvert.com/)
        * Specifically, the [PNG to ICO Converter](https://www.freeconvert.com/png-to-ico) was used.
        * Terms of Service
            * The *FreeConvert* Terms of Service can be found [here](https://www.freeconvert.com/terms).

    * [*CloudConvert*](https://cloudconvert.com/)
        * Specifically, the [PNG to ICNS Converter](https://cloudconvert.com/png-to-icns) was used.
        * Terms of Service
            * The CloudConvert Terms of Service can be found [here](https://cloudconvert.com/terms).

* #### Image editing
    * [*GIMP*](https://www.gimp.org/)
        * License
            * *GIMP* is licensed under the [GNU General Public License v3](https://www.gimp.org/docs/userfaq.html#whats-the-gimps-license-and-how-do-i-comply-with-it) and later.<br />

### Libraries
* #### Python distributions
    * [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

* #### Python packages
    * *Auto PY to EXE*
        * [GitHub](https://github.com/brentvollebregt/auto-py-to-exe)
        * [PyPI](https://pypi.org/project/auto-py-to-exe/)
        * License
            * *Auto PY to EXE* is licensed under the [MIT License](https://github.com/brentvollebregt/auto-py-to-exe/blob/master/LICENSE).<br />

    * *Tkmacosx*
        * [GitHub](https://github.com/Saadmairaj/tkmacosx)
        * [conda](https://anaconda.org/saad_7/tkmacosx)
        * [PyPI](https://pypi.org/project/tkmacosx/)
        * License
            * *Tkmacosx* is licensed under the [Apache License 2.0](https://github.com/Saadmairaj/tkmacosx/blob/master/LICENSE).<br />

    * *Py2App*
        * [GitHub](https://github.com/ronaldoussoren/py2app)
        * [conda](https://anaconda.org/conda-forge/py2app)
        * [PyPI](https://pypi.org/project/py2app/)
        * License
            * *Py2App* is licensed under the [MIT License](https://github.com/ronaldoussoren/py2app/blob/master/LICENSE.txt).<br />

    *  [*Pyglet*](https://pyglet.org/)
        * [GitHub](https://github.com/pyglet/pyglet)
        * [conda](https://anaconda.org/conda-forge/pyglet)
        * [PyPi](https://pypi.org/project/pyglet/)
        * License
            * *Pyglet* is licensed under the [BSD 3-Clause "New" or "Revised" License](https://github.com/pyglet/pyglet/blob/master/LICENSE).<br />

### File editing
* [*Resource Hacker*](http://www.angusj.com/resourcehacker/)
    * License
        * The *Resource Hacker* license can be found on the webpage linked above under the section titled "Licence to Use - Terms and Conditions:".

* [*RisohEditor*](https://katahiromz.web.fc2.com/re/en/)
    * [GitHub](https://github.com/katahiromz/RisohEditor)
    * License
        * *RisohEditor* is licensed under the [GNU General Public License v3](https://github.com/katahiromz/RisohEditor/blob/master/LICENSE.txt).
