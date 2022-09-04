# Time Stamper <br />
Run a timer and write automatically timestamped notes.<br />

**THIS IS THE SOURCE CODE. If you just want to run the Time Stamper program, download the latest executable from the releases page.**<br />

Instructions are provided below for those who are interested in either:
1. Running the Time Stamper program from the source code using their own Python interpreter
2. Building their own standalone executables from the source code

## Running/Building from Source on Windows
### Install Python 3
It is highly recommended that you install a version of Python that includes conda (i.e. either Anaconda or Miniconda). If you have no other uses for Python and all you are looking to do is run/build the Time Stamper program from the source code, Miniconda will provide everything you need. [You can download the latest Miniconda installer here](https://docs.conda.io/en/latest/miniconda.html).<br />

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

The Time Stamper program should now open in a new window. Congratulations, you are now running the Time Stamper program from the source code on Windows using your own pre-installed Python interpreter.<br />

If you would like to build your own standalone executable (.exe) of the Time Stamper program from the source code, follow the instructions below.

### Building from source on Windows
The Windows executable (.exe) for the Time Stamper program was made using auto-py-to-exe, which you can install through pip. Type the following command from a Command Prompt window:
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

However, the icons for the precompiled release of the Time Stamper program were not set using the "Icon" setting in auto-py-to-exe. Instead, the icons were set using [Resource Tuner](http://www.restuner.com/download.htm) *after* the executable was generated.<br />

Resource Tuner was used to set the icon images for the Time Stamper executable (.exe) because auto-py-to-exe only allows the user to generate an executable with one custom one icon image, whose dimensions will be scaled up or down depending on the context in which the user is viewing the icon, while Resource Tuner allows one to set multiple icons of different sizes, allowing Windows to display the most appropriately sized icon for the given context.<br />

For example, from the Desktop, icons are typically 48x48 pixels in size, but from a list view in File Explorer, icons are typically 16x16 pixels in size. If only one icon is provided for the executable, Windows will distort that icon from its original size to match the current needs of the display, which will often make the icon appear ugly.<br/>

If you do not want to bother with setting multiple icons and would simply like to select one icon within auto-py-to-exe, the best icon to use would probably be the icon titled "timestamp_48x48_32b.ico" under src/file_icons/Windows. This icon will look nice from the Windows Desktop and won't look too ugly from a list view in File Explorer.<br />

If you do not want your icons to appear distorted some of the time, and do not mind taking an extra step to set multiple icons for the Time Stamper program after you have generated the .exe file, then **do not change the icon using the "Icon" setting in auto-py-to-exe**. Leave the icon as is for now. Instructions for changing icons using Resource Tuner are provided at the end of this section.

#### Additional files
This is the most crucial section. You *must* provide all of the necessary dependencies here for your Time Stamper executable (.exe) to work.<br />

For the following steps, replace {path_to_repository} with the directory that you have saved the timestamper repository to.<br />

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
You should now be ready to build the Time Stamper program. Click the "CONVERT .PY TO .EXE" button to generate the Time Stamper executable. Once the executable has been made, click the "OPEN OUTPUT FOLDER" button to be directed to the location of the executable. The Time Stamper program should now run as a standalone executable (without needing to rely on any outside Python interpreters or packages). Congratulations, you have successfully built the Time Stamper program from the source code on Windows.

#### Changing the icons on Windows (optional step)
**NOTE:** If you decide to set a custom icon for the .exe file you generated with auto-py-to-exe, you may run into a glitch where the icon will not change *unless* you change the name of the .exe file. Why this glitch occurs is unclear, but it is not a big deal. Just change the name of "TimeStamper.exe" to literally anything else. You can even make a change as small as calling the file "Time Stamper.exe" or "timestamper.exe" instead of "TimeStamper.exe".<br />

If you want to set multiple icons for your .exe file in order to achieve maximum aesthetic appeal under any viewing conditions, make sure that you have generated the .exe file *without* changing the icon i.e., without having selected a file under the "Icon" section in auto-py-to-exe.<br />

[Download and install Resource Tuner from here](http://www.restuner.com/download.htm).<br />

Open Resource Tuner and go to "File" -> "Open File". Then open your Time Stamper executable.<br />

A folder hierarchy will appear on the left side of the window. Expand the folder that says "Icon".<br />

##### Repeat these steps until you have replaced all of the icons in the .exe file you generated
* Right-click on one of the entries in the "Icon" folder and select "Resource Tools" -> "Add or Replace Icon within Icon Group".
* In the new window that appears, next to the field labeled "Path to file:", click the button labeled "Open".
* In the new File Explorer window that appears, navigate to the following directory, replacing {path_to_repository} with the directory that you have saved the timestamper repository to:
```
{path_to_repository}\src\file_icons\Windows
```
* Select an icon file from the above folder. You should select a file whose name indicates a resolution and bit depth that **MATCHES** the resolution and bit depth of the icon you are replacing. For example, if you are replacing the icon that has a resolution of 48x48 and a bit depth of 8 (which would be marked as "48x48 8b" in the window labeled "Add or Replace Icon within Icon Group"), then you should select the file "timestamp_48x48_8b.ico".
* Now, make sure that you have highlighted the correct icon that you would like to remove from the left column (titled "Items to be replaced:"), and that the icon you would like to replace it with appears in the right column (titled "New items:"). The dimensions and bit depth of the icon you are removing and the icon you are replacing it with should match (which you can check by making sure that the names of the entries in both columns match).
* Click "OK"<br />

Repeat the above bulleted steps until you have replaced all of the icons in the .exe file you generated.

## Running/Building from Source on Mac
### Make sure your default shell is set to Z shell
Open the application "Terminal". You can find "Terminal" by searching for it at the top-right of the screen from the toolbar.<br />

From the Terminal window, enter the following command:
```
chsh -s /bin/zsh
```
You may be asked to enter your login password, which you should do. If you do not see any text being printed to the Terminal window when you type, do not worry. Your keystrokes are being registered even if you cannot read them.<br />

Once you have successfully entered your password, quit and restart Terminal.<br />

From a fresh Terminal window, enter the following command:
```
echo $0
```
If Terminal returns the line "-zsh", then you have successfully set your shell to Z shell.<br />

### Install Python 3
It is highly recommended that you install a version of Python that includes conda (i.e. either Anaconda or Miniconda). If you have no other uses for Python and all you are looking to do is run/build the Time Stamper program from the source code, Miniconda will provide everything you need. [You can download the latest Miniconda installer here](https://docs.conda.io/en/latest/miniconda.html).<br />

Unless you know what you are doing, do not concern yourself with any of the installers that end in "bash". Only select from the installers that that end in "pkg".<br />

There are installers for Intel Macs as well as M1 Macs. You should choose the installer that matches the type of processor your Mac has. To find out which type of processor your Mac has:<br />
* Click on the Apple logo in the top-left corner of your screen.<br />
* Select "About This Mac".<br />
* In the "Overview" tab, look for either "Intel" or "M1" in the field titled "Processor".<br />

Once you have downloaded the correct Miniconda installer for your Mac computer, run the installer to install Python with Miniconda.<br />

### Activate your conda environment
**NOTE:** This section will probably not apply to most people, since Z shell typically defaults to Anaconda/Miniconda as its base Python distribution (provided that you installed Anaconda/Miniconda in the default location), but your results may vary. If you *do not* see "(base)" in your command prefix when you open a new Terminal window, then this section is for you. Otherwise, you can skip to the section titled **Install Py2App**.

Newer Macintosh computers come with a preinstalled distribution of Python 3. If you have such a Macintosh, it is imperative that you make sure your computer **IS NOT** relying on this preinstalled Python 3 distribution when invoking the remaining commands throughout this README.<br />

Even if your Mac does not have a preinstalled Python 3 distribution that is separate from the Python 3 distribution that you (should have) just installed through Anaconda/Miniconda, you should still make sure that, while you invoke the remaining conda/pip/python commands in this README, you are **ALWAYS** pointing your computer to the correct Python distribution (which is the one that you installed with Anaconda/Miniconda).<br />

Therefore, when entering any Terminal commands throughout the remainder of this README, you **ALWAYS** need to make sure that the prefix of your Terminal input reads "(base)". This is an indication that all conda/pip/python commands will default to your custom Anaconda/Miniconda installation unless instructed otherwise.<br />

If you *do not* see "(base)" in your Terminal command prefix, then you must **ALWAYS** make sure that you enter the following command before typing any other commands that begin with "conda", "pip" or "python":
```
conda activate
```
Once you have typed the above command, ensure that your Terminal command prefix reads "(base)". Unfortunately, it may be the case that you will need to retype the above command every time you open a new Terminal window. It all depends on whether the Terminal window reads "(base)".<br />

### Running from source on Mac
#### Install Tkmacosx
One additional package, Tkmacosx, is needed to make the Time Stamper program function on Macs. If you installed Python through Anaconda/Miniconda, it is **recommended** that you install Tkmacosx through **conda**, which you can do by entering the following command from a Terminal window:
```
conda install -c saad_7 tkmacosx
```

**Alternatively**, you can install Tkmacosx through pip by entering the following command from a Terminal window:
```
pip install tkmacosx
```

#### Run TimeStamper.py
Download the timestamper repository to your computer if you have not done so already.<br />

From a Terminal window, navigate to the source code directory by entering the command below, replacing {path_to_repository} with the directory that you have saved the timestamper repository to.
```
cd {path_to_repository}/src
```

Then, type the following command:
```
python3 -u TimeStamper.py
```

The Time Stamper program should now open in a new window. Congratulations, you are now running the Time Stamper program from the source code on a Mac using your own pre-installed Python interpreter.<br />

If you would like to build your own standalone application (.app) of the Time Stamper program from the source code, follow the instructions below.

### Building from source on Mac
#### Install Py2App
The Mac application (.app) for the Time Stamper program was made using Py2App, which you can install through either pip or conda.<br />

If you installed Python through Anaconda/Miniconda, it is **recommended** that you install Py2App through **conda**, which you can do by entering the following command from a Terminal window:
```
conda install -c conda-forge py2app
```

**Alternatively**, you can install Py2App through pip by entering the following command from a Terminal window:
```
pip3 install py2app
```

**NOTE:** In recreating the steps for this build so that I could list them in detail here in this README, I was able to build the Time Stamper application (.app) without ever needing to explicitly download py2app through pip or conda, which is peculiar. I can think of two possible reasons for why this worked:

* One possibility is that, by simply including "py2app" in the "setup_requires" field in "setup.py" under the "src" directory of this repository, we have indicated that py2app is required to build the Time Stamper application, which provides enough of a heads-up to Python to be able to fetch the necessary Py2App scripts from the internet without ever needing to store the Py2App package files locally.

* Another possibility is that Python relied on some old Py2App package files that were cached somewhere on my computer as leftovers from a previously uninstalled copy of Py2App in order to build the Time Stamper application (.app).

#### Build the Time Stamper application (.app)
From a Terminal window, navigate to the source code directory by entering the command below, replacing {path_to_repository} with the directory that you have saved the timestamper repository to.
```
cd {path_to_repository}/src
```

Enter the following command:
```
python3 setup.py py2app
```
