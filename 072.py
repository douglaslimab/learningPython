numbers = ('zero', 'one', 'two', 'three', 'four', 'five',
           'six', 'seven', 'eight', 'nine', 'ten',
           'eleven', 'twelve', 'thirteen', 'fourteen', 'fiveteen',
           'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
while True:
    index = int(input('Enter the number you want to see: '))
    while index > 20 or index < 0:
        index = int(input('Enter the number you want to see: '))
    print(numbers[index])
    exit = str(input('Do you want to quit? [Y/N] ')).strip().upper()[0]
    if exit == 'Y':
        break
print('Finished')