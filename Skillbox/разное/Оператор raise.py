def first():
    print("\n------------------------- Оператор raise (Подсчёт символов в тексте, при условии:\n"
          "если длинна строки меньше 3 символов вызывается исключение  -------------------------\n")
    sym_sum = 0
    line_count = 0
    try:
        people_file = open('test_data_2.txt', 'r')
        for i_line in people_file:
            line_count += 1
            length = len(i_line)
            if i_line.endswith('\n'):
                length -= 1
            if length < 3:
                raise BaseException('Длинна {} строки меньше трёх символов'.format(line_count))
            sym_sum += length
        people_file.close()
    except FileNotFoundError:
        print('File not found!')
    except BaseException:
        print("Меньше 3 символов")

    finally:
        print('Сработал блок finally:')
        print('Найденная сумма символов: {}'.format(sym_sum))


def second():
    """ 2 задача"""
    print('\n--------------aa----------------\n')
    name_list = []
    while True:
        try:
            name = input('Enter name: ')
            if name.lower() == 'error':
                raise BaseException("СТОП программа!")

            if not name.isalpha():
                raise TypeError
            name_list.append(name)
            if len(name_list) == 5:
                print("Name limit reached")
                break
        except TypeError:
            print("Enter only letter!")
        except BaseException:
            name_list = []
            print('Проброс ошибки')
            raise ValueError('Проброс ошибки(Вы ввели СТОП - СЛОВО!)')
    names_file = open('names.txt', 'w')
    names_file.write('\n'.join(name_list))
    names_file.close()
    print('Programme is finish')


choice = int(input("Выберите задачу (1, 2): "))
if choice == 1:
    first()
elif choice == 2:
    second()
