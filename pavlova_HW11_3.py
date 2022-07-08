'''Создать собственный класс-исключение, который должен проверять
содержимое списка на наличие только чисел. Проверить работу исключения 
на реальном примере. Запрашивать у пользователя данные и заполнять список 
необходимо только числами. Класс-исключение должен контролировать типы данных элементов списка.
'''

class NumberError(Exception):
    def __init__(self, txt):
        self.txt = txt


num_list = []
while True:
    try:
        number = input("Введите число или 'stop' для завершения:  ")
        if number == 'stop':
            break
        elif isinstance(float(number),float):
            num_list.append(number)
        else:
            raise NumberError('Ошибка! введите число')
    except ValueError:
        print('это не число')
    except NumberError as Err:
        print(Err)
    
print(num_list)
