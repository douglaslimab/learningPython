from mod107 import *

# main
currency = float(input('Enter the value in U$ '))
print(f'The half of the value is {half(currency, format=True)}')
print(f'The half of the value is {doble(currency, format=True)}')
print(f'The half of the value is {increase(currency, 10, format=True)}')
print(f'The half of the value is {decrease(currency, 20, format=True)}')