"""Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...


@type_logger
def calc_cube(x):
   return x ** 3

>>> a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую; 
Сможете ли вывести имя функции, например, в виде:
>>> a = calc_cube(5)
calc_cube(5: <class 'int'>)"""

def type_logger(func):
    def wrap(*args):
        calc_list=[]
        for arg in args:
            calc_cube = func(arg) #??? лишняя строка?
            calc_list.append(f'{arg}:{type(arg)}')
            calc_tuple=tuple(calc_list)
        print(f'{str(func.__name__)}({calc_tuple}),')

    return wrap


@type_logger
def calc_cube(x):
   return x ** 3

calc_cube(5,15,5.5)