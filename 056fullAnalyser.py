oldest_man = ''
oldest_man_age = int(0)
unde21_woman_counter = int(0)
age_counter = int(0)
for i in range(0, 4):
    name = str(input('Name: '))
    age = int(input('Age: '))
    gen = str(input('Gender: '))
    age_counter += age
    if gen == 'male':
        if age > oldest_man_age:
            oldest_man_age = age
            oldest_man = name
    if gen == 'female':
        if age < 21:
            unde21_woman_counter =+ 1
avarage = float(age_counter/4)
print('\nThe avarage age is: {:.1f}.\n'.format(avarage))
print('The oldest man is {}.\n'.format(oldest_man))
print('{} women under 21 years.\n'.format(unde21_woman_counter))