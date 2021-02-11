line = str(input('Enter your text.\n')).upper().strip()
print(line.count('A'))
print(line.find('A') + 1)
print(line.rfind('A') + 1)