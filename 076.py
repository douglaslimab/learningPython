tup = ('pen', 3,
       'pencil', 1,
       'note book', 5,
       'book', 10,
       'comic book', 15,
       'laptop', 1000)
print('-'*40)
print(f'{"Receipt":^40}')
print('-'*40)
for i in range(len(tup)):
    if i % 2 == 0:
        print(f'{tup[i]:.<30}', end='')
    else:
        print(f'U$ {tup[i]:>7.2f}')