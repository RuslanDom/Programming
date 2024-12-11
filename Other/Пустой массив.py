# Вариант 1
X = [[[[] for _ in range(2)] for _ in range(3)] for _ in range(5)]

# Вывод
print(X)
c = 0
for s in X:
    c += 1
    print('---' * 5, f'Блок №{c}', '---' * 5)
    for i in s:
        print(i)

print("-----***-----" * 10)

# Вариант 2

Y = []
for _ in range(5):
    q1 = []
    for _ in range(3):
        q2 = []
        for _ in range(3):
            q2.append([])
        q1.append(q2)
    Y.append(q1)


# Вывод
c = 0
print(Y)
for s in Y:
    c += 1
    print('---' * 5, f'Блок №{c}', '---' * 5)
    for i in s:
        print(i)