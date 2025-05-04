def tester(A):
    flag = True
    N = len(A)
    for i in range(N - 1):
        if A[i] > A[i + 1]:
            flag = False
    return flag

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
    for i in range(1, N):
        for k in range(N - i):
            if A[k] > A[k + 1]:
                A[k], A[k + 1] = A[k + 1], A[k]

def choice_sort(A):
    N = len(A)
    for i in range(N - 1):
        for k in range(i + 1, N):
            if A[k] < A[i]:
                A[k], A[i] = A[i], A[k]

def sort_test(A):
    if len(A) <= 1:
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
    sort_test(L)
    sort_test(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1





A = [3, 5, 8, 2, 4, 1, 7, 6]
# hoar(A)
# insert_sort(A)
# bubble_sort(A)
# choice_sort(A)
sort_test(A)
print(A)
print(tester(A))
