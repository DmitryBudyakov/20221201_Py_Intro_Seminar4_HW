# Задача 4
# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x**2 + 4*x + 5 = 0 или x**2 + 5 = 0 или 10*x**2 = 0
# k=3 => 2*x**3 + 4*x**2 + 4*x + 5 = 0

from sem4_hw_task4_func import *
import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
    
title = 'Формирование многочлена степени k и запись его в файл.'
print('-'*len(title))
print(title)
print('-'*len(title))

n = int(input('Степень многочлена: '))
filename = 'file.txt'

res_polynom = create_polynom(get_indexes(n))
# print(res_polynom)

# запись в файл
write_to_file(res_polynom, filename, 1)

# чтение из файла
polynom = read_fm_file(filename)
print(f'многочлен из файла: {polynom}')
