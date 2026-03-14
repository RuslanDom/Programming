import flet as ft

def main(page: ft.Page):
    page.title = 'Game'
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    user_info = ft.Text('Info')
    user_text = ft.TextField(value='Hello', width=150, text_align=ft.TextAlign.CENTER)

    def get_info(event: ft.ContainerTapEvent):
        user_info.value = user_text.value
        page.update()
        
    
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.HOLIDAY_VILLAGE, on_click=get_info),
                ft.Icon(ft.icons.BACK_HAND),
                ft.ElevatedButton(text='Click', on_click=get_info),
                ft.OutlinedButton(text='Click', on_click=get_info),
                ft.Checkbox(label='Согласны', value=False, on_change=get_info)
            ], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.START
        ),
        ft.Row(
            [
                user_info,
                user_text
            ], alignment=ft.MainAxisAlignment.CENTER
        )
    )

if __name__ == '__main__':
    ft.app(target=main)

