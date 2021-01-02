spd = int(input('Enter the speed\n'))

if spd > 80:
    print('Too fast!!')
    fine = (spd - 80)*7
    print('You have to pay {}'.format(fine))
else:
    print('OK..')
