from time import sleep

class TrafficLight():
    color = ""
    def running(self):
        self.color = "red"
        sleep(7)
        print(self.color)
        self.color = "yellow"
        sleep(2)
        print(self.color)
        self.color = "green"
        sleep(5)
        print(self.color)
    
trafic_light = TrafficLight()
trafic_light.running()