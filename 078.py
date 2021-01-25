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