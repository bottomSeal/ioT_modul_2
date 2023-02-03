class WiFi:
    def __init__(self, standard_name, frequency):
        self.standard_name = standard_name
        self.frequency = frequency
    
    def __str__(self):
        return f"Название стандарта: {self.standard_name}\nЧастота: {self.frequency} МГц"
    
wifi = WiFi("Дом", 2.4)
print(str(wifi))