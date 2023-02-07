import flet as ft
import time

def main(page: ft.Page):
    # t = ft.Text(value="Hello, world!", color="green")
    # page.controls.append(t)
    # page.update()

    # t = ft.Text()
    # page.add(t) # it's a shortcut for page.controls.append(t) and then page.update()

    # for i in range(10):
    #     t.value = f"Step {i}"
    #     page.update()
    #     time.sleep(1)
    
    # for i in range(10):
    #     page.controls.append(ft.Text(f"Line {i}"))
    #     if i > 4:
    #         page.controls.pop(0)
    #     page.update()
    #     time.sleep(0.3)
    
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

    first_name = ft.TextField(value="zhang")
    last_name = ft.TextField(value='bo')
    first_name.disabled = True
    last_name.disabled = False
    page.add(first_name, last_name)

ft.app(target=main)