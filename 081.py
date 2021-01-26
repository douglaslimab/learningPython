list = []
i = 0
while True:
    num = int(input('Enter a number. '))
    list.append(num)
    i += 1
    exit = str(input('Do you want to quit? [Y/N] ')).strip().upper()[0]
    if exit == 'Y':
        break
print(f'Numeber of items added to the list {i}')
list.sort(reverse = True)
print(list)
if 5 in list:
    print(f'The number 5 is at the position number {list.index(5)}')
else:
    print('Number 5 is not in the list.')