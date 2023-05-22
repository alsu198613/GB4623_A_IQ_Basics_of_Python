# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = int(input("Введите трехзначное число: "))
sum = 0
temp_num = num
if num < 100 or num > 999:
    print("Вы ввели не трехзначное число")
else:
    while temp_num > 0:
        last_digit = temp_num % 10
        sum += last_digit
        temp_num //= 10
    print(f'Сумма цифр числа: {sum}')