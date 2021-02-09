person = dict()
group = list()
average_age = 0
while True:
    person.clear()
    person['name'] = str(input('Name: ')).strip().capitalize()
    person['gender'] = str(input('Gender [M/F]:')).strip().upper()[0]
    person['age'] = int(input('Age: '))
    average_age += person['age']
    group.append(person.copy())
    exit = str(input('Do you want to quit? [Y/N] ')).strip().upper()[0]
    if exit == 'Y':
        break
print(group)
print(f'{len(group)} people registered.')
average_age /= len(group)
print(f'Average age: {average_age}')
print('Women in the group: ', end='')
for i in group:
    if i['gender'] == 'F':
        print(f'{i["name"]}', end=' ')
print()
print('People over the average:')
for i in group:
    if i['age'] > average_age:
        print(f'Name: {i["name"]}; Gender: {i["gender"]}; Age: {i["age"]}')