import time

import flet as ft
from flet_route import Params, Basket
from Flet.project_pc.utils.style import *
from Flet.project_pc.utils.Database import Database
from Flet.project_pc.utils.function import hash_password

class LoginPage:
    error_field = ft.Text("", color="#ffffff", size=20, text_align=ft.TextAlign.CENTER)

    login_input = ft.Container(
        content=ft.TextField(
            label="Укажите ваш логин",
            bgcolor=secondBgColor,
            border=ft.InputBorder.NONE,
            color=secondFontColor,
            filled=True
                             ),
        border_radius=15
    )

    password_input = ft.Container(
        content=ft.TextField(
            label="Введите пароль",
            bgcolor=secondBgColor,
            border=ft.InputBorder.NONE,
            color=secondFontColor,
            filled=True,
            password=True,
            can_reveal_password=True
        ),
        border_radius=15
    )

    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = "Страница авторизации"
        page.window.width = defaultWidthWindow
        page.window.height = defaultHeightWindow
        page.window.min_width = 800
        page.window.min_height = 400
        page.theme_mode = "DARK"

        def authorization(e):
            db = Database()
            login = self.login_input.content.value
            userpass = self.password_input.content.value
            if login and userpass:
                userpass = hash_password(userpass)
                if db.authorization_user(login=login, userpass=userpass):
                    page.session.set("auth_user", True)
                    page.go('/test')
                    self.login_input.content.value = self.password_input.content.value = ''
                    page.update()
                else:
                    self.error_field.value = "ВВЕДЕНЫ НЕВЕРНЫЕ ДАННЫЕ!"
                    self.error_field.update()
                    time.sleep(3)
                    self.error_field.value = ""
                    self.error_field.update()
            else:
                self.error_field.value = "ВВЕДИТЕ ДАННЫЕ!"
                self.error_field.update()
                time.sleep(3)
                self.error_field.value = ""
                self.error_field.update()


        signup_link = ft.Container(
                                        ft.Text("Создать аккаунт", color=defaultFontColor),
                                        on_click=lambda e: page.go("/signup")
                                    )

        test_link = ft.Container(
            ft.Text("Тестовая страница", color=defaultFontColor),
            on_click=lambda e: page.go("/test")
        )

        return ft.View(
            "/",
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
                                        color=defaultFontColor,
                                        size=25,
                                        weight=ft.FontWeight.NORMAL
                                    ),
                                    self.error_field,
                                    self.login_input,
                                    self.password_input,
                                    ft.Container(
                                        ft.Text("Авторизация",
                                                color=defaultBgColor),
                                        alignment=ft.alignment.center,
                                        height=40,
                                        bgcolor=hoverBgColor,
                                        border_radius=15,
                                        on_click=lambda e: authorization(e)
                                    ),
                                    signup_link,
                                    test_link
                                ]
                            )
                        ),
                        ft.Container(
                            expand=3,
                            image_src="usa_banner_twilight.png",
                            image_fit=ft.ImageFit.COVER,
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Icon(name=ft.icons.LOCK_PERSON_ROUNDED,
                                            color=hoverBgColor,
                                            size=140
                                            ),
                                    ft.Text("Авторизация",
                                            color=hoverBgColor,
                                            size=15,
                                            weight=ft.FontWeight.BOLD)
                                ]
                            )

                        )
                    ]
                )
            ],
            bgcolor=defaultBgColor,
            padding=ft.padding.all(0)
        )
