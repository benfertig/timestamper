# timestamper
 Run a timer and write automatically timestamped notes.

There are a few steps you need to follow before you can run this program:

For Windows users:
	1. Install Python 3:
		-It is highly recommended that you install a version of Python that includes conda (i.e. either Anaconda or Miniconda). If you have no other uses for Python and all you are looking to do is run this program, Miniconda will provide you with everything you need. You can download the Miniconda installer here: https://docs.conda.io/en/latest/miniconda.html.
		-You will be downloading one of the Windows installers. There is a 32-bit and a 64-bit installer. You should download the installer that matches your operating system type. To find out whether your Windows computer is 32-bit or 64-bit:
			-Search for "This PC" from the Windows search bar.
			-Right-click on the entry that says "This PC".
			-Select "Properties".
			-Your operating system type (32-bit or 64-bit) will be displayed next to "System Type".
		-Once you have downloaded the correct installer for your Windows computer, run the installer to install Python with Miniconda.

For Mac users:
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
		-It is highly recommended that you install a version of Python that includes conda (i.e. either Anaconda or Miniconda). If you have no other uses for Python and all you are looking to do is run this program, Miniconda will provide you with everything you need. You can download the Miniconda installer here: https://docs.conda.io/en/latest/miniconda.html.
		-Unless you know what you are doing, do not concern yourself with any of the installers that end in "bash". Only select from the installers that that end in "pkg".
		-There are installers for Intel Macs as well as M1 Macs. You should choose the installer that matches the type of processor your Mac has. To find out which type of processor your Mac has:
			-Click on the Apple logo in the top-left corner of your screen.
			-Select "About This Mac".
			-In the "Overview" tab, the field titled "Processor" should tell you what kind of processor your Mac has. Look for either "Intel" or "M1" in the Processor's name.
		-Once you have downloaded the correct installer for your Mac computer, run the installer to install Python with Miniconda.
