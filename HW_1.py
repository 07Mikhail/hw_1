# Задание_1

phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'

list_1 = list(phrase_1)
list_2 = list(phrase_2)

if len(list_1) == len(list_2):
	print('Фраза 1 равна фразе 2')
else: 
	if len(list_1) > len(list_2):
		print('Фраза 1 длиннее фразы 2')
	else: 
		print('Фраза 2 длиннее фразы 1')



# Задание_2

year = int(input('Введите год: '))
some_list = list(str(year))

year_2 = some_list[2] + some_list[3]
year_2 = int(year_2)

if year_2 % 4 == 0:
  print('Весокосный год')
else:
  print('Невесокосный год')



# Задание_3

month = str(input(('Введите месяц: ')))
month_2 = month.lower()
date_birth = int(input('Введите день: '))

if month_2 == 'январь':
  if date_birth < 19:
    print('Козерог')
  else:
    print('Водолей')  

elif month_2 == 'февраль':
  if date_birth < 18:
    print('Водолей')
  else:
    print('Рыбы')

elif month_2 == 'март':
  if date_birth < 20:
    print('Рыбы')
  else:
    print('Овен')

elif month_2 == 'апрель':
  if date_birth < 19:
    print('Овен')
  else:
    print('Телец')

elif month_2 == 'май':
  if date_birth < 20:
    print('Телец')
  else:
    print('Близнецы')

elif month_2 == 'июнь':
  if date_birth < 20:
    print('Близнецы')
  else:
    print('Рак')

elif month_2 == 'июль':
  if date_birth < 22:
    print('Рак')
  else:
    print('Лев')

elif month_2 == 'август':
  if date_birth < 22:
    print('Лев')
  else:
    print('Дева')

elif month_2 == 'сентябрь':
  if date_birth < 22:
    print('Дева')
  else:
    print('Весы')

elif month_2 == 'октябрь':
  if date_birth < 22:
    print('Весы')
  else:
    print('Скорпион')

elif month_2 == 'ноябрь':
  if date_birth < 21:
    print('Скорпион')
  else:
    print('Стрелец')

elif month_2 == 'декабрь':
  if date_birth < 29:
    print('Стрелец')
  else:
    print('Козерог')



# Задание_4

width = int(input('Введи ширину, см: '))
lengh = int(input('Введи длину, см: '))
height = int(input('Введи высоту, см: '))

if lengh > 200:
	print('Упаковка для лыж')
else:
	if (50 > width > 15)  or (50 > lengh > 15) or (50 > height > 15):
		print('Коробка №2')
	elif (width and lengh and height) < 15:
		print('Коробка №1')
	else:
		print('Стандартная коробка #3')



# Задание_5

number = 123456

count_1 = 0
count_2 = 0

some_list = list(str(number))

for i in some_list[0:3]:
	count_1 = count_1 + int(i)
for x in some_list[3:]:
	count_2 = count_2 + int(x)

if(count_1 > count_2) or (count_2 > count_1):
	print('Несчастливый билет')
else:
	print('Счастливый билет')



# Задание_6

type_ = input('Введите тип фигуры: ')
type_2 = type_.lower()

if type_2 == 'круг':
  r_ = int(input('Введите радиус: '))
  s_circle = 3.14 * r_ ** 2
  print('Площадь круга: ', s_circle)
elif type_2 == 'треугольник':
  A = int(input('Введите длину стороны A: '))
  B = int(input('Введите длину стороны B: '))
  C = int(input('Введите длину стороны C: '))
  h = (A + B + C) / 2
  s_triangle = (h * (h - A) * (h - B) * (h - C)) ** 0.5
  print('Площадь треугольника: ', s_triangle)
elif type_2 == 'приямоугольник':
  a = int(input('Введите длину стороны a: '))
  b = int(input('Введите длину стороны b: '))
  s_rectangle = a * b
  print('Площадь приямоугольника: ', s_rectangle)