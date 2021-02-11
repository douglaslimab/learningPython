days = int(input('How many days?\n'))
km = int(input('How long?\n'))
days = days*60
km = km*0.15
print('You have to pay U$ {:.2f}'.format(days + km))