# Задание_1

'''
делим на 2 - находим длину половины слова, целочисленным делением находим порядковый номер символа (срез начинается с 0)
'''

word = 'testwee'
if len(word) % 2 != 0:
  print(word[int(len(word)//2)])
else:
  print((word[int(len(word)//2)-1])+(word[int(len(word)//2)]))



# Задание_2

user_input = int(input('Введи число: '))
count = 0

while user_input != 0:
  count = count + user_input
  user_input = int(input('Введи число: '))
print(count)




# Задание_3

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

boys.sort() 
girls.sort()

if len(boys) != len(girls):
  print('Внимание, кто-то может остаться без пары!')
else:
  list_zip = list(zip(boys, girls))
  for b, g in list_zip:
    print(b, g)




# Задание_4

countries_temperature = [
['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
['Germany', [57.2, 55.4, 59, 59, 53.6]],
['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]

count_Thailand = 0
count_Germany = 0
count_Russia = 0
count_Poland = 0

T = 37.78

for count in countries_temperature[0][1]:
  count_Thailand = count_Thailand + count
for count in countries_temperature[1][1]:
  count_Germany = count_Germany + count
for count in countries_temperature[2][1]:
  count_Russia = count_Russia + count
for count in countries_temperature[3][1]:
  count_Poland = count_Poland + count

print('Средняя температура в странах:')
print(f'Thailand: {round(((count_Thailand/ len(countries_temperature[0][1])) * T / 100), 1)}')
print(f'Germany: {round(((count_Germany/ len(countries_temperature[1][1])) * T / 100), 1)}')
print(f'Russia: {round(((count_Russia/ len(countries_temperature[2][1])) * T / 100), 1)}')
print(f'Poland: {round(((count_Poland/ len(countries_temperature[3][1])) * T / 100), 1)}')



# Задание_6

'''
1. С помощью генератора собираем список чисел
2. Создаём новый список, в него дальше будем добавлять числа из генерируемого списка
3. Итерируемся по первому списку, условием проверяем кол-во переменных (если > 1, то добавляем переменную в новый список из пункта 2)
4. Выводим уникальные значения в множестве
'''

user_input = [int(i) for i in input('Введи числа через пробел: ').split()]

new_user_list = []

for target_i in user_input:
  if user_input.count(target_i) > 1:
    new_user_list.append(target_i)

set_new = set(new_user_list)

print(set_new)



