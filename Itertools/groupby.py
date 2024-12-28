from itertools import groupby

group = 'aasaadddasss'
for k, g in groupby(group):
    print(k, list(g))

# a ['a', 'a']
# s ['s']
# a ['a', 'a']
# d ['d', 'd', 'd']
# a ['a']
# s ['s', 's', 's']

print("---***---" * 5)

string = '123444454'
group_2 = groupby(string, key=lambda x: int(x) % 2)
for k, g in group_2:
    print(k, list(g))

# 1 ['1']
# 0 ['2']
# 1 ['3']
# 0 ['4', '4', '4', '4']
# 1 ['5']
# 0 ['4']

print("---***---" * 5)
# Группирует в группы с ключом пользователя
k_0 = []
k_1 = []
string = '1233444454'
group_3 = groupby(string, key=lambda x: int(x) % 2)
for k, g in group_3:
    if k == 1:
        k_1 += list(g)  # 1 список с элементами
    elif k == 0:
        k_0.append(list(g))  # Список со списками сгруппированных элементов
print(k_1)
print(k_0)

print("---***---" * 5)
# Группирует не зависимо от регистра буквы
string = 'YAabBbCCddy'
for k, g in groupby(string, key=lambda x: x.upper()):
    print(k, list(g))
