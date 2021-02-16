from mod107 import *

# main
currency = float(input('Enter the value in U$ '))
print(f'The half of the value is {coin(half(currency), currency="R$")}')
print(f'The half of the value is {coin(doble(currency))}')
print(f'The half of the value is {coin(increase(currency, 10))}')
print(f'The half of the value is {coin(decrease(currency, 20))}')