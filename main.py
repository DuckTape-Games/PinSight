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
import flet as ft                       # UI framework   
#Custom imports
from ui import main_screen as ms        # Main/home screen UI
from ui import bowler_screen as bs      # Bowler management screen UI
from utils import helpers as help       # Helper functions

'''
List All imports here for easy access and organization. This includes both standard library imports and third-party libraries
import flet as ft                       # UI framework
import pandas as pd                     # Data processing and analytics
import matplotlib.pyplot as mp          # Data visualization (graphs/charts)
import sqlite3 as sqlite                # SQLite database access
import os, sys                          # For file path handling and system operations
'''


####################
### Screen Setup ###
####################

# Main entry point for the application, sets up routing and initial UI
def main(page: ft.Page):
    page.title = "PinSight"
    page.window.width = 1200
    page.window.height = 700
    page.window.resizable = False
    page.bgcolor = ft.Colors.WHITE
    page.theme = ft.Theme(
        color_scheme_seed = ft.Colors.BLUE, # Base color for the theme
    )
    page.window.icon = help.resource_path("ui/icon.ico") # Set the application icon using a helper function to get the correct path in both development and PyInstaller environments

    # Routing logic to switch between different screens/views
    def route_change(e=None):
        page.views.clear()

        # Always add the root view first
        page.views.append(ms.build_main_view(page))

        # Add extra views depending on current route
        if page.route == "/bowlers":
            page.views.append(bs.build_bowler_view(page))

        page.update() # Refresh the UI to reflect changes

    # Handle back navigation and view popping
    # When a view is popped (e.g. user clicks back), remove it from the stack and navigate to the previous view
    async def view_pop(e: ft.ViewPopEvent):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Set up event handlers for routing and view management
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Build initial UI
    route_change() # Trigger initial route setup to display the main screen


ft.app(target=main) # Start the Flet application with the main function as the entry point