tup = ('pen', 3, 'pencil', 1, 'note book', 5, 'book', 10, 'comic book', 15)
for i in range(len(tup)):
    if tup[i] % 2 == 0:
        print(f'{tup[i]}' + '.'*(20 - len(tup[1])))
    else:
        print(tup[i])