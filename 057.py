gender = ''
gender = str(input('Enter the Gender. [M/F]')).strip().upper()[0]
while gender not in 'FfMm':
    gender = str(input('Invalid input. Please, enter the Gender. [M/F]')).strip().upper()[0]
print('Gender registered: {}'.format(gender))
age = int(input('Enter your Age.'))
'''
exit = 'Y'
while exit != 'N':
    num = int(input('Enter a number. '))
    exit = str(input('Do you want to quit? [Y/N]')).upper()
print('Finished.')
'''