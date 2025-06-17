import flet as ft
from flet_route import Routing, path
from pages.login import LoginPage
from pages.signup import SignupPage
from pages.general import GeneralPage
from pages.posting import PostingPage


class Router():
    def __init__(self, page: ft.Page):
        self.page = page
        self.app_routes = [
            path(url="/posting", clear=True, view=LoginPage().view),
            path(url="/general", clear=False, view=GeneralPage().view),
            path(url="/signup", clear=False, view=SignupPage().view),
            path(url="/", clear=False, view=PostingPage().view)
        ]

        Routing(
            page=self.page,
            app_routes=self.app_routes,
        )
        self.page.go(self.page.route)
