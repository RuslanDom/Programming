import flet as ft
from flet_route import Basket, Params
from app2.utils.styles import *
import sqlite3
import time


class AppPage:

    def view(self, page: ft.Page, basket: Basket, params: Params):
        self.page = page
        self.page.window.width = windows_width
        self.page.window.height = windows_height
        self.page.window.resizable = False

        def score_up(e):
            if self.image_click.opacity == 1:
                self.image_click.opacity = 0
                self.image_click_press.opacity = 1
            self.page.update()
            time.sleep(0.5)
            self.image_click.opacity = 1
            self.image_click_press.opacity = 0
            self.page.update()

        self.image_page = ft.Image(
            src="Jocker.png",
            fit=ft.ImageFit.FILL,
            width=windows_width,
            height=windows_height
        )

        self.image_click = ft.Image(
            src="symbol2.png",
            animate_opacity=300,
            fit=ft.ImageFit.COVER,
            width=width_sym,
            height=height_sym,
            opacity=1
        )

        self.image_click_press = ft.Image(
            src="symbol_active2.png",
            animate_opacity=300,
            fit=ft.ImageFit.COVER,
            width=width_sym,
            height=height_sym,
            opacity=0
        )

        self.btn_return_auth_page = ft.ElevatedButton(
            text='Вернуться',
            width=200,
            style=btn_style,
            bgcolor=ft.colors.TRANSPARENT,
            on_click=lambda e: page.go("/signup")
        )

        return ft.View(
            route='/head',
            controls=[
                ft.Stack([
                    ft.Container(
                    width=windows_width,
                    height=windows_height,
                    content=ft.Container(
                            self.image_page,
                            margin=bg_margin
                        )
                    ), 
                    ft.Container(
                        width=windows_height,
                        height=windows_height,
                        content=ft.Column(
                        [
                                    ft.Container(
                                        expand=2,
                                        content=ft.Row([ft.Text("")])
                                    ),
                                    ft.Container(
                                        expand=2,
                                        content=ft.Container(
                                            ft.Stack(
                                                [
                                                    self.image_click_press,
                                                    self.image_click
                                                ],
                                                alignment=ft.alignment.center

                                            ),
                                            alignment=ft.alignment.center
                                        ), on_click=lambda e: score_up(e)
                                    ),
                                    ft.Container(
                                        expand=1,
                                        content=self.btn_return_auth_page,
                                        alignment=ft.alignment.center
                                    )
                                ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ) 
                    )              
                    
                ])
            ]
        )

























