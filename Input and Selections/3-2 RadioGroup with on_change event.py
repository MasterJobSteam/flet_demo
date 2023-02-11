import flet as ft

def main(page):
  def radiogroup_changed(e):
    t.value = f"Your favorite color is:  {e.control.value}"
    # t.value = f"Your favorite color is:  {cg.value}"  # 或者直接使用控件值
    page.update()

  t = ft.Text()
  cg = ft.RadioGroup(content=ft.Column([
    ft.Radio(value="red", label="Red"),
    ft.Radio(value="green", label="Green"),
    ft.Radio(value="blue", label="Blue")]), on_change=radiogroup_changed)
  
  page.add(ft.Text("Select your favorite color:"), cg, t)

ft.app(target=main)