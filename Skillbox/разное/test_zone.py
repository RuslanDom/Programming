file = open('numbers.txt', 'r')
file_2 = open('answer.txt', 'w')
summa = 0
res = []
# file_res = file.read()
result = []
for el in file:
    res.append(el)
print(res)
for el in res:
    tmp = ''
    for i_el in el:
        if i_el != ' ' and i_el != '\n':
            tmp += i_el
    result.append(tmp)
print(result)











file.close()
file_2.close()