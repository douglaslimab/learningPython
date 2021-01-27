from random import randint
matrix = [[], [], []]
counter_even = sum_3 = max_2 = 0
for i in range(0, 3):
    for l in range(0, 3):
        matrix[i].append(randint(0, 999))
#        matrix[i].append(int(input(f'Enter a number for [{i}][{l}]: ')))
for i in range(0, 3):
    for l in range(0, 3):
        print(f'[ {matrix[i][l]:^5} ]', end='')
    print()
for lin in range(0, 3):
    for col in range(0, 3):
        if matrix[lin][col] % 2 == 0:
            counter_even += matrix[lin][col]
    if col == 2:
        sum_3 += matrix[lin][2]
for col in range(0, 3):
    if col == 0 or matrix[1][col] > max_2:
        max_2 = matrix[1][col]
#max_2 = max(matrix[1])
print(f'Even: {counter_even}')
print(f'Colum 3: {sum_3}')
print(f'Max 2: {max_2}')