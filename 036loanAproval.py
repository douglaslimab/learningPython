price = int(input('How much is the house?\n'))
salary = int(input('How much is the salary?\n'))
time = int(input('How many years for finishing paying?\n'))
price = price/(time*12)
salary = salary*0.3
if price <= salary:
    print('The parcel is {:.2f}.\n'.format(price))
    print('Aproved')
else:
    print('The parcel would be {:.2f}'.format(price))
    print('Not aproved.')
"""
flg = int(1)

print('-='*20)
print('Menu')
print('-='*20)
print('1 - keep the loop')
print('0 - Get out of the loop')
print('-='*20)

while flg == 1:
    flg = int(input('Enter the key:\n'))
print('out')
"""