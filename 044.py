value = float(input('Enter the total of your shop.\n'))
print('''Ways of payment:
[ 1 ] - Cash
[ 2 ] - Debit
[ 3 ] - 2x in the Credit Card
[ 4 ] - 3x in the Credit Card''')
key = int(input('Enter your choice.\n'))
if key == 1:
    value = value*0.9
    print('you have 10% as a discount. You have to pay R$ {:.2f}.'.format(value))
elif key == 2:
    print('You have to pay {:.2f}.'.format(value))
elif key == 3:
    value = (value*1.15)/2
    print('You have to pay 2 parcels of {:.2f}.'.format(value))
elif key == 4:
    value = (value*1.2)/3
    print('You have to pay 3 parcels of {:.2f}.'.format(value))
else:
    print('Wrong choice.')