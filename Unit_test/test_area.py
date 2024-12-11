# Задача на сдвиг

list1 = [1, 2, 3, 5, -10, -8, -6, -1, 0]
list2 = [3, 4, 5, 0, 1]

def sort_list(lst):
    min_el = min(lst)
    for i in range(len(lst)):
        if lst[i] == min_el:
            return f'Сдвиг на {i} влево, список отсортирован {sorted(lst)}'



print(sort_list(list1))






















