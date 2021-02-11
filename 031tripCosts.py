num = float(input('How long is the trip?\n'))
if num <= 200:
    num = num*0.50
else:
    num = num*0.45
print('You have to pay U$ {:.2f}'.format(num))