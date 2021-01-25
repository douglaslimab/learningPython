tup = ('learn', 'code', 'language', 'python', 'course', 'free', 'work')
counter = 0
for item in tup:
    for letter in item:
        if letter.lower() in 'aeiou':
            counter += 1
    print(f'{item} has {counter} vowels.')
    counter = 0