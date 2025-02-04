import webbrowser


def validator(func):
    def wrapper(url):
        # print("Текст до функции")
        if "." in url:
            func(url)
        else:
            print("Неверный адрес")
        # print("Тест после функции")

    return wrapper

@validator # Декоратор оборачивает функции в свою обёртку


def open_url(url):
    webbrowser.open(url)

open_url('file:///C:/Users/Admin/Desktop/Programming/Cross/index1.html') #Открывает страницу по url

