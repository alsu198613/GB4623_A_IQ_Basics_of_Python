# Задача No19. Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
# на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

data = [int(i) for i in input("Введите числа: ").split()]
steps = int(input("Введите количество сдвигов: "))
steps = steps % len(data)
data = [data[i - steps] for i in range(len(data))]
print(data)

# [10, 20, 30, 40, 50]
#  -5  -4  -3  -2  -1
# steps = 3
# [30, 40, 50, 10, 20]
#  -3  -2  -1  -5  -4

#2
data = [int(i) for i in input("Введите числа: ").split()]
steps = int(input("Введите количество сдвигов: "))
for i in range(steps):
    temp = data.pop()
    data.insert(0, temp)
print(data)