list_num = [4, 2, 6, 1, 7, 5, 3, 9, 8]
print("Оригинал:", list_num)

""" Сортировка методом пузырька """


def bubble_sort(numbers):
    length = len(numbers)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    print(f"Метод пузырьковой сортировки: {numbers}")


bubble_sort(list_num)

""" Сортировка методом вставок """


def insert_sort(list_num):
    length = len(list_num)
    for i in range(1, length):
        key = list_num[i]
        j = i - 1
        while j >= 0 and list_num[j] > key:
            list_num[j + 1] = list_num[j]
            j -= 1
        list_num[j + 1] = key
    print(f"Метод сортировки вставками: {list_num}")


list_num = [4, 2, 6, 1, 7, 5, 3, 9, 8]
insert_sort(list_num)

""" Сортировка Шелла """


def shell_sort(num_list):
    len_list = len(num_list)
    gap = len_list // 2  # Инициализация начального значения интервала
    while gap > 0:
        # Применяем сортировку вставками с заданным интервалом
        for i in range(gap, len_list):
            key = num_list[i]
            j = i
            # Сдвигаем элементы, чтобы найти правильную позицию для вставки
            while j >= gap and key < num_list[j - gap]:
                num_list[j] = num_list[j - gap]
                j -= gap
            num_list[j] = key
        gap //= 2  # Уменьшаем интервал
    print(f'Сортировка методом Шелла: {num_list}')


list_num = [4, 2, 6, 1, 7, 5, 3, 9, 8]
shell_sort(list_num)
