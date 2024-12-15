try:
    num = int(input('Enter num: '))
    num += 10
    print(num)
except ValueError:
    print("Нужно ввести только цифры!!!")
finally:
    print("Finally в любом случае будет выполнена")

try:
    file = open("../data/text_2.txt", "w")
    file.write("Hello my friend")
    number = int(input("Enter text: "))
    file.write(number)
    text = str(number)
    file.write(number)
    print(file)
    file.close()
except TypeError:
    print("Нельзя записывать цифры!!!")
    file.close()
else:
    print("Если выполнится блок try, то сработает else")

# with....as

# try:
#     file_2 = open('data/text_2.txt')
#     file_2.read()
#     file_2.close()
# except FileNotFoundError:
#     print("Этот файл не найден")

try:
    with open("data/text_3.txt",'r',encoding="utf-8") as file_2:
        print(file_2.read())
except FileNotFoundError:
    print("File not found")