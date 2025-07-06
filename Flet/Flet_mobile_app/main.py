import flet as ft
from route import Router
from dotenv import load_dotenv

load_dotenv()

async def main(page: ft.Page):
    Router(page)


if __name__ == '__main__':
    ft.app(target=main, assets_dir="assets")