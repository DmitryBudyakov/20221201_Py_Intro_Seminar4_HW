# Задача 3
# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint
import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
    
title = 'Список неповторяющихся элементов исходной последовательности'
print('-'*len(title))
print(title)
print('-'*len(title))


def create_randint_list(nums: int) -> list:
    min_num = 0
    max_num = 10
    initial_list = [randint(min_num, max_num) for i in range(nums)]
    initial_list.sort()
    return initial_list

# n = int(input('Введите кол-во чисел в исходном списке: '))
n = 10
print(f'длина списка: {n}')

init_list = create_randint_list(n)
list_of_uniq = list(set(init_list))

print(f'Исходная последовательность:\t {init_list}')
print(f'Неповторяющиеся элементы:\t {list_of_uniq}')
