# Time Stamper <br />
Run a timer and write automatically timestamped notes.<br />

**THIS IS THE SOURCE CODE. If you just want to run the Time Stamper program, simply download the latest executable from the releases page.**<br />

Instructions are provided below for those who are interested in either:
1. Running the program from the source code with their own Python interpreter
2. Building their own standalone executables from the source code

## Windows
### Install Python 3
It is highly recommended that you install a version of Python that includes conda (i.e. either Anaconda or Miniconda). If you have no other uses for Python and all you are looking to do is run this program, Miniconda will provide everything you need. You can download the latest Miniconda installer here: https://docs.conda.io/en/latest/miniconda.html.<br />

You will be downloading one of the Windows installers. There is a 32-bit and a 64-bit installer. You should download the installer that matches your operating system type. To find out whether your Windows computer is 32-bit or 64-bit:<br />
* Search for "This PC" from the Windows search bar.<br />
* Right-click on the entry that says "This PC".<br />
* Select "Properties".<br />
* Your operating system type (32-bit or 64-bit) will be displayed next to "System Type".<br />

Once you have downloaded the correct Miniconda installer for your Windows computer, run the installer to install Python with Miniconda.

### Running from source on Windows
Download this repository to your computer if you have not done so already.<br />

Open a new Command Prompt window and navigate to the source code directory. Enter the command below, replacing {path_to_repository} with the directory that you have saved this repository to.
```
cd {path_to_repository}\src
```

Then, type the following command:
```
python -u TimeStamper.py
```

The program should now open in a new Window. If you would like to build your own standalone executable (.exe) from this code, continue with the instructions below.

### Building from source on Windows
The Windows executable for this program was made using auto-py-to-exe, which you can install with pip. Type the following command from a Command Prompt window:
```
pip install auto-py-to-exe
```
This next step must be done from an Administrator Command Prompt Window. Right-click on Command Prompt and select "Run as administrator". Then, type the following command.
```
auto-py-to-exe
```
A new tab should open in your internet browser.<br />

You should complete the following steps within the auto-py-to-exe window that has appeared. The following steps are labeled with their corresponding section in the auto-py-to-exe window.

#### Script location
This should point to the Python file titled "TimeStamper.py" in the respository's "src" directory. Refer to the general template below (replacing {path_to_repository} with the directory that you have saved this repository to).
```
{path_to_repository}/src/TimeStamper.py
```

#### Onefile
This option is up to you. Selecting the "One File" option will package the entire program into a single .exe file, providing maximum portability and convenience.

#### Console Window
Selecting "Console Based" will cause a command window to appear each time you run the program. Those who are interested in running the program in "debug" mode to view any error messages, this option is for you.<br />

Selecting "Window Based" will suppress the command window whenever the program is run.

#### Icon
You can provide a .ico file here to set the executable's icon image. Suitable icons of different sizes can be found under src/file_icons/Windows.<br />

However, the icon for the precompiled release of this program was not set using this option. Instead, the icon was set using [Resource Tuner](http://www.restuner.com/download.htm), *after* the executable was generated.<br />

Resource Tuner was used to set the icon images because auto-py-to-exe only allows the user to set one icon image, whose dimensions will be scaled up or down depending on the context in which the user is viewing the icon, while Resource Tuner allows one to set multiple icons of different sizes, allowing Windows to display the most appropriately sized icon for the given context.<br />

For example, from the Desktop, icons are typically 48x48 pixels in size, but from a list view in File Explorer, icons are typically 16x16 pixels in size. If only one icon is provided for the executable, Windows will distort that icon from its original size to match the current needs of the display, which will often make the icon appear ugly.<br/>

If you do not want to bother with setting multiple icons and would simply like to select one icon within auto-py-to-exe, the best icon to use would probably be the icon titled "timestamp_48x48_32b.ico" under src/file_icons/Windows. This icon will look nice from the Windows Desktop and won't look too ugly from a list view in File Explorer.<br />

If you would like to set multiple icons for the program for maximum aesthetic appeal, instructions for changing icons using Resource Tuner are provided at the end of this section.

#### Additional files
This is the most crucial option. You *must* provide all of the necessary dependencies for the program here.<br />

For the following steps, replace {path_to_repository} with the directory that you have saved this repository to.<br />

First, select "Add files" and add the following file:
{path_to_repository}/src/time_stamper_class.py

## Mac
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
It is highly recommended that you install a version of Python that includes conda (i.e. either Anaconda or Miniconda). If you have no other uses for Python and all you are looking to do is run this program, Miniconda will provide everything you need. You can download the latest Miniconda installer here: https://docs.conda.io/en/latest/miniconda.html.<br />

Unless you know what you are doing, do not concern yourself with any of the installers that end in "bash". Only select from the installers that that end in "pkg".<br />

There are installers for Intel Macs as well as M1 Macs. You should choose the installer that matches the type of processor your Mac has. To find out which type of processor your Mac has:<br />
* Click on the Apple logo in the top-left corner of your screen.<br />
* Select "About This Mac".<br />
* In the "Overview" tab, look for either "Intel" or "M1" in the field titled "Processor".<br />

Once you have downloaded the correct Miniconda installer for your Mac computer, run the installer to install Python with Miniconda.<br />
