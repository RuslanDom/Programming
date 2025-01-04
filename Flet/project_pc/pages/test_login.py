import flet as ft
from flet_route import Params, Basket
from Flet.project_pc.utils.style import *


class TestLoginPage:

    email_input = ft.Container(
        content=ft.TextField(
            label="Укажите EMAIL",
            bgcolor=secondBgColor,
            border=ft.InputBorder.NONE,
            color=secondFontColor,
            filled=True,
            width=300
        ), border_radius=15
    )
    password_input = ft.Container(
        content=ft.TextField(
            label="Укажите EMAIL",
            bgcolor=secondBgColor,
            border=ft.InputBorder.NONE,
            color=secondFontColor,
            filled=True,
            password=True,
            can_reveal_password=True,
            width=300
        ),
        border_radius=15
    )

    def view(self, page: ft.Page,  params: Params, basket: Basket):
        page.title = "Test"
        page.theme_mode = 'Dark'
        page.window.width = defaultWidthWindow
        page.window.height = defaultHeightWindow
        page.window.min_width = 800
        page.window.min_height = 400

        login_link = ft.Container(
            ft.Text("Страница авторизации", color=defaultFontColor),
            on_click=lambda e: page.go("/")
        )

        return ft.View(
            "/test",
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(),
                            ft.Column(
                                controls=[
                                    self.email_input,
                                    self.password_input,
                                    login_link
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.START
                    ),
                    image_src="usa_banner_twilight.png",
                    image_fit=ft.ImageFit.COVER,
                    padding=ft.padding.all(40),
                    expand=True
                )
            ],
            padding=ft.padding.all(0)
        )
