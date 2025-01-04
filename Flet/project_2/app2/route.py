import flet as ft
from flet_route import Routing, path
from app2.pages.login import LoginPage
from app2.pages.signup import SignupPage
from app2.pages.app_page import AppPage


class Router:
    def __init__(self, page: ft.Page) -> None:
        self.page = page

        self.app_routes = [
            path(url="/", clear=True, view=LoginPage().view),
            path(url="/signup", clear=False, view=SignupPage().view),
            path(url='/head', clear=False, view=AppPage().view)
        ]

        Routing(
            page=self.page,
            app_routes=self.app_routes
        )

        self.page.go(self.page.route)













