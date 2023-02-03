class Robot:
    __private_direction = 0
    __private_inclination_angle = 0
    __private_speed = 0
    __private_distance = 0
    __private_battery_life = 0
    
    def __init__(self, direction, inclination_angle, speed, distance, battery_life):
        self.__private_direction = direction
        self.__private_inclination_angle = inclination_angle
        self.__private_speed = speed
        self.__private_distance = distance
        self.__private_battery_life = battery_life
        
    def __str__(self):
        return (f"Направление движения: {self.__private_direction}\n" 
        + f"Угол наклона: {self.__private_inclination_angle}\n"
        + f"Скорость движения: {self.__private_speed}\n"
        + f"Пройденный путь: {self.__private_distance}\n"
        + f"Время автономной работы: {self.__private_battery_life}\n")
        
    def get_time(self):
        return self.__private_distance / self.__private_speed
    
    def is_ok(self):
        result = True
        if (self.__private_direction > 10) and (self.__private_inclination_angle > 5) and (self.__private_battery_life < 3):
            result = False
        return result
    
robot_1 = Robot(2, 3, 40, 80, 14)
print(str(robot_1))
print(robot_1.is_ok())