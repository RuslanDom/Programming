import flet as ft
from typing import Callable
# linux
# from Flet.Flet_mobile_app.utils.style import *
# windows
from Programming.Flet.Flet_mobile_app.utils.style import *


class MyButton:
    def __init__(self, text: str, width: int, height: int, function: Callable):
        self.text = text
        self.width = width
        self.height = height
        self.function = function

    def white(self) -> ft.FilledButton:
        return ft.FilledButton(text=self.text, style=ft.ButtonStyle(**ButtonWhiteStyle), width=self.width, height=self.height, on_click=lambda e: self.function(e))

    def blue(self) -> ft.FilledButton:
        return ft.FilledButton(text=self.text, style=ft.ButtonStyle(**ButtonBlueStyle), width=self.width, height=self.height, on_click=lambda e: self.function(e))


def button_white(
        text: str,
        style: dict,
        width: int,
        height: int,
        function: Callable
) -> ft.FilledButton:
    return ft.FilledButton(
        text=text,
        style=ft.ButtonStyle(**style), width=width, height=height, on_click=lambda e: function(e))


def button_blue(
        text: str,
        style: dict,
        width: int,
        height: int,
        function: Callable
) -> ft.FilledButton:
    return ft.FilledButton(
        text=text,
        style=ft.ButtonStyle(**style), width=width, height=height, on_click=lambda e: function(e))