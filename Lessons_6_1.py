from time import sleep

class Trafficlight:
    colors = ("red", "yellow", "green")
    delay = (7, 2, 10)

    def __init__(self):
        self.color = "green"

    def running(self):
        while True:
            for i in self.colors:
                self.__color = i
                print(self.__color)
                sleep(self.delay[self.colors.index(self.__color)])

traffic_light = Trafficlight()
traffic_light.running()



