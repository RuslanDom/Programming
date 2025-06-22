import flet as ft
from flet_route import Params, Basket
from dotenv import set_key, load_dotenv
from pathlib import Path
import os
from Flet.Проект_flet_youtube.utils.styles import *



class GeneralPage:
    load_dotenv()
    AUTH_USER = False
    env_file_path = Path(__file__).resolve().parent.parent / ".env"  # Путь до директории windows
    # env_file_path = Path("Flet/Проект_flet_youtube") / ".env"  # Путь до скрытой директории Linux
    token_bot = os.getenv("BOT_TOKEN")
    channel_link = os.getenv("CHANNEL")

    def view(self, page: ft.Page, params: Params, basket: Basket):
        # Получение данных из хранилища сессии
        self.AUTH_USER = page.session.get("auth_user")

        page.title = "Главная страница"
        page.window.width = defaultWidthWindow
        page.window.height = defaultHeightWindow
        page.window.min_width = 800
        page.window.min_height = 500

        # ФУНКЦИИ
        def save_settings(e):
            # Получение токенов с полей ввода
            token = token_input.content.value
            channel = channel_input.content.value
            # Установка полученных токенов в файл .env
            set_key(dotenv_path=self.env_file_path, key_to_set="BOT_TOKEN", value_to_set=token)
            set_key(dotenv_path=self.env_file_path, key_to_set="CHANNEL", value_to_set=channel)
            print(os.getenv("BOT_TOKEN"), "\n", os.getenv("CHANNEL"))
            # Отключение редактирование этих полей
            token_input.disabled = True
            channel_input.disabled = True
            # Внесение токенов в хранилище сессии
            page.session.set("TOKEN", token)
            page.session.set("CHANNEL", channel)
            # Определяем эти значения в переменные
            # self.check_token = page.session.get("TOKEN")
            # self.check_channel = page.session.get("CHANNEL")
            send_btn.text = "Сохранено"
            send_btn.icon = "save"
            send_btn.disabled = True
            # Обновления
            send_btn.update()
            token_input.update()
            channel_input.update()
            page.update()

        # Кнопка сохранения данных
        send_btn = ft.ElevatedButton(
            text="Сохранить данные",
            bgcolor=hoverBgColor,
            color=defaultFgColor,
            width=200,
            icon="settings",
            on_click=lambda e: save_settings(e)
        )

        # Функция изменения кнопки
        def update_value(e):
            send_btn.disabled = False
            send_btn.text = "Сохранить изменения"
            send_btn.icon = "settings"
            send_btn.update()

        # КОНСТРУКТОР ПОЛЕЙ ВВОДА
        def input_field(label, disabled=False, val=''):
            return ft.Container(
                padding=ft.padding.symmetric(5, 5),
                content=ft.TextField(
                    label=ft.Text(label, color="yellow", weight=ft.FontWeight.BOLD),
                    value=val,
                    bgcolor=secondaryBgColor,
                    border_radius=15,
                    disabled=disabled,
                    filled=True,
                    color="yellow",
                    opacity=0.8,
                    on_change=lambda e: update_value(e)
                )
            )
        # БОКОВАЯ ПАНЕЛЬ
        logo = ft.Container(
            padding=ft.padding.symmetric(5, 5),
            content=ft.Row(
                controls=[
                    ft.Image(src="rubik.png", width=100, height=100, fit=ft.ImageFit.FILL),
                    ft.Text("Go to play", expand=True, color="yellow", size=35, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.START
                            ),
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=5,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        # КОНСТРУКТОР КНОПОК
        def btn_build(label, bg='white', f=None):
            return ft.Container(
                        expand=True,
                        content=ft.Text(value=label, color="yellow", size=20, text_align=ft.TextAlign.CENTER),
                        bgcolor=bg,
                        height=30,
                        border_radius=15,
                        width=300,
                        alignment=ft.alignment.center,
                        on_click=f
                        )


        # РЕДАКТОР НАДПИСЕЙ КЛАССОМ И ФУНКЦИЕЙ
        class My_Field:
            def __init__(
                    self,
                    icon,
                    value,
                    bg=ft.Colors.TRANSPARENT,
                    expand:bool or int=True,
                    color="yellow"
                    ):
                self.icon = icon
                self.value = value
                self.bg = bg
                self.expand = expand
                self.color = color
                self.container = ft.Container

            def __call__(self):
                return self.container(
                    # expand=self.expand,
                    bgcolor=self.bg,
                    # on_click=lambda e: self.hover_func(e),
                    content=ft.Row(
                        controls=[
                            ft.Icon(name=self.icon, color=self.color),
                            ft.Text(value=self.value, color=self.color, size=20, text_align=ft.TextAlign.CENTER)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.START
                    )
                )

        def my_field(icon: ft.Icons, value="", bg=ft.Colors.TRANSPARENT, expand:bool or int=True, color="yellow"):
            return ft.Container(
                expand=expand,
                bgcolor=bg,
                content=ft.Row(
                    controls=[
                        ft.Icon(name=icon, color=color),
                        ft.Text(value=value, color=color, size=20, text_align=ft.TextAlign.CENTER)
                    ]
                )
            )

        # РЕДАКТОР КОНТЕЙНЕРОВ
        def my_cont(bgcolor=None, content=None, expand: bool or int=True, local=ft.alignment.center):
            return ft.Container(
                content=content,
                expand=expand,
                bgcolor=bgcolor,
                opacity=0.8,
                alignment=local
            )

        style_menu = ft.ButtonStyle(
            color={ft.ControlState.HOVERED: ft.colors.WHITE,
                   ft.ControlState.DEFAULT: ft.colors.YELLOW},
            icon_size=20,
            overlay_color=hoverBgColor
        )

        # ПРАВАЯ ЧАСТЬ
        # HEADER BODY
        header = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text("Панель управления", color="yellow", weight=ft.FontWeight.BOLD, size=20),
                    ft.Row(
                        controls=[
                            ft.CircleAvatar(
                                foreground_image_src="https://static.wikia.nocookie.net/avatar/images/6/6b/Adult_Aang.png/revision/latest?cb=20250504214148",
                                content=ft.Text("A")
                            ),
                            ft.IconButton(
                                icon=ft.icons.NOTIFICATION_ADD_ROUNDED,
                                icon_color="yellow",
                                icon_size=20
                            )
                        ]
                    )
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        )

        # КНОПКА И ПОЛЯ ВВОДА ТОКЕНА И КАНАЛА
        if not self.token_bot and not page.session.get("TOKEN"):
            token_input = input_field(label="Введите токен бота")
        elif page.session.get("TOKEN"):
            token_input = input_field(label=page.session.get("TOKEN"), disabled=True)
        else:
            token_input = input_field(label="token", val=self.token_bot, disabled=False)
        if not self.channel_link and not page.session.get("CHANNEL"):
            channel_input = input_field(label="Название канала")
        elif page.session.get("CHANNEL"):
            channel_input = input_field(label=page.session.get("CHANNEL"), disabled=True)
        else:
            channel_input = input_field(label="channel", val=self.channel_link, disabled=False)
        if self.token_bot and self.channel_link:
            send_btn.disabled = True
            send_btn.text = "Сохранено"
            send_btn.icon = "save"

        return ft.View(
            route="/general",
            controls=[
                ft.Container(
                    expand=True,
                    image_src="girl_with_racoon.png",
                    image_fit=ft.ImageFit.COVER,
                    content=ft.Column(
                        expand=True,
                        controls=[
                            # HEADER
                            ft.Container(
                                # expand=1,
                                content=ft.Row(
                                    controls=[
                                        my_cont(content=logo, expand=2),
                                        # my_cont(bgcolor="red"),
                                        # my_cont(bgcolor="yellow"),
                                        # my_cont(bgcolor="blue")
                                    ],
                                    alignment=ft.MainAxisAlignment.START
                                )
                            ),
                            # BODY
                            ft.Container(
                                expand=3,
                                content=ft.Row(
                                    controls=[
                                        # MENU
                                        my_cont(
                                            content=ft.Column(
                                                controls=[
                                                    My_Field(icon=ft.Icons.MENU, value="MENU").__call__(),
                                                    ft.TextButton("Главная", icon=ft.Icons.SPACE_DASHBOARD_ROUNDED,
                                                                  style=style_menu, width=250, on_click=lambda e: page.go("/general")),
                                                    ft.TextButton("Постинг", icon=ft.Icons.SPACE_DASHBOARD_ROUNDED, style=style_menu,
                                                                  width=250, on_click=lambda e: page.go("/posting")),
                                                    ft.TextButton("Игры", icon=ft.Icons.VIDEOGAME_ASSET,
                                                                  style=style_menu, width=250, on_click=lambda e: page.go("/games")),
                                                    ft.TextButton("ЧИТЫ", icon=ft.Icons.VIDEOGAME_ASSET,
                                                                  style=style_menu, width=250, on_click=lambda e: page.go("/cheats")),
                                                    ft.TextButton("О нас", icon=ft.Icons.PERM_DEVICE_INFO,
                                                                  style=style_menu, width=250, on_click=lambda e: page.go("/about"))
                                                ]
                                            )
                                        ),
                                        # BODY
                                        my_cont(expand=3,
                                                local=ft.alignment.top_left,
                                                content=ft.Column(
                                                    controls=[
                                                        header,
                                                        token_input,
                                                        channel_input,
                                                        send_btn
                                                    ]
                                                )
                                                ),
                                        # my_cont(bgcolor="blue"),
                                        # my_cont(bgcolor="orange")
                                    ]
                                )
                            ),
                            # FOOTER
                            ft.Container(
                                expand=1,
                                content=ft.Row(
                                    controls=[
                                        my_cont(expand=2, content=btn_build(label="EXIT", bg=hoverBgColor, f=lambda e: page.go("/"))),
                                        my_cont(bgcolor="red"),
                                        my_cont(bgcolor="yellow"),
                                        my_cont(bgcolor="blue"),
                                        my_cont(bgcolor="orange")
                                    ]
                                )
                            )
                        ]
                    )
                )
            ],
            bgcolor=defaultBgColor,
            padding=0
        )
    # www@m.r qwe111!!!