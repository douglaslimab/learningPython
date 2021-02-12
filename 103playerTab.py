def playerTab(name='<Unknown>', scores='0'):
    tab = list()
    scores = int(scores)
    tab.append(name)
    tab.append(scores)
    return tab

player = str(input('Player: ')).strip().capitalize()
marks = str(input('Marks: '))
if marks.isnumeric() == False:
    marks = 0
    tab = playerTab(player, marks)
if player == '':
    player = 0
    tab = playerTab(scores=marks)
print(f'The player {tab[0]} got {tab[1]} socres.')