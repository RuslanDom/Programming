from random import randint


def rock_paper_scissors():
    list_objects = ["камень", "ножницы", "бумага"]
    game = 1
    while game == 1:
        COM = randint(0, 2)
        COM_choice = list_objects[COM]
        Player = int(input("Выберите 0 - камень, 1 - ножницы или 2 - бумагу: "))
        print()
        if Player == 0 or Player == 1 or Player == 2:
            Player_choice = list_objects[Player]
            if Player == COM:
                print(f'Игрок: {Player_choice}\t Компьютер: {COM_choice}\t Это ничья')
            elif (Player == 0 and COM == 1) or (Player == 1 and COM == 2) or (Player == 2 and COM == 0):
                print(f'Игрок: {Player_choice}\t Компьютер: {COM_choice}\t Победил игрок!')
            elif (Player == 0 and COM == 2) or (Player == 1 and COM == 0) or (Player == 2 and COM == 1):
                print(f'Игрок: {Player_choice}\t Компьютер: {COM_choice}\t Победил компьютер!')

        else:
            print("Вводите только корректные данные!")
        print()
        game = int(input("Нажмите 1 - чтобы попробовать ещё раз, в противном случае игра завершиться! "))
    mainMenu()


def guess_the_number():
    game = 1
    bank = 1000
    while game == 1:
        if bank > 0:
            COM_number = randint(1, 10)
            print(f'Банк: {bank}. Стоимость одной попытки 100 рублей')
            Player_number = int(input("Выберите число от 1 до 10: "))
            print()
            bank -= 100
            if Player_number == COM_number:
                bank += 1000
                print(f'Вы угадали число и выграли 1000 рублей!!! Теперь у вас {bank} рублей')

            else:
                print(f'К сожалению неверное число, загаданное число было {COM_number}\nПопробуйте ещё раз!')
            print()
            game = int(input("Нажмите 1 - чтобы попробовать ещё раз, в противном случае игра завершиться! "))
        else:
            print(f'На васшем счету недостаточно средств для игры {bank} рублей')
            break
    mainMenu()


def mainMenu():
    while True:
        choice = int(
            input("Выберите игру: 1 - 'Камень, ножницы, бумага'; 2 - 'Угадай число'; 3 - Выйти из главного меню:  "))
        if choice == 1:
            rock_paper_scissors()
            break
        elif choice == 2:
            guess_the_number()
            break
        elif choice == 3:
            break
        else:
            print("Выбирайте только по указанному в меню!")


mainMenu()
