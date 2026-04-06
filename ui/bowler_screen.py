'''
Name -> "PinSight"
Description -> A tool for visualizing and analyzing bowling data
File Description -> Primary UI screen for PinSight and create/manage bowlers
Start Date -> April 6th 2026 (4/6/2026)
Lead Developer -> Chris Herriman Jr
Other Developers -> N/A
'''

import customtkinter as ctk                    # UI framework
from utils import helpers as help               # Helper functions for data processing and analytics


def show_bowler_screen(screen):
    help.clear_screen(screen)
    # create UI elements
    header = ctk.CTkLabel(screen, text="Bowlers")
    header.pack()

    # add more UI elements here as needed (buttons, labels, etc)
    open_bowler_screen_button = ctk.CTkButton(screen, text="Open Bowler Screen")
    open_bowler_screen_button.place(x=500, y=300)
