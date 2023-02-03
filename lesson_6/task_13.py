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
    
class NewRobot(Robot):
    def __init__(self, direction, inclination_angle, speed, distance, battery_life, name, battery_capacity, channel_frequency, start_time):
        super().__init__(direction, inclination_angle, speed, distance, battery_life)
        self.__private_name = name
        self.__private_battery_capacity = battery_capacity
        self.__private_channel_frequency = channel_frequency
        self.__private_start_time = start_time
    
    def __str__(self):
        return super().__str__() + (f"Наименование модели: {self.__private_name}\n" 
                                    + f"Емкость аккумулятора: {self.__private_battery_capacity}\n" 
                                    + f"Частота канала связи пульта ДУ: {self.__private_channel_frequency}\n"
                                    + f"Время начала движения: {self.__private_start_time[0]}:{self.__private_start_time[1]}:{self.__private_start_time[2]}\n")
    
    def motion_time(self, curr_time):
        start_time = self.__private_start_time[0] * 3600 + self.__private_start_time[1] * 60 + self.__private_start_time[2]
        curr_time_s = curr_time[0] * 3600 + curr_time[1] * 60 + curr_time[2]
        result_s = curr_time_s - start_time
        result = [result_s // 3600, result_s % 3600 // 60, result_s % 60]
        return result
        
    def get_battery_capacity(self):
        return self.__private_battery_capacity
    
robot_1 = NewRobot(2, 3, 40, 80, 14, "Джони", 1000, 123, [0, 0, 1])
print(str(robot_1))
print(robot_1.motion_time([1, 1, 1]))