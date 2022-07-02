'''Реализовать класс Matrix (матрица). Обеспечить перегрузку 
конструктора класса (метод __init__()), который должен принимать 
данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц). 
'''

from operator import le


class Matrix:


    def __init__(self,args):
        self.matr_list = args

    def __str__(self):
        return ('\n'.join([(f"|{' '.join(map(str,el))}|") for el in self.matr_list]))
        
    def __add__(self,other):
        new_m = [[self.matr_list[i][j]+other.matr_list[i][j]
                for j in range(len(self.matr_list[0]))]
                for i in range(len(self.matr_list))]
        return Matrix(new_m)


list1 = [[1,1,1],[2,2,2]]
list2 = [[1,2,3],[7,7,7]]
matr1 = Matrix(list1)
matr2 = Matrix(list2)

print(matr1+matr2)






