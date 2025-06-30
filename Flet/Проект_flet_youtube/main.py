import flet as ft
from routes import Router
from models import db

def main(page: ft.Page):
    Router(page)

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    ft.app(target=main, assets_dir='assets', upload_dir='assets/upload')
