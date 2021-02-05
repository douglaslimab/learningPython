country = list()
state = dict()

for colum in range(0, 3):
    state['state'] = str(input('Enter the state.')).strip().capitalize()
    state['code'] = str(input('Enter the initials.')).strip().upper()
    country.append(state.copy())

print(country)

for i in country:
    print(i)

for s in country:
    for k, v in state.items():
        print(f'{k}: {v}')

for s in country:
    for i in s.values():
        print(i, end=' ')
    print()