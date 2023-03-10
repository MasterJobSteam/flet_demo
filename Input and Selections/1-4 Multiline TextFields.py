import flet as ft

def main(page: ft.Page):

    def multiline_submit(e):
        print("触发提交事件！")

    page.add(
        ft.TextField(label="standard", multiline=True),
        ft.TextField(
            label="disabled",
            multiline=True,
            disabled=True,
            value="line1\nline2\nline3\nline4\nline5",
        ),
        ft.TextField(
            label="Auto adjusted height with max lines",
            multiline=True,
            min_lines=1,
            max_lines=3,
            shift_enter=True,
            on_submit=multiline_submit
        ),
    )

ft.app(target=main)