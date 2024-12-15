site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': {
                'first_div': 'Тут, наверное, какой-то блок',
                'second_div': 'Второй блок',
                'third_div': 'Третий блок',
            },
            'p': 'А вот здесь новый абзац',
            'div2': {
                '4': 'Четвёртый',
                '5': 'Пятый',
                '6': 'Шестой',
            }
        }
    }
}

count = 0
count_for_search_key = 0


def deep_count(work_dict):
    """ Эта функция расчитывает максимальную вложенность словаря полученного
        в параметр функции и возвращает значение типа int
    """
    global count
    for i_val in work_dict.values():
        if isinstance(i_val, dict):
            count += 1
            deep_count(i_val)
    return count


def search_key(find_key, work_dict, deep_user=deep_count(site)):
    """ Данная функция ищет полученный от пользователя ключ (find_key) в базе данных имеющих
        структуру словаря (work_dict), поиск возможно регулировать на заданную глубину вложенности
        указанную в параметре (deep_user), возвращает функция значение по найденному ключу, при отсутствии
        ключа возвращает значение None
    """
    global count_for_search_key
    if find_key in work_dict:
        return work_dict[find_key]

    for i_value in work_dict.values():
        if isinstance(i_value, dict):
            count_for_search_key += 1
            if count_for_search_key <= deep_user:
                result = search_key(find_key, i_value, deep_user)
                if result:
                    break

    else:
        result = None
    return result


key_user = input('Введите искомый ключ: ')
deep_search = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if deep_search == 'y':
    my_deep = int(input('Введите максимальную глубину: '))
    result = search_key(key_user, site, my_deep)
else:
    result = search_key(key_user, site)

if result:
    print("Значение ключа: ", result)
else:
    print("Значение ключа: ", result)