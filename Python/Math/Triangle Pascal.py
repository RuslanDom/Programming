# n = int(input())
# _list = []
# for i in range(n+1):
#     _list.append([1]+[0]*n)
#
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         _list[i][j] = _list[i-1][j] + _list[i-1][j-1]
#
#
#
# for i in range(0, n+1):
#     for j in range(0, n+1):
#         print(_list[i][j], end=' ')
#     print()
































n = int(input('__'))
Pascal = []

for i in range(n+1):
    Pascal.append([1] + [0]*n)


for i in range(1, n+1):
    for j in range(1, i+1):
        Pascal[i][j] = Pascal[i-1][j] + Pascal[i-1][j-1]

for i in range(0, n+1):
    for j in range(0, i+1):
        P = Pascal[i][j]
        print(P, end=' ')
    print()































# n = int(input('___= '))
# Pascal = []
# for i in range(n+1):
#     Pascal.append([1]+[0]*n)
#
# for i in range(n+1):
#     for j in range(n+1):
#      Pascal[i][j] = Pascal[i-1][j] + Pascal[i-1][j-1]
#
# for i in Pascal:
#     print(i)

