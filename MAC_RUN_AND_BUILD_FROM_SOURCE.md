# Run and Build from Source on Mac

To jump back up to the Windows instructions, [click here](https://github.com/benfertig/timestamper/blob/main/README.md#runbuild-from-source-on-windows).
## Make sure your default shell is set to Z shell
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

## Install Python 3
It is highly recommended that you install a version of *Python* that includes *conda* i.e., *Anaconda* or *Miniconda*. In fact, later steps in this README assume that you have installed a *conda*-based distribution of *Python*. If you insist on using a *Python* distribution that you acquired through other means, then it is not guaranteed that you will be able to follow along with the rest of this README without running into additional problems.<br />

If you have no other uses for *Python* and all you are looking to do is run/build the *Time Stamper* program from the source code, *Miniconda* will provide everything you need. [You can download the latest *Miniconda* installer here](https://docs.conda.io/en/latest/miniconda.html).<br />

Unless you know what you are doing, do not concern yourself with any of the installers that end in "bash". Only select from the installers that that end in "pkg".<br />

There are *Miniconda* installers for ***Intel*** *Macs* as well as ***M1*** *Macs*. You should choose the installer that matches the type of processor your *Mac* has. To find out which type of processor your *Mac* has:<br />
* Click on the *Apple* logo in the top-left corner of your screen.<br />
* Select "About This Mac".<br />
* In the "Overview" tab, look for either "Intel" or "M1" in the field titled "Processor".<br />

Once you have downloaded the correct *Miniconda* installer for your *Mac*, run the installer to install *Python* with *Miniconda*.<br />

## Activate your conda environment
**NOTE:** This section will probably not apply to most people. Since *Z shell* typically defaults to *Anaconda*/*Miniconda* as its base *Python* distribution, your base *conda* environment will probably be activated automatically whenever you start *Terminal*. You can find out whether your base *conda* environment is activated by seeing whether the text "(base)" appears in your command prefix when you open a new *Terminal* window. If you *do not* see "(base)" in your command prefix when you open a new *Terminal* window, then this section is for you. Otherwise, you can skip to the section titled **Running from source on Mac**.

When entering any *Terminal* commands found throughout the rest of this README, you **ALWAYS** need to make sure that the prefix of your Terminal input reads "(base)". This is an indication that all *conda*/*pip*/*python* commands will default to your custom *Anaconda*/*Miniconda* installation unless instructed otherwise.<br />

Whenever you *do not* see "(base)" in your *Terminal* command prefix, you must **ALWAYS** make sure that you enter the following command before typing any other commands that begin with "conda", "pip" or "python":
```
conda activate
```
Once you have typed the above command, ensure that your *Terminal* command prefix reads "(base)". It may be the case that you will only need to type the above command once. You will know this is the case if any subsequent *Terminal* windows you open automatically contain "(base)" in their command prefix. Unfortunately, it may be that "(base)" does not appear in your *Terminal* command prefix whenever you open a new *Terminal* window, in which case you will need to retype the above command in every new *Terminal* window you open (until, at the very least, you have finished following along with this README, and even then, ensuring that "(base)" appears in your *Terminal* command prefix is really only necessary when you plan on entering a command that starts with "conda", "pip" or "python").<br />

## Run from source on Mac
### Install Tkmacosx
To make the *Time Stamper* program function on a *Macintosh* computer, you will need to install one additional *Python* package called *Tkmacosx*. If you installed *Python* through *Anaconda*/*Miniconda*, it is **recommended** that you [install *Tkmacosx* through *conda*](https://anaconda.org/saad_7/tkmacosx), which you can do by entering the following command from a *Terminal* window:
```
conda install -c saad_7 tkmacosx
```

Alternatively, you can [install *Tkmacosx* through *pip*](https://pypi.org/project/tkmacosx/) by entering the following command from a *Terminal* window:
```
pip3 install tkmacosx
```

### Run TimeStamper.py
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

## Build from source on Mac
### Tkmacosx
If you have been following along with these instructions since the section titled **Run from source on Mac**, then you should have already installed *Tkmacosx*. If you have not yet installed *Tkmacosx*, [go ahead and refer to the above section titled **Install Tkmacosx**](https://github.com/benfertig/timestamper/blob/main/README.md#install-tkmacosx) before coming back here.

### Install Py2App
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

### Build the Time Stamper application (.app)
From a *Terminal* window, navigate to the *Time Stamper* source code directory by entering the command below, replacing {path_to_repository} with the directory that you have saved the *timestamper* repository to.
```
cd {path_to_repository}/src
```

Enter the following command:
```
python3 setup.py py2app
```

Your new *Time Stamper* application (.app) will be created in a directory called "dist" within the "src" directory. This program should run when you double-click on it. However, you will likely need to follow one additional step in order to make the *Time Stamper* application you built a truly standalone program.<br />

### Copy some extra libraries to the Time Stamper application (.app) package
On the particular *Macintosh* computer where the *Time Stamper* application (.app) was initially built, a glitch was causing the *Time Stamper* application not to run if the preconfigured *Anaconda*/*Miniconda* distribution from earlier had not been installed on the computer.<br />

This obviously defeats the purpose of creating a *Time Stamper* application (.app) package, as the standalone *Time Stamper* application is meant to be truly standalone in the sense that it should not to rely on any outside libraries that do not already come preinstalled on any modern *Macintosh* computer.<br />

There is a workaround for this problem which involves copying a few libraries from your *anaconda3*/*miniconda3* folder to the *Time Stamper* .app package:
* Find your *anaconda3*/*miniconda3* directory by entering the following command from *Terminal*:
```
which python
```
* A file path should be displayed that has either "anaconda3" (if you installed *Python 3* through *Anaconda*) or "miniconda3" (if you installed *Python 3* through Miniconda) somewhere in its name.
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
