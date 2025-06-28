import flet as ft
from routes import Router

def main(page: ft.Page):
    Router(page)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets', upload_dir='assets/upload')
