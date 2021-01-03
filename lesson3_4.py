def my_func(x, y):
    """ возвращает значение числа в отрицательной  степени """
    if x >= 0:
        x1 = x
        x2 = x
        x **= abs(y)
        print('первой вариант')
        print(x)
        for i in range(abs(y)-1):
            x1 = x2 * x1
        print('второй вариант')
        print(x1)
        return 1/x, 1/x1
    else:
        print('Действительное число должно быть больше 0')
        return


arg_1 = float(input('Введите действительное число: '))
arg_2 = int(input('Введите показатель спепени: '))

print('Результат ' + str(my_func(arg_1, arg_2)))
