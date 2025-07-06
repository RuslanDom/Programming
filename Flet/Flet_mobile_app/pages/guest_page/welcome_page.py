import flet as ft
from Flet.Flet_mobile_app.utils.style import *
from flet_route import Params, Basket
from Flet.Flet_mobile_app.pages.components.buttons import button_blue, button_white, MyButton

class WelcomePage:

    def view(self, page: ft.Page, basket: Basket, params: Params):
        page.title = "Welcome to Flet Mobile"
        page.theme_mode = "dark"
        page.window.width = pageWidth
        page.fonts = pageFont


        # FUNCTIONS (ФУНКЦИИ)
        def link_signup(e):
            pass

        def link_loading(e):
            pass

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
                color="#ffffff",
                font_family=pageFont["Roboto"],
                size=20,
                text_align=ft.TextAlign.CENTER
            ),
            alignment=ft.alignment.center
        )

        register_button = button_white(
            text="Зарегистрироваться",
            style=ButtonWhiteStyle,
            width=200,
            height=50,
            function=link_signup
        )
        register_button_2 = MyButton(
            text="Зарегистрироваться!!!",
            width=200,
            height=50,
            function=link_signup
        ).white()

        load_button = button_blue(
            text="Войти",
            style=ButtonBlueStyle,
            width=200,
            height=50,
            function=link_loading
        )
        load_button_2 = MyButton(
            text="Войти!",
            width=200,
            height=50,
            function=link_loading
        ).blue()


        # STRUCTURE
        page_body = ft.Column(
            controls=[
                logo_message,
                welcome_message,
                register_button,
                # register_button_2,
                load_button,
                # load_button_2
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        # АДАПТИВНОСТЬ
        st = ft.ResponsiveRow(
            controls=[
            ft.Column(col={"xs": 12, "sm": 4, "xl": 6}, controls=[images]),
            ft.Column(col={"xs": 12, "sm": 8, "xl": 6}, controls=[page_body])
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        )

        return ft.View(
            route="/",
            controls=[
                st
            ],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            bgcolor=PageBgColor,
            padding=0
        )




