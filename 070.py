exit = 'N'
total = over1000 = cheapest = 0
while True:
    product = str(input('Product: '))
    price = float(input('Price: '))

    total += price

    if price > 1000:
        over1000 += 1

    if cheapest == 0:
        cheapest = price
        cheapest_product = product
    if price < cheapest:
        cheapest = price
        cheapest_product = product

    exit = str(input('Do you want to quit? [Y/N] ')).strip().upper()[0]
    while exit not in 'YyNn':
        exit = str(input('Invalid char! Do you want to quit? [Y/N] '))
    if exit == 'Y':
        break

print('Total: {}'.format(total))
print('Number of products over U$ 1000,00: {}'.format(over1000))
print('Cheapest product: {} for U$ {}'.format(cheapest_product, cheapest))