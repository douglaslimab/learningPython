from random import randint

items = ('Rock', 'Paper', 'Scisor')
machine = randint(0, 2)

print('''[ 0 ] - Rock
[ 1 ] - Paper
[ 2 ] - Scisor''')
key = int(input('Enter your choice.'))

print('Computer choice: {}'.format(items[machine]))
print('You chose: {}'.format(items[key]))

if(machine == 0):
    if(key == 0):
        print('Equal.')
    elif(key == 1):
        print('You have won.')
    elif(key == 2):
        print('You have lost.')
    else:
        print('Wrong choice.')

if(machine == 1):
    if(key == 0):
        print('You have lost')
    elif(key == 1):
        print('Equal.')
    elif(key == 2):
        print('You have won.')
    else:
        print('Wrong choice.')

if(machine == 2):
    if(key == 0):
        print('You have won')
    elif(key == 1):
        print('You have lose.')
    elif(key == 2):
        print('Equal.')
    else:
        print('Wrong choice.')