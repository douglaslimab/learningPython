line = str(input('Enter your full name.\n')).strip()
print(line.upper())
print(line.lower())
print(len(line) - line.count(' '))
print(line.find(' '))
cut = line.split()
print(cut)
print('First name is {} and has {} letters'.format(cut[0], len(cut[0])))
"""
print(line[8:12])
print(len(line))
print(line.count('d',12,len(line)))
print(line.find(('bene')))
print(line.replace('ben','mal'))
"""