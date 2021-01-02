num1 = int(input('Enter the 1st number.\n'))
num2 = int(input('Enter the 2nd number.\n'))
num3 = int(input('Enter the 3th number.\n'))
aux = num1
aux1 = num1
if num2 < num1 and num2 < num3:
    aux = num2
if num3 < num1 and num3 < num2:
    aux = num3
if num2 > num1 and num2 > num3:
    aux1 = num2
if num3 > num1 and num3 > num2:
    aux1 = num3
print('The lowest number is {}'.format(aux))
print('The highest number is {}'.format(aux1))