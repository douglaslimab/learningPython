card_grades = list()
student_number = 0
while True:
    name = str(input('Name: ')).strip().capitalize()
    score1 = float(input('Scores 1: '))
    score2 = float(input('Scores 1: '))
    final_score = (score2 + score1) / 2
    card_grades.append([name,[score1, score2], final_score])

    student_number += 1
    exit = str(input('Do you want to quit? [Y/N]')).strip().upper()[0]
    if exit == 'Y':
        break

print('-='*30)
print(f'{"No.":<4}{"Student":<10}{"Final":>8}')
print('-'*22)
for num, lin in enumerate(card_grades):
    print(f'{num:<4}{lin[0]:<10}{lin[2]:>8}')

while True:
    print('-'*22)
    index = int(input('Which student marks do you want to check? '))
    if index < len(card_grades):
        print(f'{card_grades[index][0]}{card_grades[index][1]}')
    exit = str(input('Do you want to quit? [Y/N]')).strip().upper()[0]
    if exit == 'Y':
        break