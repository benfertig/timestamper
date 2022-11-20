# Time Stamper <br />
Run a timer and write automatically timestamped notes.<br />

**THIS IS THE SOURCE CODE. If you just want to run the *Time Stamper* program, [download the latest release here](https://github.com/benfertig/timestamper/releases/).**<br />

If you would like to run and build this program from the source code, check out the instructions for:
* [Running/building from source on Windows](https://github.com/benfertig/timestamper/blob/main/WINDOWS_RUN_AND_BUILD_FROM_SOURCE.md)
* [Running/building from source on Mac](https://github.com/benfertig/timestamper/blob/main/MAC_RUN_AND_BUILD_FROM_SOURCE.md)

## Usage Instructions
![src/ts_images/timestamper_window_labeled.png](https://github.com/benfertig/timestamper/blob/main/src/ts_images/timestamper_window_labeled.png?raw=true)

### 1 - Pause button
* This button pauses the timer. You must have already selected an output file and begun recording to be able to press the pause button.

### 2 - Play button
* This button resumes the timer. You must be already paused to be able to press the play button.

### 3 - Stop button
* This button stops the timer. Pressing the stop button will also record a new note, timestamped with the timer's current time, indicating that the user has finished entering notes, as well as allow the user to select a different output file. After you have pressed the stop button, you cannot enter new notes until you have pressed the record button again.

### 4 - Rewind button
* This button rewinds the timer the specified number of seconds (see 4.1).

### 4.1 - Rewind amount
* Enter the number of seconds you would like to rewind the timer here.

### 5 - Fast-forward button
* This button fast-forwards the timer the specified number of seconds (see 5.1).

### 5.1 - Fast-forward amount
* Enter the number of seconds you would like to fast-forward the timer here.

### 6 - Record button
* This button starts the timer. Pressing the record button will also record a new note, timestamped with the timer's current time, indicating that the user has begun entering notes. You must press the record button to be able to enter notes, and you cannot press the record button until you have selected an output file (see 7).

### 7 - Output select button
* Press this button to open a new file dialog window in which you can select an output file to save your notes to. Output file names normally end in ".txt". You must have selected an output file and pressed the record button to be able to enter notes.

### 8 - Merge output files button
* If you have multiple output files whose notes you would like to merge and sort based on their timestamps, press this button. You will first be prompted to select the output files whose notes you would like to merge. Then, you will be prompted to select file you would like to save the merged notes to.

### 9 - Output path
* If an output file is currently selected, the path to that file will be displayed here. If an output file is not currently selected, a message prompting the user to select an output file will be displayed here.

### 10 - Notes log
* All past notes will be displayed here. This area cannot be edited by the user.

### 11 - Timestamp
* This displays the current timestamp. The value displayed here will be added to the beginning of your next note. To set a timestamp, press the timestamp button (see 11.1).

### 11.1 - Timestamp button
* Press this button to freeze the timestamp, setting it to the value currently displayed on the timer. The timestamp button does NOT stop the timer.

### 11.2 - Clear timestamp button
* Press this button to unfreeze the timestamp and resynchronize it with the timer.

### 12 - Help button
* Press this button for instructions on how to use this program (which you probably won't have any need for, considering you are already reading this).

### 13 - License button
* Press this button to view this program's licensing information.

### 14 - Attribution button
* Press this button to view attribution for the outside sources used to help create this program.

### 15 - Current note
* This is the area where the user should type their current note. Pressing the "Cancel note" button (see 15) will clear this area. Pressing the "Save note" button (see 16) will clear this area AND record BOTH the previously entered text AS WELL AS the current timestamp (see 11) in the current output file as well as in the notes log (see 10).

### 16 - Cancel note button
* Press this button to clear the "Current note" box (see 14) WITHOUT RECORDING THE CURRENT NOTE OR TIMESTAMP in the notes log (see 10) or the current output file.

### 17 - Save note button
* Press this button to clear the "Current note" box (see 14) AND RECORD THE CURRENT NOTE WITH THE TIMESTAMP in the notes log (see 10) and the current output file.

### 18 - Timer
* This area displays the timer's current time. As long as the timer is not running, the user can edit these values. The minimum time supported by this timer is 00:00:00.00 (zero hours, zero minutes and zero seconds) and the maximum supported time is 99:59:59.99 (99 hours, 59 minutes and 59.99 seconds).

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

### File editing
* [*Resource Hacker*](http://www.angusj.com/resourcehacker/)
    * License
        * The *Resource Hacker* license can be found on the webpage linked above under the section titled "Licence to Use - Terms and Conditions:".

* [*RisohEditor*](https://katahiromz.web.fc2.com/re/en/)
    * [GitHub](https://github.com/katahiromz/RisohEditor)
    * License
        * *RisohEditor* is licensed under the [GNU General Public License v3](https://github.com/katahiromz/RisohEditor/blob/master/LICENSE.txt).
