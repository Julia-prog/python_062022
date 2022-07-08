'''Начать работу над проектом «Склад оргтехники». Создать класс, 
описывающий склад. А также класс «Оргтехника», который будет базовым 
для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведённых типов. 
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над предыдущим заданием. Разработать методы, 
которые отвечают за приём оргтехники на склад и передачу в определённое 
подразделение компании. Для хранения данных о наименовании и количестве 
единиц оргтехники, а также других данных, можно использовать любую подходящую 
структуру (например, словарь).
6. Продолжить работу над предыдущим заданием. Реализовать механизм валидации 
вводимых пользователем данных. Например, для указания количества принтеров, 
отправленных на склад, нельзя использовать строковый тип данных.
'''
import random


class Warehouse:
    STATUS = {
            'Printer' : 0,
            'Scanner' : 0,
            'Copier' : 0}
    
    def __str__(self):
        return f'{Warehouse.STATUS}\n' + '-'*50

    @staticmethod
    def type_num(num):
        return type(abs(num)) == int

    @classmethod
    def zerotest(cls,name,count):
        rez = cls.STATUS[name] + count
        if rez < 0:
            rez = 0
            print(f'Не хватило {abs(cls.STATUS[name] + count)} единиц {name}')
        return rez
    
    @classmethod
    def transferred(cls,value):
        if type(value) == dict:
            for name, count in value.items():
                if cls.type_num(count):
                    cls.STATUS[name.name_eq] = cls.zerotest(name.name_eq,count)
        else:
            cls.STATUS[value.name_eq] += 1
        print(cls.__str__(cls.STATUS))


class Equipment:
    def __init__(self):
        self.name_eq = self.__class__.__name__
        rand_n = random.randint(1000, 2000)
        self.id = f'{self.name_eq[0]}{rand_n}'

    def __str__(self):
        return f'{self.name_eq} :{self.id}'
    

class Printer(Equipment):
     pass
class Scanner(Equipment):
    pass
class Copier(Equipment):
    pass

printer = Printer()
print(printer)
scanner = Scanner()
copier = Copier()
arehouse= Warehouse()
dolist1 = {
    printer:2,
    scanner:-4,
    copier:10}
dolist2 = {
    printer:-5,
    scanner:8,
    copier:60}

print(arehouse)

arehouse.transferred(printer)
arehouse.transferred(dolist1)
arehouse.transferred(dolist2)







                    