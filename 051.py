num = int(input('Enter the first number of the Aritimetic Progression.'))
q = int(input('Enter the iteration of the Progression.'))
nten = num + (10 - 1)*q
for n in range(num, nten + q, q):
    print('{} '.format(n), end=' > ')
print('Finished')