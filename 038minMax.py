num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

if num1 > num2:
    print('{} is bigger than {}.'.format(num1, num2))
elif num2 > num1:
    print('{} is bigger than {}'.format(num2, num1))
else:
    print('{} and {} are equals.'.format(num1, num2))