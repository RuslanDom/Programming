
""" ----------------------------- format() ----------------------------- """

text = ('Sometimes {he} likes a game of some sort when he comes downstairs,\n'
        'and sometimes {he} likes to sit quietly in front of the fire and listen to a story.').format(he='Winnie-the-Pooh')
print(text)

text_2 = ('Once upon a time, a very long time ago now,'
          ' about last Friday, {0} lived in a forest all by himself under the name of {1}.').format(
    'Winnie-the-Pooh',
    'Sanders'
)
print(text_2)


""" ------------------------- split() and join() -------------------------"""
print('\n--------------------Методы split() and join(), strip() and replace()--------------------\n')
name = input("Enter names separated by comma: ").split(', ')  # split() Разбивает строку на список
print(name)
age = input("Enter age this people: ").split()
print(age)

result = [" ".join([name[i_man], age[i_man]]) for i_man in range(len(name))]
print(result)

finish_text = ', '.join(result)  # join() Объединяет строку через указанный символ
print(finish_text)
# Одним из решений этой задачи является использование метода strip() в Python.
# Однако, этот метод удаляет пробелы только в начале и в конце строки.
# Чтобы удалить все пробелы из строки, в том числе и между словами, можно использовать метод replace().


""" ------------------------------- startswith(), endswith(), upper(), lower() -------------------------------"""
print('\n--------------------Методы startswith(), endswith(), upper(), lower()--------------------\n')
file = input('Enter file (.txt): ')                         # startswith проверка с чего начинается строка
if file.endswith('.txt'):                                   # endswith() проверка на что заканчивается строка
    print(file)
else:
    print('Error')

txt = input("Enter new text: ").lower()                     # lower() всё в нижний регистр
print(txt)
print(txt.upper())                                          # upper() всё в верхний регистр


""" -------------------------------- {:} Placeholder (подстановка)  -------------------------------- """
print('\n-------------------- {:} Placeholder (подстановка) --------------------\n')

integer_amount = 3500000
_int_ = 50000000
print("Величина целового числа 3500000 равна {:,d}".format(integer_amount))
print("Экспонентоциальное представление числа 50000000 = {:.0e}".format(_int_))

float_amount = 3.14159265
print("Величина вещественного числа 3.14159265 до 4 знаков после , равна {:.4f}".format((float_amount)))

amount_for_percent = 0.1325
print("Перевод числа в проценты через placeholder. Число 0.1325 равно {:.1%}".format(amount_for_percent))