# Задача 1
# Вычислить число Пи c заданной точностью d.
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.0001, π = 3.1415

import math
import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
    
title = 'Число Пи c заданной точностью d'
print('-'*len(title))
print(title)
print('-'*len(title))

# точность
# d = '0.000001'
d = input('Введите точность числа Пи [напр: 0.001]: ')
print(f'число Пи: {math.pi}')

fraction_length = len(d.split('.')[1])
dot_id = str(math.pi).index('.')
sliced_num = str(math.pi)[:dot_id + fraction_length + 1]

print(f'при d = {d} -> {sliced_num}')
