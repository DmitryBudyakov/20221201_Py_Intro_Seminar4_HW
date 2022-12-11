from random import randint

# создание индексов для полинома
def get_indexes(degree: int) -> list:
    """ создает коэффициенты для полинома """
    min_val = 0
    max_val = 100
    indexes = [randint(min_val, max_val) for i in range(degree + 1)]
    print(f'коэффициенты: {indexes}')
    return indexes

# создание полинома
def create_polynom(index_list: list) -> str:
    """ создает полином на основе списка коэффициентов """
    poly_degree = len(index_list) - 1
    # print(f'коэффициенты: {index_list}')
    polynom = ''
    poly_tail = index_list[-1]
    for i in range(poly_degree):
        if i == poly_degree - 1 and index_list[i] == 0 and poly_tail == 0:
            polynom += f''
        elif i == poly_degree - 1 and index_list[i] == 0:
            polynom += f'{poly_tail}'
        elif i == poly_degree - 1 and index_list[i] == 1 and poly_tail == 0:
            polynom += f'x'
        elif i == poly_degree - 1 and index_list[i] == 1:
            polynom += f'x + {poly_tail}'
        elif i == poly_degree - 1 and poly_tail == 0:
            polynom += f'{index_list[i]}*x'
        elif i == poly_degree - 1:
            polynom += f'{index_list[i]}*x + {poly_tail}'
        else:
            if index_list[i] == 0:
                polynom += ''
            elif index_list[i] == 1:
                polynom += f'x**{poly_degree - i} + '
            else:
                polynom += f'{index_list[i]}*x**{poly_degree - i} + '
        # print(f'i={i} -> {polynom}')
    return polynom

# запись в файл
def write_to_file(string: str, filename: str, verb: int = 0):
    """ запись в файл \n
        при verb = 1 выводит сообщение о записи в файл
    """
    with open(filename, 'w') as file:
        file.write(string)
    if verb == 1:   # собщение о записи в файл
        print(f'Writing to file {filename} is done.')

# чтение из файла
def read_fm_file(filename: str, verb: int = 0) -> str:
    """ чтение из файла \n
        при verb = 1 выводит ссобщение о чтении
    """
    with open(filename, 'r') as f:
        string = f.read()
        # print(f'{string}')
    if verb == 1:
        print(f'Reading from file {filename} is done.')
    return string
