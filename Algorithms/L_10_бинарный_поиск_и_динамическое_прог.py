"""
Бинарный поиск
Требование: список должен быть отсортирован
"""
def left_bound(A: list, key):
    """
    Находит левую границу
    :param A: список
    :param key: искомый элемент
    :return: левая граница
    """
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (right + left) // 2
        if key > A[middle]:
            left = middle
        else:
            right = middle
    return left

def right_bound(A: list, key):
    """
    Находит правую границу
    :param A: список
    :param key: искомый элемент
    :return: правая граница
    """
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (right + left) // 2
        if key >= A[middle]:
            left = middle
        else:
            right = middle
    return right

"""
Динамическое программирование
"""
def fib(n):
    """
    Число Фибоначчи рекурсией
    """
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
n = 4
fib(n)

fib_list = [0, 1] + [0] * (n - 1)
for i in range(2, n + 1):
    fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
print(fib_list[n])





