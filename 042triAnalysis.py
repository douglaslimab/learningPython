side1 = int(input('Enter the first triangle side.'))
side2 = int(input('Enter the second triangle side.'))
side3 = int(input('Enter the thirth triangle side.'))

if (side1 < side2 + side3) and (side2 < side1 + side3) and (side3 < side1 + side2):
    print('Triangle allowed.')
    if side1 == side2 == side3:
        print('3 equal sides.')
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print('2 equal sides.')
    elif side1 != side2 !=side3:
        print('3 different sides.')
else:
    print('Triangle not allowed.')
