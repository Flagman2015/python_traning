class Exclusion:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите значения '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                print(f'Текущий список - {self.my_list} \n ')
                y_or_n = input(f'Продолжите вводить цифры? Y/Stop ')
                print(f'Текущий список - {self.my_list} \n ')
                if y_or_n == 'Y' or y_or_n == 'y':
                     print(try_except.my_input())
                elif y_or_n == 'Stop' or y_or_n == 'stop':
                     return f'Вы вышли'
                print(f'Текущий список - {self.my_list} \n ')

try_except = Exclusion(1)
print(try_except.my_input())

