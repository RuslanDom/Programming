import re  # regular expressions (регулярные выражения)

text = 'AV - welcome to home Winnie-the-Pooh'

# print(text.startswith('AV'))

# match() - поиск в начале строки по шаблону
result = re.match(r'AV', text)
print(f'Поиск в начале строки по шаблону {result}')
# group() - метод для подстроки
print(f'Найденное слово: {result.group(0)}')  # Вывод: AV
# statr(), end() - для начальной и конечной позиции
print(result.start())  # Вывод: 0
print(result.end())  # Вывод: 2

# r перед текстом делает сырой текст
'AV\n - welcome to home'
r'AV\n - welcome to home'  # r убрало экранирование \n

print('=' * 40)
# search() - метод для поиска нужной подстроки
result_search = re.search(r'welcome', text)
print(f'Поиск в строке по шаблону {result_search}')
print(f'Найденное слово: {result_search.group(0)}')

print('=' * 40)
# findall() - метод для поиска всех совпадений по шаблону
new_text = (r'Winnie-the-Pooh sat down at the foot of the tree, put his head between his paws, '
            r'and began to think. First of all he said to himself: That buzzing-noise means something.'
            r'First of all he said to himself: That buzzing-noise means something.'
            r'You don’t get a buzzing-noise like that, just buzzing and buzzing, without its meaning something.'
            r'Winnie-the-Pooh thought, if there’s a buzzing-noise, somebody’s making a buzzing-noise, '
            r'and the only reason for making a buzzing-noise that I know of is because you’re a bee.')

result_find_all = re.findall(r'something', new_text)
print(f'Все совпадения по шаблону {result_find_all}')

print('=' * 40)
# sub() - метод замены шаблона (заменит все повторения слова в тексте на другое)
result_sub = re.sub(r'buzzing-noise', "'loud noise'", new_text)
print(f'Замена всех найденных шаблонов: {result_sub}')

print('=' * 40)
# compile() - метод собирает регулярные выражения в объект (который можно будет затем использовать для поиска)
pattern = re.compile(r'Winnie-the-Pooh')
result_compile = pattern.findall(new_text)
print(result_compile)
result_compile = pattern.findall(text)
print(result_compile)
