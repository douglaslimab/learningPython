num = int(input('Enter the number: '))
result = num
while num != 1:
    result = result*(num - 1)
    num -= 1
print(result)