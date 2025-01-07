import time
from Flet.project_pc.utils.Database import Database
import flet as ft
from flet_route import Params, Basket
from Flet.project_pc.utils.style import *
from Flet.project_pc.utils.validation import Validator
from Flet.project_pc.utils.function import hash_password


class SignupPage:

    validation = Validator()

    error_field = ft.Text("", color="#ffffff", size=20, text_align=ft.TextAlign.CENTER)

    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = "Страница регистрации"
        page.window.width = defaultWidthWindow
        page.window.height = defaultHeightWindow
        page.window.min_width = 800
        page.window.min_height = 400
        page.theme_mode = 'DARK'

        def update_BG_field(e):
            self.error_field.value = ""
            self.email_input.content.bgcolor = secondBgColor
            self.login_input.content.bgcolor = secondBgColor
            self.password_input.content.bgcolor = secondBgColor
            self.repeat_password_input.content.bgcolor = secondBgColor
            page.update()

        self.email_input = ft.Container(
            content=ft.TextField(
                label="Укажите EMAIL",
                bgcolor=secondBgColor,
                border=ft.InputBorder.NONE,
                color=secondFontColor,
                filled=True
            ),
            border_radius=15
        )

        self.login_input = ft.Container(
            content=ft.TextField(
                label="Придумайте логин",
                bgcolor=secondBgColor,
                border=ft.InputBorder.NONE,
                color=secondFontColor,
                filled=True
            ),
            border_radius=15
        )

        self.password_input = ft.Container(
            content=ft.TextField(
                label="Придумайте пароль",
                bgcolor=secondBgColor,
                border=ft.InputBorder.NONE,
                color=secondFontColor,
                filled=True,
                password=True,
                can_reveal_password=True
            ),
            border_radius=15
        )

        self.repeat_password_input = ft.Container(
            content=ft.TextField(
                label="Повторите пароль",
                bgcolor=secondBgColor,
                border=ft.InputBorder.NONE,
                color=secondFontColor,
                filled=True,
                password=True,
                can_reveal_password=True
            ),
            border_radius=15
        )


        login_link = ft.Container(
            ft.Text("Страница авторизации", color=defaultFontColor),
            on_click=lambda e: page.go('/')
        )

        button_register = ft.Container(
            ft.Text("Зарегистрироваться", color=defaultBgColor),
            height=40,
            bgcolor=hoverBgColor,
            alignment=ft.alignment.center,
            on_click=lambda e: check_valid_signup(e),
            border_radius=15
        )

        def check_valid_signup(e):
            login_value = self.login_input.content.value
            email_value = self.email_input.content.value
            password_value = self.password_input.content.value
            repeat_pass_value = self.repeat_password_input.content.value
            update_BG_field(e)
            if login_value and email_value and password_value and repeat_pass_value:
                db = Database()
                if db.check_login(login_value):
                    self.error_field.value = "ТАКОЙ LOGIN УЖЕ ЕСТЬ СУЩЕСТВУЕТ!"
                    self.login_input.content.bgcolor = errorFieldBgColor
                    page.update()
                elif not self.validation.check_email(email_value):
                    self.error_field.value = "НЕ ВЕРНЫЙ ФОРМАТ EMAIL!"
                    self.email_input.content.bgcolor = errorFieldBgColor
                    page.update()
                elif db.check_email(email_value):
                    self.error_field.value = "ТАКОЙ EMAIL УЖЕ ЕСТЬ СУЩЕСТВУЕТ!"
                    self.email_input.content.bgcolor = errorFieldBgColor
                    page.update()
                elif not self.validation.check_password(password_value):
                    self.error_field.value = "СЛИШКОМ СЛАБЫЙ ПАРОЛЬ!"
                    self.password_input.content.bgcolor = errorFieldBgColor
                    page.update()
                elif password_value != repeat_pass_value:
                    self.error_field.value = "ПАРОЛИ НЕ СОВПАДАЮТ!"
                    self.repeat_password_input.content.bgcolor = errorFieldBgColor
                    page.update()
                else:
                    db.insert_user(login=login_value, email=email_value, userpass=hash_password(password_value))
                    self.error_field.value = "ПОЗДРАВЛЯЕМ!\nУСПЕШНАЯ РЕГИСТРАЦИЯ!"
                    self.email_input.content.value =\
                        self.login_input.content.value =\
                        self.password_input.content.value =\
                        self.repeat_password_input.content.value = ""
                    page.update()
                    time.sleep(3)
                    self.error_field.value = ""
                    page.update()
            else:
                self.error_field.value = "НЕ ВСЕ ПОЛЯ ЗАПОЛНЕНЫ!"
                self.error_field.update()


        return ft.View(
            "/signup",
            controls=[
                ft.Row(
                    [
                                ft.Container(
                                    expand=2,
                                    padding=ft.padding.all(40),
                                    bgcolor=defaultBgColor,
                                    content=ft.Column(
                                        [
                                            ft.Text("Регистрация", color=defaultFontColor, size=25),
                                            self.error_field,
                                            self.login_input,
                                            self.email_input,
                                            self.password_input,
                                            self.repeat_password_input,
                                            button_register,
                                            login_link
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                    )
                                ),
                                ft.Container(
                                    expand=3,
                                    content=ft.Column(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Icon(name=ft.icons.VERIFIED_USER_ROUNDED, color=hoverBgColor, size=140),
                                            ft.Text("Форма регистрация", color=hoverBgColor, size=15)
                                        ]
                                    ),
                                    image_src="usa_banner_twilight.png",
                                    image_fit=ft.ImageFit.COVER
                                )
                            ], expand=True
                    )
                ],
            bgcolor=defaultBgColor,
            padding=ft.padding.all(0)
        )

