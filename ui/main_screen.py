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
import flet as ft                               # UI framework
#Custom imports
from ui import bowler_screen as bs              # Bowler management screen UI
from utils import helpers as help               # Helper functions
from utils import theme                         # Theme colors and styles

def build_main_view(page: ft.Page) -> ft.View:
    async def open_bowler_screen(e):
        await page.push_route("/bowlers")
    return ft.View(
        route="/",
        controls=[
            ft.Container(
                bgcolor=theme.BG_COLOR, # Set background color from theme
                content=ft.Column(
                    [
                        
                        ft.Text("Welcome to PinSight!", size=28, weight=ft.FontWeight.BOLD, color=theme.TEXT_PRIMARY),
                        ft.ElevatedButton(
                            "Open Bowler Screen",
                            on_click=open_bowler_screen,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                expand=True,
                alignment=ft.Alignment.CENTER,
            )
        ],
    )