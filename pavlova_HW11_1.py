'''1. Реализовать класс «Дата», функция-конструктор которого должна
принимать дату в виде строки формата «день-месяц-год». В рамках класса
реализовать два метода. Первый — с декоратором @classmethod. Он должен 
извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй — с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
структуры на реальных данных.'''

class Data:
    def __init__(self) -> None:
        pass

    @classmethod
    def in_numb(cls, data_str):
        if Data.valid(data_str):
            data_str = data_str.split('-')
            print(f"{'.'.join(data_str)}:{[int(el) for el in data_str]}")
        
        

    @staticmethod
    def valid(data_str):
        data = [int(el) for el in data_str.split('-')]
        if 0<data[0]<32 and 0<data[1]<13 and data[2]>1900:
            print(f'{data_str}: OK')
            return True
        else:
            print(f'{data_str}: Error!')
            return False
            

            
print(Data.valid('09-10-1990'))
print(Data.valid('09-10-1890'))
print(Data.valid('09-0-1990'))
print(Data.valid('40-10-1890'))
Data.in_numb('10-10-2020')
Data.in_numb('99-10-2020')