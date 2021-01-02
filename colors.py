name = 'Hello World!!'
colors = {'clean':'\033[m',
          'blue':'\033[34m',
          'yellow':'\033[33m',
          'blackandwhite':'\033[7;30m'}
print('\033[1:31:43mHello!!\033[m')
print('{}{}{}'.format('\033[4:33:44m',name,'\033[m'))
print('{}{}{}'.format(colors['blackandwhite'],name,colors['clean']))