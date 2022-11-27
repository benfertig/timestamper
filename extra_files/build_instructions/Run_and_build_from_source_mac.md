# Run and Build from Source on Mac

## Table of Contents
* [Make sure your default shell is set to *Z shell*](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_mac.md#make-sure-your-default-shell-is-set-to-z-shell)
* [Install *Python 3*](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_mac.md#install-python-3)
* [Activate your *conda* environment](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_mac.md#activate-your-conda-environment)
* [Run from source on *Mac*](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_mac.md#run-from-source-on-mac)
    * [Install *Tkmacosx*](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_mac.md#install-tkmacosx)
    * [Run *Time Stamper.py*](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_mac.md#run-time-stamperpy)
* [Build from source on *Mac*](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_mac.md#build-from-source-on-mac)
    * [*Tkmacosx*](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_mac.md#tkmacosx)
    * [Install *Py2App*](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_mac.md#install-py2app)
    * [Build the *Time Stamper* application (.app)](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_mac.md#build-the-time-stamper-application-app)
    * [Copy some extra libraries to the *Time Stamper* application (.app) package](https://github.com/benfertig/timestamper/blob/main/extra_files/build_instructions/Run_and_build_from_source_mac.md#copy-some-extra-libraries-to-the-time-stamper-application-app-package)
* [Bundle the *Time Stamper* program into a disk image (.dmg) (optional)]()
    * [Move the *Time Stamper* application (.app) to the appropriate directory]()
    * [Include any other files that you would like to be bundled in the *Time Stamper* disk image (.dmg)]()
    * [Create the *Time Stamper* disk image (.dmg)]()

## Make sure your default shell is set to *Z shell*
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

## Install *Python 3*
It is highly recommended that you install a version of *Python* that includes *conda* i.e., *Anaconda* or *Miniconda*. In fact, later steps in this README assume that you have installed a *conda*-based distribution of *Python*. If you insist on using a *Python* distribution that you acquired through other means, then it is not guaranteed that you will be able to follow along with the rest of this README without running into additional problems.<br />

If you have no other uses for *Python* and all you are looking to do is run/build the *Time Stamper* program from the source code, *Miniconda* will provide everything you need. [You can download the latest *Miniconda* installer here](https://docs.conda.io/en/latest/miniconda.html).<br />

Unless you know what you are doing, do not concern yourself with any of the installers that end in "bash". Only select from the installers that that end in "pkg".<br />

There are *Miniconda* installers for ***Intel*** *Macs* as well as ***M1*** *Macs*. You should choose the installer that matches the type of processor your *Mac* has. To find out which type of processor your *Mac* has:<br />
* Click on the *Apple* logo in the top-left corner of your screen.<br />
* Select "About This Mac".<br />
* In the "Overview" tab, look for a field labeled either "Chip" or "Processor".
    * **If you see "M1":**
        * Download the *Miniconda* installer with "M1" in its name.
    * **If you see "Intel":**
        * Download the *Miniconda* installer with "Intel" in its name.<br />

Once you have downloaded the correct *Miniconda* installer for your *Mac*, run the installer to install *Python* with *Miniconda*.<br />

## Activate your *conda* environment
**NOTE:** If you *do not* see "(base)" in your command prefix when you open a new *Terminal* window, then this section is for you. Otherwise, you can skip to the section titled [**Run from source on Mac**](https://github.com/benfertig/timestamper/blob/main/MAC_RUN_AND_BUILD_FROM_SOURCE.md#run-from-source-on-mac).

When entering any *Terminal* commands found throughout the rest of this README, you **ALWAYS** need to make sure that the prefix of your Terminal input reads "(base)". This is an indication that all *conda*/*pip*/*python* commands will default to your custom *Anaconda*/*Miniconda* installation unless instructed otherwise.<br />

Whenever you *do not* see "(base)" in your *Terminal* command prefix, you must **ALWAYS** make sure that you enter the following command before typing any other commands that begin with "conda", "pip" or "python":
```
conda activate
```
This command should have activated your base *conda* environment. You will know if your base *conda* environment has been activated if you can see the text "(base)" in your *Terminal* command prefix.<br />

Remember, **ALWAYS** make sure that you enter any *conda*/*pip*/*python* commands from within your base *conda* environment.

## Run from source on *Mac*
### Install *Tkmacosx*
To make the *Time Stamper* program function on a *Macintosh* computer, you will need to install one additional *Python* package called *Tkmacosx*. If you installed *Python* through *Anaconda*/*Miniconda*, it is **recommended** that you [install *Tkmacosx* through *conda*](https://anaconda.org/saad_7/tkmacosx), which you can do by entering the following command from a *Terminal* window:
```
conda install -c saad_7 tkmacosx
```

Alternatively, you can [install *Tkmacosx* through *pip*](https://pypi.org/project/tkmacosx/) by entering the following command from a *Terminal* window:
```
pip3 install tkmacosx
```

### Run *Time Stamper.py*
[**Download the *timestamper* repository to your computer**](https://github.com/benfertig/timestamper/archive/refs/heads/main.zip) if you have not done so already.<br />

From a *Terminal* window, navigate to the source code directory by entering the command below, replacing {path_to_repository} with the directory that you have saved the *timestamper* repository to:
```
cd {path_to_repository}/src
```

Then, enter the following command:
```
python3 -u "Time Stamper.py"
```

The *Time Stamper* program should now open in a new window. Congratulations, you are now running the *Time Stamper* program from the source code on a *Mac* using your own pre-installed *Python* interpreter.<br />

If you would like to build your own standalone application (.app) of the *Time Stamper* program from the source code, follow the instructions below.

## Build from source on *Mac*
### *Tkmacosx*
If you have been following along with these instructions since the section titled [**Run from source on Mac**](https://github.com/benfertig/timestamper/blob/main/MAC_RUN_AND_BUILD_FROM_SOURCE.md#run-from-source-on-mac), then you should have already installed *Tkmacosx*. If you have not yet installed *Tkmacosx*, go ahead and refer to the above section titled [**Install Tkmacosx**](https://github.com/benfertig/timestamper/blob/main/MAC_RUN_AND_BUILD_FROM_SOURCE.md#install-tkmacosx) before coming back here.

### Install *Py2App*
The *Mac* application (.app) for the *Time Stamper* program was made using *Py2App*, which you can install through either *conda* or *pip*.<br />

If you installed *Python* through *Anaconda*/*Miniconda*, it is **recommended** that you [install Py2App through *conda*](https://anaconda.org/conda-forge/py2app), which you can do by entering the following command from a *Terminal* window:
```
conda install -c conda-forge py2app
```

Alternatively, you can [install *Py2App* through *pip*](https://pypi.org/project/py2app/) by entering the following command from a *Terminal* window:
```
pip3 install py2app
```

**NOTE:** In recreating the steps for this build so that I could list them in detail here in this README, I was able to build the *Time Stamper* application (.app) without ever needing to explicitly download *Py2App* through *conda* or *pip*, which is peculiar. There is clearly something I do not quite understand about the way *Py2App* works. Nonetheless, it will not hurt to install *Py2App* manually as outlined in this section. If you are feeling adventurous, you can go ahead and try following along with the rest of this README without installing *Py2App*.

### Build the *Time Stamper* application (.app)
From a *Terminal* window, navigate to the *Time Stamper* source code directory by entering the command below, replacing {path_to_repository} with the directory that you have saved the *timestamper* repository to:
```
cd {path_to_repository}/src
```

Enter the following command:
```
python3 setup.py py2app
```

Your new *Time Stamper* application (.app) will be created in a directory called "dist" within the "src" directory. This program should run when you double-click on it. However, you will likely need to follow one additional step in order to make the *Time Stamper* application you built a truly standalone program.<br />

### Copy some extra libraries to the *Time Stamper* application (.app) package
On the particular *Macintosh* computer where the *Time Stamper* application (.app) was initially built, a glitch was causing the *Time Stamper* application not to run if the preconfigured *Anaconda*/*Miniconda* distribution from earlier had not been installed on the computer.<br />

This obviously defeats the purpose of creating a *Time Stamper* application (.app) package, as the standalone *Time Stamper* application is meant to be truly standalone in the sense that it should not need to rely on any outside libraries that do not already come preinstalled on any modern *Macintosh* computer.<br />

There is a workaround for this problem which involves copying a few libraries from your *anaconda3*/*miniconda3* folder to the *Time Stamper* .app package:
* Find your *anaconda3*/*miniconda3* directory by entering the following command from *Terminal*:
    ```
    which python
    ```
* A file path should be displayed that has either "anaconda3" (if you installed *Python 3* through *Anaconda*) or "miniconda3" (if you installed *Python 3* through Miniconda) somewhere in its name.
* Navigate to the displayed *anaconda3*/*miniconda3* directory from a *Finder* window, disregarding the part of the file path that comes after "anaconda3"/"miniconda3".
* Your *anaconda3*/*miniconda3* directory may very well be hidden in *Finder*, but you can make *Finder* display hidden files and folders by pressing command+shift+. (command shift dot). You can hide these files and folders by pressing the same keys again.
* Once you have navigated to your *anaconda3*/*miniconda3* folder, enter the folder named "lib"
* **If your *Mac* has an *M1* processor:**
    * Copy the following three files to your clipboard:
        ```
        libffi.8.dylib
        libtcl8.6.dylib
        libtk8.6.dylib
        ```
    * Now navigate to the *Time Stamper* application (.app) you created earlier, right-click on it and select "Show Package Contents".
    * Then, go to "Contents" -> "Frameworks".
    * Paste the three .dylib files you just copied into this "Frameworks" folder.<br />
* **Alternatively, if your *Mac* has an *Intel* processor:**
    * Copy the following three files to your clipboard:
        ```
        libffi.7.dylib
        libtcl8.6.dylib
        libtk8.6.dylib
        ```
    * Now navigate to the *Time Stamper* application (.app) you created earlier, right-click on it and select "Show Package Contents".
    * Then, go to "Contents" -> "Resources" -> "lib".
    * Paste the three .dylib files you just copied into this "lib" folder.<br />

You can now exit out of all *Finder* windows. You should now be able to run the *Time Stamper* application (.app) as a standalone program that does not require any external libraries. Congratulations, you have successfully built the *Time Stamper* program from the source code on a *Mac*.

## Bundle the *Time Stamper* program into a disk image (.dmg) (optional)
The *Time Stamper* application (.app) that you just generated provides a fully functional build of the *Time Stamper* program. By simply double-clicking on this application (.app), you can run the *Time Stamper* program.

However, the *Mac* downloads for the *Time Stamper* program on [the releases page for this repository](https://github.com/benfertig/timestamper/releases) are not simply standalone *Time Stamper* application (.app) files like the one you just generated, but rather disk image (.dmg) files that, when run, create a disk image on your *Mac* that contain the *Time Stamper* program files which you can then save to your hard drive.

There are two reasons why the official *Mac* releases for the *Time Stamper* program are bundled into disk image (.dmg) files:
* Additional files can be included in a disk image (e.g. a copy of the *Time Stamper* program's license).
* *GitHub* does not allow *Mac* application (.app) files to be uploaded as part of a release. This is mainly due to the fact that *Mac* application (.app) files are technically not files at all, but rather folders containing all of the files necessary to make the relevant application run properly. *Mac* computers simply know to interpret folders ending in ".app" as applications when the user double clicks on-them.

With that being said, packaging the *Time Stamper* program into a disk image (.dmg) is not necessary in order to make the *Time Stamper* program run properly, and will not alter the functionality of the *Time Stamper* program in any way. Therefore, creating a *Time Stamper* disk image (.dmg) is optional.

If you would like to know how to package the *Time Stamper* program into a disk image (.dmg), follow the instructions below.

### Move the *Time Stamper* application (.app) to the appropriate directory
You are free to include whichever files you like within the disk image (.dmg) for the *Time Stamper* program.

Versions 0.2.0 and later of the official *Time Stamper* release bundle the following files along the *Time Stamper* application (.app) in the *Time Stamper* disk image (.dmg):
* A copy of the *Time Stamper* program's license ("LICENSE.txt")
* A list of outside sources that were used to help create the *Time Stamper* program ("Attribution.txt")

To include the aforementioned files in the *Time Stamper* disk image (.dmg), first navigate to the following directory:
```
{path_to_repository}/extra_files/setup_files/mac
```
Then, find the folder whose name corresponds to the version of the *Time Stamper* program the source code you downloaded is associated with. The name of this folder will have the following format (where {release_number} is replaced with the version of the *Time Stamper* program that is associated with the source code you downloaded):
```
Time Stamper {release_number}
```
For example, if you downloaded the source code associated with release 0.2.0 of the *Time Stamper* program, locate the folder with the following name:
```
Time Stamper 0.2.0
```
Once you have located the correct folder, place the *Time Stamper* application (.app) you previously generated into this folder.

### Include any other files that you would like to be bundled in the *Time Stamper* disk image (.dmg)
In addition to the *Time Stamper* application (.app) that you previously generated, you should now place any other files that you would like to be included in the *Time Stamper* disk image (.dmg) into the folder that you just placed the *Time Stamper* application (.app) into.

### Create the *Time Stamper* disk image (.dmg)
You are now ready to create the *Time Stamper* disk image (.dmg).

First, open *Disk Utility*. You can find *Disk Utility* by searching for it at the top-right of the screen from the toolbar.

Next, select "File" from the drop-down menu at the top of the screen and then select "New Image" -> "Image from Folder...".

In the new *Finder* window that appears, select the folder that you have saved the *Time Stamper* application (.app) to.
* Remember, this folder should also include any of the other files that you want to be bundled in the *Time Stamper* disk image (.dmg).
* Also, make sure that you are satisfied with the name of this folder, as the name of this folder will be the name of the virtual drive that is extracted from the disk image (.dmg) file that you are about to create.

Once you have selected the folder that contains all of the files you would like to include in your *Time Stamper* disk image (.dmg), a new drop-down menu will appear. This menu will ...
* prompt you to enter a name for the *Time Stamper* disk image (.dmg). You can name the disk image whatever you like.
* allow you to select the location that you would like to save the *Time Stamper* disk image (.dmg) to.
* ask you whether you would like the *Time Stamper* disk image (.dmg) to be encrypted.
* allow you to set the image format of the *Time Stamper* disk image (.dmg).

Once you are satisfied with your settings, click "Save". Your new disk image (.dmg) will be generated. Congratulations, you have successfully bundled the *Time Stamper* program into a *Mac* disk image (.dmg).
