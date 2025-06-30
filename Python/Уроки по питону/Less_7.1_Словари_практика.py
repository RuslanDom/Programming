
def create_dict():
    students = input("Введите данные учеников\n"
                     "(имя, фамилия, город, курс, оценки): ")
    students = students.split()

    print("""--------------------------1 version--------------------------""")
    students_dict = {
        "Имя": students[0],
        "Фамилия": students[1],
        "Город": students[2],
        "Курс": students[3],
        "Оценки": students[4:]
    }
    for key in students_dict:
        print("{0} - {1}".format(key, students_dict[key]))

    print("--------------------------2 version--------------------------")
    students_new = dict()
    students_new['Имя'] = students[0]
    students_new['Фамилия'] = students[1]
    students_new['Город'] = students[2]
    students_new['Курс'] = students[3]
    students_new['Оценки'] = []
    for i_grade in students[4:]:
        students_new['Оценки'].append(i_grade)
    for i_info in students_new:
        print(f'{i_info} - {students_new[i_info]}')

    """Словари можно копировать использая метод copy()"""
    print("-----------------Словари можно копировать использая метод copy()-----------------")
    stud = students_dict.copy()
    print("{Имя} {Фамилия} {Город} {Курс} {Оценки}".format(**stud))


def method_dict():
    print("\n------------------------ Method dictionary ------------------------\n")

    def histogram(string):
        letter_dict = {}
        for letter in string:
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
        return letter_dict

    text = input("Введите текст для подсчёта символов: ").lower()
    hist = histogram(text)

    for i_letter in sorted(hist.keys()):
        print("{0}: {1}".format(i_letter, hist[i_letter]))

    print(f'Максимальная частота повторения символа: {max(hist.values())}')

    print('/n----------------- Method upload() and pop() -----------------\n')
    first_dict = {
        'Rus': 34,
        'Kris': 33
    }
    print('\nПервый словарь\n')
    for i_family in first_dict:
        print(f'{i_family} возраст: {first_dict[i_family]}')
    second_dict = {
        'Bog': 15,
        'Zlo': 13
    }
    print('\nВторой словарь\n')
    for i_family in second_dict:
        print(f'{i_family} возраст: {second_dict[i_family]}')
    first_dict.update(second_dict)
    first_dict['Zlat'] = first_dict.pop('Zlo')          # (Удаляем через pop() key 'Zlo' и записываем 'Zlat'
                                                        # Можно просто переназвать ключ first_dict['Zlo'] = 'Zlat')
    print('\nРезультат после слияния и замены элемента "Zlo" на "Zlat"\n')
    for i_family in first_dict:
        print(f'{i_family} возраст: {first_dict[i_family]}')


def nested_dict():
    print("\n------------------------ Вложенные словари ------------------------\n")
    print("Let`s create dict called 'data' (Создадим словарь под названием 'data')\n")

    data = dict()
    print("Add keys and values (Добавим ключи и значения)\n")
    data['server'] = {
        'host': "127.0.0.1",
        'port': "10"
    }
    data['configuration'] = {
        'ssh': {
            'access': 'true',
            'login': 'Ivan',
            'password': 'qwerty'
        }
    }
    check = input("Введите название ключа для проверки на наличие такого: ")
    print("Вызовем метод get()   =>   data.get(check)\n")
    print(data.get(check, "Такого ключа нет!!!"), "\n")
    print("Обращение к вложенным ключам через get()    =>    data.get('configuration', {}).get('ssh', {}).get('login', {})\n")
    print("Искомое значение вложенного ключа 'login':", data.get('configuration', {}).get('ssh', {}).get('login', {}), "\n")
    print(data)


def sets():
    from random import randint
    print("----------------------- Множества. Функция set ----------------------\n")
    print("Создадим список через list comprehension\n")
    number_list = [randint(1, 5) for _ in range(10)]
    print("Поличился вот такой список: {0}".format(number_list))
    print("\nИзменим список на множество и выведем значение.\n")
    number_set = set(number_list)
    print("Результат: {}".format(number_set))

    print("\n---------------------- Пересечение множеств intersection() и & ----------------------\n")
    nums_1 = {1, 2, 3, 4, 5}
    nums_2 = {4, 5, 6, 7, 8}
    print("nums_1", nums_1)
    print("nums_2", nums_2)
    new_num = nums_1.intersection(nums_2)
    print("\nРезультат пересечения: {}".format(new_num))
    print("Также работает такая запись nums_1 & nums_2 будет равно == {4, 5}")

    print("\n----------------------- Объединение union() и | -----------------------\n")
    nums_union = nums_1.union(nums_2)
    print("Результат объединения: {}".format(nums_union))
    print("\nТакже работает такая запись nums_1 | nums_2 ")

    print("\n----------------------- Разность множеств difference() и '-' -----------------------\n")
    nums_difference = nums_1.difference(nums_2)
    print("Результат разности: {}".format(nums_difference))
    print("\nТакже работает такая запись nums_1 - nums_2 ")


print("Какую часть кода выполнить?\n1 - Создание словаря\n2 - Работа с методами sorted(), max(),"
      " upload() and pop()\n3 - Вложенные словари\n4 - Множества. Функция set")
select = int(input())
if select == 1:
    create_dict()
"""------------------- Методы словарей-------------------"""
if select == 2:
    method_dict()

"""------------------------ Вложенные словари ------------------------"""
if select == 3:
    nested_dict()

"""----------------------- Множества. Функция set ----------------------"""
if select == 4:
    sets()