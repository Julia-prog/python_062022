'''Создать собственный класс-исключение, обрабатывающий ситуацию
деления на ноль. Проверить его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать 
эту ситуацию и не завершиться с ошибкой.'''

class MyZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:
    try:
        dat1 = int(input("Введите делитимое:  "))
        dat2 = int(input("Введите делитель:  "))
        if dat2 == 0:
            raise MyZeroError('Ошибка! На ноль делить нельзя')
    except ValueError:
        print('это не число')
    except MyZeroError as Err:
        print(Err)
    else:
        print(f'{dat1}/{dat2} = {round(dat1/dat2,2)}')

    

    