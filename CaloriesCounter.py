result = 0
while True:
    name = str(input('Name: '))
    size = int(input('Portion size: '))
    calories = float(input('Calories per portion: '))
    calories_size = float(input('Size of portion calories: '))
    result += size*calories/calories_size
    print('Amount of calories: {}'.format(result))
    choice = str(input('Do you want to quit? [Y/N]'))
    if choice == 'Y':
        break