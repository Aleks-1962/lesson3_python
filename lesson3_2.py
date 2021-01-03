def us_func(name, family, b_day, city, mail, tel):
    return name + ' ' + family + ' ' + b_day + ' ' + city + ' ' + mail + ' ' + tel


name = input('Ваше имя: ')
family = input('Ваше фамилия: ')
b_day = input('Дата рождения: ')
city = input('Город: ')
mail = input('Электронный адрес: ')
tel = input('Телефон: ')
gg = us_func(name, family, b_day, city, mail, tel)
print('Введен пользователь ' + gg)
