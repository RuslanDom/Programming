import flet as ft
from flet_route import Params, Basket
from Flet.Проект_flet_youtube.utils.styles import *


class SignupPage:
    login_input = ft.Container(
        ft.TextField(
            label="Придумайте логин",
            bgcolor=secondaryBgColor,
            color=secondaryFgColor,
            border=ft.InputBorder.NONE,
            filled=True
        ),
        border_radius=15
    )
    email_input = ft.Container(
        ft.TextField(
            label="Введите EMAIL",
            bgcolor=secondaryBgColor,
            color=secondaryFgColor,
            border=ft.InputBorder.NONE,
            filled=True
        ),
        border_radius=15
    )
    password_input = ft.Container(
        ft.TextField(
            label="Придумайте пароль",
            bgcolor=secondaryBgColor,
            color=secondaryFgColor,
            border=ft.InputBorder.NONE,
            password=True,
            can_reveal_password=True,
            filled=True
        ),
        border_radius=15
    )
    confirm_password_input = ft.Container(
        ft.TextField(
            label="Повторите пароль",
            bgcolor=secondaryBgColor,
            color=secondaryFgColor,
            border=ft.InputBorder.NONE,
            password=True,
            can_reveal_password=True,
            filled=True
        ),
        border_radius=15
    )

    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = "Страница регистрации"
        page.window.width = defaultWidthWindow
        page.window.height = defaultHeightWindow
        page.window.min_width = 600
        page.window.min_height = 400

        return ft.View(
            route="/signup",
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
                                        "Добро пожаловать",
                                        color=defaultFgColor,
                                        weight=ft.FontWeight.NORMAL,
                                        size=25
                                    ),
                                    self.login_input,
                                    self.email_input,
                                    self.password_input,
                                    self.confirm_password_input,
                                    ft.Container(
                                        ft.Text(
                                            "Зарегистрироваться",
                                            color=defaultFgColor,
                                            weight=ft.FontWeight.NORMAL,
                                            size=20
                                        ),
                                        bgcolor=hoverBgColor,
                                        alignment=ft.alignment.center,
                                        height=40,
                                        border_radius=15
                                    ),
                                    ft.Container(
                                        ft.Text(
                                            "Страница авторизации",
                                            color=defaultFgColor,
                                            weight=ft.FontWeight.NORMAL,
                                            size=20
                                        ),
                                        on_click=lambda e: page.go("/")
                                    )
                                ]
                            )
                        ),
                        ft.Container(
                            expand=3,
                            image_src="white_girl.png",
                            image_fit=ft.ImageFit.COVER,
                            content=ft.Column(
                                controls=[
                                    ft.Icon(
                                        name=ft.icons.LOCK_PERSON_ROUNDED,
                                        color=hoverBgColorPink,
                                        size=140,
                                        opacity=0.4
                                    ),
                                    ft.Text(
                                        "Регистрация",
                                        color=hoverBgColorPink,
                                        size=25,
                                        weight=ft.FontWeight.BOLD
                                    ),
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