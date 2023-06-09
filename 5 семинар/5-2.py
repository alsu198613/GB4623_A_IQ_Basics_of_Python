# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.  
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные. 
# Input: 5 -> 1 3 3 3 4 
# Output: 1 3 3 3 1 
 
n = int(input()) 
numbers = [int(i) for i in input().split()][:n] 
new_numbers = [sorted(numbers)[0] if n == sorted(numbers)[-1] else n for n in numbers] 
print(new_numbers)