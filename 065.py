max_num = min_num = counter = avarage = 0
exit = 'N'
while exit != 'Y':
    num = float(input('Enter a number. '))
    avarage += num
    counter += 1
    print(num)
    if min_num == 0:
        min_num = num
    if num > max_num:
        max_num = num
    elif num < min_num:
        min_num = num
    exit = str(input('Do you want to quit? [Y/N] ')).strip().upper()[0]
avarage /= counter
print('Avarage: {:.2f}'.format(avarage))
print('Maximum number: {:.2f}'.format(max_num))
print('Minimum number: {:.2f}'.format(min_num))
print('Finished')