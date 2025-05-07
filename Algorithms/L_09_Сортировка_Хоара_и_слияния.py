from typing import List

# Сортировка слиянием
# Алгоритм слияния
def merge(A: List, B: List):
    C = [0] * (len(A) + len(B))          # Сделал список для слияния
    i = k = c = 0                        # Определил начальное значение коэффициентов
    while i < len(A) and k < len(B):     # Цикл, который проверяет не выходят ли коэф., за границы списков
        if A[i] <= B[k]:                 # Условие сравнения
            C[c] = A[i]
            i += 1
        else:
            C[c] = B[k]
            k += 1
        c += 1
    while i < len(A):                    # Цикл до записи остатков списка
        C[c] = A[i]
        i += 1
        c += 1
    while k < len(B):
        C[c] = B[k]
        k += 1
        c += 1
    return C

# Рекуррентная функция
def mergeSort(A: List[int]):
    if len(A) <= 1:
        return
    middle = len(A) // 2
    l = A[:middle]
    r = A[middle:]
    mergeSort(l)
    mergeSort(r)
    C = merge(l, r)
    A[:] = C[:]
    # for i in range(len(A)):
    #     A[i] = C[i]

A = [6, 2, 4, 1, 3, 5]
mergeSort(A)
print(A)

"""
Сортировка Тони Хоара (QuickSort)
"""
A = [6, 2, 4, 1, 3, 5]
def hoar_sort(A: List[int]):
    """
    Сортировка Хоара
    :param A: список целых чисел
    :return: None
    """
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []
    M = []
    R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x > barrier:
            R.append(x)
        else:
            M.append(x)
    hoar_sort(L)
    hoar_sort(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1

hoar_sort(A)
print(A)

def check_sorted(A, ascending=True):
    """
    Проверка отсортированности за O(len(A))
    :param ascending: Показывает восходящий ли список или нисходящий
    """
    flag = True
    s = 2 * int(ascending) - 1  # Алгебра f(x)=2x - 1, при x=True=1 "2*1-1=1"; при x=False=0 "2*0-1=-1"
    N = len(A)
    for i in range(0, N - 1):
        if s * A[i] > s * A[i + 1]:
            flag = False
            break
    return flag


print(check_sorted(A))































