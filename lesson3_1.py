def f_func():
    """ Проверяет введенные данные и возвращает значение частного """
    try:
        arg_1 = float(input('Введите делимое: '))
        arg_2 = float(input('Введите делитель: '))
    except ValueError:
        print('Нужно вводить числовые данные')
        return
    if arg_2 != 0:
        toch = int(input('Укажите точность расчета(количество знаков после запятой: '))
        rezlt = float(arg_1/arg_2)
        return round(rezlt, toch)
    else:
        print('Делитель должен быть не равным нулю')


gg = f_func()
print(gg)
