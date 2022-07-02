'''Осуществить программу работы с органическими клетками, состоящими из ячеек.
 Необходимо создать класс «Клетка». В его конструкторе инициализировать параметр, 
 соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы
методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__floordiv__, __truediv__()). Эти методы должны применяться
только к клеткам и выполнять увеличение, уменьшение, умножение и округление до целого числа 
деления клеток, соответственно.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество 
ячеек в ряду. Этот метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n 
равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд
записываются все оставшиеся.
'''

class Cell:
    def __init__(self,quantity):
        self.__quantity = int(quantity)

    def getname(self):
        return [i for i, j in globals().items() if j is self]
    
    def __add__(self,other):
        return f'{self.getname()} + {other.getname()}= {(self.__quantity+other.__quantity)}'
    
    def __sub__(self,other):
        if self.__quantity > 0 and other.__quantity > 0:
            return f'{self.getname()} - {other.getname()} = {(self.__quantity - other.__quantity)}'
        else:
            return f'Ошибка. Число меньше 0'

    def __mul__(self,other):
        return f'{self.getname()} * {other.getname()} = {(self.__quantity * other.__quantity)}'
    def __floordiv__(self,other):
        if other.__quantity > 0:
            return f'{self.getname()} // {other.getname()} = {(self.__quantity // other.__quantity)}'
        else:
            return f'Ошибка. Делитель меньше 0'
    def __truediv__(self,other):
        if other.__quantity > 0:
            return f'{self.getname()} / {other.getname()} = {round((self.__quantity / other.__quantity),2)}'
        else:
            return f'Ошибка. Делитель меньше 0'

    def make_order(self, number):
        self.number = number
        return ('*'*self.number+'\n')*(self.__quantity//self.number)+ '*'*(self.__quantity%self.number)

sample_1 = Cell(120)
sample_2 = Cell(151)
sample_3 = Cell(0)
print(sample_2 + sample_1)
print(sample_2 - sample_1)
print(sample_2 * sample_1)
print(sample_2 / sample_1)
print(sample_2 // sample_1)
print(sample_2 // sample_3)
sample_4 = Cell(17)
print(sample_4.make_order(4))



