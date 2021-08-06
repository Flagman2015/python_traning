class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Start drawing")

class  Pen(Stationery):
    def draw(self):
        print("Start drawing with pen")

class  Pensil(Stationery):
    def draw(self):
        print("Start drawing with pensil")

class  Handle(Stationery):
    def draw(self):
        print("Start drawing with handle")

pen = Pen("a")
pensil = Pensil ("b")
handle= Handle ("c")

for s in (pen, pensil, handle):
    s.draw()


