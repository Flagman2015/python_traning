class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("GO")

    def stop(self):
        print("stop")

    def turn(self, direction):
        print(f"Car turned to {direction}")

    def show_speed(self):
        print(f"Current speed is {self.speed}")

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Вы превысили скорость")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Вы превысили скорость")

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

Town = TownCar (90, "green", "town")
Sport = SportCar(120, "red", "Sport")
Work = WorkCar(41, "yellow", "Work")
police = PoliceCar(100, "blue", "Police")

Town.show_speed()
Work.show_speed()

Work.speed = 30
Work.show_speed()
police.turn ("left")

