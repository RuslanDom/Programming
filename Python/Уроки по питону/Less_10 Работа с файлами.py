file = open('../data/text.txt', 'w') # "w" для записи "a" для добавления "r" для чтения


file.write('Hello\n')
file.write(input("Enter text: ") + "\n")


file.close()

newData = input("Enter text: ")

file = open('../data/text.txt', 'a') # "w" для записи "a" для добавления "r" для чтения

file.write(newData + "\n")

file.close()

file = open('../data/text.txt', 'r')
#print(file.read(10))
for stroka in file:
    print(stroka)
file.close()