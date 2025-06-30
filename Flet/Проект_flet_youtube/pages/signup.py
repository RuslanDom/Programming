import flet as ft
from flet_route import Params, Basket
from Flet.Проект_flet_youtube.utils.styles import *
from Flet.Проект_flet_youtube.utils.validation import Validator
from Flet.Проект_flet_youtube.utils.funcs import hash_password
from Flet.Проект_flet_youtube.models import db, AdminUserTable
import time

class SignupPage:
    validation = Validator()

    image_container = ft.Container(
        expand=3,
        image_src="white_girl.png",
        image_fit=ft.ImageFit.COVER,
        content=ft.Column(
            controls=[
                ft.Icon(
                    name=ft.icons.VERIFIED_USER_ROUNDED,
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

    error = ft.Container(
        ft.Text(
            "", color="red", size=20, text_align=ft.TextAlign.CENTER
        ),
        alignment=ft.alignment.center
    )

    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = "Страница регистрации"
        page.window.width = defaultWidthWindow
        page.window.height = defaultHeightWindow
        page.window.min_width = 600
        page.window.min_height = 400
        register_button = ft.Container(
                                        ft.Text(
                                            "Зарегистрироваться",
                                            color=defaultFgColor,
                                            weight=ft.FontWeight.NORMAL,
                                            size=20
                                        ),
                                        bgcolor=hoverBgColor,
                                        alignment=ft.alignment.center,
                                        height=40,
                                        border_radius=15,
                                        on_click=lambda e: signup(e)
                                    )
        backup_button = ft.Container(
                                        ft.Text(
                                            "Страница авторизации",
                                            color=defaultFgColor,
                                            weight=ft.FontWeight.NORMAL,
                                            size=20
                                        ),
                                        on_click=lambda e: page.go("/")
                                    )


        # ФУНКЦИЯ РЕГИСТРАЦИИ
        def signup(e):
            user: AdminUserTable = AdminUserTable()

            login: str = self.login_input.content.value
            email: str = self.email_input.content.value
            password: str = self.password_input.content.value
            confirm_password: str = self.confirm_password_input.content.value
            # print(login, email, password, confirm_password)

            # Проверки (валидация) на актуальность передаваемых данных при регистрации
            if email and password and confirm_password:
                if self.validation.email_valid(email):
                    self.error.content.value = "EMAIL не верный формат"
                    self.error.update()
                    time.sleep(3)
                elif user.check_email(email):
                    self.error.content.value = "Этот EMAIL уже зарегистрирован"
                    self.error.update()
                    time.sleep(3)
                elif user.check_login(login):
                    self.error.content.value = "Этот логин уже зарегистрирован"
                    self.error.update()
                    time.sleep(3)
                elif self.validation.password_valid(password):
                    self.error.content.value = "Пароль слишком слабый"
                    self.error.update()
                    time.sleep(3)
                elif password != confirm_password:
                    self.error.content.value = "Пароли не совпадают"
                    self.error.update()
                    time.sleep(3)
                else:
                    # Добавление в таблицу admin_user новой записи регистрации
                    user.insert_new_user(login, email, hash_password(password))
                    self.error.content.value = "Вы успешно зарегистрировались!"
                    self.error.content.color = "green"
                    self.login_input.content.value = ""
                    self.email_input.content.value = ""
                    self.password_input.content.value = ""
                    self.confirm_password_input.content.value = ""
                    page.update()
                    time.sleep(5)
                    self.error.content.color = "yellow"
                    self.error.content.value = "Вернитесь на страницу авторизации ->"
                    self.error.update()
                    time.sleep(5)
                    self.error.content.color = "red"
                    self.error.content.value = ""
                    self.error.update()
            else:
                self.error.content.value = "Не все поля заполнены"
                self.error.update()
                time.sleep(3)


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
                                    self.error,
                                    self.login_input,
                                    self.email_input,
                                    self.password_input,
                                    self.confirm_password_input,
                                    register_button,
                                    backup_button
                                ]
                            )
                        ),
                        self.image_container
                    ]
                )
            ],
            bgcolor=defaultBgColor,
            padding=0
        )