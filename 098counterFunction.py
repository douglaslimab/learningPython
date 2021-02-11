def counter(a, b, c):
    if c == 0:
        c = 1
    if ((b - a) < 0) and c > 0:
        c *= -1
    elif ((b - a) > 0) and c < 0:
        c *= -1
    for i in range(a, b, c):
        print(f'{i} ', end='')
    print()

# main
counter(1, 10, 1)
counter(10, 0, -2)
r = int(input('Enter the beginning of the sequence. '))
s = int(input('Enter the end of the sequence. '))
t = int(input('Enter the pitch. '))
counter(r, s, t)