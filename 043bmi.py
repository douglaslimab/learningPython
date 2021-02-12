weight = float(input('Enter your weight.\n'))
height = float(input('Enter your height in m.\n'))

index = weight/(height**2)

print('Your index is: {:.2f}'.format(index))

if index < 18.5:
    print('You are under your regular weight.')
elif 18.5 <= index < 25:
    print('You are at you ideal weight.')
elif 25 <= index < 30:
    print('You are over you regular weight.')
elif 30 <= index < 40:
    print('You are obese.')
else:
    print('You have morbid obesety.')