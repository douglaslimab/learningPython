num = int(input('How many numbers do you want to see? '))
zero = int(0)
one = int(1)
i = int(2)
fibo = int(0)
print('{} - {} - '.format(zero, one), end = '')
while i < num:
    fibo = zero + one
    zero = one
    one = fibo
    i += 1
    print('{} - '.format(fibo), end = '')
print('Finished')