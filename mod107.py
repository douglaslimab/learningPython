def half(num, format=False):
    num /= 2
    if format == True:
        num = str(f'U$ {num:.2f}')
    return num

def doble(num, format=False):
    num *= 2
    if format == True:
        num = str(f'U$ {num:.2f}')
    return num

def increase(num, perc, format=False):
    num *= (1 + perc/100)
    if format == True:
        num = str(f'U$ {num:.2f}')
    return num

def decrease(num, perc, format=False):
    num *= (1 - perc/100)
    if format == True:
        num = str(f'U$ {num:.2f}')
    return num