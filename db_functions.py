import sqlite3
from random import randint

conn = sqlite3.connect('db_cards.sql')
cursor = conn.cursor()

def db_creation():
    global conn, cursor

    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS Cards (card_number INTEGER, name TEXT NOT NULL, password INTEGER(4), money INTEGER)''')
    conn.commit()
    







def create_card_number(card_number):
    check_for = cursor.execute('''SELECT card_number FROM Cards ''')
    while True:
        if card_number in check_for:
            card_number == randint(8600000000000000, 8600999999999999)
            
        else:
            break
    return card_number

def card_addition1(name1, card_password):
    card_number = randint(8600000000000000, 8600999999999999)
    create_card_number(card_number)
    global conn, cursor

    cursor.execute('''INSERT INTO Cards (card_number, name, password, money) VALUES (?,?,?,?)''', (card_number, name1, card_password, 0))
    conn.commit()







def card_delete():
    global cursor, conn
    
    last_4 = input('Введите последние 4 цыфры карты >>>')
    found_card_number = None
    cursor.execute("SELECT card_number FROM Cards")
    cards = cursor.fetchall()
    for number in cards:
        number2 = number[0]
        if number2 % 10000 == int(last_4):
            found_card_number = number2
            break
    else:
        print("\n\nКарта не найдена...\n\n")
            

    

        
    password = int(input("Введите пароль карты >>> "))
    cursor.execute("SELECT password FROM Cards WHERE card_number = ?", (found_card_number,))
    tuple = cursor.fetchone()
    if tuple:
        check_password = tuple[0]
        if password == check_password:
            cursor.execute("DELETE FROM Cards WHERE card_number = ?", (found_card_number,))
            print("\n\nУдаленно успешно\n\n")
            conn.commit()
            return
        else:
            print("\n\nНе верный пароль\n\n")
            return
    else:
        print("\n\nКарта не найдена\n\n")
        return
            
            
        
        
    

        


def check_amount():
    global conn, cursor
    last_4 = input('Введите последние 4 цыфры карты >>>')
    if last_4.isdigit() and len(last_4) == 4:
        last_4 = int(last_4)
        
    else:
        print("Введиет последние 4 цыфры номера карты !!! ")
        return
    found_card_number = None
    cursor.execute("SELECT card_number FROM Cards")
    cards = cursor.fetchall()
    for number in cards:
        number2 = number[0]
        if number2 % 10000 == int(last_4):
            found_card_number = number2
            break
    else:
        print("\n\nКарта не найдена...\n\n")
            
    cursor.execute("SELECT * FROM Cards WHERE card_number = ?", (found_card_number,))
    balance = cursor.fetchone()
    if balance:
        print(f'\n\nБаланс : {balance[3]}$\n\n')
    else:
        print("\n\nКарта не найдена\n\n")
    
    
    
    

    


def cash():
    global conn, cursor
    last_4 = input('Введите последние 4 цыфры карты >>>')
    if last_4.isdigit() and len(last_4) == 4:
        last_4 = int(last_4)
        
    else:
        print("Введиет последние 4 цыфры номера карты!!! ")
        return
    found_card_number = None
    cursor.execute("SELECT card_number FROM Cards")
    cards = cursor.fetchall()
    for number in cards:
        number2 = number[0]
        if number2 % 10000 == int(last_4):
            found_card_number = number2
            break
    else:
        print("\n\nКарта не найдена...\n\n")
    
    password = int(input("Введите пароль карты >>> "))
    cursor.execute("SELECT password FROM Cards WHERE card_number = ?", (found_card_number,))
    tuple = cursor.fetchone()
    if tuple:
        check_password = tuple[0]
        if password == check_password:
            pass
        else:
            print("\n\nНе верный пароль\n\n")
            return
    
    cursor.execute('''SELECT * FROM Cards WHERE card_number = ?''', (found_card_number,))
    balance = cursor.fetchone()
    fact_balance = balance[3]
    
    cashh = input("Введите сумму вывода >>> ")
    as_int = int(cashh)
    
    if fact_balance < as_int:
        print("\n\nНедостаточео средств\n\n")
    else:
        result = fact_balance - as_int
        cursor.execute('''UPDATE Cards SET money = ? WHERE card_number = ?''', (result, found_card_number,))
        print("\n\nВывод прошел успешно\n\n")
    conn.commit()
    return
    
    
    
    
    
    
    


def fill():
    global conn, cursor
    last_4 = input('Введите последние 4 цыфры карты >>>')
    if last_4.isdigit() and len(last_4) == 4:
        last_4 = int(last_4)
        
    else:
        print("Введиет последние 4 цыфры номера карты!!! ")
        return
    found_card_number = None
    cursor.execute("SELECT card_number FROM Cards")
    cards = cursor.fetchall()
    for number in cards:
        number2 = number[0]
        if number2 % 10000 == int(last_4):
            found_card_number = number2
            break
    else:
        print("\n\nКарта не найдена...\n\n")
    
    password = int(input("Введите пароль карты >>> "))
    cursor.execute("SELECT password FROM Cards WHERE card_number = ?", (found_card_number,))
    tuple = cursor.fetchone()
    if tuple:
        check_password = tuple[0]
        if password == check_password:
            pass
        else:
            print("\n\nНе верный пароль\n\n")
            return
    
    cashh = input("Введите сумму пополнения >>> ")
    as_int = int(cashh)
    cursor.execute('''SELECT * FROM Cards WHERE card_number = ?''', (found_card_number,))
    balance = cursor.fetchone()
    fact_balance = balance[3]
    result = fact_balance + as_int
    cursor.execute('''UPDATE Cards SET money = ? WHERE card_number = ?''', (result, found_card_number,))
    conn.commit()
    
    print("\n\nПополнение прошло успешно\n\n")
    return
   
   
   
   
   

def send():
    global conn, cursor
    try:
        card_from = int(input("Введите номер карты отправителя >>> "))
    except ValueError:
        print("Ошибка: введите корректное число ")
        exit(1)
        
    found_card_number1 = None
    
    cursor.execute("SELECT * FROM Cards")
    cards = cursor.fetchall()
    
    for number in cards:
        if card_from == number[0]:
            found_card_number1 = number[0]
            break 
        
    else:
        print("\n\nКарта не найдена...\n\n")
        
    
    password = int(input("Введите пароль >>> "))
    cursor.execute('''SELECT password FROM Cards WHERE card_number = ?''', (found_card_number1,))
    tuple = cursor.fetchone()
    if tuple:
        check_password = tuple[0]
        if password == check_password:
            pass
        else:
            print("\n\nНе верный пароль\n\n")
            return
    
    
    try:
        card_to = int(input("Введите номер карты получателя >>> "))
    except ValueError:
        print("Ошибка: введите корректное число ")
        exit(1)
        
    found_card_number2 = None
    
    cursor.execute("SELECT * FROM Cards")
    recipient = cursor.fetchall()
    
    for number2 in recipient:
        if card_to == number2[0]:
            found_card_number2 = number2[0]
             
            break 
        
    else:
        print("\n\nКарта не найдена...\n\n")
    
    money_to_transfer = input("Введите сумму перевода >>> ")
    
    cursor.execute('''SELECT * FROM Cards WHERE card_number = ?''', (found_card_number1,))
    balance = cursor.fetchone()
    fact_balance1 = balance[3]
    as_int = int(money_to_transfer)
    
    cursor.execute('''SELECT * FROM Cards WHERE card_number = ?''', (found_card_number2,))
    balance2 = cursor.fetchone()
    fact_balance2 = balance2[3]
    
    if fact_balance1 < as_int:
        print("\n\nНедостаточео средств\n\n")
        return
    else:
        result = fact_balance1 - as_int
        cursor.execute('''UPDATE Cards SET money = ? WHERE card_number = ?''', (result, found_card_number1,))
        
        result2 = fact_balance2 + as_int
        cursor.execute('''UPDATE Cards SET money = ? WHERE card_number = ?''', (result2, found_card_number2,))
        conn.commit()
        print("\n\nПеревод прошел успешно\n\n")
    
    
    
    
    

def cards_list():
    global conn, cursor 
    
    cursor.execute("SELECT * FROM Cards")
    cards = cursor.fetchall()
    
    info = ''
    order = 1 
    for element in cards:
        info += f'\n___{order}___\n\nНомер карты : {element[0]}\n\nИмя : {element[1]}\n\nБаланс : {element[3]}\n\n'
        order += 1
    print(info)

    

