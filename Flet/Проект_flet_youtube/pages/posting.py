import flet as ft
from flet_route import Params, Basket
import os
from Flet.Проект_flet_youtube.utils.styles import *
from Flet.Проект_flet_youtube.utils.validation import Validator
from Flet.Проект_flet_youtube.models import db, AdminUser



class PostingPage:
    # Валидатор
    validation = Validator()
    token_bot = os.getenv("BOT_TOKEN")
    channel_link = os.getenv("CHANNEL")
    admin_user = AdminUser()

    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = "Постинг страница"
        page.window.width = defaultWidthWindow
        page.window.height = defaultHeightWindow
        page.window.min_width = 800
        page.window.min_height = 500

        # ФУНКЦИИ
        def checkbox_change(e):
            if e.control.value:
                posting_data_field.visible, posting_button.visible = True, True
            else:
                posting_data_field.visible, posting_button.visible = False, False
            posting_button.update()
            posting_data_field.update()


        # КОНСТРУКТОР ПОЛЕЙ ВВОДА
        def input_field(label, disabled=False, val=''):
            return ft.Container(
                padding=ft.padding.symmetric(5, 5),
                content=ft.TextField(
                    label=ft.Text(label, color="blue", weight=ft.FontWeight.BOLD),
                    value=val,
                    bgcolor=secondaryBgColor,
                    border_radius=15,
                    disabled=disabled,
                    filled=True,
                    color="blue",
                    opacity=0.8,
                    on_change=...
                )
            )

        # БОКОВАЯ ПАНЕЛЬ
        logo = ft.Container(
            padding=ft.padding.symmetric(5, 5),
            content=ft.Row(
                controls=[
                    ft.Image(src="rubik.png", width=100, height=100, fit=ft.ImageFit.FILL),
                    ft.Text("Go to play", expand=True, color="blue", size=35, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.START
                            ),
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=5,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

        # КОНСТРУКТОР КНОПОК И КНОПКИ
        def btn_build(label, bg='white', f=None):
            return ft.Container(
                        expand=True,
                        content=ft.Text(value=label, color="white", size=20, text_align=ft.TextAlign.CENTER),
                        bgcolor=bg,
                        height=30,
                        border_radius=15,
                        width=300,
                        alignment=ft.alignment.center,
                        on_click=f
                        )

        send_btn = ft.ElevatedButton(
            text="Сохранить данные",
            bgcolor=hoverBgColor,
            color=defaultFgColor,
            width=200,
            icon="settings",
            on_click=...
        )

        # РЕДАКТОР НАДПИСЕЙ КЛАССОМ И ФУНКЦИЕЙ
        class My_Field:
            def __init__(
                    self,
                    icon,
                    value,
                    bg=ft.Colors.TRANSPARENT,
                    expand:bool or int=True,
                    color="blue"
                    ):
                self.icon = icon
                self.value = value
                self.bg = bg
                self.expand = expand
                self.color = color
                self.container = ft.Container

            def __call__(self):
                return self.container(
                    bgcolor=self.bg,
                    content=ft.Row(
                        controls=[
                            ft.Icon(name=self.icon, color=self.color),
                            ft.Text(value=self.value, color=self.color, size=20, text_align=ft.TextAlign.CENTER)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.START
                    )
                )

        # ТЕКСТОВЫЕ ПОЛЯ
        def form_message(label):
            return ft.TextField(
                label=label,
                bgcolor=secondaryBgColor,
                border=ft.InputBorder.NONE,
                multiline=True,
                min_lines=1,
                max_lines=4,
                filled=True,
                color=secondaryFgColor
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
        # СТИЛЬ КНОПОК
        style_menu = ft.ButtonStyle(
            color={ft.ControlState.HOVERED: ft.colors.WHITE,
                   ft.ControlState.DEFAULT: ft.colors.BLUE},
            icon_size=20,
            overlay_color=hoverBgColor
        )

        # HEADER
        header = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text(value="Страница постинга", color="blue", weight=ft.FontWeight.BOLD, size=20),
                    ft.Row(
                        controls=[
                            ft.CircleAvatar(
                                foreground_image_src="https://static.wikia.nocookie.net/avatar/images/6/6b/Adult_Aang.png/revision/latest?cb=20250504214148",
                                content=ft.Text("A")
                            ),
                            ft.IconButton(
                                icon=ft.icons.NOTIFICATION_ADD_ROUNDED,
                                icon_color="blue",
                                icon_size=20
                            )
                        ]
                    )
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        )

        # КНОПКИ И СООБЩЕНИЯ

        selected_files = ft.Image(
            src="preview.png",
            error_content=ft.Text("Нет изображения", size=30, color="white",
                                  text_align=ft.TextAlign.CENTER, bgcolor="red", opacity=0.8),
            width=200,
            height=200,
            fit=ft.ImageFit.FILL
        )
        message_filled = form_message(
            "Введите текст сообщения"
        )
        message_btn = ft.ElevatedButton(
            "Отправить сразу", icon="send", bgcolor="blue", color=defaultFgColor
        )
        upload_button = ft.ElevatedButton(
            "Выберите файл"
        )
        posting_data = ft.Checkbox(
            label="Отложенный постинг",
            label_style=ft.TextStyle(color=defaultFgColor),
            on_change=checkbox_change
        )
        posting_data_field = ft.TextField(
            label="Укажите дату в формате '12:00'", bgcolor=secondaryBgColor, border=ft.InputBorder.NONE,
            visible=False, filled=True, color="blue"
        )
        posting_button = ft.ElevatedButton(
            "Отложенный постинг", bgcolor=hoverBgColor,
            color=defaultFgColor, icon="schedule_send_rounded", visible=False
        )

        setting_content = ft.Column(
            controls=[
                selected_files,
                message_filled,
                posting_data,
                ft.Row(
                    controls=[
                        message_btn,
                        upload_button,
                    ]
                ),
                ft.Row(
                    controls=[
                        posting_button,
                        posting_data_field
                    ]
                )
            ]
        )



        return ft.View(
            route="/posting",
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
                                        my_cont(content=logo, expand=2)
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
                                                        setting_content
                                                    ]
                                                )
                                                ),
                                    ]
                                )
                            ),
                            # FOOTER
                            ft.Container(
                                expand=1,
                                content=ft.Row(
                                    controls=[
                                        my_cont(expand=1, content=btn_build(label="EXIT", bg="blue", f=lambda e: page.go("/"))),
                                        my_cont(expand=3),
                                        # my_cont(bgcolor="yellow"),
                                        # my_cont(bgcolor="blue"),
                                        # my_cont(bgcolor="orange")
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
