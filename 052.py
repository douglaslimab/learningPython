cnt = int(0)
num = int(input('Enter the number.\n'))
for n in range(1, num + 1):
    if num%n == 0:
        print('\033[33m', end='')
        cnt += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(n), end='')

if cnt == 2:
    print('\n\033[m{} is a prime number.'.format(num))
else:
    print('\n\033[m{} is not a prime number.'.format(num))