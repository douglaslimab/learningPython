counter_over21 = counter_under21 = 0
people = list()
person = list()
'''
person.append('Douglas')
person.append(34)
people.append(person[:])
print(people)
person[0] = 'Laura'
person[1] = 33
people.append(person[:])
print(people)
'''
for counter in range(0, 2):
    person.append(str(input('Name: ')))
    person.append(int(input('Age: ')))
    people.append(person[:])
    person.clear()

for i in people:
    print(f'{i[0]} is {i[1]} years old.')

for n in people:
    if n[1] >= 21:
        print(f'{n[0]} is over 21.')
        counter_over21 += 1
    else:
        print(f'{n[0]} is under 21 years old.')
        counter_under21 += 1
print(f'Over 21: {counter_over21}')
print(f'Under 21: {counter_under21}')