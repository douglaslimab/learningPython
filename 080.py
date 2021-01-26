list = []
for i in range(0, 5):
    num = int(input('Enter a number. '))
    if i == 0 or num > list[-1]:
        list.append(num)
        print('Added at the ent of the list.')
    else:
        counter = 0
        while counter < len(list):
            if num <= list[counter]:
                list.insert(counter, num)
                print(f'Added at position {counter}')
                break
            counter += 1
print(list)