from flet_route import Routing, path
import flet as ft
# linux
# from Flet.Flet_mobile_app.pages.guest_page.login_page import LoginPage
# from Flet.Flet_mobile_app.pages.guest_page.signup_page import SignupPage
# from Flet.Flet_mobile_app.pages.guest_page.welcome_page import WelcomePage
# windows
from pages.guest_page.login_page import LoginPage
from pages.guest_page.welcome_page import WelcomePage
from pages.guest_page.signup_page import SignupPage

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.app_routes = [
            path(url="/", clear=True, view=WelcomePage().view),
            # path(url="/login", clear=True, view=LoginPage().view),
            # path(url="/signup", clear=True, view=SignupPage().view)
        ]

        Routing(
            page=self.page,
            app_routes=self.app_routes
        )
        self.page.go(self.page.route)
