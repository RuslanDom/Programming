import flet as ft
from Flet.Flet_mobile_app.utils.style import *
from typing import Callable



def button_white(
        text: str,
        style: dict,
        width: int,
        height: int,
        function: Callable) -> ft.FilledButton:
    return ft.FilledButton(text=text, style=ft.ButtonStyle(**style), width=width, height=height, on_click=lambda e: function(e))


def button_blue(
        text: str,
        style: dict,
        width: int,
        height: int,
        function: Callable) -> ft.FilledButton:
    return ft.FilledButton(text=text, style=ft.ButtonStyle(**style), width=width, height=height, on_click=lambda e: function(e))