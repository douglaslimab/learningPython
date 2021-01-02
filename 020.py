import random
name1 = str(input('First:\n'))
name2 = str(input('Second:\n'))
name3 = str(input('Thirth:\n'))
name4 = str(input('Fourth:\n'))

list = [name1, name2, name3, name4]
random.shuffle(list)
print(list)