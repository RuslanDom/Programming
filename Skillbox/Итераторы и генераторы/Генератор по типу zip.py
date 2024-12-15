arg_1 = 'abcd'
arg_2 = (1, 2, 3, 4, 5)

res = ((arg_1[i_el], arg_2[i_el]) for i_el in range(min(len(arg_1), len(arg_2))))
print(res)
print(*res, sep='\n')

print()
res_zip = zip(arg_1, arg_2)
print(res_zip)
print(*res_zip, sep='\n')