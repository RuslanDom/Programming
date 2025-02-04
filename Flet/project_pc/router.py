import flet as ft
from flet_route import Routing, path
from Flet.project_pc.pages.signup import SignupPage
from Flet.project_pc.pages.login import LoginPage
from Flet.project_pc.pages.test_login import TestLoginPage
from pages.dashboard import DashboardPage


class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.app_routes = [
            path(url='/', clear=True, view=LoginPage().view),
            path(url='/test', clear=False, view=TestLoginPage().view),
            path(url='/signup', clear=False, view=SignupPage().view),
            path(url='/panel', clear=False, view=DashboardPage().view)
        ]

        Routing(
            page=self.page,
            app_routes=self.app_routes
        )
        self.page.go(self.page.route)





