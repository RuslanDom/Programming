import flet as ft
from flet_route import Routing, path
from pages.login import LoginPage
from pages.signup import SignUpPage

# Маршрутизатор
class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        # Маршруты приложений
        self.app_routes = [
            path(url='/', clear=True, view=LoginPage().view),
            path(url='/signup', clear=False, view=SignUpPage().view)
        ]

        # Объект класса роутинг в который передаём страницу и маршруты
        Routing(
            page=self.page,
            app_routes=self.app_routes
        )

        # Метод который осуществляет переход на другую страницу
        self.page.go(self.page.route)






