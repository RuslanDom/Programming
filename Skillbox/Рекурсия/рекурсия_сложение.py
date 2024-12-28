def summa(n):
    if n == 1:
        return 1
    return n + summa(n-1)

print(summa(5))