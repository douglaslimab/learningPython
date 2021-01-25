counter = 0
tup = (int(input('Enter a number: ')),
       int(input('Enter a number: ')),
       int(input('Enter a number: ')),
       int(input('Enter a number: ')))

print(tup)
print(f'The number 9 appears {tup.count(9)} times')
if 3 in tup:
    print(f'The number 3 is at the {tup.index(3) + 1}ª position')
else:
    print('There is no number 3 in this tuple.')
for i in range(len(tup)):
    if tup[i] % 2 == 0:
        counter += 1
print(f'This tuple has {counter} even numbers')