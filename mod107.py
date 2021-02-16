def half(num, format=False):
    num /= 2
    return num if format==False else coin(num)

def doble(num, format=False):
    num *= 2
    return num if format==False else coin(num)


def increase(num, perc, format=False):
    num *= (1 + perc/100)
    return num if format==False else coin(num)


def decrease(num, perc, format=False):
    num *= (1 - perc/100)
    return num if format==False else coin(num)


def coin(num=0, currency='U$'):
    return f'{currency} {num:>.2f}'.replace('.', ',')

def analysis(num, inc, dec):
    print('-'*30)
    print('       Analysis')
    print('-'*30)
    print(f'Value: \t\t{coin(num)}')
    print(f'Half: \t\t{coin(half(num))}')
    print(f'Double: \t{coin(doble(num))}')
    print(f'Taxed: \t\t{coin(increase(num, inc))}')
    print(f'Discount: \t{coin(decrease(num, dec))}')
    print('-'*30)