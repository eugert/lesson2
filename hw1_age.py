age = int(input ('Введите возраст: '))

if age <=6:
    massege = 'Вы можете посещать детский сад'
elif  age <=16:
    massege = 'Вы учитесь в школе'
elif  age <=23:
    massege = 'Вы вероятно учитесь в ВУЗе'
elif  age <=65:
    massege = 'Вы работаете'
else: 
    massege = 'Вы можете выйти на песнию'

print (massege)
