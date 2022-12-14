"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from glob import glob
from setuptools import setup

APP = ["Time Stamper.py"]

DATA_FILES = [

    # Add the macros.
    ("classes/macros", glob("classes/macros/*.*")),

    # Add the templates.
    ("classes/template", glob("classes/template/*.*")),
    ("classes/template/buttons", glob("classes/template/buttons/*.*")),
    ("classes/template/entries", glob("classes/template/entries/*.*")),
    ("classes/template/labels", glob("classes/template/labels/*.*")),
    ("classes/template/texts", glob("classes/template/texts/*.*")),
    ("classes/template/windows", glob("classes/template/windows/*.*")),

    # Add the timing files.
    ("classes/timing", glob("classes/timing/*.*")),

    # Add the widget files.
    ("classes/widgets", glob("classes/widgets/*.*")),

    # Add the images.
    ("images", glob("images/*.*")),

    # Add the messages.
    ("messages", glob("messages/*.*"))
]

OPTIONS = {"includes": ["tkmacosx"],
"iconfile": "../extra_files/setup_files/mac/file_icon_mac.icns"}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
