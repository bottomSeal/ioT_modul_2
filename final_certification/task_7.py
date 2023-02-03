from time import sleep

class LED:
    is_light = False
    delay = 0
    
    def __init__(self, is_light, delay):
        self.is_light = is_light
        self.delay = delay
    
    def flashing(self):
        while True:
            if self.is_light:
                self.is_light = False
            else:
                self.is_light = True
            print(self.is_light)
            sleep(self.delay)
            
            
LED(False, 5).flashing()
