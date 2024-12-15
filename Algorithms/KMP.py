a = 'lililali'
#Массив pi заполнели нулями
pi = [0] * len(a)
# pi = [0, 0. 0, 0, 0, 0]

j = 0
i = 1
while i < len(a):           #Первым сразу записывается [0]
    if a[j] == a[i]:        #1-ая итерация (j!=i)(l!=l), j==0, pi[1]=0, теперь i=2 записывается [0]
        pi[i] = j + 1       #2-ая итерация (j==i)(l==l), pi[2]=0+1=1, теперь i=3,j=1 записывается [1]
        j += 1              #3-ая итерация (j==i)(i==i), pi[3]=1+1=2, теперь i=4,j=2 записывается [2]
        i += 1              #4-ая итерация (j==i)(l==l), pi[4]=2+1=3, теперь i=5,j=3 записывается [3]
    else:                   #5-ая итерация (j!=i)(i!=a), j=pi[3-1], теперь i=5,j=2 записывается [0]
        if j == 0:
            pi[i] = 0
            i += 1
        else:
            j = pi[j - 1]

print(pi)

# ar = 'lililali'
# pe = [0] * len(ar)
# x = 0        # j
# y = 1        # i
# while y < len(ar):
#     if ar[x] != ar[y]:
#         if x == 0:
#             pe[y] = 0
#             y += 1
#         else:
#             x = pe[x - 1]
#             print(pe[x])
#     else:
#         pe[y] = x + 1
#         x += 1
#         y += 1
# print(pe)

# text = 'lalolilula llililo lalililali'
# a = 'lililali'
# tx = len(text)
# ax = len(a)
# j = 0
# i = 0
# pi = [0] * ax
# while i < tx:
#     if a[j] == text[i]:
#         i += 1
#         j += 1
#         if j == ax:
#             print("Слово найдено")
#             break
#     else:
#         if j > 0:
#             j = pi[j - 1]
#         else:
#             i += 1
#     if i == tx:
#         print("Слова здесь нет!")

text = "ararsarrararrrararrarararsrsrararsararsrrsar"
word = "sara"

length_all_text = len(text)
length_word = len(word)
i_text = 0
i_word = 0
while i_text < length_all_text:
    if text[i_text] == word[i_word]:
        i_text += 1
        i_word += 1
        if i_word == length_word:
            print("Found word")
            break
    else:
        if i_word > 0:
            i_word = 0
        else:
            i_text += 1
if i_text == length_all_text:
    print("Word is not found")