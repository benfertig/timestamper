# Run and Build from Source on Windows

## Table of Contents
* [Install *Python 3*](https://github.com/benfertig/timestamper/blob/main/WINDOWS_RUN_AND_BUILD_FROM_SOURCE.md#install-python-3)
* [Run from source on *Windows*](https://github.com/benfertig/timestamper/blob/main/WINDOWS_RUN_AND_BUILD_FROM_SOURCE.md#run-from-source-on-windows)
* [Build from source on *Windows*](https://github.com/benfertig/timestamper/blob/main/WINDOWS_RUN_AND_BUILD_FROM_SOURCE.md#build-from-source-on-windows)
     * [Install *Auto PY to EXE*](https://github.com/benfertig/timestamper/blob/main/WINDOWS_RUN_AND_BUILD_FROM_SOURCE.md#install-auto-py-to-exe)
     * [Run *Auto PY to EXE*](https://github.com/benfertig/timestamper/blob/main/WINDOWS_RUN_AND_BUILD_FROM_SOURCE.md#run-auto-py-to-exe)
     * [*Auto PY to EXE* configuration](https://github.com/benfertig/timestamper/blob/main/WINDOWS_RUN_AND_BUILD_FROM_SOURCE.md#auto-py-to-exe-configuration)
         * [Script location](https://github.com/benfertig/timestamper/blob/main/WINDOWS_RUN_AND_BUILD_FROM_SOURCE.md#script-location)
         * [Onefile](https://github.com/benfertig/timestamper/blob/main/WINDOWS_RUN_AND_BUILD_FROM_SOURCE.md#onefile)
         * [Console Window](https://github.com/benfertig/timestamper/blob/main/WINDOWS_RUN_AND_BUILD_FROM_SOURCE.md#console-window)
         * [Icon](https://github.com/benfertig/timestamper/blob/main/WINDOWS_RUN_AND_BUILD_FROM_SOURCE.md#icon)
         * [Additional files](https://github.com/benfertig/timestamper/blob/main/WINDOWS_RUN_AND_BUILD_FROM_SOURCE.md#additional-files)
         * [Advanced](https://github.com/benfertig/timestamper/blob/main/WINDOWS_RUN_AND_BUILD_FROM_SOURCE.md#advanced)
         * [Settings](https://github.com/benfertig/timestamper/blob/main/WINDOWS_RUN_AND_BUILD_FROM_SOURCE.md#settings)
         * [CONVERT .PY TO .EXE](https://github.com/benfertig/timestamper/blob/main/WINDOWS_RUN_AND_BUILD_FROM_SOURCE.md#convert-py-to-exe)

## Install *Python 3*
It is highly recommended that you install a version of *Python* that includes *conda* i.e., *Anaconda* or *Miniconda*. If you have no other uses for *Python* and all you are looking to do is run/build the *Time Stamper* program from the source code, *Miniconda* will provide everything you need. [You can download the latest *Miniconda* installer here](https://docs.conda.io/en/latest/miniconda.html).<br />

You will be downloading one of the *Windows* installers for *Miniconda*. There is a 32-bit and a 64-bit *Miniconda* installer. You should download the installer that matches your operating system type. To find out whether your *Windows* computer is 32-bit or 64-bit:<br />
* Search for "This PC" from the *Windows* search bar.<br />
* Right-click on the entry that says "This PC".<br />
* Select "Properties".<br />
* Your operating system type (32-bit or 64-bit) will be displayed next to "System Type".<br />

Once you have downloaded the correct *Miniconda* installer for your *Windows* computer, run the installer to install *Python* with *Miniconda*.

## Run from source on *Windows*
Download the *timestamper* repository to your computer if you have not done so already.<br />

Open a new *Command Prompt* window and navigate to the source code directory by entering the command below, replacing {path_to_repository} with the directory that you have saved the *timestamper* repository to on your computer:
```
cd {path_to_repository}\src
```

Then, type the following command:
```
python -u Time Stamper.py
```

The *Time Stamper* program should now open in a new window. Congratulations, you are now running the *Time Stamper* program from the source code on *Windows* using your own pre-installed *Python* interpreter.<br />

If you would like to build your own standalone executable (.exe) of the *Time Stamper* program from the source code, follow the instructions below.

## Build from source on *Windows*
### Install *Auto PY to EXE*
The *Windows* executable (.exe) for the *Time Stamper* program was made using [*Auto PY to EXE*](https://pypi.org/project/auto-py-to-exe/), which you can install through *pip*. Type the following command from a *Command Prompt* window:
```
pip install auto-py-to-exe
```

### Run *Auto PY to EXE*
This next step must be done from an Administrator *Command Prompt* Window. Right-click on *Command Prompt* and select "Run as administrator". Then, type the following command:
```
auto-py-to-exe
```
A new tab should open in your internet browser.<br />

You should complete the following steps within the *Auto PY to EXE* browser tab that has appeared. The following steps are labeled with their corresponding section in the *Auto PY to EXE* browser tab.

### *Auto PY to EXE* configuration
#### Script location
This should point to the *Python* file titled "Time Stamper.py" in the *timestamper* respository's "src" directory. Refer to the general template below, replacing {path_to_repository} with the directory that you have saved the *timestamper* repository to.
```
{path_to_repository}/src/Time Stamper.py
```

#### Onefile
This option is up to you. Selecting the "One File" option will package the entire *Time Stamper* program into a single .exe file, providing maximum portability and convenience.

#### Console Window
Selecting "Console Based" will cause a *Command Prompt* window to appear each time you run the *Time Stamper* program. If you are interested in running the program in "debug" mode to view any error messages, this option is for you.<br />

Selecting "Window Based" will suppress the *Command Prompt* window when the *Time Stamper* program is run.

#### Icon
You can provide a .ico file here to set the *Time Stamper* executable's icon. A pregenerated icon can be found under src/file_icons/file_icon_windows.ico

#### Additional files
This is the most crucial section. You *must* provide all of the necessary dependencies here for your *Time Stamper* executable (.exe) to run properly.<br />

For the following steps, replace {path_to_repository} with the directory that you have saved the *timestamper* repository to.<br />

First, select "Add files" and add the following file:
```
{path_to_repository}/src/time_stamper_class.py
```
Now, you must add four folders. Select "Add folder" four times and add one of each of the following folders each time.
```
{path_to_repository}/src/ts_images
{path_to_repository}/src/ts_macros
{path_to_repository}/src/ts_template
{path_to_repository}/src/ts_timer
```

#### Advanced
You should not need to make any changes to this section.

#### Settings
You should not need to make any changes to this section.

#### CONVERT .PY TO .EXE
You should now be ready to build the *Time Stamper* program. Click the "CONVERT .PY TO .EXE" button to generate the *Time Stamper* executable. Once the executable has been made, click the "OPEN OUTPUT FOLDER" button to be directed to the location of the executable. The *Time Stamper* program should now run as a standalone executable (without needing to rely on any outside *Python* interpreters or packages). Congratulations, you have successfully built the *Time Stamper* program from the source code on *Windows*.
