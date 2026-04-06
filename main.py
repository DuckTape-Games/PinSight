'''
Name -> "PinSight"
Description -> A tool for visualizing and analyzing bowling data
File Description -> Entry point for PinSight application
Start Date -> April 6th 2026 (4/6/2026)
Lead Developer -> Chris Herriman Jr
Other Developers -> N/A
'''

###############
### IMPORTS ###
###############
import customtkinter as ctk                    # UI framework
#Custom imports
from ui import main_screen as ms        # Main/home screen UI
from utils import helpers as help       # Helper functions

'''
List All imports here for easy access and organization. This includes both standard library imports and third-party libraries
import customtkinter as ctk             # UI framework
import pandas as pd                     # Data processing and analytics
import matplotlib.pyplot as mp          # Data visualization (graphs/charts)
import sqlite3 as sqlite                # SQLite database access
import os, sys                          # For file path handling and system operations
'''


####################
### Screen Setup ###
####################
screen = ctk.CTk()
screen.geometry("1200x700")
screen.resizable(False, False)
screen.title("PinSight")   
screen.iconbitmap(help.resource_path("ui/icon.ico"))

ms.show_main_screen(screen)



screen.mainloop()
