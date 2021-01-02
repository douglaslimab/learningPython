medida = float(input('Enter the measure.\n'))

mm = medida*1000
cm = medida*100
dc = medida*10
dec = medida/10
hec = medida/100
km = medida /1000

print('the measure in cm is {:.0f} cm.\n'.format(cm))
print('The measure in decimeters is {:.0f} dec.\n'.format(dc))