'''
Name -> "PinSight"
Description -> A tool for visualizing and analyzing bowling data
File Description -> Helper functuions for PinSight application
Start Date -> April 6th 2026 (4/6/2026)
Lead Developer -> Chris Herriman Jr
Other Developers -> N/A
'''
###############
### IMPORTS ###
###############
import os, sys                          # For file path handling and system operations


### Makes onefile mode work in pyinstaller
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


### Helper function to clear all widgets from a screen/frame
def clear_screen(screen):
    for widget in screen.winfo_children():
        widget.destroy()