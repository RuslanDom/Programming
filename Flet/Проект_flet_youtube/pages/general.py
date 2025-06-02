import flet as ft
from flet_route import Params, Basket
from Flet.Проект_flet_youtube.utils.styles import *

class GeneralPage:

    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = "Главная страница"
        page.window.width = defaultWidthWindow
        page.window.height = defaultHeightWindow
        page.window.min_width = 600
        page.window.min_height = 400

        return ft.View(
            route="/general",
            controls=[
                ft.Container(
                    expand=True,
                    image_src="girl_with_racoon.png",
                    image_fit=ft.ImageFit.COVER,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                content=ft.Text("Выйти из аккаунта", color=defaultFgColor, size=20),
                                bgcolor=defaultBgColor,
                                border_radius=15,
                                height=40,
                                width=300,
                                alignment=ft.alignment.center,
                                on_click=lambda e: page.go("/")
                            ),
                            ft.Container(
                                expand=2
                            ),
                            ft.Container(
                                expand=2
                            )

                        ]
                    )
                )
            ],
            bgcolor=defaultBgColor,
            padding=0
        )