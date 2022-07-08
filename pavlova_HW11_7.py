''' Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения
и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте 
экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.'''
class Comp_num:
    def __init__(self,real,imaginary):
        self.imaginary = imaginary
        self.real = real
    
    def __str__(self):
        return f'({self.real} + {self.imaginary}i)'

    def __add__(self,other):
        print(f"= {Comp_num((self.real+other.real),(self.imaginary+other.imaginary))}")

    def __mul__(self,other):
        new_real = self.real*other.real - self.imaginary*other.imaginary
        new_imang = self.real*other.imaginary + other.real*self.imaginary
        print(f'{Comp_num(new_real,new_imang)}')

num1 = Comp_num(2,3)
num2 = Comp_num(5,6)
print(num1)
print('+')
print(num2)
num1 + num2
print('-'*30)
print(num1)
print('*')
print(num2)
num1 * num2
print('-'*30)

