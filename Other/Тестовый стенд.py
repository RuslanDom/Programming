a = [14, 42, 31, 26, 62, 55]

s_a = sorted(a)
print(s_a)
x = int(input('enter num: '))
res = None
for i in s_a:
    difference = abs(i - x)
    if res is None:
        res = i
    else:
        if difference < abs(res - x):
            res = i

print(res)