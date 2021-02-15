c = ('\033[m',          # 0 - no colors
     '\033[0;30;41m',   # 1 - red
     '\033[0;30;42m',   # 2 - green
     '\033[0;30;43m',   # 3 - yellow
     '\033[0;30;44m',   # 4 - blue
     '\033[0;30;45m',   # 5 - purple
     '\033[7;30m'       # 6 - white
     );

def getHelp(msg):
    ttl(f'Opening the function \'{msg}\'', 4)
    print(c[6],end='')
    help(msg)
    print(c[0], end='')

def ttl(msg, color=0):
    print(c[color], end='')
    print('-'*(len(msg)+6))
    print(f'   {msg}')
    print('-'*(len(msg)+6))
    print(c[0], end='')

ttl('Interactive Help System', 2)
while True:
    func = str(input('Enter the function. '))
    getHelp(func)
    exit = str(input('Do you want to quit? [Y/N]')).strip().upper()[0]
    if exit == "Y":
        break