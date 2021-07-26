def my_func(x, y, z):
    sum = x + y + z
    return sum - min(x, y, z)

x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

d = my_func(x, y, z)
print(d)
