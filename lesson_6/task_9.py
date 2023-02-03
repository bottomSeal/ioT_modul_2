class Reciever:
    def __init__(self, min_frequency, curr_frequency, max_frequency, koef_aplif, modulation_type, interm_frequency):
        self.__private_min_frequency = min_frequency
        self.__private_curr_frequency = curr_frequency
        self.__private_max_frequency = max_frequency
        self.__private_koef_aplif = koef_aplif
        self.__private_modulation_type = modulation_type
        self.__private_interm_frequency = interm_frequency
        
    def get_min_frequency(self):
        return self.__private_min_frequency
    
    def get_curr_frequency(self):
        return self.__private_curr_frequency
    
    def get_max_frequency(self):
        return self.__private_max_frequency
    
    def get_koef_aplif(self):
        return self.__private_koef_aplif
    
    def get_modulation_type(self):
        return self.__private_modulation_type
    
    def get_interm_frequency(self):
        return self.__private_interm_frequency
    
    def frequency_range(self):
        return self.__private_max_frequency - self.__private_min_frequency
    
    def interm_frequency_multipli(self, n):
        return self.__private_interm_frequency * n
    
    def mirror_chanel_frequency(self):
        return self.__private_curr_frequency + self.__private_interm_frequency * 2
    
    
reciever_1 = Reciever(1, 1, 1, 1, 1, 1)
reciever_2 = Reciever(2, 2, 2, 2, 2, 2)
reciever_3 = Reciever(3, 3, 3, 3, 3, 3)