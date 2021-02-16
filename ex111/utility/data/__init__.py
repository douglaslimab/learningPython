def readMoney(msg):
    ok = False
    while not ok:
        inData = str(input(msg)).replace(',', '.').strip()
        if inData.isalpha() or inData == '':
            print(f'\033[0;31mInalid input!\033[m')
        else:
            ok = True
            return float(inData)