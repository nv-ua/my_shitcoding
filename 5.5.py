#задачка на проверку цветов
#стоило бы добавить ловушку исключений для срабатывания else, но я забыл как это делать
alien_color = ['green', 'yellow', 'red']
if alien_color[int(input('Number: '))] == 'green':
    print(alien_color[0], 'You earned 5 points!')
elif alien_color[int(input('Number: '))] == 'yellow':
    print(alien_color[1], 'You earned 10 points!')
elif alien_color[int(input('Number: '))] == 'red':
    print(alien_color[2], 'You earned 15 points!')
else:
    print('You earned po jebalu)))')