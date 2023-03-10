import flet as ft


def main(page: ft.Page):
    page.title = "Elevated buttons with icons"
    page.add(
        ft.ElevatedButton("Button with icon", icon="chair_outlined"),
        ft.ElevatedButton(
            "Button with colorful icon",
            icon="park_rounded",
            icon_color="green400",
        ),
    )

ft.app(target=main)