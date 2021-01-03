def my_func(a, b, c):
    """ Возвращает сумму 2-х мах из 3 введенных"""
    rez1 = (max(a, b, c) + min(max(a, b), max(a, c), max(b, c)))
    return rez1


arg_1 = float(input('Введите 1 значение: '))
arg_2 = float(input('Введите 2 значение: '))
arg_3 = float(input('Введите 3 значение: '))
makc = my_func(arg_1, arg_2, arg_3)
print(makc)
