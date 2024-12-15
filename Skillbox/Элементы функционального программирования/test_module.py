def func() -> None:
    print(f'Я первая функция {func.__name__} из test_module')


def func2() -> None:
    print('Вторая функция модуля test_module')


if __name__ == '__main__':
    print("Основной код")
    func2()
else:
    pass

