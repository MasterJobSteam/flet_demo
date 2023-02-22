import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Dropdown(
            label="Color",
            icon=ft.icons.COLOR_LENS,
            prefix_text="color: ",
            hint_text="Choose your favourite color?",
            options=[
                ft.dropdown.Option("Red"),
                ft.dropdown.Option("Green"),
                ft.dropdown.Option("Blue"),
            ],
            alignment=ft.alignment.Alignment(1,1)
        )
    )

ft.app(target=main)