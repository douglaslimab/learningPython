import random
name1 = str(input('First:\n'))
name2 = str(input('Second:\n'))
name3 = str(input('Thirth:\n'))
name4 = str(input('Fourth:\n'))

lista = [name1, name2, name3, name4]

print('The choosen one is: \n{}'.format(random.choice(lista)))