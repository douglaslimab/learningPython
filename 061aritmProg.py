first_num = int(input('Enter the first number of the sequence. '))
q = int(input('Enter the iteration. '))
i = int(0)
while i < 10:
    print('{} - '.format(first_num + q*i), end='')
    i += 1
print('Finished')