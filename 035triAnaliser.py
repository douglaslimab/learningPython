num1 = int(input('Enter the 1st value.\n'))
num2 = int(input('Enter the 2nd value.\n'))
num3 = int(input('Enter the 3th value.\n'))
if (num1 + num2) > num3 and (num1 + num3) > num2 and (num2 + num3) > num1:
    print('True')
else:
    print('False')