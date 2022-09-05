# Time Stamper <br />
Run a timer and write automatically timestamped notes.<br />

**THIS IS THE SOURCE CODE. If you just want to run the *Time Stamper* program, download the latest executable from the releases page.**<br />

Instructions are provided below for those who are interested in either:
1. Running the *Time Stamper* program from the source code using their own *Python* interpreter
2. Building their own standalone *Time Stamper* executables from the source code

## Attribution
### Images
#### Flaticon
<a href="https://www.flaticon.com/free-icons/timestamp" title="timestamp icons">Timestamp icons created by Freepik - Flaticon</a>
* These images are licensed under the [Flaticon License](https://www.freepikcompany.com/legal#nav-flaticon) (Section 8).
#### Iconfinder
https://www.iconfinder.com/iconsets/ionicons
* These images are licensed under the [MIT License](https://opensource.org/licenses/MIT).

### Software
#### Python distributions
[Python](https://www.python.org/)<br />
[Anaconda](https://docs.conda.io/en/latest/miniconda.html)<br />
[Miniconda](https://docs.conda.io/en/latest/miniconda.html)
#### Python packages
[Auto PY to EXE](https://pypi.org/project/auto-py-to-exe/)<br />
Tkmacosx
* [GitHub](https://github.com/Saadmairaj/tkmacosx)
* [conda](https://anaconda.org/saad_7/tkmacosx)
* [PyPI](https://pypi.org/project/tkmacosx/)<br /><br />
[Py2App](https://py2app.readthedocs.io/en/latest/)
* [GitHub](https://github.com/ronaldoussoren/py2app)
* [conda](https://anaconda.org/conda-forge/py2app)
* [PyPI](https://pypi.org/project/py2app/)


## Run/Build from Source on Windows
To jump down to the Mac instructions, [click here](https://github.com/benfertig/timestamper/blob/main/README.md#runbuild-from-source-on-mac).
### Install Python 3
It is highly recommended that you install a version of *Python* that includes *conda* i.e., *Anaconda* or *Miniconda*. If you have no other uses for *Python* and all you are looking to do is run/build the *Time Stamper* program from the source code, *Miniconda* will provide everything you need. [You can download the latest *Miniconda* installer here](https://docs.conda.io/en/latest/miniconda.html).<br />

You will be downloading one of the *Windows* installers for *Miniconda*. There is a 32-bit and a 64-bit *Miniconda* installer. You should download the installer that matches your operating system type. To find out whether your *Windows* computer is 32-bit or 64-bit:<br />
* Search for "This PC" from the *Windows* search bar.<br />
* Right-click on the entry that says "This PC".<br />
* Select "Properties".<br />
* Your operating system type (32-bit or 64-bit) will be displayed next to "System Type".<br />

Once you have downloaded the correct *Miniconda* installer for your *Windows* computer, run the installer to install *Python* with *Miniconda*.

### Run from source on Windows
Download the *timestamper* repository to your computer if you have not done so already.<br />

Open a new *Command Prompt* window and navigate to the source code directory by entering the command below, replacing {path_to_repository} with the directory that you have saved the *timestamper* repository to on your computer.
```
cd {path_to_repository}\src
```

Then, type the following command:
```
python -u TimeStamper.py
```

The *Time Stamper* program should now open in a new window. Congratulations, you are now running the *Time Stamper* program from the source code on *Windows* using your own pre-installed *Python* interpreter.<br />

If you would like to build your own standalone executable (.exe) of the *Time Stamper* program from the source code, follow the instructions below.

### Build from source on Windows
The *Windows* executable (.exe) for the *Time Stamper* program was made using [*Auto PY to EXE*](https://pypi.org/project/auto-py-to-exe/), which you can install through *pip*. Type the following command from a *Command Prompt* window:
```
pip install auto-py-to-exe
```
This next step must be done from an Administrator *Command Prompt* Window. Right-click on *Command Prompt* and select "Run as administrator". Then, type the following command.
```
auto-py-to-exe
```
A new tab should open in your internet browser.<br />

You should complete the following steps within the *Auto PY to EXE* browser tab that has appeared. The following steps are labeled with their corresponding section in the *Auto PY to EXE* browser tab.

#### Script location
This should point to the *Python* file titled "TimeStamper.py" in the *timestamper* respository's "src" directory. Refer to the general template below, replacing {path_to_repository} with the directory that you have saved the *timestamper* repository to.
```
{path_to_repository}/src/TimeStamper.py
```

#### Onefile
This option is up to you. Selecting the "One File" option will package the entire *Time Stamper* program into a single .exe file, providing maximum portability and convenience.

#### Console Window
Selecting "Console Based" will cause a *Command Prompt* window to appear each time you run the *Time Stamper* program. If you are interested in running the program in "debug" mode to view any error messages, this option is for you.<br />

Selecting "Window Based" will suppress the *Command Prompt* window when the *Time Stamper* program is run.

#### Icon
You can provide a .ico file here to set the *Time Stamper* executable's icon. Suitable icons of different sizes can be found under src/file_icons/Windows. [The original versions of these images were retrieved from this page.](https://www.flaticon.com/free-icons/timestamp)<br />

However, the icons for the precompiled release of the *Time Stamper* program were not set using the "Icon" setting in *Auto PY to EXE*, and it is not recommended that you set the icon using this method if you want the *Time Stamper* entry in your File Explorer to be visually pleasing. Instead, you should consider setting icons with [*Resource Tuner*](http://www.restuner.com/download.htm) *after* you generate a *Time Stamper* executable.<br />

*Resource Tuner* was used to set the icon images for the Time Stamper executable (.exe) because *Auto PY to EXE* only allows the user to generate an executable with **ONE** custom icon image whose dimensions will be scaled up or down depending on the context in which the user is viewing the icon, while *Resource Tuner* allows one to set multiple icons of different sizes, allowing *Windows* to display the most appropriately sized icon depending on the given context.<br />

For example, from the desktop, icons are typically 48x48 pixels in size, but from a list view in *File Explorer*, icons are typically 16x16 pixels in size. If only one icon is provided for the executable, *Windows* will distort that icon from its original size to match the current needs of the display, which will often make the icon appear ugly.<br/>

If you do not want to bother with setting multiple icons and would simply like to select one icon within *Auto PY to EXE*, the best icon to use would probably be the icon titled "timestamp_48x48_32b.ico" under src/file_icons/Windows. This icon will look nice from the *Windows* desktop and won't look too ugly from a list view in *File Explorer*.<br />

If you do not want your icons to appear distorted some or all of the time, and do not mind taking an extra step to set multiple icons for the *Time Stamper* program after you have generated the *TimeStamper.exe* file, then **do not change the icon using the "Icon" setting in *Auto PY to EXE***. Leave the default icon as-is for now. Instructions for changing file icons using *Resource Tuner* are provided at the end of this section.

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
You should now be ready to build the *Time Stamper* program. Click the "CONVERT .PY TO .EXE" button to generate the *Time Stamper* executable. Once the executable has been made, click the "OPEN OUTPUT FOLDER" button to be directed to the location of the executable. The *Time Stamper* program should now run as a standalone executable (without needing to rely on any outside Python interpreters or packages). Congratulations, you have successfully built the *Time Stamper* program from the source code on *Windows*.

#### Change the icons on Windows using Resource Tuner (optional step)
**NOTE:** If you decide to set a custom icon for the *Auto PY to EXE* executable (.exe) file you generated, you may run into a glitch where the icon of the .exe file will not change *unless* you change the .exe file's name. Why this glitch occurs is unclear, but it is not a big deal. Just change the name of "TimeStamper.exe" to literally anything else. You can even make a change as small as calling the file "Time Stamper.exe" or "timestamper.exe" instead of "TimeStamper.exe".<br />

If you want to set multiple icons for your .exe file in order to achieve maximum aesthetic appeal under any viewing conditions from *File Explorer*, make sure that you have generated the .exe file *without* changing the icon i.e., without having selected a file under the "Icon" section in *Auto PY to EXE*.<br />

[Download and install *Resource Tuner* here](http://www.restuner.com/download.htm).<br />

Open *Resource Tuner* and then go to "File" -> "Open File". Select your *Time Stamper* executable (.exe).<br />

A folder hierarchy will appear on the left side of the window. Expand the folder that says "Icon".<br />

##### Repeat these steps until you have replaced all of the icons in the .exe file you generated
* Right-click on one of the entries in the "Icon" folder and select "Resource Tools" -> "Add or Replace Icon within Icon Group".
* In the new window that appears, next to the field labeled "Path to file:", click the button labeled "Open".
* In the new *File Explorer* window that appears, navigate to the following directory, replacing {path_to_repository} with the directory that you have saved the *timestamper* repository to:
```
{path_to_repository}\src\file_icons\Windows
```
* Select an icon file from the above folder. You should select a file whose name indicates a resolution and bit depth that **MATCHES** the resolution and bit depth of the icon you are replacing. For example, if you are replacing the icon that has a resolution of 48x48 and a bit depth of 8 (which would be marked as "48x48 8b" in the window labeled "Add or Replace Icon within Icon Group"), then you should select the file "timestamp_48x48_8b.ico".
* Now, make sure that you have highlighted the correct icon that you would like to remove from the left column (titled "Items to be replaced:"), and that the icon you would like to replace it with appears in the right column (titled "New items:"). The dimensions and bit depth of the icon you are removing and the icon you are replacing it with should match (which you can check by making sure that the names of the entries in both columns match).
* Click "OK"<br />

Repeat the above bulleted steps until you have replaced all of the icons in the .exe file you generated.

## Run/Build from Source on Mac
To jump back up to the Windows instructions, [click here](https://github.com/benfertig/timestamper/blob/main/README.md#runbuild-from-source-on-windows).
### Make sure your default shell is set to Z shell
Open the application *Terminal*. You can find *Terminal* by searching for it at the top-right of the screen from the toolbar.<br />

From the *Terminal* window, enter the following command:
```
chsh -s /bin/zsh
```
You may be asked to enter your login password, which you should do. If you do not see any text being printed to the *Terminal* window when you type, do not worry. Your keystrokes are being registered even if you cannot read them.<br />

Once you have successfully entered your password, quit and restart *Terminal*.<br />

From a fresh *Terminal* window, enter the following command:
```
echo $0
```
If *Terminal* returns the line "-zsh", then you have successfully set your shell to *Z shell*.<br />

### Install Python 3
It is highly recommended that you install a version of *Python* that includes *conda* i.e., *Anaconda* or *Miniconda*. In fact, later steps in this README assume that you have installed a *conda*-based distribution of *Python*. If you insist on using a *Python* distribution that you acquired through other means, then it is not guaranteed that you will be able to follow along with the rest of this README without running into additional problems.<br />

If you have no other uses for *Python* and all you are looking to do is run/build the *Time Stamper* program from the source code, *Miniconda* will provide everything you need. [You can download the latest *Miniconda* installer here](https://docs.conda.io/en/latest/miniconda.html).<br />

Unless you know what you are doing, do not concern yourself with any of the installers that end in "bash". Only select from the installers that that end in "pkg".<br />

There are *Miniconda* installers for ***Intel*** *Macs* as well as ***M1*** *Macs*. You should choose the installer that matches the type of processor your *Mac* has. To find out which type of processor your *Mac* has:<br />
* Click on the *Apple* logo in the top-left corner of your screen.<br />
* Select "About This Mac".<br />
* In the "Overview" tab, look for either "Intel" or "M1" in the field titled "Processor".<br />

Once you have downloaded the correct *Miniconda* installer for your *Mac*, run the installer to install *Python* with *Miniconda*.<br />

### Activate your conda environment
**NOTE:** This section will probably not apply to most people. Since *Z shell* typically defaults to *Anaconda*/*Miniconda* as its base *Python* distribution, your base *conda* environment will probably be activated automatically whenever you start *Terminal*. You can find out whether your base *conda* environment is activated by seeing whether the text "(base)" appears in your command prefix when you open a new *Terminal* window. If you *do not* see "(base)" in your command prefix when you open a new *Terminal* window, then this section is for you. Otherwise, you can skip to the section titled **Running from source on Mac**.

When entering any *Terminal* commands found throughout the rest of this README, you **ALWAYS** need to make sure that the prefix of your Terminal input reads "(base)". This is an indication that all *conda*/*pip*/*python* commands will default to your custom *Anaconda*/*Miniconda* installation unless instructed otherwise.<br />

Whenever you *do not* see "(base)" in your *Terminal* command prefix, you must **ALWAYS** make sure that you enter the following command before typing any other commands that begin with "conda", "pip" or "python":
```
conda activate
```
Once you have typed the above command, ensure that your *Terminal* command prefix reads "(base)". It may be the case that you will only need to type the above command once. You will know this is the case if any subsequent *Terminal* windows you open automatically contain "(base)" in their command prefix. Unfortunately, it may be that "(base)" does not appear in your *Terminal* command prefix whenever you open a new *Terminal* window, in which case you will need to retype the above command in every new *Terminal* window you open (until, at the very least, you have finished following along with this README, and even then, ensuring that "(base)" appears in your *Terminal* command prefix is really only necessary when you plan on entering a command that starts with "conda", "pip" or "python").<br />

### Run from source on Mac
#### Install Tkmacosx
To make the *Time Stamper* program function on a *Macintosh* computer, you will need to install one additional *Python* package called *Tkmacosx*. If you installed *Python* through *Anaconda*/*Miniconda*, it is **recommended** that you [install *Tkmacosx* through *conda*](https://anaconda.org/saad_7/tkmacosx), which you can do by entering the following command from a *Terminal* window:
```
conda install -c saad_7 tkmacosx
```

Alternatively, you can [install *Tkmacosx* through *pip*](https://pypi.org/project/tkmacosx/) by entering the following command from a *Terminal* window:
```
pip3 install tkmacosx
```

#### Run TimeStamper.py
Download the *timestamper* repository to your computer if you have not done so already.<br />

From a *Terminal* window, navigate to the source code directory by entering the command below, replacing {path_to_repository} with the directory that you have saved the *timestamper* repository to.
```
cd {path_to_repository}/src
```

Then, enter the following command:
```
python3 -u TimeStamper.py
```

The *Time Stamper* program should now open in a new window. Congratulations, you are now running the *Time Stamper* program from the source code on a *Mac* using your own pre-installed *Python* interpreter.<br />

If you would like to build your own standalone application (.app) of the *Time Stamper* program from the source code, follow the instructions below.

### Build from source on Mac
#### Tkmacosx
If you have been following along with these instructions since the section titled **Run from source on Mac**, then you should have already installed *Tkmacosx*. If you have not yet installed *Tkmacosx*, [go ahead and refer to the above section titled **Install Tkmacosx**](https://github.com/benfertig/timestamper/blob/main/README.md#install-tkmacosx) before coming back here.

#### Install Py2App
The *Mac* application (.app) for the *Time Stamper* program was made using *Py2App*, which you can install through either *conda* or *pip*.<br />

If you installed *Python* through *Anaconda*/*Miniconda*, it is **recommended** that you [install Py2App through *conda*](https://anaconda.org/conda-forge/py2app), which you can do by entering the following command from a *Terminal* window:
```
conda install -c conda-forge py2app
```

Alternatively, you can [install *Py2App* through *pip*](https://pypi.org/project/py2app/) by entering the following command from a *Terminal* window:
```
pip3 install py2app
```

**NOTE:** In recreating the steps for this build so that I could list them in detail here in this README, I was able to build the *Time Stamper* application (.app) without ever needing to explicitly download *Py2App* through *conda* or *pip*, which is peculiar. There is clearly something I do not quite understand about the way *Py2App* works. Nonetheless, it will not hurt to install *Py2App* manually as outlined in this section. If you are feeling adventurous, you can go ahead and try following along with the rest of this README without installing *Py2App* (at your own peril).

#### Build the Time Stamper application (.app)
From a *Terminal* window, navigate to the *Time Stamper* source code directory by entering the command below, replacing {path_to_repository} with the directory that you have saved the *timestamper* repository to.
```
cd {path_to_repository}/src
```

Enter the following command:
```
python3 setup.py py2app
```

Your new *Time Stamper* application (.app) will be created in a directory called "dist" within the "src" directory. This program should run when you double-click on it. However, you will likely need to follow one additional step in order to make the *Time Stamper* application you built a truly standalone program.<br />

#### Copy some extra libraries to the Time Stamper application (.app) package
On the particular *Macintosh* computer where the *Time Stamper* application (.app) was initially built, a glitch was causing the *Time Stamper* application not to run if the preconfigured *Anaconda*/*Miniconda* distribution from earlier had not been installed on the computer.<br />

This obviously defeats the purpose of creating a *Time Stamper* application (.app) package, as the standalone *Time Stamper* application is meant to be truly standalone in the sense that it should not to rely on any outside libraries that do not already come preinstalled on any modern *Macintosh* computer.<br />

There is a workaround for this problem which involves copying a few libraries from your *anaconda3*/*miniconda3* folder to the *Time Stamper* .app package:
* Find your *anaconda3*/*miniconda3* directory by entering the following command from *Terminal*:
```
which python
```
* A file path should be displayed to you that has either "anaconda3" (if you installed *Python 3* through *Anaconda*) or "miniconda3" (if you installed *Python 3* through Miniconda) somewhere in its name.
* Navigate to the displayed *anaconda3*/*miniconda3* directory from a *Finder* window, disregarding the part of the file path that comes after "anaconda3"/"miniconda3".
* Your *anaconda3*/*miniconda3* directory may very well be hidden in *Finder*, but you can make *Finder* display hidden files and folders by pressing command+shift+. (command shift dot). You can hide these files and folders by pressing the same keys again.
* Once you have navigated to your *anaconda3*/*miniconda3* folder, enter the folder named "lib"
* Copy the following three files to your clipboard
```
libffi.7.dylib
libtcl8.6.dylib
libtk8.6.dylib
```
* Now navigate to the *Time Stamper* application (.app) you created earlier, right-click on it and select "Show Package Contents"
* Then, go to "Contents" -> "Resources" -> "lib"
* Paste the three .dylib files you just copied into this "lib" folder.<br />

You can now exit out of all *Finder* windows. You should now be able to run the *Time Stamper* application (.app) as a standalone program that does not require any external libraries. Congratulations, you have successfully built the *Time Stamper* program from the source code on a *Mac*.
