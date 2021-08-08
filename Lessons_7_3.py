class Cell:
    def __init__(self, parts):
        self.parts = parts

    def __add__(self, other):
        return Cell(self.parts + other.parts)

    def __sub__(self, other):
        diff = self.parts - other.parts
        if diff > 0:
            return Cell(diff)
        else:
            print(f"ошибка счета")

    def __mul__(self, other):
        return Cell(self.parts * other.parts)

    def __truediv__(self, other):
        return Cell(self.parts // other.parts)

    def make_oder(self, count):
        s = ""
        for i in range(self.parts // count):
            s += '*' *  count + '\n'
        s += '*' * (self.parts % count) + '\n'
        return

    def __str__(self):
        return f'{self.parts}'


cell = Cell(22)
print(cell.make_oder(8))
cell2 = Cell(15)
print(cell2.make_oder(5))

print(cell - cell2)
print(cell + cell2)
print(cell * cell2)
print(cell / cell2)
print(cell2 - cell)

