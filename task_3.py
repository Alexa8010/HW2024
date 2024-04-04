# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)

for _ in range(10):
    guess = int(input("Введите вашу догадку: "))
    
    if guess < num:
        print("Больше")
    elif guess > num:
        print("Меньше")
    else:
        print("Поздравляем! Вы угадали число.")
        break

print(f"Загаданное число было: {num}")
