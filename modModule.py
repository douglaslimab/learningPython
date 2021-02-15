def fator(num, show = False):
    result = 1
    for i in range(0, num):
        if show == True:
            print(f'{num - i} ', end='')
        result *= (num - i)
    return result

def doble(num):
    num *= 2
    return num

def triple(num):
    num *= 3
    return num