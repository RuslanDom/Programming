wordList = 'Любая строка это список'

print(wordList[1])
print(len(wordList))
print(wordList.count("с"))
print(wordList.upper())
print(wordList.find('о')) # Ищет с начала элемент по индексу
print(wordList.rfind('к')) # Ищет с конца элемент по индексу

wordList = wordList.split( ) # Разбиваем строку по параметру и создаём список
print(wordList)

# wordList.upper() в верхний регистр
# wordList.lower() в нижний регистр
# wordList.isupper() в верхнем регистре True or False
# wordList.islower() в нижнем регистре True or False
# wordList.capitalize() каждое слово с буквы в верхнем регистре
wordList = "-".join(wordList) # Объединяет в строку по указанному символу
print(wordList)

print(wordList[2:20:2]) # 1 - начальный индекс; 2 - конечный индекс; 3 - шаг
print(wordList[::-1]) # перевернёт весь список