#Игра царство драконов
import random
print('Здравствуй незнакомец.')

name = input(' Как тебя зовут? ')
print(name + ' ты попал в подземелье дракона и за каждым поворотом тебя может ждать чудовище.')
print('Но если у тебя получится выйти из логова ты получишь сокровище дракона!')
def choice():
    door = ''
    while door != '1' and door != '2':
        print('И так перед тобой 2 пещеры в какую ты пойдёшь: ')
        door = input('В 1-ую или во 2-ую, введи цифру: ')
    return door

def covernumb(cover):
    numb = random.randint(1, 2)
    numb = str(numb)

    if cover == numb:
        print("Тебе повезло, в этой пещере не оказалось дракона")
    else:
        print("Ты встрелил голодного дракона и он проглотил тебя")

playAgain = 'да'

while playAgain=='да' or playAgain =='д':
    cover = choice()
    print('Ты выбрал пещеру - ', cover)
    covernumb(cover)
    playAgain = input('Попробуешь ещё раз, (да или нет): ')








