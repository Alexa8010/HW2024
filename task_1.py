
# 1. Треугольник существует только тогда, 
# когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. 
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника 
# с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, 
# равнобедренным или равносторонним.

a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

if a < b + c and b < a + c and c < a + b:
    print("Ура, такой треугольник существует!")
    
    if a != b and a != c and b != c:
        print("Этот треугольнык разносторонний")
    elif a == b and b == c:
        print("Этот треугольник равносторонний")
    else:
        print("Этот треугольник равнобедренный")
else:
    print("Такого треугольника не существует")




# 2. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
# 3. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)