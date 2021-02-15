def intRead(msg):
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('\033[0;31mInvalid Character.\033[m')
    return valor

# main
n = intRead('Enter a number. ')
print(f'The answer is: {n}')