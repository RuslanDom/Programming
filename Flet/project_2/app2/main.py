import flet as ft
# from Flet.project_2.app2.route import Router
from Programming.Flet.project_2.app2.route import Router

def func(page: ft.Page):
    Router(page)


ft.app(target=func, assets_dir=r".\assets")
