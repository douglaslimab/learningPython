num = sum = counter = 0
while True:
    num = int(input('Enter the number: '))
    if num == 999:
        break
    sum += num
    counter += 1
print('Total: {}'.format(sum))
print('Number of times: {}'.format(counter))

