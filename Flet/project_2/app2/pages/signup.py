import flet as ft
from flet_route import Basket, Params
# from Flet.project_2.app2.utils.styles import *
from Programming.Flet.project_2.app2.utils.styles import *
import sqlite3
import time


class SignupPage:
    def view(self, page: ft.Page, basket: Basket, params: Params):
        self.page = page
        self.page.window.width = windows_width
        self.page.window.height = windows_height
        self.page.window.resizable = False

        # АУТЕНФИКАЦИЯ
        def panel_auth_user(e):
            login = self.login_user.value
            password = self.password.value

            with sqlite3.connect(r"database\database_project.db") as conn:
                cur = conn.cursor()
                cur.execute(f"""SELECT * FROM user_data WHERE log='{login}' AND password = '{password}'""")
                data = cur.fetchone()

            if data != None:
                login = ''
                password = ''
                self.page.update()
                self.page.go(route="/head")

            else:
                self.login_btn.text = btn_text_auth_after
                self.password.value = ""
                self.login_btn.disabled = True
                self.page.update()
                time.sleep(2)
                self.login_btn.text = btn_text_auth_before
                self.login_btn.update()

        # ANIMATION
        def animation_eyes(e):
            if self.image_deactive.opacity == 1:
                self.image_deactive.opacity = 0
            if (self.login_user.value == '' and self.password.value == '' and self.image_deactive.opacity == 0):
                self.image_deactive.opacity = 1
            if (self.login_user.value != '' and self.password.value != ''):
                self.login_btn.disabled = False
            if (self.login_user.value == '' or self.password.value == ''):
                self.login_btn.disabled = True
            self.login_btn.update()
            self.image_deactive.update()

        # IMAGES
        self.image_deactive = ft.Image(
            src="Jocker_deative.png",
            animate_opacity=300,
            fit=ft.ImageFit.FILL,
            width=windows_width,
            height=windows_height,
            opacity=1
        )
        self.image_active = ft.Image(src="Jocker_active.png",
                                     animate_opacity=300,
                                     fit=ft.ImageFit.FILL,
                                     width=windows_width,
                                     height=windows_height,
                                     opacity=1)

        # КНОПКА ОТПРАВКИ login and password
        self.login_btn = ft.ElevatedButton(
            text=btn_text_auth_before,
            width=250,
            style=btn_style,
            bgcolor=ft.colors.TRANSPARENT,
            on_click=panel_auth_user
        )

        # ТЕКСТОВЫЕ ПОЛЯ login and password
        self.login_user = ft.TextField(label='User Login',
                                       color='red',
                                       label_style=ft.TextStyle(color='red'),
                                       on_change=animation_eyes)
        self.password = ft.TextField(label='Password',
                                     color='red',
                                     label_style=ft.TextStyle(color='red'),
                                     on_change=animation_eyes,
                                     password=True,
                                     can_reveal_password=True)

        # КНОПКА ДЛЯ ПЕРЕКЛЮЧЕНИЯ СТРАНИЦ
        self.navigate_btn = ft.ElevatedButton(
            text="ОКНО РЕГИСТРАЦИИ",
            width=250,
            style=btn_style,
            bgcolor=ft.colors.TRANSPARENT,
            on_click=lambda e: page.go("/")
        )
        return ft.View(
            route="/signup",
            controls=[
                ft.Container(
                    ft.Stack(
                        [
                            self.image_active,
                            self.image_deactive,
                            ft.Container(
                                ft.Row([ft.Text('WELCOME', size=30, color='red')],
                                       alignment=ft.MainAxisAlignment.CENTER
                                       ), padding=ft.padding.only(top=windows_height / 3)
                            ),
                            ft.Container(
                                ft.Column(
                                    [
                                        self.login_user,
                                        self.password,
                                        ft.Row([self.login_btn], alignment=ft.MainAxisAlignment.CENTER),
                                        ft.Row([self.navigate_btn], alignment=ft.MainAxisAlignment.CENTER)
                                    ]
                                ),
                                padding=ft.padding.only(top=windows_height / 2.2, left=50, right=50)
                            )

                        ]
                    ), margin=bg_margin
                )
            ]
        )
