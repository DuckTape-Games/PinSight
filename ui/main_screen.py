'''
Name -> "PinSight"
Description -> A tool for visualizing and analyzing bowling data
File Description -> Primary UI screen for PinSight
Start Date -> April 6th 2026 (4/6/2026)
Lead Developer -> Chris Herriman Jr
Other Developers -> N/A
'''

###############
### IMPORTS ###
###############
import customtkinter as ctk                     # UI framework
#Custom imports
from ui import bowler_screen as bs              # Bowler screen UI
from utils import helpers as help               # Helper functions

def show_main_screen(screen):
    help.clear_screen(screen)

    # create UI elements
    header = ctk.CTkLabel(screen, text="Welcome to PinSight")
    header.pack()

    # add more UI elements here as needed (buttons, labels, etc)
    open_bowler_screen_button = ctk.CTkButton(screen, text="Open Bowler Screen", command=lambda: bs.show_bowler_screen(screen))
    open_bowler_screen_button.place(x=500, y=300)
