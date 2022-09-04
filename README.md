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

Once you have downloaded the correct Miniconda installer for your Windows computer, run the installer to install Python through Miniconda.

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

The program should now open in a new Window. If you would like to build your own executable (.exe) from this code, continue with the instructions below.

### Building from source on Windows
The Windows executable for this program was made using auto-py-to-exe, which you can install with pip. Type the following command from a Command Prompt window:
```
pip install auto-py-to-exe
```

This next step must be done from an Administrator Command Prompt Window. Right-click on the Command Prompt program and select "Run as administrator". Then, type the following command.
```
auto-py-to-exe
```

A new window should open in your internet browser.

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
&nbsp;echo $0
```
If Terminal returns the line "-zsh", then you have successfully set your shell to Z shell.<br />
### Install Python 3
It is highly recommended that you install a version of Python that includes conda (i.e. either Anaconda or Miniconda). If you have no other uses for Python and all you are looking to do is run this program, Miniconda will provide everything you need. You can download the latest Miniconda installer here: https://docs.conda.io/en/latest/miniconda.html.<br />

Unless you know what you are doing, do not concern yourself with any of the installers that end in "bash". Only select from the installers that that end in "pkg".<br />

There are installers for Intel Macs as well as M1 Macs. You should choose the installer that matches the type of processor your Mac has. To find out which type of processor your Mac has:<br />
* Click on the Apple logo in the top-left corner of your screen.<br />
* Select "About This Mac".<br />
* In the "Overview" tab, look for either "Intel" or "M1" in the field titled "Processor".<br />

Once you have downloaded the correct Miniconda installer for your Mac computer, run the installer to install Python through Miniconda.<br />
