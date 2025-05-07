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

# Задача про кузнечика
# С использованием запрещённых точек allowed
def grasshopper(N: int, allowed: list):
    K = [0, 1, int(allowed[2])] + [0] * (N - 3)
    for i in range(3, N + 1):
        if allowed[i]:
            K[i] = K[i - 1] + K[i - 2] + K[i + 3]

# С минимальной стоимостью достижения N
# price[i] - стоимость посещения клетки i
# C[i] - минимальная стоимость достижения клетки i
def min_grasshopper(N, price: list):
    C = [float("-inf"), price[1], price[1] + price[2]] + [0] * (N - 2)
    for i in  range(3, N + 1):
        C[i] = price[i] + min(C[i - 1], C[i - 2])
    return C[N]

# Двумерные массивы
m = 3
n = 3

# !!!!! НЕПРАВИЛЬНОЕ СОЗДАНИЕ СПИСКА все элементы ссылаются на первый
L = [[0] * m] * n
L[0][0] = 1  # ИЗМЕНИЛ ТОЛЬКО один элемент, а поменялись все
print(L)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

# Правильно
L = [[0] * m for _ in range(n)]
L[0][0] = 1
print(L)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]



