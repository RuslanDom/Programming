def counter(num):
    if num < 1:
        return 1
    return counter(num - 1), print(num)


number = int(input("Введите число: "))
counter(number)

"""-------------------------------------------------------------------------------------------------"""

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
            'p': 'А вот здесь новый абзац'
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


"""---------------------------------------------------------------------------------------"""
import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def title_site(brand, data_site, orig):

    if 'title' in data_site or 'h2' in data_site:
        data_site['title'] = f'Куплю/продам {brand} недорого'
        data_site['h2'] = f'У нас самая низкая цена на {brand}'
        return orig

    for i_val in data_site.values():
        if isinstance(i_val, dict):
            result = title_site(brand, i_val, orig)
            if result:
                break
    else:
        result = None
    return result


numbers_site = int(input("Сколько сайтов: "))

list_site = []
print_info = []

for i_num in range(numbers_site):
    print_info.append(input("\nВведите название продукта для нового сайта: "))
    list_site.append(copy.deepcopy(site))
    list_site[i_num] = title_site(print_info[i_num], list_site[i_num], list_site[i_num])
    print(list_site[i_num])
    for i_dict in range(len(list_site)):
        print("\nСайт для {}:\n".format(print_info[i_dict]))
        for key, val in list_site[i_dict].items():
            print(key, "---", val)

"""-------------------------------------------------------------------------------------------"""

def summa_nums(result: list, *args):
    if isinstance(args, int):
        return result.append(args)

    for i_el in args:
        if isinstance(i_el, list):
            for i in i_el:
                summa_nums(result, i)
        else:
            result.append(i_el)

    res = 0
    for num in result:
        res += num
    return res


res_num = []
res_num_2 = []
print(f'Ответ в консоли: {summa_nums(res_num, [[1, 2, [3]], [1], 3])}')
print(f'Ответ в консоли: {summa_nums(res_num_2, 1, 2, 3, 4, 5)}')

"""--------------------------------------------------------------------------------------------"""

def open_list(work_list, res_list):

    if isinstance(work_list, int):
        res_list.append(work_list)

    for i_num in work_list:
        if isinstance(i_num, list):
            open_list(i_num, res_list)
        else:
            res_list.append(i_num)

    return res_list


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
result_list = []
print(f'Ответ: {open_list(nice_list, result_list)}')

"""----------------------------------------------------------------------------------------------"""
def sort_list(work_list):
    if len(work_list) > 1:
        less_list = [el for el in work_list if el < work_list[-1]]
        equal_list = [el for el in work_list if el == work_list[-1]]
        larger_list = [el for el in work_list if el > work_list[-1]]
    else:
        return work_list

    result = sort_list(less_list) + equal_list + sort_list(larger_list)
    return result


user_list = [5, 8, 9, 4, 2, 9, 1, 8]

print()
print(sort_list(user_list))
