# Задача №39. Даны два массива чисел. Требуется вывести 
# те элементы первого массива (в том порядке, в каком они 
# идут в первом массиве), которых нет во втором массиве. 
# Пользователь вводит  число N - количество элементов в первом 
# массиве, затем N чисел - элементы массива. Затем число M - 
# количество элементов во втором массиве. Затем элементы второго массива
# Ввод: 					Вывод:
# 7					        3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

n = int(input('Введите число элементов первого списка: '))
list_1 = [int(i) for i in input().split()]
m = int(input('Введите число элементов второго списка: '))
list_2 = [int(i) for i in input().split()]
for elem in list_1:
    if elem not in list_2:
        print(elem, end=' ')

# 2 list comprehensions
# print([x for x in list_1 if x not in list_2])

# 3 множества (только для уникальных значений)
# list_1 = set([int(i) for i in input().split()])
# m = int(input('Введите число элементов второго списка: '))
# list_2 = set([int(i) for i in input().split()])
# print(list_1 - list_2)
