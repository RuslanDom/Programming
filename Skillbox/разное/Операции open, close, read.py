import os
data_file = open('test_data.txt', 'r', encoding='utf-8')      # "r" read только читать
"""1 способ считывания файла"""
data = data_file.read()
another_data = data_file.read()  # Второй раз не считывает

print(data)
""" Domashevskiy Ruslan 34
    Domashevskay Kristina 33
    Domashevskiy Bogdan 15
    Domashevskay Zlata 13
"""
print(another_data)  # Чтобы считать второй раз нужно снова запустить open('test_data.txt', 'r', encoding='utf-8')
"""
"""
data_file.close()

"""2 способ считывания(более правильный по строчно) с использованием цикла"""
data_file = open('test_data.txt', 'r', encoding='utf-8')
for i_line in data_file:
    print(i_line, end='')
data_file.close()

print('\n-----------------Практика по работе с файлами-----------------\n')

file = open(os.path.abspath('test_data.txt'), 'r')
summa = 0
for i_line in file:
    info = i_line.split()
    summa += int(info[2])
file.close()

file_2 = open(os.path.abspath('test_data_2.txt'), 'r')
summa_2 = 0
for i_line in file_2:
    info = i_line.split()
    summa_2 += int(info[2])
file_2.close()

diff = summa - summa_2


print("Сумма возрастов 1-го файла", summa)
print("Сумма возрастов 2-го файла", summa_2)
print("Разность между 1-ой суммой и 2-ой", diff)

print()
print("""--------------------Метод write--------------------""")
file = open(os.path.abspath('test_data.txt'), 'r')
letter_count = []
for i_line in file:
    print(i_line, end='')
    letter_count.append(str(len(i_line)))
letter_count_str = '\n'.join(letter_count)
print('------------------test_data_2.txt------------------')
print(letter_count_str)
file.close()

new_file_create = open('test_data_3.txt', 'w')
new_file_create.write(letter_count_str)
new_file_create.close()
print('------------------test_data_3.txt(создан через write)------------------')
new_file_create = open('test_data_3.txt', 'r')
result = new_file_create.read()
print(result)
new_file_create.close()
