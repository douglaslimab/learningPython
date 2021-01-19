import random
quit = str('N')
guessing_counter = int(0)
while quit != 'Y':
    num = random.randint(0, 10)
    guess = int(input('Enter you number: '))
    while guess != num:
        guessing_counter += 1
        guess = int(input('Enter your number again: '))
    print('After {} guessings, you got it!'.format(guessing_counter))
    print('The number is {}'.format(num))
    quit = str(input('Do you want to quit? [Y/N]')).strip().upper()[0]
print('Game Over')