def sum_chis():
    sum_r = 0
    vixod = False
    while vixod == False:
        str_numb = input('Введите строку чисел, через пробел. Для выход нажмите Q: ')
        str_numb = str_numb.split()
        print(str_numb)
        sum_total = 0
        for i in range(len(str_numb)):
            if str_numb[i] == 'Q' or str_numb[i] == 'q':
                vixod = True
                break
            else:
                print(str_numb[i])
            sum_r = sum_r + int(str_numb[i])
            print('Сумма ' + str(sum_r))
            print('_сумма' + str(sum_total))
    sum_total = sum_total + sum_r
    print('сумма '+str(sum_total))
    return sum_total


print(sum_chis())
