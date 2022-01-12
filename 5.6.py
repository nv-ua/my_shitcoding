#задачка на период жизни
age = int(input('Enter age: '))
if age < 2:
    print('Личинус')
elif age >= 2 and age < 4:
    print('Песдюк')
elif age >= 4 and age < 13:
    print('Шкет')
elif age >= 13 and age < 20:
    print('Кидалт')
elif age >= 20 and age < 65:
    print('Волк')
else:
    print('Подмети песок за собой в коридоре')