exit = 'N'
counter_men = counter_women = counter_over18 = 0
while True:
    name = str(input('Name: '))
    gender = str(input('Gender: [M/F] ')).strip().upper()[0]
    while gender not in 'MmFf':
        gender = str(input('Invalid char. Please enter the gender: [M/F] ')).strip().upper()[0]

    age = int(input('Age: '))

    if age > 18:
        counter_over18 += 1

    if gender == 'M':
        counter_men += 1

    if age < 20 and gender == 'F':
        counter_women += 1

    exit = str(input('Do you want to quit? [Y/N]')).strip().upper()[0]
    while exit not in 'YyNn':
        exit = str(input('Invalid char. Do you want to quit? [Y/N]')).strip().upper()[0]

    if exit == 'Y':
        break
print('Number of people over 18 years: {}'.format(counter_over18))
print('Number of men: {}'.format(counter_men))
print('Number of women under 20 years old: {}'.format(counter_women))