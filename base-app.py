import flet as ft

def main(page: ft.Page):
    # add/update controls on Page
    pass

ft.app(target=main)  # 默认在操作系统窗口启动
# ft.app(target=main, view=ft.WEB_BROWSER)  # 指定在 Web 中启动
# ft.app(target=main, port=9880)  # 指定端口启动