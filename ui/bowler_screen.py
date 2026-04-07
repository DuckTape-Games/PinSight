'''
Name -> "PinSight"
Description -> A tool for visualizing and analyzing bowling data
File Description -> Primary UI screen for PinSight and create/manage bowlers
Start Date -> April 6th 2026 (4/6/2026)
Lead Developer -> Chris Herriman Jr
Other Developers -> N/A
'''

import flet as ft                               # UI framework
from utils import helpers as help               # Helper functions for data processing and analytics
from utils import theme                         # Theme colors and styles
from data import database as db                 # Database access and management functions for PinSight application


def build_bowler_view(page: ft.Page) -> ft.View:
    selected_bowler_id = {"value": None} # Use a dict to allow modification within nested functions

    first_name_field = ft.TextField(label="First Name", width=260)
    last_name_field = ft.TextField(label="Last Name", width=260)
    nickname_field = ft.TextField(label="Nickname", width=260)
    dominant_hand_field = ft.Dropdown(
        label="Dominant Hand",
        width=260,
        options=[
            ft.dropdown.Option("Right"),
            ft.dropdown.Option("Left"),
            ft.dropdown.Option("Ambidextrous")
        ],
    )
    notes_field = ft.TextField(
        label="Notes", 
        multiline=True,
        min_lines = 3,
        max_lines=5,
        width=260,
    )
    status_text = ft.Text("", color=theme.TEXT_PRIMARY)
    bowler_list = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)

    def clear_form():
        selected_bowler_id["value"] = None
        first_name_field.value = ""
        last_name_field.value = ""
        nickname_field.value = ""
        dominant_hand_field.value = None
        notes_field.value = ""
        status_text.value = "Creating New Bowler"
        page.update()

    def load_bowler(bowler_id):
        row = db.get_bowler_by_id(bowler_id)
        if not row:
            status_text.value = "Bowler Not Found"
            return
        selected_bowler_id["value"] = row[0]
        first_name_field.value = row[1] or ""
        last_name_field.value = row[2] or ""
        nickname_field.value = row[3] or ""
        dominant_hand_field.value = row[4] or None
        notes_field.value = row[5] or ""
        status_text.value = f"Editing Bowler ID: {row[0]}"
        page.update()

    def refresh_bowler_list():
        rows = db.get_all_bowlers()
        bowler_list.controls.clear()

        if not rows:
            bowler_list.controls.append(
                ft.Text("No bowlers found.", color=theme.TEXT_SECONDARY)
            )
        else:
            for bowler_id, first_name, last_name, nickname, dominant_hand, notes in rows:
                display_name = f"{first_name} {last_name}"
                if nickname:
                    display_name += f' ("{nickname}")'

                subtitle_parts = []
                if dominant_hand:
                    subtitle_parts.append(dominant_hand)
                if notes:
                    subtitle_parts.append("Has notes")

                subtitle_text = " • ".join(subtitle_parts)

                bowler_list.controls.append(
                    ft.Container(
                        bgcolor=theme.CARD_COLOR,
                        border_radius=10,
                        padding=8,
                        content=ft.ListTile(
                            title=ft.Text(display_name, color=theme.TEXT_PRIMARY),
                            subtitle=ft.Text(subtitle_text, color=theme.TEXT_SECONDARY) if subtitle_text else None,
                            on_click=lambda e, bid=bowler_id: load_bowler(bid),
                        ),
                    )
                )

        page.update()

    def save_bowler(e):
        first_name = first_name_field.value.strip()
        last_name = last_name_field.value.strip()
        nickname = nickname_field.value.strip() if nickname_field.value else None
        dominant_hand = dominant_hand_field.value
        notes = notes_field.value.strip() if notes_field.value else None

        if not first_name or not last_name:
            status_text.value = "First name and last name are required."
            page.update()
            return

        if selected_bowler_id["value"] is None:
            db.add_bowler(first_name, last_name, nickname, dominant_hand, notes)
            status_text.value = "Bowler created."
        else:
            db.update_bowler(
                selected_bowler_id["value"],
                first_name,
                last_name,
                nickname,
                dominant_hand,
                notes,
            )
            status_text.value = "Bowler updated."

        refresh_bowler_list()
        clear_form()

    async def go_back(e):
        await page.push_route("/")

    form_section = ft.Container(
        expand=1,
        bgcolor=theme.CARD_COLOR,
        border_radius=12,
        padding=20,
        content=ft.Column(
            [
                ft.Text("Bowler Form", size=22, weight=ft.FontWeight.BOLD, color=theme.TEXT_PRIMARY),
                first_name_field,
                last_name_field,
                nickname_field,
                dominant_hand_field,
                notes_field,
                ft.Row(
                    [
                        ft.ElevatedButton("Save Bowler", on_click=save_bowler),
                        ft.OutlinedButton("Clear / New", on_click=lambda e: clear_form()),
                        ft.TextButton("Back to Main Screen", on_click=go_back),
                    ],
                    wrap=True,
                ),
                status_text,
            ],
            spacing=12,
        ),
    )

    list_section = ft.Container(
        expand=1,
        bgcolor=theme.CARD_COLOR,
        border_radius=12,
        padding=20,
        content=ft.Column(
            [
                ft.Text("Existing Bowlers", size=22, weight=ft.FontWeight.BOLD, color=theme.TEXT_PRIMARY),
                bowler_list,
            ],
            expand=True,
        ),
    )

    refresh_bowler_list()
    clear_form()

    return ft.View(
        route="/bowlers",
        appbar=ft.AppBar(title=ft.Text("Bowlers")),
        controls=[
            ft.Container(
                expand=True,
                bgcolor=theme.BG_COLOR,
                padding=20,
                content=ft.Row(
                    [
                        form_section,
                        ft.VerticalDivider(width=20, color="transparent"),
                        list_section,
                    ],
                    expand=True,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),
            )
        ],
    )