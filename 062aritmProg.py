first_num = int(input('Enter the first number of the sequence. '))
q = int(input('Enter the iteration. '))
i = int(0)
i_more = int(10)
while i < i_more:
    current_num = first_num + i*q
    print('{} - '.format(current_num), end='')
    i += 1
    if i == i_more:
        print('Pause')
        i_more = int(input('How many more numbers do you want to see? '))
        i = 0
        first_num = current_num + q
print('Finished')