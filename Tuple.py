import time
meal = ('burger', 'pizza', 'juice', 'pudim')

for i in meal:
    print('I want to eat a {}.'.format(i))
    time.sleep(1)

for i in range(0, len(meal)):
    print(f'I am eating a {meal[i]}')
    time.sleep(1)

print(sorted(meal))
print('Finished')

i = 0
while True:
    name = str(input('Name: ')).strip().capitalize()
    age = int(input('Age: '))
    gender = str(input('Gender: ')).strip().upper()[0]
    weight = float(input('Weight: '))
    height = float(input('Height: '))
    BMI = weight/(height*height)
    person = (name, age, gender, weight, height, BMI)
    exit = str(input('Do you want to quit? [Y/N] ')).strip().upper()[0]
    if exit == 'Y':
        break
print(person)