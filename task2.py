# Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input('Введите трехзначное число: '))
if number >= 100 and number < 1000:
    result = (number // 100) + ((number % 100) // 10) + (number % 10)
    print(result)
else:
    print('Число не трехзначное')