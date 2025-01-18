import flet as ft
from flet_route import Params, Basket
from Flet.project_pc.utils.style import *
import os
from pathlib import Path
from dotenv import load_dotenv, set_key


class DashboardPage:
    load_dotenv()
    AUTH_USER = False
    env_file_path = Path(".")/".env"
    token_bot = os.getenv("BOT_TOKEN")
    channel_link = os.getenv("CHANNEL")

    def view(self, page: ft.Page,  params: Params, basket: Basket):

        self.AUTH_USER = page.session.get('auth_user')
        page.title = "Панель управления"
        page.theme_mode = 'Lime'
        page.window.width = defaultWidthWindow
        page.window.height = defaultHeightWindow
        page.window.min_width = 800
        page.window.min_height = 400

        # ФУНКЦИЯ СОХРАНЕНИЯ
        def save_settings(e):
            token = token_input.content.value
            channel = channel_input.content.value
            # Изменить токен-бот который хранится в .env на значение введенное от пользователя
            set_key(dotenv_path=self.env_file_path, key_to_set="BOT_TOKEN", value_to_set=token)
            set_key(dotenv_path=self.env_file_path, key_to_set="CHANNEL", value_to_set=channel)
            # Отключение возможности редактирования полей
            token_input.content.disabled = True
            channel_input.content.disabled = True
            # Внести полученные значения в сессию
            page.session.set("TOKEN", token)
            page.session.set("CHANNEL", channel)
            token_input.content.bgcolor = ft.colors.GREEN_100
            token_input.content.color = "GREEN"
            channel_input.content.bgcolor = ft.colors.GREEN_100
            channel_input.content.color = "GREEN"
            send_btn.text = " Сохранено "
            page.update()

        def change_settings(e):
            token_input.content.value = ''
            channel_input.content.value = ''
            token_input.content.bgcolor = ft.colors.GREEN_300
            channel_input.content.bgcolor = ft.colors.GREEN_300
            token_input.content.color = "WHITE"
            channel_input.content.color = "WHITE"
            token_input.content.disabled = False
            channel_input.content.disabled = False

            send_btn.text = "Сохранить данные"
            page.update()

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
                    ft.TextButton("Главная", icon=ft.icons.SPACE_DASHBOARD_ROUNDED, style=style_meny,
                                  on_click=lambda e: page.go('/panel')),
                    ft.TextButton("Постинг", icon=ft.icons.POST_ADD, style=style_meny,
                                  on_click=lambda e: page.go('/post')),
                    ft.TextButton("Текстовая кнопка", icon=ft.icons.VERIFIED_USER, style=style_meny),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.START
            )
        )
        # END SIDEBAR

        # СТИЛЬ ТЕКСТОВОГО ПОЛЯ ВСТАВКИ ТОКЕНА ТЕЛЕБОТА
        def style_input_token(label):
            return ft.TextField(
                '',
                label=f"{label}",
                label_style=ft.TextStyle(color=ft.colors.YELLOW),
                bgcolor=ft.colors.GREEN_300,
                filled=True,
                color=ft.colors.WHITE,
                border=ft.InputBorder.NONE
            )

        # СТИЛЬ ТЕКСТОВОГО ПОЛЯ DISABLED (если нужно сразу закрыть поля при наличии имеющегося токена и канала(channel))
        # def input_disabled(value):
        #     return ft.TextField(value=value, disabled=True, border=ft.InputBorder.NONE,
        #                         bgcolor=ft.colors.GREEN_100, filled=True, color=ft.colors.GREEN)

        # ТЕКСТОВЫЕ ПОЛЯ ДЛЯ ПОЛУЧЕНИЯ И СОХРАНЕНИЯ ДАННЫХ

        token_input = ft.Container(
            content=style_input_token("Введите токен бота"),
            border_radius=15)
        channel_input = ft.Container(
            content=style_input_token("Введите название канала"),
            border_radius=15)

        if page.session.get("TOKEN"):
            token_input.content.bgcolor = ft.colors.GREEN_100
            token_input.content.disabled = True
            token_input.content.value = page.session.get("TOKEN")
        elif self.token_bot:
            token_input.content.bgcolor = ft.colors.GREEN_100
            token_input.content.disabled = True
            token_input.content.value = self.token_bot
        else:
            token_input.content.disabled = False

        if page.session.get("CHANNEL"):
            channel_input.content.bgcolor = ft.colors.GREEN_100
            channel_input.content.disabled = True
            channel_input.content.value = page.session.get("CHANNEL")
        elif self.channel_link:
            channel_input.content.bgcolor = ft.colors.GREEN_100
            channel_input.content.disabled = True
            channel_input.content.value = self.channel_link
        else:
            channel_input.content.disabled = False
        page.update()

        # elif page.session.get('CHANNEL'):
        #     channel_input = ft.Container(
        #         content=input_disabled(page.session.get('CHANNEL')),
        #         border_radius=15)
        # else:
        #     channel_input = ft.Container(
        #         content=input_disabled(self.channel_link),
        #         border_radius=15)

        send_btn = ft.ElevatedButton("Сохранить данные", bgcolor=ft.colors.GREEN_300, color="YELLOW",
                                     icon='save', width=200, on_click=lambda e: save_settings(e))

        change_data = ft.ElevatedButton("Изменить данные", bgcolor=ft.colors.GREEN_300, color="YELLOW",
                                     icon='settings', width=200, on_click=lambda e: change_settings(e))

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
                                        send_btn,
                                        change_data
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
