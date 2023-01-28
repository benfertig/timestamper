#-*- coding: utf-8 -*-
"""This module contains a dictionary, settings_default, which
contains all of the default settings of the Time Stamper program."""

settings_default = \
    {
        "output": {
            "path": "",
            "file_encoding": "utf-8"
        },
        "audio": {
            "path": ""
        },
        "pause": {
            "message_enabled": False,
            "message": "PAUSE"
        },
        "play": {
            "message_enabled": False,
            "message": "RESUME"
        },
        "stop": {
            "message_enabled": True,
            "message": "STOP"
        },
        "rewind": {
            "message_enabled": False,
            "message": "REWIND $amount seconds to $dest"
        },
        "fast_forward": {
            "message_enabled": False,
            "message": "FAST-FORWARD $amount seconds to $dest"
        },
        "record": {
            "message_enabled": True,
            "message": "START"
        },
        "hotkey_1": {
            "message": "HOTKEY 1"
        },
        "hotkey_2": {
            "message": "HOTKEY 2"
        },
        "hotkey_3": {
            "message": "HOTKEY 3"
        }
    }
