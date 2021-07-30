def wade():
    try:
        time = float(input('Выработка в часах: '))
        bid = int(input('Ставка, рубли: '))
        prize = int(input('Премия, рубли: '))
        salary = time * bid + prize
        print(f'заработная плата сотрудника  {salary}')
    except ValueError:
        return print('Введите числовое значение')


wade()
