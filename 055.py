max_weight = float(0)
min_weight = float(0)
for i in range(0, 5):
    current_weight = float(input('Enter your weight: '))
    if min_weight == 0:
        min_weight = current_weight
    if current_weight > max_weight:
        max_weight = current_weight
    elif current_weight < min_weight:
        min_weight = current_weight

print('The maximum is {:.1f}'.format(max_weight))
print('The minimum is {:.1f}'.format(min_weight))