test = 1

def f1():
    print(test)
    test = 7
    print(test)


f1()  # Будет ошибка первый print(test) не знает переменной test


def f2():
    test = 2
    print(test)
    if 'test' not in globals():  # test - есть в глобальной области test == 1 ошибки нет False
        raise Exception
    if 'test' not in locals():  # test - есть в локальной области test == 2 ошибки нет False
        raise Exception


f2()


def func():
    var = 1

    def f3():
        par = 2
        if 'var' not in locals():  # переменная var не в локальной видимости выполнится ошибка True
            raise Exception
        print('var' in locals())

    f3()

    def f4():
        par = 3
        print(var)
        if 'var' not in locals():  # переменная var теперь в локальной видимости и ошибка не выполнится False
            raise Exception

    f4()

    def f5():
        var = 4
        par = 4
        print(var)
        if 'var' not in globals():  # var - теперь в локальной видимости в глобальной var нет и ошибка выполнится True
            raise Exception

    f5()


func()
