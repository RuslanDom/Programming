from random import randint
balance = 1000
try:
    while balance > 0:
        print(f'Количество депозита: {balance}')
        cash = int(input("Введите ставку: "))
        play = True
        if cash > 0 and cash <= balance:
            add_cash = 0
            balance -= cash
            cube_player = randint(1, 6)
            cube_computer = randint(1, 6)
            print(f'Кубик игрока: {cube_player}\nКубик компьютера: {cube_computer}')
            while play:

                if cube_player > cube_computer:
                    balance += cash * 2
                    print(f'Выиграл игрок! Ставка: {cash} Баланс: {balance}')
                    break
                elif cube_computer > cube_player:
                    print(f'Вы проиграли! Ставка: {cash} Баланс: {balance}')
                    break
                else:
                    print(f'Выпало одинаковое значение. Хотите добавить ставку? Ваш баланс: {balance}')
                    add_cash = int(input('Введите сумму которую хотите добавить к предыдущей ставке: '))
                    if add_cash >= 0 and add_cash <= balance:
                        balance -= add_cash
                        cash += add_cash
                        cube_player = randint(1, 6)
                        cube_computer = randint(1, 6)
                        print(f'Кубик игрока: {cube_player}\nКубик компьютера: {cube_computer}')
                    else:
                        print("У вас недостаточно средств для ставки! Или вы ввели некорректное число")

        else:
            print('Ставка должна быть больше 0 и не превышать количество вашего депозита!')

    print("Вы проиграли все деньги!")
except ValueError:
    print("Вводите только числа!\nПопробуйте начать игру заново!")