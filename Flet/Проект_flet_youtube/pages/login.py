import flet as ft
from flet_route import Params, Basket
from Flet.Проект_flet_youtube.utils.styles import *


class LoginPage:

    email_input = ft.Container(
        content=ft.TextField(
            label="Укажите email",
            bgcolor=secondaryBgColor,
            border=ft.InputBorder.NONE,
            filled=True,
            color=secondaryFgColor
        ),
        border_radius=15
    )

    password_input = ft.Container(
        content=ft.TextField(
            label="Укажите пароль",
            bgcolor=secondaryBgColor,
            border=ft.InputBorder.NONE,
            filled=True,
            color=secondaryFgColor,
            password=True,
            can_reveal_password=True
        ),
        border_radius=15
    )

    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = "Страница авторизации"
        page.window.width = defaultWidthWindow
        page.window.height = defaultHeightWindow
        page.window.min_width = 600
        page.window.min_height = 400


        return ft.View(
            route="/",
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        ft.Container(
                            expand=2,
                            padding=ft.padding.all(40),
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(
                                        "Приветствую Вас",
                                        color=defaultFgColor,
                                        size=25,
                                        weight=ft.FontWeight.NORMAL),
                                    self.email_input,
                                    self.password_input,
                                    ft.Container(
                                        content=
                                            ft.Text(
                                                "Войти в аккаунт",
                                                color=defaultFgColor,
                                                size=20
                                            ),
                                        alignment=ft.alignment.center,
                                        height=40,
                                        bgcolor=hoverBgColor,
                                        border_radius=15,
                                        on_click=lambda e: page.go("/general")

                                    ),
                                    ft.Container(
                                        content=
                                            ft.Text(
                                                "Регистрация",
                                                color=defaultFgColor,
                                                size=20
                                            ),
                                        on_click=lambda e: page.go("/signup")
                                    )
                                ]
                            )
                        ),
                        ft.Container(
                            expand=3,
                            image_src="red_girl.png",
                            image_fit=ft.ImageFit.COVER,
                            content=ft.Column(
                                controls=[
                                    ft.Icon(
                                        name=ft.icons.LOCK_PERSON_ROUNDED,
                                        color=hoverBgColorPink,
                                        size=140,
                                        opacity=0.3
                                    ),
                                    ft.Text(
                                        'Авторизация',
                                        color=hoverBgColorPink  ,
                                        size=20,
                                        weight=ft.FontWeight.BOLD
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            )
                        )
                    ]
                )
            ],
            bgcolor=defaultBgColor,
            padding=0
        )