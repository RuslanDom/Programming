import flet as ft
from flet_route import Routing, path
from pages.signup import SignupPage
from pages.login import LoginPage
from pages.test_login import TestLoginPage

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.app_routes = [
            path(url='/', clear=True, view=LoginPage().view),
            path(url='/test', clear=False, view=TestLoginPage().view),
            path(url='/signup', clear=False, view=SignupPage().view)
        ]

        Routing(
            page=self.page,
            app_routes=self.app_routes
        )
        self.page.go(self.page.route)





