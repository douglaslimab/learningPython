list = []
for item in range(0, 5):
    list.append(int(input('Enter a number. ')))
print(list)
print(f'The max value is {max(list)} ', end='')
for i, n in enumerate(list):
    if n == max(list):
        print(f'at the positon {i}..', end='')
print(f'\nThe min value is {min(list)} ', end='')
for i, n in enumerate(list):
    if n == min(list):
        print(f'at the position {i}..', end='')
'''
from random import randint
max_num = min_num = 0
list = [randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)]
print(list)
for i in range(len(list)):
    if i == 0:
        max_num = min_num = list[i]
    if list[i] > max_num:
        max_num = list[i]
    if list[i] < min_num:
        min_num = list[i]
print(min_num, max_num)
print(min(list))
print(max(list))
'''