import time
import flet as ft
from flet_route import Params, Basket
import os
from Flet.Проект_flet_youtube.utils.styles import *
from Flet.Проект_flet_youtube.utils.validation import Validator
from Flet.Проект_flet_youtube.models import db, AdminUserTable, PendingPostTable
from Flet.Проект_flet_youtube.utils.request import sendMessage, sendMessagePhoto
from Flet.Проект_flet_youtube.utils.funcs import p_link_generate
import shutil
from pathlib import Path
from apscheduler.schedulers.background import BackgroundScheduler
import datetime

class PostingPage:
    # ВАЛИДАТОР
    validation = Validator()

    token_bot = os.getenv("BOT_TOKEN")
    channel_link = os.getenv("CHANNEL")
    admin_user = AdminUserTable()
    pending_post = PendingPostTable()
    no_preview = False
    preview = ""
    # ФОНОВЫЙ ПЛАНИРОВЩИК ЗАДАЧ ДЛЯ ВЫПОЛНЕНИЯ ОТЛОЖЕННЫХ ЗАДАЧ
    scheduler = BackgroundScheduler(timezone="Europe/Moscow")
    scheduler.start()

    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = "Постинг страница"
        page.window.width = defaultWidthWindow
        page.window.height = defaultHeightWindow
        page.window.min_width = 800
        page.window.min_height = 500

        # БЛОК С СООБЩЕНИЕМ ОБ ОШИБКЕ
        error_message = ft.Container(
            content=ft.Text("", size=25, color="red"),
            alignment=ft.alignment.center
        )
        # ФУНКЦИЯ КНОПКИ ОТЛОЖЕННОГО ПОСТИНГА
        def checkbox_change(e):
            if e.control.value:  # ПРОВЕРКА
                deferred_posting_data_field.visible, posting_button.visible = True, True
            else:
                deferred_posting_data_field.visible, posting_button.visible = False, False
            posting_button.update()
            deferred_posting_data_field.update()

        # ФУНКЦИЯ КНОПКИ ОТПРАВИТ СРАЗУ
        def on_submit(e):
            message = message_filled.value
            if self.no_preview:
                sendMessagePhoto(token=self.token_bot, channel=self.channel_link, photo=selected_files.src, caption=message)
                selected_files.src = "preview.png"
                selected_files.update()
                self.no_preview = False
            else:
                sendMessage(self.token_bot, self.channel_link, message)
            message_send_success.value = "Сообщение успешно отправлено"
            message_send_success.update()
            message_filled.value = ""
            message_filled.update()
            time.sleep(2)
            message_send_success.value = ""
            message_send_success.update()

        # ФУНКЦИЯ ДОБАВЛЕНИЯ ПОСТА С КАРТИНКОЙ
        def deferred_img(link):
            data_record = self.pending_post.get_post(link=link)
            images = f"assets/upload/{data_record.path_image}"
            sendMessagePhoto(token=self.token_bot, channel=self.channel_link, photo=images, caption=data_record.message)

        # ФУНКЦИЯ ДОБАВЛЕНИЯ ПОСТА БЕЗ КАРТИНКИ
        def deferred_message(link):
            data_record = self.pending_post.get_post(link=link)
            sendMessage(token=self.token_bot, channel=self.channel_link, text=data_record.message)

        # ФУНКЦИЯ ОТЛОЖЕННОЙ ОТПРАВКИ
        def on_deferred_post(e):
            if self.validation.time_valid(deferred_posting_data_field.value):
                time_data = deferred_posting_data_field.value
                time_for_message = datetime.datetime.strptime(time_data, "%H:%M")
                link = p_link_generate(9)

                if self.no_preview:
                    new_post = PendingPostTable(
                        message=message_filled.value,
                        path_image=self.preview,
                        link_post=link,
                        time=time_for_message,
                    )
                    db.session.add(new_post)
                    db.session.commit()
                    self.scheduler.add_job(
                        func=deferred_img,
                        args=[link],
                        trigger='date',
                        run_date=datetime.datetime.today().replace(hour=time_for_message.hour, minute=time_for_message.minute, second=0)
                    )

                    selected_files.src = "preview.png"
                    self.preview = ""
                    self.no_preview = False
                    selected_files.update()
                else:
                    new_post = PendingPostTable(
                        message=message_filled.value,
                        path_image="NULL",
                        link_post=link,
                        time=time_for_message,
                    )
                    db.session.add(new_post)
                    db.session.commit()
                    self.scheduler.add_job(
                        func=deferred_message,
                        args=[link],
                        trigger='date',
                        run_date=datetime.datetime.today().replace(hour=time_for_message.hour,
                                                                   minute=time_for_message.minute, second=0)
                    )
                message_send_success.value = f"Congratulations! Your message has been sent at {time_for_message.strftime('%H:%M')}"
                message_filled.value = ""
                deferred_posting_data_field.value = ""
                deferred_posting_data_field.update()
                message_filled.update()
                message_send_success.update()
                time.sleep(2)
                message_send_success.value = ""
                message_send_success.update()
                db.session.close()
            else:
                error_message.content.value = "Неверный формат времени"
                error_message.update()
                time.sleep(5)
                error_message.content.value = ""
                error_message.update()

        # ФУНКЦИЯ ДЛЯ ВЫБОРА И ЗАГРУЗКИ КАРТИНКИ
        def pick_files_result(e: ft.FilePickerResultEvent):
            if e.files:
                file_name = p_link_generate(length=7)
                selected_files.src = e.files[0].path
                path_dir = os.path.dirname(os.path.abspath(__file__))
                # LINUX
                # upload_files = os.path.join(os.path.dirname(path_dir), "assets/upload") # возвращает строку, представляющую собой полный путь к текущей рабочей директории
                # WINDOWS
                upload_files = Path(path_dir).parent  / "assets" / "upload"
                new_file_name = f"{file_name}_{os.path.basename(e.files[0].path)}"
                new_file_path = os.path.join(upload_files, new_file_name)
                shutil.copy(e.files[0].path, new_file_path)
                self.preview = new_file_name
                # ЧТОБЫ ОТПРАВИЛАСЬ КАРТИНКА В ФУНКЦИИ on_submit нужно перевести в True
                self.no_preview = True
                selected_files.update()


        # КОНСТРУКТОР ПОЛЕЙ ВВОДА
        # def input_field(label, disabled=False, val=''):
        #     return ft.Container(
        #         padding=ft.padding.symmetric(5, 5),
        #         content=ft.TextField(
        #             label=ft.Text(label, color="blue", weight=ft.FontWeight.BOLD),
        #             value=val,
        #             bgcolor=secondaryBgColor,
        #             border_radius=15,
        #             disabled=disabled,
        #             filled=True,
        #             color="blue",
        #             opacity=0.8,
        #             on_change=...
        #         )
        #     )

        # БОКОВАЯ ЛЕВАЯ ПАНЕЛЬ
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
                multiline=True,  # Возможность добавление мин и макс числа строк
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

        # ПОЛЕ ДЛЯ ОТПРАВКИ СООБЩЕНИЯ
        message_filled = form_message(
            "Введите текст сообщения"
        )
        # КНОПКА ДЛЯ ОТПРАВКИ СООБЩЕНИЯ
        message_btn = ft.ElevatedButton(
            "Отправить сразу", icon="send", bgcolor="blue", color=defaultFgColor, on_click=lambda e: on_submit(e)
        )
        # ВЫБОРЩИК ФАЙЛОВ ДЛЯ ОТПРАВКИ
        pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
        page.overlay.append(pick_files_dialog)

        # КНОПКА ДЛЯ ОТПРАВКИ КАРТИНКИ
        upload_button = ft.ElevatedButton(
            "Выберите файл", on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=False)
        )

        # СООБЩЕНИЕ ОБ УСПЕШНОЙ ОТПРАВКИ
        message_send_success = ft.Text(
            value="",
            color="green",
            size=20
        )
        # ЧЕК_БОКС ОТЛОЖЕННОГО ПОСТИНГА
        posting_data = ft.Checkbox(
            label="Отложенный постинг",
            label_style=ft.TextStyle(color=defaultFgColor),
            on_change=checkbox_change
        )
        # ПОЛЕ ДЛЯ ВВОДА ВРЕМЕНИ ОТПРАКИ ОТЛОЖЕННОГО СООБЩЕНИЯ
        deferred_posting_data_field = ft.TextField(
            label="Укажите дату в формате '12:00'", bgcolor=secondaryBgColor, border=ft.InputBorder.NONE,
            visible=False, filled=True, color="blue"
        )
        # КНОПКА ДЛЯ ОТПРАВКИ ОТЛОЖЕННОГО СООБЩЕНИЯ
        posting_button = ft.ElevatedButton(
            "Отложенный постинг", bgcolor=hoverBgColor,
            color=defaultFgColor, icon="schedule_send_rounded", visible=False, on_click=lambda e: on_deferred_post(e)
        )
        # СТРУКТУРА РАСПОЛОЖЕНИЯ КНОПОК
        setting_content = ft.Column(
            controls=[
                message_send_success,
                selected_files,
                message_filled,
                posting_data,
                ft.Row(
                    controls=[
                        message_btn,
                        upload_button,
                    ]
                ),
                error_message,
                ft.Row(
                    controls=[
                        posting_button,
                        deferred_posting_data_field
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
                                content=ft.Row(
                                    controls=[
                                        my_cont(expand=1, content=btn_build(label="EXIT", bg="blue", f=lambda e: page.go("/"))),
                                        # my_cont(expand=3),
                                        # my_cont(bgcolor="yellow"),
                                        # my_cont(bgcolor="blue"),
                                        # my_cont(bgcolor="orange")
                                    ]
                                ),
                                padding=ft.padding.only(bottom=5)
                            )
                        ]
                    )
                )
            ],
            bgcolor=defaultBgColor,
            padding=0
        )

# СЛОВАРЬ
# deferred - отложенный
# pending - в ожидании
# waiting, expectation - ожидание
# scheduler - планировщик
#
