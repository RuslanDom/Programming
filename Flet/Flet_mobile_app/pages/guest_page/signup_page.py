import flet as ft
from flet_route import Params, Basket
# linux
# from Flet.Flet_mobile_app.pages.components.inputs import *
# from Flet.Flet_mobile_app.utils.style import *
# from Flet.Flet_mobile_app.pages.components.buttons import button_blue, button_white, MyButton
# from Flet.Flet_mobile_app.utils.validator import Validator
# windows
from Programming.Flet.Flet_mobile_app.pages.components.inputs import *
from Programming.Flet.Flet_mobile_app.pages.components.buttons import button_blue, button_white, MyButton
from Programming.Flet.Flet_mobile_app.utils.style import *
from Programming.Flet.Flet_mobile_app.utils.validator import Validator

class SignupPage:
    validator = Validator()

    def view(self, page: ft.Page, basket: Basket, params: Params):
        page.title = "Registration panel"
        page.theme_mode = "dark"
        page.window.width = pageWidth
        page.fonts = pageFont

        # FUNCTIONS


        # VIEW
        if page.window.width < 321:
            login_hint = input_phone("Укажите логин: ")
            login_input = ft.TextField(**InputPhoneStyle)
            password_hint = input_phone("Укажите пароль: ")
            password_input = ft.TextField(**InputPhoneStyle,
                                          can_reveal_password=True,
                                          password=True)
            email_hint = input_phone("Укажите email: ")
            email_input = ft.TextField(**InputPhoneStyle)
            car_number_hint = input_phone("Укажите номер машины: ")
            car_number_input = ft.TextField(**InputPhoneStyle)
            phone_hint = input_phone("Укажите телефон: ")
            phone_input = ft.TextField(**InputPhoneStyle)







