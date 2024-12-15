def divide(number):
    return 1 / number


def summa_of_divided(first_num, second_num):
    div_summa = 0
    for i_num in (first_num, second_num + 1):
        try:
            div_summa += divide(i_num)
        except ZeroDivisionError:
            print("Can`t divide by zero")
    return div_summa


total = 0
nums_list = []
try:
    with open('number.txt', 'r') as number_file:
        for i_line in number_file:
            try:
                nums_list += i_line.split()
                print(nums_list)
                f_num = int(nums_list[0])
                s_num = int(nums_list[1])

                total += summa_of_divided(f_num, s_num)
                print("Summa equal:", total)
            except IndexError:
                print('В списке чисел только одно число. Функция суммы невозможна.')
                continue

except ZeroDivisionError:
    print("Can`t divide by zero")
