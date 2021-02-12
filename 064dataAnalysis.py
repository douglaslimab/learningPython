counter = int(0)
sum = int(0)
num = int(input('Enter the number 999 to stop.'))
while num != 999:
    counter += 1
    sum += num
    num = int(input('Enter the number 999 to stop.'))
print('You have entered {} numbers and it sumarize {}.'.format(counter, sum))