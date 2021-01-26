equa = str(input('Enter your mathematical expression. '))
open_counter = closed_counter = counter = 0
for item, char in enumerate(equa):
    if char == '(':
        counter += 1
    elif char == ')':
        counter -= 1
    if counter == -1:
        break
if counter != 0:
    print('Invalid Expression!')
else:
    print('Expression ok')