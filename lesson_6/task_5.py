class PrintedCircleBoard:
    def __init__(self, width, length, layers, holes = 5):
        self.__private_width = width
        self.__private_length = length
        self.__private_layers = layers
        self.__private_holes = holes
        
    def increase_holes(self, n):
        self.__private_holes *= n
        
    def set_width(self, width):
        self.__private_width = width
        
    def set_length(self, length):
        self.__private_length = length
        
    def set_layers(self, layers):
        self.__private_layers = layers
        
    def set_holes(self, holes):
        self.__private_holes = holes
        
    def get_width(self):
        return self.__private_width
    
    def get_length(self):
        return self.__private_length
    
    def get_layers(self):
        return self.__private_layers
    
    def get_holes(self):
        return self.__private_holes
    