import flet as ft

def main(page: ft.Page):
    page.title = 'TEST'
    page.theme_mode = 'dark'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 1200
    page.window.height = 1000

    def func_btn1(e):
        result.value = f"{first_name.current.value} and {second_name.current.value}"
        first_name.current.value = ''
        second_name.current.value = ''
        page.update()

    headers = ft.Text('header', size=20)
    headers2 = ft.Text('header_2', size=20)
    field_1 = ft.TextField(label='enter', width=150, autofocus=True)
    field_2 = ft.TextField(label='enter', width=150)
    t1 = ft.Text('text1', size=20, bgcolor='red')
    t2 = ft.Text('text2', size=20, bgcolor='yellow')
    t3 = ft.Text('text3', size=20, bgcolor='green')
    t4 = ft.Text('text4', size=20, color='yellow' )
    first_name = ft.Ref[ft.TextField]()
    second_name = ft.Ref[ft.TextField]()
    
    f1 = ft.TextField(ref=first_name, label='first')
    f2 = ft.TextField(ref=second_name, label='second')
    result = ft.Text(size=20, color='yellow')
    btn1 = ft.ElevatedButton('test', bgcolor='blue', on_click=func_btn1, scale=1)



    page.add(
        ft.Row(
            [
                ft.Row(
                    [
                        ft.Column([t1, t2, t3, t4]),
                        ft.Column([t1, t2, t3, t4])
                    ], alignment=ft.MainAxisAlignment.START
                ),
                ft.Row(
                    [
                        ft.Column([headers, headers2],),
                        ft.Column([field_1, field_2])
                    ], alignment=ft.MainAxisAlignment.END
                ),
                ft.Row(
                    [
                        ft.Column([f1, f2, btn1, result])
                        
                    ]
                )
            ]
        )
    )

def main2(page: ft.Page):

    first_name = ft.Ref[ft.TextField]()
    last_name = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.Column]()

    def btn_click(e):
        greetings.current.controls.append(
            ft.Text(f"Hello, {first_name.current.value} {last_name.current.value}!")
        )
        first_name.current.value = ""
        last_name.current.value = ""
        page.update()
        first_name.current.focus()

    page.add(
        ft.TextField(ref=first_name, label="First name", autofocus=True),
        ft.TextField(ref=last_name, label="Last name"),
        ft.ElevatedButton("Say hello!", on_click=btn_click),
        ft.Column(ref=greetings),
    )



if __name__ == '__main__':
    ft.app(main)
