def tester(A, ascending=True):
    flag = True
    N = len(A)
    for i in range(N - 1):
        if (A[i] > A[i + 1] and ascending) or (A[i] < A[i + 1] and not ascending):
            flag = False
            break
    return flag

def merge(L: list, R: list):
    C = [0] * (len(L) + len(R))
    c = l = r = 0
    while l < len(L) and r < len(R):
        if L[l] <= R[r]:
            C[c] = L[l]
            l += 1
        else:
            C[c] = R[r]
            r += 1
        c += 1
    while l < len(L):
        C[c] = L[l]
        l += 1
        c += 1
    while r < len(R):
        C[c] = R[r]
        r += 1
        c += 1
    return C

def hoar(A):
    if len(A) < 1:
        return
    L = []
    M = []
    R = []
    barrier = A[0]
    for x in A:
        if x < barrier:
            L.append(x)
        elif x > barrier:
            R.append(x)
        else:
            M.append(x)
    hoar(L)
    hoar(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1

def insert_sort(A):
    N = len(A)
    for i in range(1, N - 1):
        k = i
        while A[k] > A[k + 1] and k >= 0:
            A[k], A[k + 1] = A[k + 1], A[k]
            k -= 1

def bubble_sort(A):
    N = len(A)
    for i in range(N):
        for k in range(N - i):
            if A[k] < A[k - 1]:
                A[k], A[k - 1] = A[k - 1], A[k]

def choice_sort(A):
    N = len(A)
    for i in range(N - 1):
        for k in range(i + 1, N):
            if A[k] < A[i]:
                A[k], A[i] = A[i], A[k]

def sort_test(A):
    ...


def merge_sort(A):
    if len(A) <= 1:
         return
    middle = len(A) // 2
    l = A[:middle]
    r = A[middle:]
    merge_sort(l)
    merge_sort(r)
    C = merge(l, r)
    A[:] = C[:]


A = [3, 5, 8, 2, 9, 4, 1, 7, 6]
B = [3, 6, 2, 4, 7, 1, 8, 5]
# hoar(A)
# insert_sort(A)
# bubble_sort(A)
# choice_sort(A)
# sort_test(A)
# merge_sort(A)
# print(A)
# print(tester(A))

def num_was_in_prefix(x, A):
    if x in A:
        return True
    return False

def permutation(N, M, prefix=None):
    if M == 0:
        print(prefix)
        return
    prefix = prefix or []
    for num in range(1, N + 1):
        if num_was_in_prefix(num, prefix):
            continue
        prefix.append(num)
        permutation(N, M - 1, prefix)
        prefix.pop()

COUNT = 0
def generate_num(N, M, prefix=None):
    if M == 0:
        global COUNT
        print(COUNT, ":", prefix)
        COUNT += 1
        return
    prefix = prefix or ""
    for num in range(N):
        generate_num(N, M - 1, prefix + str(num))




# permutation(3, 3)
# generate_num(2, 4)

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def fib_list(n):
    F = [0, 1] + [0] * (n - 1)  # Добавил 2 элемента, отнял 1, если n = 6 el будет 7
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F


print(fib(6))
print(fib_list(8))

def lcs(A: list, B: list):
    F = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j -1]:
                F[i][j] = 1 + F[i - 1][j - 1]
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])
    return F[-1][-1]


l = lcs(A, B)
print("LCS: ", l)

def b_s(A: list):
    n = len(A)
    for i in range(n):
        for j in range(1, n - i):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
    return A
# print("b_s: ", b_s(B))

def i_s(A: list):
    n = len(A)
    for i in range(n):
        j = i
        while j >= 1 and A[j - 1] > A[j]:
            A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1
    return A
# print("i_s: ", i_s(B))

def c_s(A: list):
    n = len(A)
    for i in range(n - 1):
        for j in range(i, n):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    return A
# print("c_s: ", c_s(B))

def sss(l, n, prefix=None):
    if l <= 0:
        print(prefix)
        return
    prefix = prefix or ''
    for i in range(n):
        sss(l - 1, n, prefix + str(i))
    return 'Ok'

# print("sss: ", sss(4, 2))

def ss(n, prefix:str):
    if n in prefix:
        return True
    return False


def perm_2(l, n, prefix=None):
    if l == 0:
        print(prefix)
        return
    prefix = prefix or []
    for i in range(1, n + 1):
        if ss(str(i), prefix):
            continue
        prefix.append(i)
        perm_2(l - 1, n, prefix)
        prefix.pop()

perm_2(3, 2)




