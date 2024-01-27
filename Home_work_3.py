print('Hello, Lena')
print('Hello, Git!')


#Task1
# import datetime as dt

# def my_date(some_date):
#     current = dt.datetime.today()
#     some_date_dt = dt.datetime.strptime(some_date,"%Y-%m-%d")
#     result_dniv = current - some_date_dt
#     print(result_dniv.days)

# my_date('2025-10-09')

#Task2

# import random


# def get_numbers_ticket(min, max, quantity):
#     lottery_numbers = []
#     for i in range(quantity):
#         if min>0 and max<1001:
#             lottery_numbers.append(random.randint(min, max))
            
#         else:    
#             print("Введіть числа від 1 до 1000")
#     lottery_numbers.sort()
#     return lottery_numbers


# result = get_numbers_ticket(1,49,6) 

# print("Ваші лотерейні числа:", result)
  

#Task 3
import re

# pattern = r"^\+380\d{9}$"
# str = r"+380672251695"
# a = re.findall(pattern,str)
# print(a)

# def normalize_phone(phone_number):
    
     
    
#     a = re.sub( "[^\+\d]", '', phone_number)
#     print(a)  

#     b =list(a)
#     if b[0]!='+':
#         b.insert(0,'+')
#     else:
#         True 
#     if b[1]!=3:
#         b.insert(1,3) 
#     else:
#         True
#     if b[2]!=8:
#         b.insert(2,8) 
#     else:
#         True       
    
#     a=(''.join(map(str, b)))
#     print(a) 

#     if len(a)>13:
#         print("Довжина номеру перевищена. Будуть враховані перші 12 цифр")
#         a = a[0:13]
#     else:
#         True

#     print(a)


# normalize_phone("%$^0672er2516955690876453")

#Task 4


import datetime as dt
from datetime import datetime as dtdt

def get_upcoming_birthdays(users):
    current_date = dtdt.today().date()

    congrats_list=[]

    for user in users:
        name = user["name"]
        user_birthday = dtdt.strptime(user.get('birthday'), '%Y.%m.%d').date()
        user_birthday = ('2024'+'.%m.%d')
    print(user_birthday)
    
# from datetime import datetime, timedelta

# def get_upcoming_birthdays(users):
#     upcoming_birthdays = []

#     # Поточна дата
#     current_date = datetime.now()

#     for user in users:
#         name = user['name']
#         birthday = datetime.strptime(user['birthday'], '%Y.%m.%d')

#         # Визначаємо різницю в датах
#         time_until_birthday = birthday - current_date

#         # Перевіряємо, чи день народження випадає вперед на 7 днів включаючи поточний день
#         if 0 <= time_until_birthday.days <= 7:
#             congratulation_date = birthday

#             # Перенесення дати привітання на наступний робочий день, якщо вона випадає на вихідний
#             if congratulation_date.weekday() >= 5:  # 5 і 6 - це субота та неділя
#                 days_until_monday = 7 - congratulation_date.weekday()
#                 congratulation_date += timedelta(days=days_until_monday)

#             # Додавання інформації про користувача та дату привітання до списку
#             upcoming_birthdays.append({'name': name, 'congratulation_date': congratulation_date.strftime('%Y.%m.%d')})

#     return upcoming_birthdays



users = [
    {"name":"Olena Petrenko", "birthday": "1985.01.31"},
    {"name": "Petro Vulkan", "birthday": "1990.02.03"},
    {"name": "Stepan Bandera", "birthday": "1910.01.27"}
]

result = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", )