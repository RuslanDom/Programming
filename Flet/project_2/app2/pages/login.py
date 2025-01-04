import flet as ft
from flet_route import Basket, Params
from app2.utils.styles import *
import sqlite3
import time


class LoginPage:

    def view(self, page: ft.Page, basket: Basket, params: Params):
        self.page = page
        self.page.window.width = windows_width
        self.page.window.height = windows_height
        self.page.window.resizable = False
        
        # СОЗДАНИЕ БД И РЕГИСТРАЦИЯ
        def panel_registr(e):
            with sqlite3.connect(r"database\database_project.db") as conn:
                    cur = conn.cursor()
                    cur.execute("""CREATE TABLE IF NOT EXISTS user_data 
                                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                log VARCHAR(20), password VARCHAR(20))""")
                    
                    sql = """INSERT INTO user_data (log, password) VALUES (?, ?)"""
                    cur.execute(sql, (self.login_user.value, self.password.value))
                    conn.commit()
            self.login_user.value = ''
            self.password.value = ''
            self.login_btn.text = btn_text_after
            self.page.update()
            time.sleep(2)
            self.login_btn.text = btn_text_before
            self.login_btn.update()

        # IMAGES
        self.image_deactive = ft.Image(
                                    src="./Jocker_deative.png",
                                    animate_opacity=300,
                                    fit=ft.ImageFit.FILL,
                                    width=windows_width,
                                    height=windows_height,
                                    opacity=1
                                    )
        self.image_active = ft.Image(src="./Jocker_active.png",
                                    animate_opacity=300,
                                    fit=ft.ImageFit.FILL,
                                    width=windows_width,
                                    height=windows_height,
                                    opacity=1)
       
                           

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

        # КНОПКА ОТПРАВКИ login and password
        self.login_btn = ft.ElevatedButton(
                                            text="ОТДАТЬ ДУШУ",
                                            width=250,
                                            style= btn_style,
                                            bgcolor=ft.colors.TRANSPARENT,
                                            disabled=True,
                                            on_click=panel_registr
                                        )
        
        # КНОПКА ДЛЯ ПЕРЕКЛЮЧЕНИЯ СТРАНИЦ
        self.navigate_btn = ft.ElevatedButton(
                                            text="ОКНО АВТОРИЗАЦИИ",
                                            width=250,
                                            style= btn_style,
                                            bgcolor=ft.colors.TRANSPARENT,
                                            on_click=lambda e: page.go("/signup")
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
        

        return ft.View(
            route="/",
            controls=[
                        ft.Container(
                            margin=bg_margin,
                            content=ft.Stack(
                                [
                                    self.image_active,
                                    self.image_deactive,
                                    ft.Container(
                                            ft.Row([ft.Text('WELCOME', size=30, color='red')],
                                            alignment=ft.MainAxisAlignment.CENTER
                                            ),padding=ft.padding.only(top=windows_height/3)
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
                                            padding=ft.padding.only(top=windows_height/2.2, left=50, right=50)
                                        )
                                    ]
                                )
                            )

                        ]
                    )






