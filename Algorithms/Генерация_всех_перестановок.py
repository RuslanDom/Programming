from random import randint

def gen_number():
    password = []
    n = int(input("Длинна пароля: "))

    g = 10 ** n
    for i in range(g):
        while True:
            num = [randint(0, 9) for _ in range(n)]
            num = "".join(map(str, num))
            if len(password) == 0:
                password.append(num)
            try:
                password.index(num)
                if len(password) == g:
                    break
            except:
                password.append(num)
    return password

def gen_bin(M: int, prefix=""):
    """
    Функция генерации двоичных чисел
    """
    if M == 0:
        print(prefix)
        return
    for i in "0", "1:":
        gen_bin(M - 1, prefix + i)


def generate_numbers(N: int, M: int, prefix=None):
    """
    Функция, которая генерирует все числа с лидирующими нулями в N-чной системе счисления (N <= 10) длины M
    N - система счисления
    M - длина числа
    """
    if M == 0:
        print(prefix)
        return
    # prefix = prefix or []
    # for digit in range(N):
    #     prefix.append(digit)
    #     generate_numbers(N, M - 1, prefix)
    #     prefix.pop()
    prefix = prefix or ""
    for digit in range(N):
        generate_numbers(N, M - 1, prefix+str(digit))



# Для двоичной СС
# gen_bin(3)
# Для произвольной СС
generate_numbers(3, 3)

# ФУНКЦИЯ ДЛЯ ПЕРЕСТАНОВКИ МЕСТ ЭЛЕМЕНТОВ
def find_num(num, A_list):
    if num in A_list:
        return True
    return False


def generate_permutation(N:int, M:int=-1, prefix=None):
    M = N if M == -1 else M
    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return
    for i in range(1, N + 1):
        if find_num(i, prefix):
            continue
        prefix.append(i)
        generate_permutation(N, M - 1, prefix)
        prefix.pop()


generate_permutation(3, 3)



















