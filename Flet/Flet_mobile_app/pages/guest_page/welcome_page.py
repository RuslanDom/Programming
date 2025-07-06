import flet as ft
from Flet.Flet_mobile_app.utils.style import *
from flet_route import Params, Basket
from Flet.Flet_mobile_app.pages.components.buttons import *


class WelcomePage:

    def view(self, page: ft.Page, basket: Basket, params: Params):
        page.title = "Welcome to Flet Mobile"
        page.theme_mode = "dark"
        page.window.width = PageWidth
        page.fonts = PageFont


        # FUNCTIONS (ФУНКЦИИ)
        def link_signup():
            pass

        def link_login():
            pass


        # VIEW (ЭЛЕМЕНТЫ СТРАНИЦЫ)

        # Стартовая картинка
        Images = ft.Image(
            src="assets/images/car_1.png",
            fit=ft.ImageFit.FIT_WIDTH,
            repeat=ft.ImageRepeat.NO_REPEAT,
            width=220
        )

        LogoMessage = ft.Container(
            content=ft.Text(
                "Аренда авто",
                size=20,
                color=TextColor,
                font_family=PageFont["Roboto-italic"],
                weight=ft.FontWeight.BOLD
            ),
            alignment=ft.alignment.center
        )

        WelcomeMessage = ft.Container(
            content=ft.Text(
                "Приложение ищет авто для аренды",
                color="white",
                font_family=PageFont["Roboto"],
                size=20,
                text_align=ft.TextAlign.CENTER
            ),
            alignment=ft.alignment.center
        )

        RegisterButton = button_white(
            text="Зарегистрироваться",
            style=ButtonWhiteStyle,
            width=200,
            height=50,
            function=link_signup
        )
        LoginButton = button_blue(
            text="Войти",
            style=ButtonBlueStyle,
            width=200,
            height=50,
            function=link_login
        )

        # STRUCTURE
        PageBody = ft.Column(
            controls=[
                LogoMessage,
                WelcomeMessage,
                RegisterButton,
                LoginButton
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        # ADAPTABILITY (АДАПТИВНОСТЬ)
        st = ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"xs": 12, "sm": 4, "xl": 6},
                    controls=[Images]
                ),
                ft.Column(
                    col={"xs": 12, "sm": 4, "xl": 6},
                    controls=[PageBody]
                )
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        )

        #------------------------------------------------
        return ft.View(
            route="/",
            controls=[
                st
            ],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            bgcolor=PageBgColor,
            padding=0
        )








