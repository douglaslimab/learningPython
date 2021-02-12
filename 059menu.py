exit = str('N')
num_max = int(0)
while exit != 'Y':
    num1 = float(input('Enter the first number.'))
    num2 = float(input('Enter the second number.'))
    print('''    [ 1 ] - Add
    [ 2 ] - Mult
    [ 3 ] - Highest
    [ 4 ] - New numbers
    [ 5 ] - Exit''')
    read_key = int(input('Enter your choice: '))
    if read_key == 1:
        num1 = num1 + num2
        print('Result: {}'.format(num1))
    elif read_key == 2:
        num1 = num1 * num2
        print('Result: {}'.format(num1))
    elif read_key == 3:
        if num1 > num2:
            num_max = num1
        elif num2 > num1:
            num_max = num2
        else:
            num_max = num1
        print('Result: {}'.format(num_max))
    elif read_key == 4:
        exit = 'N'
    elif read_key == 5:
        exit = 'Y'
    else:
        print('Invalid choice.')
#    exit = str(input('Do you want to quit? [Y/N]'))
print('Finished')