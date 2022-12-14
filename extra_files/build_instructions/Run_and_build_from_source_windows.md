# Run and Build from Source on Windows

## Table of Contents
* [Install *Python 3*](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_windows.md#install-python-3)
* [Run from source on *Windows*](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_windows.md#run-from-source-on-windows)
* [Build from source on *Windows*](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_windows.md#build-from-source-on-windows)
     * [Install *Auto PY to EXE*](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_windows.md#install-auto-py-to-exe)
     * [Run *Auto PY to EXE*](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_windows.md#run-auto-py-to-exe)
     * [*Auto PY to EXE* configuration](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_windows.md#auto-py-to-exe-configuration)
         * [Script location](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_windows.md#script-location)
         * [Onefile](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_windows.md#onefile)
         * [Console Window](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_windows.md#console-window)
         * [Icon](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_windows.md#icon)
         * [Additional files](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_windows.md#additional-files)
         * [Advanced](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_windows.md#advanced)
         * [Settings](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_windows.md#settings)
         * [CONVERT .PY TO .EXE](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_windows.md#convert-py-to-exe)
* [Create a *Windows* installer for the *Time Stamper* program (optional)](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_windows.md#create-a-windows-installer-for-the-time-stamper-program-optional)
    * [Move the *Time Stamper* executable to the appropriate directory](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_windows.md#move-the-time-stamper-executable-to-the-appropriate-directory)
    * [Download *Inno Setup*](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_windows.md#download-inno-setup)
    * [Locate the *Inno Setup* configuration file](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_windows.md#locate-the-inno-setup-configuration-file)
    * [Edit the *Inno Setup* configuration file](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_windows.md#edit-the-inno-setup-configuration-file)
    * [Create the *Inno Setup* installer for the *Time Stamper* program](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_windows.md#create-the-inno-setup-installer-for-the-time-stamper-program)

## Install *Python 3*
It is highly recommended that you install a version of *Python* that includes *conda* i.e., *Anaconda* or *Miniconda*. If you have no other uses for *Python* and all you are looking to do is run/build the *Time Stamper* program from the source code, *Miniconda* will provide everything you need. [You can download the latest *Miniconda* installer here](https://docs.conda.io/en/latest/miniconda.html).<br />

You will be downloading one of the *Windows* installers for *Miniconda*. There is a 32-bit and a 64-bit *Miniconda* installer. You should download the installer that matches your operating system type. To find out whether your *Windows* computer is 32-bit or 64-bit:<br />
* Search for "This PC" from the *Windows* search bar.<br />
* Right-click on the entry that says "This PC".<br />
* Select "Properties".<br />
* Your operating system type (32-bit or 64-bit) will be displayed next to "System Type".<br />

Once you have downloaded the correct *Miniconda* installer for your *Windows* computer, run the installer to install *Python* with *Miniconda*.

## Run from source on *Windows*
[**Head over to the releases page for the *Time Stamper* program**](https://github.com/benfertig/timestamper/releases) and download the source code for the version of the *Time Stamper* program that you would like to build. To find the source code, expand the "Assets" tab for your desired version and download the "Source code (zip)" or "Source code (tar.gz)" file. Once you have downloaded the compressed archive of the source code, extract its contents.<br />

Open a new *Command Prompt* window and navigate to the source code directory by entering the command below, replacing {path_to_repository} with the directory that you have saved the *timestamper* repository to on your computer:
```
cd {path_to_repository}\src
```

Then, type the following command:
```
python -u "Time Stamper.py"
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
{path_to_repository}\src\Time Stamper.py
```

#### Onefile
This option is up to you. Selecting the "One File" option will package the entire *Time Stamper* program into a single .exe file, providing maximum portability and convenience.

#### Console Window
Selecting "Console Based" will cause a *Command Prompt* window to appear each time you run the *Time Stamper* program. If you are interested in running the program in "debug" mode to view any error messages, this option is for you.<br />

Selecting "Window Based" will suppress the *Command Prompt* window when the *Time Stamper* program is run.

#### Icon
You can provide a .ico file here to set the *Time Stamper* executable's icon. A pregenerated icon can be found under:
```
src\file_icons\file_icon_windows.ico
```

#### Additional files
This is the most crucial section. You *must* provide all of the necessary dependencies here for your *Time Stamper* executable (.exe) to run properly.<br />

For the following step, replace {path_to_repository} with the directory that you have saved the *timestamper* repository to.<br />

You must add three folders. Select "Add folder" three times and add one of each of the following folders each time.
```
{path_to_repository}\src\classes
{path_to_repository}\src\images
{path_to_repository}\src\messages
```

#### Advanced
You should not need to make any changes to this section.

#### Settings
You should not need to make any changes to this section.

#### CONVERT .PY TO .EXE
You should now be ready to build the *Time Stamper* program. Click the "CONVERT .PY TO .EXE" button to generate the *Time Stamper* executable. Once the executable has been made, click the "OPEN OUTPUT FOLDER" button to be directed to the location of the executable. The *Time Stamper* program should now run as a standalone executable (without needing to rely on any outside *Python* interpreters or packages). Congratulations, you have successfully built the *Time Stamper* program from the source code on *Windows*.

## Create a *Windows* installer for the *Time Stamper* program (optional)
The *Time Stamper* executable (.exe) file that you just generated using *Auto PY to EXE* provides a fully functional build of the *Time Stamper* program. By simply double-clicking on this executable, you can run the *Time Stamper* program.

However, the *Windows* executables (.exe) for the *Time Stamper* program on the [releases page for this repository](https://github.com/benfertig/timestamper/releases/) are not simply standalone *Time Stamper* executables like the one you just generated, but rather *Inno Setup* installation wizards that extract the *Time Stamper* program files onto your computer.

Some of the advantages of packaging the *Time Stamper* executable into an *Inno Setup* installer are...
* you can display additional information about the *Time Stamper* program within the *Inno Setup* installation wizard.
* you can include additional files in the *Time Stamper* installation (e.g. a copy of the *Time Stamper* program's license).
* you can decide where the contents of the *Time Stamper* installer should extract to (e.g. the user's desktop).
* you can grant an extra sense of professionalism to the *Time Stamper* program.

With that being said, packaging the *Time Stamper* program into an *Inno Setup* installer is not necessary in order to make the *Time Stamper* program run properly, and will not alter the functionality of the *Time Stamper* program in any way. Therefore, creating a *Time Stamper* installer is optional.

If you would like to know how to package the *Time Stamper* program into an *Inno Setup* installer, follow the instructions below.

### Move the *Time Stamper* executable to the appropriate directory
You are free to include whichever files you like within the *Inno Setup* installer for the *Time Stamper* program.

Versions 0.2.0 and later of the official *Time Stamper* release bundle the following files alongside the *Time Stamper* program in the *Inno Setup* installer:
* A copy of the *Time Stamper* program's license ("LICENSE.txt")
* A list of outside sources that were used to help create the *Time Stamper* program ("ATTRIBUTION.txt")

To include the aforementioned files in the *Time Stamper* installer, move the *Time Stamper* executable (.exe) that you previously generated into the following directory:
```
{path_to_repository}\extra_files\setup_files\windows\inno_setup_source_files
```
This directory is also where you should place any additional files that you would like the *Inno Setup* installer to extract alongside the *Time Stamper* program.

### Download *Inno Setup*
To be able to read *Inno Setup* configuration files, you must have *Inno Setup* installed on your computer. You can download the *Inno Setup* installer [here](https://jrsoftware.org/isdl.php).

### Locate the *Inno Setup* configuration file
The name of the *Inno Setup* configuration file for the *Time Stamper* installer will change depending on which version of the *Time Stamper* program the source code you downloaded is associated with. The *Inno Setup* configuration file for the *Time Stamper* program can be found in the following directory:
```
{path_to_repository}\extra_files\setup_files\windows
```
The name of the *Inno Setup* configuration file for the *Time Stamper* program has the following format:
```
timestamper-{version}-windows-{bits}.iss
```
For example, if you have the *Time Stamper* source code associated with release 0.2.0 for 64-bit *Windows* computers, then you should replace {version} and {bits} in the above example with "r0.2.0" and "64" respectively. So, in this case, the name of the *Inno Setup* configuration file for the *Time Stamper* program would be...
```
timestamper-r0.2.0-windows-64.iss
```

### Edit the *Inno Setup* configuration file
After you have found the *Inno Setup* configuration file, open it using *Inno Setup*.

You can edit any properties of the *Time Stamper* installer in this configuration file. I will not go over the meanings of the variables found in this configuration file. To learn more about what each setting in this configuration file does, refer to [the "Help" page on the *Inno Setup* website](https://jrsoftware.org/ishelp/).

### Create the *Inno Setup* installer for the *Time Stamper* program
Once you are satisfied with the configuration that you have specified in the .iss file, run the script by clicking on the "Run" drop-down menu at the top of the *Inno Setup* page and then clicking on the option named "Run". By default, the "Run" function is also mapped to the F9 key.

Once *Inno Setup* has finished creating the *Time Stamper* installer, you will find the installer in the directory that you specified in the "OutputDir" attribute in the .iss file. Congratulations, you have successfully created an installer for the *Time Stamper* program using *Inno Setup*.
