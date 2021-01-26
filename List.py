num = [2, 3, 51, 8, 9]
print(num)
num.append(10)
print(num)
num.sort(reverse=True)
print(num)
num.insert(0, 2)
print(num)
num.remove(2)
print(num)

newList = []
for counter in range(0, 5):
    newList.append(int(input('Enter the number. ')))

for i, n in enumerate(newList):
    print(f'in position {i} item {n} ')