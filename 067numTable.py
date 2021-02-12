while True:
    num = int(input('Ente the number you want to se the table: '))
    if num < 0:
        break
    for i in range(0, 10):
        print(f'{num} x {i} = {num*i}')
print('Finished')