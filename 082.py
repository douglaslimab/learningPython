from random import randint
general_list = []
even_list = []
odd_list = []
while True:
#    num = int(input('Enter a number. '))
    num = randint(0, 999)
    general_list.append(num)
    print(general_list)
    exit = str(input('Do you want to quit? [Y/N] ')).strip().upper()[0]
    if exit == 'Y':
        break
for item in general_list:
    if item % 2 != 0:
        odd_list.append(item)
    else:
        even_list.append(item)
general_list.sort()
even_list.sort()
odd_list.sort()
print(f'General List: {general_list}')
print(f'Even List: {even_list}')
print(f'Odd List: {odd_list}')