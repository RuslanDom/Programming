import flet as ft
from PIL import Image
import time

path = ''



def main(page: ft.Page):
    page.title = 'CONVERTER'
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = 'dark'
    page.window.resizable = False
    page.window.width = 400
    page.window.height = 500


    def converter_jpg_to_png(event):
        for i in event.files:
            path = i.path
        print(path)
        im = Image.open(path)
        file = im.convert("RGB")
        file.save(path[:-3] + "jpg")


    
    def converter_png_to_jpg(event):
        for i in event.files:
            path = i.path
        print(path)
        im = Image.open(path)
        im.save(path[:-3] + 'png')


    def func_pick(event: ft.FilePickerResultEvent):
        for el in event.files:
            path = el.path
        if path[-3:] == 'jpg':
            btn_png.disabled = False
        elif path[-3:] == 'png':
            btn_jpg.disabled = False
        page.update()
        


    pick_dialog = ft.FilePicker(on_result=func_pick)
    page.overlay.append(pick_dialog)
    btn_jpg = ft.ElevatedButton(text='Перевести в jpg', on_click=converter_png_to_jpg, disabled=True)
    btn_png = ft.ElevatedButton(text='Перевести в png', on_click=converter_jpg_to_png, disabled=True) 

    page.add(
        ft.Row([ft.Text('Конвертер файлов', size=30)], alignment=ft.MainAxisAlignment.CENTER),
        ft.ElevatedButton(text="Загрузить файл", 
                          on_click=lambda _: pick_dialog.pick_files(allow_multiple=False)),
        btn_jpg,                  
        btn_png      
    )


if __name__ == "__main__":
    ft.app(target=main)








