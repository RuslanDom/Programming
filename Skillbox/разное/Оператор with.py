sym_sum = 0
line_count = 0
try:
    with open('test_data_2.txt', 'r') as people_file:
        for i_line in people_file:
            line_count += 1
            length = len(i_line)
            if i_line.endswith('\n'):
                length -= 1
            if length < 3:
                raise BaseException('Длинна {} строки меньше трёх символов'.format(line_count))
            sym_sum += length

except FileNotFoundError:
    print('File not found!')
except BaseException:
    print("Меньше 3 символов")
    raise
finally:
    print('Сработал блок finally:')
    print('Найденная сумма символов: {}'.format(sym_sum))
    print("Проверка на закрытие файла", people_file.closed)