person = list()
people = list()
while True:
    person.append(str(input('Name: ')).capitalize())
    person.append(float(input('Weight: ')))
    people.append(person[:])
    person.clear()
    exit = str(input('Do you want to quit? [Y/N] ')).strip().upper()[0]
    if exit == 'Y':
        break

max_weight = min_weight = 0
for i, p in enumerate(people):
    if i == 0:
        max_weight = min_weight = p[1]
    if p[1] > max_weight:
        max_weight = p[1]
        max_weight_name = p[0]
    elif p[1] < min_weight:
        min_weight = p[1]
        min_weight_name = p[0]

print(f'{len(people)} person added.')
print(f'The heavier person in the list is {max_weight_name} with {max_weight} Kg')
print(f'The lighter person in the list is {min_weight_name} with {min_weight} Kg')