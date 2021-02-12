num = int(input('Enter one integer number: '))
print('''Choice the numeric system:
[ 1 ] Binary
[ 2 ] Ocatal
[ 3 ] Hexadecimal''')
opt = int(input('Enter your choice: '))

if opt == 1:
    print('{} in binary is: {}'.format(num, bin(num)[2:]))
elif opt == 2:
    print('{} in octal is: {}'.format(num, oct(num)[2:]))
elif opt ==3:
    print('{} in hexadecimal is: {}'.format(num, hex(num)[2:]))