import enchant
d = enchant.Dict("en_US")
if d.check("Helo"):
    print('True')
else:
    print('False')
