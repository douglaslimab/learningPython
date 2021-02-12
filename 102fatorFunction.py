def fator(num, show = False):
    '''
    -> Getting the fatorial of a number.
    :param num: Enter the number.
    :param show: (OPTIONAL) to check the numbers
    :return: result
    '''
    result = 1
    for i in range(0, num):
        if show == True:
            print(f'{num - i} ', end='')
        result *= (num - i)
    return result
print(fator(4, show=True))
# help(fator)