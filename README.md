# Time Stamper <br />
Run a timer and write automatically timestamped notes.<br />

**THIS IS THE SOURCE CODE. If you just want to run the Time Stamper program, simply download the latest executable from the releases page.**<br />

Instructions are provided below for those who are interested in either:
1. Running the Time Stamper program from the source code using their own Python interpreter
2. Building their own standalone executables from the source code

## Running/Building from Source on Windows
### Install Python 3
It is highly recommended that you install a version of Python that includes conda (i.e. either Anaconda or Miniconda). If you have no other uses for Python and all you are looking to do is run/build the Time Stamper program from the source code, Miniconda will provide everything you need. You can download the latest Miniconda installer [here](https://docs.conda.io/en/latest/miniconda.html).<br />

You will be downloading one of the Windows installers of Miniconda. There is a 32-bit and a 64-bit Miniconda installer. You should download the installer that matches your operating system type. To find out whether your Windows computer is 32-bit or 64-bit:<br />
* Search for "This PC" from the Windows search bar.<br />
* Right-click on the entry that says "This PC".<br />
* Select "Properties".<br />
* Your operating system type (32-bit or 64-bit) will be displayed next to "System Type".<br />

Once you have downloaded the correct Miniconda installer for your Windows computer, run the installer to install Python with Miniconda.

### Running from source on Windows
Download the timestamper repository to your computer if you have not done so already.<br />

Open a new Command Prompt window and navigate to the source code directory by entering the command below, replacing {path_to_repository} with the directory that you have saved the timestamper repository to.
```
cd {path_to_repository}\src
```

Then, type the following command:
```
python -u TimeStamper.py
```

The Time Stamper program should now open in a new Window. Congratulations, you are now running the Time Stamper program from the source code using your own pre-installed Python interpreter.<br />

If you would like to build your own standalone executable (.exe) of the Time Stamper program from the source code, follow the instructions below.

### Building from source on Windows
The Windows executable (.exe) for the Time Stamper program was made using auto-py-to-exe, which you can install with pip. Type the following command from a Command Prompt window:
```
pip install auto-py-to-exe
```
This next step must be done from an Administrator Command Prompt Window. Right-click on Command Prompt and select "Run as administrator". Then, type the following command.
```
auto-py-to-exe
```
A new tab should open in your internet browser.<br />

You should complete the following steps within the auto-py-to-exe browser tab that has appeared. The following steps are labeled with their corresponding section in the auto-py-to-exe browser tab.

#### Script location
This should point to the Python file titled "TimeStamper.py" in the timestamper respository's "src" directory. Refer to the general template below, replacing {path_to_repository} with the directory that you have saved the timestamper repository to.
```
{path_to_repository}/src/TimeStamper.py
```

#### Onefile
This option is up to you. Selecting the "One File" option will package the entire Time Stamper program into a single .exe file, providing maximum portability and convenience.

#### Console Window
Selecting "Console Based" will cause a command window to appear each time you run the Time Stamper program. If you are interested in running the program in "debug" mode to view any error messages, this option is for you.<br />

Selecting "Window Based" will suppress the command window when the Time Stamper program is run.

#### Icon
You can provide a .ico file here to set the executable's icon. Suitable icons of different sizes can be found under src/file_icons/Windows.<br />

However, the icons for the precompiled release of the Time Stamper program were not set using the "Icon" option in auto-py-to-exe. Instead, the icons were set using [Resource Tuner](http://www.restuner.com/download.htm) *after* the executable was generated.<br />

Resource Tuner was used to set the icon images because auto-py-to-exe only allows the user to set one icon image, whose dimensions will be scaled up or down depending on the context in which the user is viewing the icon, while Resource Tuner allows one to set multiple icons of different sizes, allowing Windows to display the most appropriately sized icon for the given context.<br />

For example, from the Desktop, icons are typically 48x48 pixels in size, but from a list view in File Explorer, icons are typically 16x16 pixels in size. If only one icon is provided for the executable, Windows will distort that icon from its original size to match the current needs of the display, which will often make the icon appear ugly.<br/>

If you do not want to bother with setting multiple icons and would simply like to select one icon within auto-py-to-exe, the best icon to use would probably be the icon titled "timestamp_48x48_32b.ico" under src/file_icons/Windows. This icon will look nice from the Windows Desktop and won't look too ugly from a list view in File Explorer.<br />

If you do not want your icons to appear distorted some of the time, and do not mind taking an extra step to set multiple icons for the Time Stamper program after you have generated the .exe file, then **do not change the icon here**. Leave the icon as is for now. Instructions for changing icons using Resource Tuner are provided at the end of this section.

#### Additional files
This is the most crucial section. You *must* provide all of the necessary dependencies here for your Time Stamper executable (.exe) to work.<br />

For the following steps, replace {path_to_repository} with the directory that you have saved the timestamper repository to.<br />

First, select "Add files" and add the following file:
```
{path_to_repository}/src/time_stamper_class.py
```
Now, you must add four folders. Select "Add folder" and add one of the following folders. Repeat the process for the remaining three folders.
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
You should now be ready to build the Time Stamper program. Click the "CONVERT .PY TO .EXE" button to generate the executable. Once the executable has been made, click the "OPEN OUTPUT FOLDER" button to be directed to the location of the executable. This program should now run as a standalone executable (without needing to rely on any outside Python installations). Congratulations, you have successfully built the Time Stamper program from source on Windows.

#### Changing the icons on Windows (optional step)
##### NOTE
You may run into a glitch where the icon for the .exe file you generated will not change, even if you set a custom icon, **UNLESS** you change the name of the .exe file to anything other than "TimeStamper". Why this glitch occurs is unclear, but it is not a big deal. Just change the name of the .exe file to anything else. You can even make a change as small as calling the file "Time Stamper" or "timestamper" instead of "TimeStamper".<br />

If you want to set multiple icons for your .exe file in order to achieve maximum aesthetic appeal under any viewing conditions, make sure that you have generated the .exe file without changing the icon (i.e., without having selected a file under the "Icon" section in auto-py-to-exe).<br />

[Download and install Resource Tuner from here](http://www.restuner.com/download.htm).<br />

Open Resource Tuner and go to "File" -> "Open File". Then open your Time Stamper executable.<br />

A folder hierarchy will appear on the left side of the window. Expand the folder that says "Icon".<br />

##### Repeat these steps until you have replaced all of the icons
* Right-click on one of the entries in the "Icon" folder and select "Resource Tools" -> "Add or Replace Icon within Icon Group".
* In the new window that appears, next to the field labeled "Path to file:" and click the button labeled "Open".
* In the new File Explorer window that appears, navigate to the following directory, replacing {path_to_repository} with the directory that you have saved the timestamper repository to:
```
{path_to_repository}\src\file_icons\Windows
```
* Select an icon file from the above folder. You should select a file whose name indicates an icon with a resolution and bit depth that **MATCHES** the resolution and bit depth of the icon you are replacing. For example, if you are replacing the icon that has a resolution of 48x48 and a bit depth of 8 (which would be marked as "48x48 8b" in the window labeled "Add or Replace Icon within Icon Group"), then you should select the file "timestamp_48x48_8b.ico".
* Now, make sure that you have highlighted the correct icon that you would like to remove from the left column (titled "Items to be replaced:"), and that the icon you would like to replace it with appears in the right column (titled "New items:"). The dimensions and bit depth of the icon you are removing and the icon you are replacing it with should match (check that the names of the entries in both columns match to be sure of this).
* Click "OK"
* Repeat these bulleted steps until you have replaced all icons.

## Running/Building from Source on Mac
### Make sure your default shell is set to Z shell
Open the application "Terminal". You can find "Terminal" by searching for it at the top-right of the screen from the toolbar.<br />

From the Terminal window, enter the following command:
```
chsh -s /bin/zsh
```
You may be asked to enter your login password, which you should do. Don't worry, your keystrokes are being registered even if you can't read them.<br />

Quit and restart Terminal<br />

Type the following command:
```
echo $0
```
If Terminal returns the line "-zsh", then you have successfully set your shell to Z shell.<br />
### Install Python 3
It is highly recommended that you install a version of Python that includes conda (i.e. either Anaconda or Miniconda). If you have no other uses for Python and all you are looking to do is run this program, Miniconda will provide everything you need. You can download the latest Miniconda installer [here](https://docs.conda.io/en/latest/miniconda.html).<br />

Unless you know what you are doing, do not concern yourself with any of the installers that end in "bash". Only select from the installers that that end in "pkg".<br />

There are installers for Intel Macs as well as M1 Macs. You should choose the installer that matches the type of processor your Mac has. To find out which type of processor your Mac has:<br />
* Click on the Apple logo in the top-left corner of your screen.<br />
* Select "About This Mac".<br />
* In the "Overview" tab, look for either "Intel" or "M1" in the field titled "Processor".<br />

Once you have downloaded the correct Miniconda installer for your Mac computer, run the installer to install Python with Miniconda.<br />
