import flet as ft
from flet_route import Params, Basket
from Flet.project_pc.utils.style import *


class DashboardPage:

    def view(self, page: ft.Page,  params: Params, basket: Basket):
        page.title = "Панель управления"
        page.theme_mode = 'Dark'
        page.window.width = defaultWidthWindow
        page.window.height = defaultHeightWindow
        page.window.min_width = 800
        page.window.min_height = 400

        # ФУНКЦИЯ ВСТАВКИ ТОКЕНА ТЕЛЕБОТА
        def insert_token(label):
            return ft.TextField(
                '',
                label=f"{label}",
                label_style=ft.TextStyle(color=ft.colors.YELLOW),
                # bgcolor=secondBgColor,
                bgcolor=ft.colors.GREEN_300,
                filled=True,
                # color=secondFontColor,
                color=ft.colors.WHITE,
                border=ft.InputBorder.NONE
            )

        # SIDEBAR
        logo = ft.Container(
            content=ft.Row(
                [
                    ft.Image(src="Passport-Image-Website.png", width=75, height=62, fit=ft.ImageFit.FILL),
                    ft.Text("Greencard", expand=True, color="GREEN", size=25, weight=ft.FontWeight.BOLD, max_lines=1)
                ],
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5
            ),
            padding=ft.padding.symmetric(17, 13),
        )

        sidebar_meny = ft.Container(
            padding=ft.padding.symmetric(0, 13),
            content=ft.Column(
                [
                    ft.Text('Меню', color="GREEN", size=25, weight=ft.FontWeight.BOLD),
                    ft.TextButton("Главная", icon=ft.icons.SPACE_DASHBOARD_ROUNDED, style=style_meny),
                    ft.TextButton("Постинг", icon=ft.icons.POST_ADD, style=style_meny),
                    ft.TextButton("Текстовая кнопка", icon=ft.icons.VERIFIED_USER, style=style_meny),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.START
            )
        )
        # END SIDEBAR

        # ЭЛЕМЕНТЫ ПОЛУЧЕНИЯ И СОХРАНЕНИЯ ДАННЫХ
        token_input = ft.Container(
            content=insert_token("Введите токен бота"),
            border_radius=15
        )

        channel_input = ft.Container(
            content=insert_token("Введите название канала"),
            border_radius=15
        )

        send_btn = ft.ElevatedButton("Сохранить данные", bgcolor=ft.colors.GREEN_300, color="YELLOW", icon='settings')


        # START HEADER
        header = ft.Container(
            ft.Row(
                [
                    ft.Text("Панель управления", color=ft.colors.YELLOW, size=20),
                    ft.Row(
                            [
                                # СОЗДАНИЕ АВАТАРА
                                ft.CircleAvatar(
                                    foreground_image_src="https://avatars.mds.yandex.net/i?id=86e0a2f3e9b03378a30f3ad961958548_l-5276461-images-thumbs&ref=rim&n=13&w=900&h=900",
                                    content=ft.Text("A")
                                ),
                                # КНОПКА ОПОВЕЩЕНИЯ
                                ft.IconButton(
                                    icon=ft.icons.NOTIFICATIONS_ROUNDED,
                                    icon_size=20,
                                    icon_color=defaultFontColor
                                )
                            ]
                    )
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        )
        # END HEADER

        # ВЫХОД НА СТРАНИЦУ АВТОРИЗАЦИИ
        login_link = ft.Container(
            ft.Text("Страница авторизации", color="GREEN",  size=20),
            on_click=lambda e: page.go("/")
        )

        return ft.View(
            "/panel",
            controls=[
                ft.Container(
                    content=ft.Row(
                        [
                            # left
                            ft.Container(
                                expand=1,
                                content=ft.Column(
                                    [
                                        logo,
                                        sidebar_meny
                                    ]
                                )
                            ),
                            # right
                            ft.Container(
                                expand=3,
                                padding=ft.padding.symmetric(15, 10),
                                content=ft.Column(
                                    [
                                        header,
                                        token_input,
                                        channel_input,
                                        send_btn
                                    ]
                                )
                            )

                        ]
                        ),
                    image_src="usa_banner_twilight.png",
                    image_fit=ft.ImageFit.COVER,
                    padding=ft.padding.all(0),
                    expand=True
                )
            ],
            padding=ft.padding.all(0)
        )
