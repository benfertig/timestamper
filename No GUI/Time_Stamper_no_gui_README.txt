Time Stamper by Benjamin Fertig (2022)

This program runs a timer and lets you write timestamped notes to a text file.

How to run this program:

For Windows users:
	Setting up this program for Windows is quite simple:
		1. Install Python 3:
			-It is highly recommended that you install a version of Python that includes conda (i.e. either Anaconda or Miniconda). If you have no other uses for Python and all you are looking to do is run this program, Miniconda will provide everything you need. You can download the Miniconda installer here: https://docs.conda.io/en/latest/miniconda.html.
			-You will be downloading one of the Windows installers. There is a 32-bit and a 64-bit installer. You should download the installer that matches your operating system type. To find out whether your Windows computer is 32-bit or 64-bit:
				-Search for "This PC" from the Windows search bar.
				-Right-click on the entry that says "This PC".
				-Select "Properties".
				-Your operating system type (32-bit or 64-bit) will be displayed next to "System Type".
			-Once you have downloaded the correct installer for your Windows computer, run the installer to install Python with Miniconda.
		2. Install the Python module "keyboard":
			-Run "Command Prompt" as an administrator. You can search for Command Prompt from the Windows search bar. Then, right click "Command Prompt" and select "Run as administrator"
			-If you installed Python with Anaconda or Miniconda, type the following command from the command line:
				conda install -c conda-forge keyboard
			-Alternatively, if you installed Python as a standalone program, type the following command from the command line:
				pip3 install keyboard
		3. You are now ready to run the program. Double-click "Run_Windows.bat" and follow the instructions.

For Mac users:
	Trial and error has proven the process of getting this program to run properly on Macs a bit difficult. Fear not, for Python is a very portable programming language and should never be too hard to get up and running. Follow the steps below.
		1. Make sure your default shell is set to Z shell:
			-Open the application "Terminal". You can find "Terminal" by searching for it at the top-right of the screen from the toolbar.
			-From the Terminal window, enter the following command:
				chsh -s /bin/zsh
			-You may be asked to enter your login password, which you should do. Don't worry, your keystrokes are being registered even if you can't read them.
			-Quit and restart Terminal
			-Type the following command:
				echo $0
			-If Terminal returns the line "-zsh", then you have successfully set your shell to Z shell.
		2. Install Python 3:
			-It is highly recommended that you install a version of Python that includes conda (i.e. either Anaconda or Miniconda). If you have no other uses for Python and all you are looking to do is run this program, Miniconda will provide everything you need. You can download the Miniconda installer here: https://docs.conda.io/en/latest/miniconda.html.
			-Unless you know what you are doing, do not concern yourself with any of the installers that end in "bash". Only select from the installers that that end in "pkg".
			-There are installers for Intel Macs as well as M1 Macs. You should choose the installer that matches the type of processor your Mac has. To find out which type of processor your Mac has:
				-Click on the Apple logo in the top-left corner of your screen.
				-Select "About This Mac".
				-In the "Overview" tab, the field titled "Processor" should tell you what kind of processor your Mac has. Look for either "Intel" or "M1".
			-Once you have downloaded the correct installer for your Mac computer, run the installer to install Python with Miniconda.
		3. Install the Python module "keyboard":
			-Open "Terminal" if you haven't already.
			-If you installed Python with Anaconda or Miniconda, type the following command:
				conda install -c conda-forge keyboard
			-Alternatively, if you installed Python as a standalone program, type the following command:
				pip3 install keyboard
		4. Make "Run_Mac.command" executable:
			-Open "Terminal" if you haven't already.
			-Within Terminal, navigate to the Time Stamper folder by typing "cd" followed by the path to the folder. For example, that command might look something like:
				cd "/Users/john/Desktop/Time Stamper"
			-Don't forget to include quotation marks around the file path if the file path includes spaces (like the one in the above example does).
			-Type the following command:
				chmod 755 Run_Mac.command
		5. Try running the program:
			-Try running the program now by double-clicking "Run_Mac.command".
			-If the program does not run, installing a few more dependencies might do the trick, so follow step 5a below and then follow this step again.
		5a. Install a few more dependencies:
			-Open "Terminal" if you haven't already.
			-Enter the following commands, one-by-one:
				pip install pyobjc-core==8.0b1
				pip install pyobjc-framework-Cocoa==8.0b1
				pip install pyobjc-framework-Quartz==8.0b1

Image attribution:
<a href="https://www.flaticon.com/free-icons/timestamp" title="timestamp icons">Timestamp icons created by Freepik - Flaticon</a>
