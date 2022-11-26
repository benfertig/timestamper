"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from glob import glob
from setuptools import setup

# The "classes" directory
classes_dir =  "classes"

# The "macros" directory
macros_dir = f"{classes_dir}/macros"

# The "template" directory
template_dir = f"{classes_dir}/template"

# The template subdirectories
buttons_dir = f"{classes_dir}/template/buttons"
entries_dir = f"{classes_dir}/template/entries"
labels_dir = f"{classes_dir}/template/labels"
texts_dir = f"{classes_dir}/template/texts"
windows_dir = f"{classes_dir}/template/windows"

# The "timing" directory
timing_dir = f"{classes_dir}/timing"

# The "widgets" directory
widgets_dir = f"{classes_dir}/widgets"

# The "images" directory
images_dir = "images"

# The "messages" directory
messages_dir = "messages"

APP = ["Time Stamper.py"]

DATA_FILES = [

    # Add the macros to the data files.
    (macros_dir, glob(f"{macros_dir}/*.*")),

    # Add the templates to the data files.
    (template_dir, glob(f"{template_dir}/*.*")),
    (buttons_dir, glob(f"{buttons_dir}/*.*")),
    (entries_dir, glob(f"{entries_dir}/*.*")),
    (labels_dir, glob(f"{labels_dir}/*.*")),
    (texts_dir, glob(f"{texts_dir}/*.*")),
    (windows_dir, glob(f"{windows_dir}/*.*")),

    # Add the timing files to the data files.
    (timing_dir, glob(f"{timing_dir}/*.*")),

    # Add the widget files. to the data files.
    (widgets_dir, glob(f"{widgets_dir}/*.*")),

    # Add the images to the data files.
    (images_dir, glob(f"{images_dir}/*.*")),

    # Add the messages to the data files.
    (messages_dir, glob(f"{messages_dir}/*.*"))
]

OPTIONS = {"includes": ["tkmacosx"],
"iconfile": "../extra_files/setup_files/mac/file_icon_mac.icns"}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
