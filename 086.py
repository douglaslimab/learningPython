from random import randint
matrix = [[], [], []]
for i in range(0, 3):
    for l in range(0, 3):
        matrix[i].append(randint(0, 999))
#        matrix[i].append(int(input(f'Enter a number for [{i}][{l}]: ')))
for i in range(0, 3):
    for l in range(0, 3):
        print(f'[ {matrix[i][l]:^5} ]', end='')
    print()