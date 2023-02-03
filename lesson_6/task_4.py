class Radio:
    def __init__(self, frequency = 0, name= ""):
        self.__private_frequency = frequency
        self.__private_name = name
    
    def get_frequency(self):
        return self.__private_frequency
    
    def get_name(self):
        return self.__private_name
    
print(Radio(12).get_frequency())