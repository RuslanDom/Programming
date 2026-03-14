import flet as ft
import requests

def app_weather(page: ft.Page):
    page.title = 'Weather'
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    text_field= ft.TextField(label="Enter city", width=450, text_align=ft.TextAlign.CENTER)
    get_data = ft.Text('')

    def change_theme(event):
        page.theme_mode = ft.ThemeMode.LIGHT if page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        page.update()

    def get_weather(event):
        API = 'e93d99bb6863b1a797d261f54cccb745'
        URL = f'https://api.openweathermap.org/data/2.5/weather?q={text_field.value}&appid={API}&units=metric'
        response = requests.get(URL).json()
        temp = response["src"]["temp"]
        print(temp)
        get_data.value = f"Температура: {str(temp)}"
        page.update()

    page.add(
        ft.Row([
            ft.IconButton(icon=ft.icons.SUNNY, on_click=change_theme),
            ft.Text(value='WEATHER IN YOR CITY')
        ], 
        alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([
            get_data
        ],
        alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([
            text_field
        ],
        alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.ElevatedButton(
                    text='GET',
                    on_click=get_weather
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

    )



if __name__ == "__main__":
    ft.app(
        target=app_weather
    )




