from typing import List, Callable


def insert_sort(num_list: List[int]) -> List[int]:
    """
    Сортировка методом вставки
    :param num_list: Рабочий список
    :return: Отсортированный список
    """
    N = len(num_list)
    for k in range(1, N):
        top = k
        while top > 0 and num_list[top - 1] > num_list[top]:
            num_list[top], num_list[top - 1] = num_list[top - 1], num_list[top]
            top -= 1
    return num_list



def choice_sort(num_list: List[int]) -> List[int]:
    """
    Сортировка методом выбора
    :param num_list: Рабочий список
    :return: Отсортированный список
    """
    N = len(num_list)
    for k in range(N):
        for i in range(k + 1, N):
            if num_list[i] < num_list[k]:
                num_list[i], num_list[k] = num_list[k], num_list[i]
    return num_list

def bubble_sort(num_list: List[int]) -> List[int]:
    """
    Сортировка методом пузырька
    :param num_list: Рабочий список
    :return: Отсортированный список
    """
    N = len(num_list)
    for k in range(N):
        for i in range(1, N - k):
            if num_list[i - 1] > num_list[i]:
                num_list[i], num_list[i - 1] = num_list[i - 1], num_list[i]
    return num_list


def test_case(func: Callable):
    """
    Тест - кейсы 3 вариантов
    :param func: Функция сортировки
    :return: Возвращает отсортированный список
    """
    print(func.__doc__)
    # case 1
    A_list = [4, 1, 3, 6, 2, 7, 5]
    check_list = sorted(A_list)
    func(A_list)
    print(A_list)
    print(f"Testcase  #1: ok" if A_list == check_list else f"Testcase  #1: fail")

    # case 2
    A_list = [-1, 4, 1, 3, 1, 2, 1, 5, -1]
    check_list = sorted(A_list)
    func(A_list)
    print(f"Testcase  #2: ok" if A_list == check_list else f"Testcase  #2: fail")

    # case 3
    A_list = [5, 4, 3, 2, 1, -1, -2, -3, -4, -5]
    check_list = sorted(A_list)
    func(A_list)
    print(f"Testcase  #3: ok" if A_list == check_list else f"Testcase  #3: fail")

if __name__ == "__main__":
    test_case(insert_sort)
    test_case(choice_sort)
    test_case(bubble_sort)