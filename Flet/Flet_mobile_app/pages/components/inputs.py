from Flet.Flet_mobile_app.utils.style import *

def input_phone(text: str) -> ft.Container:
    return ft.Container(
        content=ft.Text(text),
        alignment=ft.alignment.center_left,
        width=230
    )

def input_web(text: str) -> ft.Container:
    return ft.Container(
        content=ft.Text(text),
        alignment=ft.alignment.center_left,
        width=360
    )