def get_pow(x, y):
    if x < 0:
        return "х должно быть больше 0"
    if y > 0:
        return "y должно быть меньше 0"
    else:
        return get_pow(x, y)
x = float(input(("пожалуйста введите позитивное число х: ")))
y = float(input(("пожалуйста введите негативное число y: ")))
print(get_pow(x, y))

