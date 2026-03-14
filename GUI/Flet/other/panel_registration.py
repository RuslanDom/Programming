import flet as ft
import sqlite3
import time

def main(page: ft.Page):
    page.title = 'Panel'
    page.window.height = 500
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 400
    page.window.frameless = False
    page.window.resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def func_reg(event):
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS users 
                        (ID INTEGER PRIMARY KEY AUTOINCREMENT, login TEXT, pass TEXT)""")
            conn.commit()
            cur.execute(f"""INSERT INTO users (login, pass) VALUES('{user_reg.value}', '{user_pass.value}')""")
            conn.commit()
        user_reg.value = ''
        user_pass.value = ''
        btn_reg.disabled = True
        page.update()


    def func_auth(event):
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute(f"""SELECT * FROM users WHERE login = '{user_reg.value}' AND pass = '{user_pass.value}'""")
            data = cur.fetchone()
            if data:
                page.overlay.append(ft.SnackBar(
                    content=ft.Text('SUCCESS', size=40, text_align=ft.TextAlign.CENTER),
                    bgcolor=ft.colors.GREEN_300,
                    open=True
                ))
                user_data.value = f"Ваш логин: {user_reg.value}\nПароль: {user_pass.value}"

                if len(page.navigation_bar.destinations) == 2:
                    page.navigation_bar.destinations.append(
                        ft.NavigationBarDestination(
                            icon=ft.icons.BOOK,
                            label="Личный кабинет"
                        )
                    )
                
                page.update()
                
            else:
                page.overlay.append(ft.SnackBar(
                    content=ft.Text('NOT ACCESS', size=40, text_align=ft.TextAlign.CENTER),
                    bgcolor=ft.colors.RED_300,
                    open=True,
                ))
                if len(page.navigation_bar.destinations) == 3:
                    page.navigation_bar.destinations.pop()
                page.update()
                return


    def validation(event):
        if all([user_reg.value, user_pass.value]):
            btn_reg.disabled = False
            btn_auth.disabled = False
        else:
            btn_reg.disabled = True
            btn_auth.disabled = True 
        page.update()


    user_reg = ft.TextField(
        label="Введите логин",
        on_change=validation
    )
    user_pass = ft.TextField(
        label='Введите пароль',
        password=True,
        can_reveal_password=True,
        on_change=validation
    )
    user_data = ft.Text('', color=ft.colors.YELLOW, size=30)
    all_data = ft.Text('', size=20)
    btn_reg = ft.ElevatedButton(
        text='Зарегистрироваться',
        on_click=func_reg,
        scale=1.5,
        disabled=True
    )
    btn_auth = ft.ElevatedButton(
        text='Отправить',
        on_click=func_auth,
        disabled=True,
        scale=1.5
    )
    
    panel_reg = ft.Row(
        [
            ft.Column(
                [
                    ft.Text('Регистрация', color=ft.colors.YELLOW, size=30),
                    user_reg,
                    user_pass,
                    btn_reg
                ],
                 alignment=ft.MainAxisAlignment.CENTER,
                 horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        ], alignment=ft.MainAxisAlignment.CENTER
    )

    panel_auth = ft.Row(
        [
            ft.Column(
                [
                    ft.Text('Войти в систему', color=ft.colors.YELLOW, size=30),
                    user_reg,
                    user_pass,
                    btn_auth
                ], 
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        ], alignment=ft.MainAxisAlignment.CENTER
    )
    
    panel_private = ft.Row(
        [
            ft.Column(
                [
                    ft.Text("ЛИЧНЫЙ КАБИНЕТ", color=ft.colors.RED, size=30),
                    user_data,
                    all_data
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        ], alignment=ft.MainAxisAlignment.CENTER
    )

    def select_panel(event):
        index = page.navigation_bar.selected_index
        page.clean()
        if index == 0:
            page.add(panel_reg)
        elif index == 1:
            page.add(panel_auth)
        elif index ==2:
            page.add(panel_private)
            with sqlite3.connect("database.db") as conn:
                cur = conn.cursor()
                cur.execute("""SELECT * FROM users""")
                data = cur.fetchall()
                for user in data:
                    all_data.value += f"Пользователь: {user[1]}\n"
        page.update()

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(label="Регистрация", icon=ft.icons.APP_REGISTRATION),
            ft.NavigationBarDestination(label="Аутетификация", icon=ft.icons.VERIFIED_USER_OUTLINED)
        ], on_change=select_panel
    )

    page.add(
        panel_auth
    )




    page.update()










if __name__ == "__main__":
    ft.app(target=main)



