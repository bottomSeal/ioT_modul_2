class Joystick:
    def __init__(self, position = 0, click = False):
        self.__private_position = position
        self.__private_click = click
        
    def get_condition(self):
        result = "Джойстик "
        if self.__private_position > 0:
            result += "поднят. "
        elif self.__private_position < 0:
            result += "опущен. "
        else:
            result += "лежит. "
        if self.__private_click:
            result += "На джойстик нажали."
        else:
            result += "На джойстик не нажимали."
        return result
    
    
print(Joystick(1, False).get_condition())