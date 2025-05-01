from typing import List, Callable



def insert_sort(num_list: List[int]) -> List[int]:
    """
    Сортировка методом вставки (insert sort)
    :param num_list: список который необходимо отсортировать
    :return: отсортированный список
    """
    N = len(num_list)
    for k in range(1, N):
        top = k
        while top > 0 and num_list[top - 1] > num_list[top]:
            num_list[top - 1], num_list[top] = num_list[top], num_list[top - 1]
            top -= 1
    return num_list



def bubble_sort(num_list: List[int]) -> List[int]:
    """
    Сортировка методом пузырька (bubble sort)
    :param num_list: список который необходимо отсортировать
    :return: отсортированный список
    """
    N = len(num_list)
    for k in range(N):
        for i in range(1, N - k):
            if num_list[i - 1] > num_list[i]:
                num_list[i], num_list[i - 1] = num_list[i - 1], num_list[i]
    return num_list



def choice_sort(num_list: List[int]) -> List[int]:
    """
    Сортировка методом выбора
    :param num_list: список который необходимо отсортировать
    :return: отсортированный список
    """
    N = len(num_list)
    for k in range(N - 1):
        for i in range(k + 1, N):
            if num_list[i] < num_list[k]:
                num_list[i], num_list[k] = num_list[k], num_list[i]
    return num_list


def test_cases(func: Callable):
    """
    Тесты для функций сортировки
    :param func: функция сортировки
    :return: Ok or Fail
    """
    print(func.__doc__)
    test_1 = [8, 6, 3, 7, 9, 2, 4, 1, 5]
    result = func(test_1)
    print("Testcase 1 ok\nResult: {}".format(result) if result == sorted(test_1) else "Testcase 1 fail")
    test_2 = [-10, 6, -3, -7, 3, 2, 4, 1, -5]
    result = func(test_2)
    print("Testcase 2 ok\nResult: {}".format(result) if result == sorted(test_2) else "Testcase 2 fail")
    test_3 = [3, 6, 3, 7, 3, 2, 4, 3, 5]
    result = func(test_3)
    print("Testcase 3 ok\nResult: {}".format(result) if result == sorted(test_3) else "Testcase 3 fail")


if __name__ == '__main__':
    test_cases(insert_sort)
    test_cases(bubble_sort)
    test_cases(choice_sort)