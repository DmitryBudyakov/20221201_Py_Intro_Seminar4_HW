# Задача 2
# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# 6 -> [1,2,3]  
# 144 -> [2,3]

import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
    
title = 'Список простых множителей числа N'
print('-'*len(title))
print(title)
print('-'*len(title))


def get_simple_divs(num: int, uniq: int = 0) -> list:
    """ Получение простых множителей числа \n
        при uniq = 1 выводятся только уникальные множители
    """
    div = 2
    divs = []
    while div**2 <= num:
        if num % div == 0:
            num //= div
            divs.append(div)
        else:
            div += 1
    if num != 1:
        divs.append(num)
    
    if uniq == 1:   # вывод уникальных множителей
        divs = list(set(divs))
    
    return divs
    
n = int(input('Введите натуральное число N: '))
n_orig = n

simple_divs = get_simple_divs(n)
uniq_divs = get_simple_divs(n, 1)

print(f'все множители:\t {n_orig} -> {simple_divs}')
print(f'уникальные:\t {n_orig} -> {uniq_divs}')
    