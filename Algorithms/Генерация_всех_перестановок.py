from random import randint

password = []
# def generate_num(n):
#     if n <= 0:
#         return 1
#     return generate_num(n - 1) * n
n = int(input("Длинна пароля: "))
# g = generate_num(n=n)
# print(g)
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



print(password)
print(len(password))
# a = [1, "2", 3]
# try:
#     if a.index("2"):
#         print(a)
# except:
#     print("MMM")
