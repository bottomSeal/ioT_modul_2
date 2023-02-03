class Rangefinder:
    def __init__(self, time):
        if time[1].lower() == "секунды":
            time[0] *= 10**(-6) 
        elif time[1].lower() == "миллисекунды":
            time[0] *= 10**(-3)
        self.__private_time = time[0]
        self.__private_distance = 3 * 10**8 * (time[0] / 2)
        
    def get_time(self):
        return self.__private_time
    
    def get_distance(self):
        return self.__private_distance
    
print(Rangefinder([int(input("Введите время задержки: ")), input("Введите единицы измерения: ")]).get_distance())