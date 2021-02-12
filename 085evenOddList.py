num = [[], []]
data = 0
for i in range(0, 7):
    data = int(input('Enter a number: '))
    if data % 2 == 0:
        num[0].append(data)
    else:
        num[1].append(data)
num[0].sort()
num[1].sort()
print(num[0])
print(num[1])
'''
from random import randint
even_data = list()
odd_data = list()
numbers = list()
for i in range(0, 7):
#    num = int(input('Enter a number: '))
    numbers.append(randint(0, 7))
print(numbers)
for i in numbers:
    if i % 2 != 0:
        odd_data.append(i)
    else:
        even_data.append(i)
print(even_data)
print(odd_data)
#    data.append(int(input('Enter a number: ')))
'''