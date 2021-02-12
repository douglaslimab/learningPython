group = list()
student = dict()

student['name'] = str(input('Enter the student name.')).strip().capitalize()
student['scores'] = float(input('Enter the scores.'))
if student['scores'] < 7:
    student['result'] = 'reproved'
else:
    student['result'] = 'approved'

print(student)
print(f'{student["name"]} has {student["scores"]} points. {student["result"].upper()}')