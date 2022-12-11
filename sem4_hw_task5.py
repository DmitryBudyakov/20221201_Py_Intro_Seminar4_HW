# Задача 5
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9

from sem4_hw_task4_func import *
from sympy import simplify
import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')


# сумирование 2-х полиномов
def sum_of_polynoms(poly1: str, poly2: str) -> str:
    sum_of_poly = simplify(poly1 + ' + ' + poly2)
    return str(sum_of_poly)

title = 'Запись суммы 2-х многочленов в файл'
print('-'*len(title))
print(title)
print('-'*len(title))

############
# ПОДГОТОВКА
############
# создание полиномов и запись их в файлы
filename1 = 'file1.txt'
filename2 = 'file2.txt'
file_sum = 'file_sum.txt'

# создание полиномов
n1 = int(input('Введите степень многочлена 1: '))
polynom1 = create_polynom(get_indexes(n1))
# print(polynom1)

n2 = int(input('Введите степень многочлена 2: '))
polynom2 = create_polynom(get_indexes(n2))
# print(polynom2)
print()

# запись в файл
write_to_file(polynom1, filename1)
write_to_file(polynom2, filename2)


#################
# ОСНОВНАЯ ЧАСТЬ
#################
# чтение из файлов
poly1 = read_fm_file(filename1, 1)
print(f'многочлен 1: {poly1}')
poly2 = read_fm_file(filename2, 1)
print(f'многочлен 2: {poly2}')
print()

# сумма полиномов
sum_of_poly = sum_of_polynoms(poly1, poly2)
# print(f'сумма многочленов: {sum_of_poly}')

# запись результата в новый файл:
write_to_file(sum_of_poly, file_sum, 1)

# чтение из файла:
sum_of_poly_from_file = read_fm_file(file_sum, 1)
print(f'сумма многочленов из файла: {sum_of_poly_from_file}')
