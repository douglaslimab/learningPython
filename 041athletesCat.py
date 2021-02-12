from datetime import date
current_year = date.today().year
birth_year = int(input('Enter the year of your birth\n'))
age = current_year - birth_year
print('The athlete is {} years old.'.format(age))
if (age <= 9):
    print('Cathegory: Mirin')
elif (age <= 14):
    print('Cathegory: Infantil')
elif (age <= 19):
    print('Cathegory: Junior')
elif (age <= 25):
    print('Cathegory: Senior')
else:
    print('Cathegory: Master')