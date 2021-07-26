def div_func(x, y):
    if y == 0:
        return "y не может быть равен 0"
    else:
        return x / y
x = float(input("введите x:"))
y = float(input("введите y:"))
print(div_func(x, y))