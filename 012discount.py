num = float(input('What is the value?\n'))
dis = float(input('How much is the discount?\n'))
num = num - num*dis/100
print('You have to pay U$ {:.2f}.'.format(num))