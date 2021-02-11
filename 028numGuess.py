import random
import time
num = random.randint(1,6)
guess = int(input('Guess...\n'))

print('.')
time.sleep(1)
print('..')
time.sleep(1)
print('...')
time.sleep(1)

if guess == num:
    print('True')
else:
    print('False')
print(num)
"""
num1 = int(input('Ente1r the first number:\n'))
num2 = int(input('Enter the second number:\n'))

if num1 > num2:
    print('{} > {}'.format(num1, num2))
else:
    print('{} > {}'.format(num2, num1))
"""