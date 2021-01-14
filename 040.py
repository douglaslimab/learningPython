n1 = int(input('Enter the scores of the first exam.\n'))
n2 = int(input('Enter the scores of the second exam.\n'))

m = (n1 + n2)/2
print('You got {}'.format(m))
if (m >= 7):
    print('You are aproved.')
elif (m < 7) and (m >= 5):
    print('You need more exams')
elif (m < 5):
    print('You have failed.')