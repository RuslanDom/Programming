import flet as ft
from Flet.Flet_mobile_app.utils.style import *
from flet_route import Params, Basket

class WelcomePage:

    def view(self, page: ft.Page, basket: Basket, params: Params):
        page.title = "Welcome to Flet Mobile"
        page.theme_mode = "dark"
        page.window.width = pageWidth
        page.fonts = pageFont


        # FUNCTIONS (ФУНКЦИИ)


        # VIEW (ЭЛЕМЕНТЫ СТРАНИЦЫ)

        # Стартовая картинка
        images = ft.Image(
            src="assets/images/car_1.png",
            fit=ft.ImageFit.FIT_WIDTH,
            repeat=ft.ImageRepeat.NO_REPEAT,
            width=220
        )

        logo_message = ft.Container(
            content=ft.Text(
                "Аренда авто",
                size=20,
                color=textColor,
                font_family=pageFont["Roboto-italic"],
                weight=ft.FontWeight.BOLD
            ),
            alignment=ft.alignment.center
        )

        welcome_message = ft.Container(
            content=ft.Text(
                "Приложение ищет авто для аренды",
                color="white",
                font_family=pageFont["Roboto"],
                size=20,
                text_align=ft.TextAlign.CENTER
            ),
            alignment=ft.alignment.center
        )











