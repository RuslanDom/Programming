import datetime
from typing import Callable


def bubble_sort(A: list):
    n = len(A)
    for i in range(n):
        for j in range(1, n - i):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]

def insert_sort(A: list):
    n = len(A)
    for i in range(n - 1):
        j = i
        while A[j] > A[j + 1] and j >= 0:
            A[j], A[j + 1] = A[j + 1], A[j]
            j -= 1

def choice_sort(A: list):
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if A[j] < A[i]:
                A[i], A[j] = A[j], A[i]


def auto_test_sorter(func_sort: Callable):
    # testcase 1
    A = [7, 2, 9, 1, 4, 3, 5, 8, 6]
    right_answer = sorted(A)
    func_sort(A)
    print(f"{func_sort.__name__} test №1", end='')
    if A == right_answer:
        print(": OK")
    else:
        print(": FAIL")

    # testcase 2
    A = [4, 4, 2, 1, 1, 3, 5, 3, 3]
    right_answer = sorted(A)
    func_sort(A)
    print(f"{func_sort.__name__} test №2", end='')
    if A == right_answer:
        print(": OK")
    else:
        print(": FAIL")

    # testcase 3
    A = ['c', 'h', 'ag', 'da', 'fff', 'fwf', 'dxd']
    right_answer = sorted(A)
    func_sort(A)
    print(f"{func_sort.__name__} test №3", end='')
    if A == right_answer:
        print(": OK")
    else:
        print(": FAIL")
    print("\n")


def number_generate(num, length, prefix=None):
    if length <= 0:
        print(prefix)
        return
    prefix = prefix or ''
    for n in range(num):
        number_generate(num, length - 1, prefix + str(n))

def check_number(num, prefix):
    if num in prefix:
        return True
    return False

def generate_original_num(num, length, prefix=None):
    if length <= 0:
        print(prefix)
        return
    prefix = prefix or []
    for n in range(1, num + 1):
        if check_number(n, prefix):
            continue
        prefix.append(n)
        generate_original_num(num, length - 1, prefix)
        prefix.pop()

def test_sort():
    new_data = datetime.date.today().replace(day=30)
    print(new_data - datetime.date.today())


if __name__ == "__main__":
    # auto_test_sorter(test_sort)
    # auto_test_sorter(bubble_sort)
    # auto_test_sorter(insert_sort)
    # auto_test_sorter(choice_sort)
    # number_generate(2, 4)
    # generate_original_num(3, 3)
    test_sort()