# Задача № 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, 
# а для тещи полегче. Но вот незадача: арбузов слишком 
# много и он не знает как же выбрать самый легкий и самый 
# тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. 
# Вторая строка содержит N чисел, записанных на новой строчке 
# каждое. Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

n = int(input("Введите количество арбузов: "))
masses = []
for i in range(n):
    mass = int(input("Введите массу арбуза: "))
    masses.append(mass)

min_mass = min(masses)
max_mass = max(masses)

print("Самый легкий арбуз:", min_mass)
print("Самый тяжелый арбуз:", max_mass)

# 2
n = int(input("Введите количество арбузов: "))
# 1 <= n <= 1000
max_weight = 0
min_weight = 1000
for i in range(n):
    weight = int(input("Введите массу арбуза: "))
    if weight > max_weight:
        max_weight = weight
    if weight < min_weight:
        min_weight = weight

print(f"Самый легкий арбуз: {min_weight} кг, Самый тяжелый арбуз: {max_weight} кг")
     
