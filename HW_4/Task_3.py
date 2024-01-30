'''
Возьмите задачу о банкомате из семинара 2.
Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
'''

import decimal

decimal.getcontext().prec = 2
MULTIPLICITY = 50
PERCENT = decimal.Decimal(15) / decimal.Decimal(1000)
PERCENT_BONUS = decimal.Decimal(3) / decimal.Decimal(100)
COUNT_PERC = 3
MIN_LIMIT = decimal.Decimal(30)
MAX_LIMIT = decimal.Decimal(600)
PERCENT_RICHNESS = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_AMOUNT = 5_000_000
CMD_DEPOSIT = "1"
CMD_WITHDRAW = "2"
CMD_EXIT = "3"


def deposit(amount: int, balance: int) -> int:
    balance += amount
    all_amount.append(amount)
    return balance


def withdraw(amount: int, comission: int, balance: int) -> int:
    withdraw_sum = amount + comission
    balance -= withdraw_sum
    all_amount.append(-int(withdraw_sum))
    return balance


def comissions(amount: int) -> int:
    comis = amount * PERCENT
    if comis < MIN_LIMIT:
        comis = MIN_LIMIT
    elif comis > MAX_LIMIT:
        comis = MAX_LIMIT
    return int(comis)


def bonus(balance: int) -> int:
    bonus_sum = balance * PERCENT_BONUS
    return int(bonus_sum)


def percent_richness(balance: int) -> int:
    sum_percent = balance * PERCENT_RICHNESS
    return int(sum_percent)


balance = 0
operations = 0
all_amount = []

while True:
    action = input(
        f"пополнить-{CMD_DEPOSIT}\n"
        f"снять-{CMD_WITHDRAW}\n"
        f"выход-{CMD_EXIT}\n"
        f"Введите действие:  "
    )
    if balance > RICHNESS_AMOUNT and action != "3":
        sum_percent = percent_richness(balance)
        balance -= sum_percent
        print(f"Вычтен налог на богатство в размере {sum_percent:.0f}")
        print(f"Текущий баланс {balance:.0f}")
    if action == "1" or action == "2":
        amount = 1
        while amount % MULTIPLICITY != 0:
            amount = int(input(f"Введите сумму кратную {MULTIPLICITY}: "))
        if action == "1":
            operations += 1
            balance = deposit(amount, balance)
            # print(f"Текущий баланс {balance}")
        else:
            comission = comissions(amount)
            if comission + amount > balance:
                print("На балансе недостаточно средств")
            else:
                operations += 1
                balance = withdraw(amount, comission, balance)
            print(f"Сумма снятия {amount}, комиссия {comission}, общая сумма {amount + comission:.0f}")
            # print(f"Текущий баланс {balance}")
        if operations % COUNT_PERC == 0:
            bonus_sum = bonus(balance)
            balance += bonus_sum
            print(f"Сумма бонуса {bonus_sum:.0f}")
            # print(f"Текущий баланс {balance}")
        print(f"Текущий баланс {balance:.0f}")
        print(all_amount)
    elif action == "3":
        break
    else:
        print("Введена неверная команда")
