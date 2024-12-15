import re

text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'

print(f"Поиск шаблона в начале строки: {re.match(r'wo', text)}")
print(f"Поиск первого найденного совпадения по шаблону: {re.search(r'wo', text)}")
print(f"Содержимое найденной подстроки:  {re.search(r'wo', text).group(0)}")
print(f"Начальная позиция: {re.search(r'wo', text).start()}")
print(f"Конечная позиция: {re.search(r'wo', text).end()}")
print(f"Список всех упоминаний шаблона: {re.findall(r'wo', text)}")
print(f"Текст после замены: {re.sub(r'wo', 'ЗАМЕНА', text)}")

print('=' * 60)
text = r'How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?'
print(re.findall(r'\\wwood\+\?', text))
