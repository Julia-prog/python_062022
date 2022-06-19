"""2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного 
кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т."""

class Road:
    def __init__(self,length, width):
        self._length = length
        self._width = width

    def calc(self, weight=1,thickness=1):
        self.weight =weight
        self.thickness = thickness
        self.calc_ = self._length * self._width * self.weight * self.thickness/1000
        print(f'{self._length} м* {self._width} м* {self.weight} кг/м* {self.thickness} см = {self.calc_} т.')

road=Road(20,5000)
road.calc(25,5)