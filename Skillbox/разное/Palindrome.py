# text = input("Введите слово, к примеру 'довод': ")
# reverse_text = ""
# print("Оригинал слова: {}".format(text))
# for letter in text:
#     reverse_text = letter + reverse_text
# if text == reverse_text:
#     print("Это палиндром = '{}'".format(text))
# else:
#     print("Это не палиндром '{}'".format(text))
# print()
# reverse_text_2 = text[::-1]
# print("Слово наоборот: {}".format(reverse_text_2))
# if text == reverse_text_2:
#     print("Это палиндром = '{}'".format(text))
# else:
#     print("Это не палиндром '{}'".format(text))


text = input('Введите текст: ').lower().strip()
count = 1
text_dict = dict()
for letter in text:

    if letter in text_dict:
        text_dict[letter] += count
    else:
        text_dict[letter] = count
print(text_dict)

odd_count = 0
for i_value in text_dict.values():
    if i_value % 2 != 0:
        odd_count += 1

if odd_count > 1:
    print("Нельзя сделать палиндромом")
else:
    print("Можно сделать палиндромом")

# aaabb         aaabbaaa
# a = 3         a = 6
# b = 2         b = 2