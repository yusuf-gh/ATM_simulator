
from db_functions import *

print("\n\nДобро пожаловать в симулятор банкомата))))\n\n Выберите действие...")



db_creation()



def operations():
    while True:
        print("Личный кабинет...\n\n 1: Проверить средства\n2: Обналичка\n3: Добавление средств\n4: Переводы\n5: Назад ")
        action1 = int(input(">>> "))
        if action1 == 1:
            check_amount()
        elif action1 == 2:
            cash()
        elif action1 == 3:
            fill()
        elif action1 == 4:
            send()
        elif action1 == 5:
            actions()
        else:
            print("Выберите предоставленные варианты...")
            
            
            


def card_addition():
    name = input('Enter your full name, which will display at your card data >>> ')
    password = int(input("Enter the password of your card >>> "))
    card_addition1(name, password)

    




def actions():
    while True:
        print("1: Личный кабинет\n2: Удалить карту\n3: Добавить карту\n4: Список карт\n5: Выйти...")
        try:
            action = int(input(" >>> "))
        except ValueError:
            print("Ошибка: Выберите предоставленные варианты... ")
            exit(1)
        
        match action:

            case 1:
                operations()
            case 2:
                card_delete()
            case 3:
                card_addition()
            case 4:
                cards_list()
            case 5:
                print("\n\nХорошего дня!\n\n")
                break
            case _:
                print("Выберите предоставленные варианты...")
    return
                
actions()