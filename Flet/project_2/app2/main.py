import flet as ft
from app2.route import Router

def func(page:ft.Page):
    Router(page)


ft.app(target=func, assets_dir=r".\assets")








