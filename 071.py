exit = 'N'
while True:
    withdraw = float(input('Withdraw: '))
    num_50 = int(withdraw // 50)
    withdraw -= num_50*50
    num_20 = int(withdraw // 20)
    withdraw -= num_20*20
    num_10 = int(withdraw // 10)
    withdraw -= num_10*10
    num_5 = int(withdraw // 5)
    withdraw -= num_5*5

    exit = str(input('Do you want to quit? [Y/N]')).strip().upper()[0]
    while exit not in 'YyNn':
        exit = str(input('Do you want to quit? [Y/N]')).strip().upper()[0]
    if exit == 'Y':
        break

if num_50 > 0:
    print('{} notes of U$ 50,00'.format(num_50))
if num_20 > 0:
    print('{} notes of U$ 20,00'.format(num_20))
if num_10 > 0:
    print('{} notes of U$ 10,00'.format(num_10))
if num_5 > 0:
    print('{} notes of U$ 5,00'.format(num_5))