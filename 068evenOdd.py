import random
counter = 0
while True:
    print('''    [ E ] - Even
    [ O ] - Odd\n''')
    guess = str(input('What is your choice? ')).strip().upper()[0]
    if guess not in 'OoEe':
        guess = str(input('Wrong option. What is your choice? ')).strip().upper()[0]
    machine = random.randint(0, 10)
    num = int(input('Enter your number. '))
    print('Computer choice: {}'.format(machine))
    sum = machine + num
    if (sum % 2) == 0:
        if guess in 'Ee':
            counter += 1
            print('You have won!')
        else:
            print('You have lost! Total of wins: {}'.format(counter))
            break
    else:
        if guess in 'Oo':
            counter += 1
            print('You have won!')
        else:
            print('You have lost! Total of wins: {}'.format(counter))
            break

print('GAME OVER!')
'''
cal = int(input('How many grams of tapioca: '))
print(cal*69/30)'''