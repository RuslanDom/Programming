import sys

# сохраняем старый поток вывода
old_stdout = sys.stdout
# перенаправляем поток вывода в файл output.txt
new_stdout = open('output.txt', 'w')
sys.stdout = new_stdout
# теперь print будет выводить в файл
print('hello output.txt')
# закрываем файл и возвращаем старый поток вывода
new_stdout.close()
sys.stdout = old_stdout  # or sys.stdout = sys.__stdout__
