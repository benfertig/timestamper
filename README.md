# Time Stamper <br />
 Run a timer and write automatically timestamped notes.<br />
This is the source code, if you are simply looking for the latest release, head over to the releases page.<br />
<br />
There are a few steps you need to follow before you can run this program:<br />
<br />
# Build from source on Windows
1. Install Python 3:<br /><br />
-It is highly recommended that you install a version of Python that includes conda (i.e. either Anaconda or Miniconda). If you have no other uses for Python and all you are looking to do is run this program, Miniconda will provide you with everything you need. You can download the Miniconda installer here: https://docs.conda.io/en/latest/miniconda.html.<br /><br />
-You will be downloading one of the Windows installers. There is a 32-bit and a 64-bit installer. You should download the installer that matches your operating system type. To find out whether your Windows computer is 32-bit or 64-bit:<br /><br />
-Search for "This PC" from the Windows search bar.<br />
-Right-click on the entry that says "This PC".<br />
-Select "Properties".<br />
-Your operating system type (32-bit or 64-bit) will be displayed next to "System Type".<br /><br />
-Once you have downloaded the correct installer for your Windows computer, run the installer to install Python with Miniconda.<br /><br />

# Build from source on Mac
### Make sure your default shell is set to Z shell
-Open the application "Terminal". You can find "Terminal" by searching for it at the top-right of the screen from the toolbar.<br /><br />
-From the Terminal window, enter the following command:
> chsh -s /bin/zsh<br /><br />
-You may be asked to enter your login password, which you should do. Don't worry, your keystrokes are being registered even if you can't read them.<br /><br />
-Quit and restart Terminal<br /><br />
-Type the following command:
> echo $0<br /><br />
-If Terminal returns the line "-zsh", then you have successfully set your shell to Z shell.<br /><br />
### Install Python 3
-It is highly recommended that you install a version of Python that includes conda (i.e. either Anaconda or Miniconda). If you have no other uses for Python and all you are looking to do is run this program, Miniconda will provide you with everything you need. You can download the Miniconda installer here: https://docs.conda.io/en/latest/miniconda.html.<br /><br />
-Unless you know what you are doing, do not concern yourself with any of the installers that end in "bash". Only select from the installers that that end in "pkg".<br /><br />
-There are installers for Intel Macs as well as M1 Macs. You should choose the installer that matches the type of processor your Mac has. To find out which type of processor your Mac has:<br /><br />
&emsp;-Click on the Apple logo in the top-left corner of your screen.<br />
&emsp;-Select "About This Mac".<br />
&emsp;-In the "Overview" tab, look for either "Intel" or "M1" in the field titled "Processor".<br /><br />
-Once you have downloaded the correct installer for your Mac computer, run the installer to install Python with Miniconda.<br />
