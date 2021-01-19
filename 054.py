cnt = int(0)
for i in range(0, 7):
    age = int(input('Enter the age: '))
    if age < 21:
        cnt += 1
print('{} are under 21 years old.'.format(cnt))
print('{} are above 21 years old'.format(7 - cnt))