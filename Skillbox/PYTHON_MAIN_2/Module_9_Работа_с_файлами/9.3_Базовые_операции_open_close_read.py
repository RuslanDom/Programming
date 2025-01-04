def func():
    speakers_file = open('9.3_List_speakers.txt', 'r', encoding='utf-8')

    # 1
    data = speakers_file.read(10)  # Печатате первые 10 символов
    print(data + '\n')
    data_2 = speakers_file.read(20)  # Печатает 20 символов с момента остановки курсора
    print(data_2 + '\n')
    speakers_file.seek(0)  # Метод seek() перемещает файловый курсор (плохо работает с кириллицей)
    data_3 = speakers_file.read(30)  # Печатает 30 символов после перемещения курсора
    print(data_3)

    # 2
    # for i_line in speakers_file:
    #     print(i_line.strip())


    speakers_file.close()

func()

print('---***---' * 5)
"""
Практическое задание
"""

def get_points():
    with open('9.3_List_speakers.txt', 'r', encoding='utf-8') as file:
        data = [i_line.strip('\n').split() for i_line in file.readlines()]
    result = [i for elem in data for i in elem if i.isdigit()]
    return result


def summa_points(list_points):
    res = [int(num) for num in list_points]
    return "Сумма всех возрастов: {}".format(sum(res))


def difference_points(list_points):
    res = int(list_points[0])
    for num in list_points[1:]:
        res -= int(num)
    return "Разность всех возрастов равна: {}".format(res)

g = get_points()
print(summa_points(g))
print(difference_points(g))
