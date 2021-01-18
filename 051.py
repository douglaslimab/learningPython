s = int(0)
for n in range(1, 7):
    num = int(input('Enter your number, you have {} of 6.'.format(n)))
    if(num%2) == 0:
        s = s + num
print(s)