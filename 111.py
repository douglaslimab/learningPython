try:
    a = int(input('A: '))
    b = int(input('B: '))
    r = a / b
except:
    print('Wrong!!')
else:
    print(r)
finally:
    print('Finally finished..')