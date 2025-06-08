import flet as ft
from flet_route import Routing, path
from Flet.Проект_flet_youtube.pages.general import GeneralPage
from pages.login import LoginPage
from pages.signup import SignupPage
from pages.general import GeneralPage


class Router():
    def __init__(self, page: ft.Page):
        self.page = page
        self.app_routes = [
            path(url="/vcf", clear=True, view=LoginPage().view),
            path(url="/signup", clear=False, view=SignupPage().view),
            path(url="/", clear=False, view=GeneralPage().view)
        ]

        Routing(
            page=self.page,
            app_routes=self.app_routes,
        )
        self.page.go(self.page.route)
