list = []
while True:
    num = int(input('Enter a number: '))
    if num not in list:
        list.append(num)
    else:
        print('Double number.')
    exit = str(input('Do you want to quit? [Y/N]')).strip().upper()[0]
    if exit == 'Y':
        break
list.sort()
print(list)