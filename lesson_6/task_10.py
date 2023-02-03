class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        
    def go(self):
        if self.speed > 0:
            print("Машина поехала.")
    
    def stop(self):
        if self.speed == 0:
            print("Машина остановилась.")
    
    def turn(self, direction):
        print("Машина повернула " + direction + ".")
    
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        
    def show_speed(self):
        print(self.speed)
        if self.speed > 60:
            print("Превышение допустимой скорости.")
            
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        
    def show_speed(self):
        print(self.speed)
        if self.speed > 40:
            print("Превышение допустимой скорости.")
            
            
car_1 = TownCar(70, "red", "ddd", False)
car_1.go()
car_1.turn("налево")
car_1.show_speed()