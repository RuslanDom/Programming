import flet as ft
import json
import time

path = ''

def main(page: ft.Page):
    page.title = 'Текстовый редактор'
    page.theme_mode = 'dark'
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 350
    page.window_height = 500
    page.window_resizable = False


    def change_color(event):
        text_field.color = ft.colors.YELLOW
        page.update()

    def save_file(event):
        global path
        f = open(path, 'w', encoding='utf-8')
        f.write(text_field.value)
        f.close()

        text_field.color = ft.colors.GREEN
        save_button.text = 'Готово'
        save_button.disabled = True
        page.update()
        time.sleep(3)
        save_button.text = 'Сохранить'
        save_button.disabled = False
        page.update()


    def pick_result(event: ft.FilePickerResultEvent):
        if not event.files:
            text_row.value = 'Файл не выбран'
        else:
            text_row.value = ''
            save_button.text = 'Сохранить'
            save_button.disabled = False
            global path
            for el in event.files:
                path = el.path
            f = open(path, 'r', encoding='utf-8')
            text_field.value = f.read()
            f.close()
        page.update()


    pick_dialog = ft.FilePicker(on_result=pick_result)
    page.overlay.append(pick_dialog)
    text_row = ft.Text()
    text_field = ft.TextField(
        label='Текст файла',
        width=320,
        multiline=True,
        color=ft.colors.GREEN,
        on_change=change_color
    )
    save_button = ft.FilledButton(text='Сохранить', on_click=save_file)

    page.add(
        ft.Row([ft.Text("Файловый редактор", size=30, width=150)], alignment=ft.MainAxisAlignment.CENTER),
        ft.ElevatedButton("Добавить файл", icon=ft.icons.FILE_OPEN,
                           on_click=lambda _: pick_dialog.pick_files(allow_multiple=False)),
        ft.Row([text_field]),
        ft.Row([save_button], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([text_row])
    )


if __name__ == "__main__":
    ft.app(
        target=main
    )
