print ('Введите возраст')
age = int(input())
let=16-age
if age>= 16 and age<75:
    print ('Введите имя')
    name = input()
    if name=='Иван':
        print('Вы нам не подходите.')
    elif age >= 16 and age<75:
        print ('Поздравляем вы поступили в ВГУИТ')
else:
    print ('Сначала нужно окончить школу!')
    print ('Столько лет осталось учиться в школе:',let)
 
