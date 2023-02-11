import flet as ft

def main(page: ft.Page):
    def button_clicked(e):
        t.value = f"Textboxes values are:  '{tb1.value}', '{tb2.value}', '{tb3.value}', '{tb4.value}', '{tb5.value}'."
        page.update()

    t = ft.Text()
    tb1 = ft.TextField(border_color=ft.colors.TRANSPARENT)
    tb2 = ft.TextField(label="Disabled", disabled=True, value="First name", border_radius=ft.border_radius.horizontal(30,30), content_padding=ft.padding.only(left=100))
    tb3 = ft.TextField(label="Read-only", read_only=True, value="Last name", filled=True)
    tb4 = ft.TextField(label="With placeholder", hint_text="Please enter text here", counter_text='0/12', helper_text="help text", dense=True)
    tb5 = ft.TextField(label="With an icon", icon=ft.icons.EMOJI_EMOTIONS, error_text="error text")
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    page.add(tb1, tb2, tb3, tb4, tb5, b, t)

ft.app(target=main)