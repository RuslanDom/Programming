summa = 1000000

def one_deposit(summa):
    for _ in range(2):
        summa = round(summa + (summa * 0.21 / 12))
    return summa

def counter(deposit):
    start_sum = deposit
    print(f"Начальная сумма вклада: {start_sum} руб")
    for _ in range(6):
        deposit = one_deposit(deposit)
    print(f"Сумма на вкладе через год без вычета налога: {deposit} руб")
    if (deposit - start_sum) > 210000:
        print("Эта сумма облагается налогом")
        saldo = deposit - start_sum
        tax = (saldo - 210000) * 0.13
        print(f"Налог составит: {round(tax)}\nДоход чистый: {round(saldo - tax)} руб")
        result = saldo - tax + start_sum
    else:
        print("Эта сумма не облагается налогом")
        result = deposit
    return f"С вычетом налогов конечная сумма на вкладе составит: {round(result)} руб"


res = counter(summa)
print(res)