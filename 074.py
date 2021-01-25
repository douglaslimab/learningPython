from random import randint
max_num = min_num = 0
tup = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
for i in range(len(tup)):
    if i == 0:
        max_num = min_num = tup[i]
    if tup[i] > max_num:
        max_num = tup[i]
    if tup[i] < min_num:
        min_num = tup[i]
print(tup)
print(f'The maximum number is: {max_num}')
print(f'The minimum number is: {min_num}')