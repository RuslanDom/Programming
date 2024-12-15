origin_list = [4, 2, 6, 1, 7, 5, 3, 9, 8]
print(f"Оригинал: {origin_list}")

""" Сортировка выбором"""


def selection_sort(num_list):
    len_list = len(num_list)
    for i in range(len_list - 1):
        temp_min = i
        for j in range(i + 1, len_list):
            if num_list[i] > num_list[j] and num_list[temp_min] > num_list[j]:
                temp_min = j
        num_list[i], num_list[temp_min] = num_list[temp_min], num_list[i]
    print(f"Сортировка выбором: {num_list}")


selection_sort(origin_list)

""" Сортировка слиянием"""


def merge_sort(num_list):
    # Условие выхода рекурсии
    if len(num_list) <= 1:
        return num_list
    # Разделяем список на 2 половины
    mid = len(num_list) // 2
    left_half = num_list[:mid]
    right_half = num_list[mid:]
    # Рекурсивно сортируем каждую половину
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    # Объединяем отсортированные половины в один список
    return merge(left_half, right_half)


def merge(left, right):
    merged_list = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        # Сравниваем элементы из обоих списков и добавляем меньший в объединённый список
        if left[left_index] <= right[right_index]:
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[right_index])
            right_index += 1
    # Добавляем оставшиеся элементы из левого списка
    merged_list.extend(left[left_index:])
    # Добавляем оставшиеся элементы из правого списка
    merged_list.extend(right[right_index:])
    return merged_list


origin_list = [4, 2, 6, 1, 7, 5, 3, 9, 8]
print(f"Сортировка слиянием: {merge_sort(origin_list)}")

""" Карманная сортировка """


def bucket_sort(num_list):
    # Определяем количество карманов
    num_buckets = len(num_list)
    # Создаём пустые карманы
    buckets = [[] for _ in range(num_buckets)]
    # Распределяем элементы по карманам
    for num in num_list:
        n = num * num_buckets
        index = int(n)  # Вычисляем (генерируем) индекс кармана для текущего элемента
        buckets[index].append(num)  # Добавляем элемент списка по сгенерированному индексу
    # Сортируем каждый карман отдельно
    for bucket in buckets:
        bucket.sort()
    # Объединяем элементы из всех карманов
    sorted_list = []
    for bucket in buckets:
        sorted_list += bucket
    return sorted_list


numbers = [0.9, 0.42, 0.25, 0.43, 0.75, 0.41, 0.12, 0.1]
result = bucket_sort(numbers)
print(f"Карманная сортировка: {result}")
