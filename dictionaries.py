people = {'name': 'Douglas', 'gender': 'M', 'age': 34}

print(f'{people["name"]} is {people["age"]} years old.')
print(people)
del people['gender']
people['peso'] = 72
print(people.keys())
print(people.values())
print(people.items())

for k, v in people.items():
    print(f'{k}: {v}')