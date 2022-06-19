'''4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: 
speed, color, name, is_police(булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, 
остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) 
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, 
выведите результат. Вызовите методы и покажите результат.'''

class Car:
    def __init__(self,speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(self.name)

    def go(self):
        print(f'{self.name} поехала')
    def stop(self):
        print(f'{self.name} остановилась')
    def turn(self,direction):
        self.direction = direction
        print(f'{self.name} повернула {self.direction}')
    def show_speed(self):
        print(f'{self.name} набрала скорость {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"скорость превышена!!!")
    
class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
    
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            print(f"скорость превышена!!!")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.is_police = True
        
townCar = TownCar(100,'blue','renault')
townCar.go()
townCar.turn('к мосту')
sportCar =  SportCar(50,'red','kia')
work = WorkCar(200,'black','audi')
police = PoliceCar(40,'white','nissan')
sportCar.turn('направо')
work.turn('налево')
police.stop()


