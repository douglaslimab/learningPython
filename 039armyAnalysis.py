from datetime import date
birth_year = int(input('Enter the year of your birth.\n'))
current_year = date.today().year
age = current_year - birth_year
print('Your age is: {}.'.format(age))

if (age == 18):
    print('You have to apply for the army by the end of the year.')
elif (age < 18):
    future = birth_year + 18 - current_year
    print('You have to apply in {} years.'.format(future))
elif (age > 18):
    past = current_year - birth_year - 18
    print('You should have applied {} years ago.'.format(past))