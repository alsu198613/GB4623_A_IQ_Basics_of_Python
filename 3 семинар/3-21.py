# data = [[1, -1.575], ['Hello world', True], [15, -7]]
# #            0                 1                2
# print(data[2][0])

data = {'Ivan': 27, 'Alexandr': 31, 'Konstantin': {'age': 21, 'hobby': ['tennis', 'football']}}
# вывести на экран слово 'tennis'
print(data['Konstantin']['hobby'][0])

# print(data.values())  # dict_values([27, 31, {'age': 21, 'hobby': ['tennis', 'football']}])
# print(data.keys())  # dict_keys(['Ivan', 'Alexandr', 'Konstantin'])

print(list(data.values()))  # [27, 31, {'age': 21, 'hobby': ['tennis', 'football']}]
print(list(data.keys()))  # ['Ivan', 'Alexandr', 'Konstantin']
print(list(data.items()))  # [('Ivan', 27), ('Alexandr', 31), ('Konstantin', {'age': 21, 'hobby': ['tennis', 'football']})]
for k, v in data.items():
    print(k, v)

# Ivan 27
# Alexandr 31
# Konstantin {'age': 21, 'hobby': ['tennis', 'football']}

# Задача No21. Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
           {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, 
           {"VIII": "S007"}]
result = set()
for key in data:
    for value in key:
        result.add(key[value])
print(result)  # {'S009', 'S002', 'S005', 'S001', 'S007'}