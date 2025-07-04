from flet_route import Routing, path
import flet as ft

class Route():
    def __init__(self, page: ft.Page):
        self.page = page
        app_route = [
            path("/", clear=False, view=IndexPage().view),
            path("/signup", clear=False, view=SignupPage().view),
            path("/login", clear=False, view=LoginPage().view),
            path("/root", clear=False, view=RootPage().view)
        ]
        Routing(
            page=self.page,
            app_routes=app_route
        )

        self.page.go(self.page.route)