
import random
number = random.randint(1, 100)
#print('комп загадал ', number)
select_level = None

user_number = None
count = 1
levels = {1: 3, 2: 5, 3: 10}
select_level = int(input('Выбери уровень сложности 1, 2 или 3: '))
while 1 > select_level or select_level > 3:
    select_level = int(input('Такого уровня нет, выбери 1, 2 или 3: '))

user_count = int(input('Введите количество игроков: '))
users = []

for user in range(user_count):
    name = input(f'Введите имя игрока № {user + 1}: ')
    users.append(name)
winner = False

while not winner:
    for user in users:
        print(f'Попытка №{count} для игрока {user}')
        user_number = int(input('Введите число: '))
        if user_number > number and not user_number < number:
            print('Загаданое число должно быть меньше')
        elif user_number < number and not user_number > number:
            print('Загаданое число больше')
        else:
            winner = True
            print(f'Поздравляем {user}, вы угадали!')
            break
    count += 1
    if count > levels[select_level]:
        print('Все попытки исчерпаны. Вы проиграли!!!')
        break