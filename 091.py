from random import randint
from time import sleep
from operator import itemgetter
game = {
    'player1': randint(1, 6),
    'player2': randint(1, 6),
    'player3': randint(1, 6),
    'player4': randint(1, 6)
}
ranking = list()
for k, v in game.items():
    print(f'{k} got {v}')
    sleep(1)

ranking = sorted(game.items(), key = itemgetter(1), reverse = True)

print('==Ranking==')
for index, value in enumerate(ranking):
    print(f'{index + 1}º | {value[0]} | {value[1]}')
    sleep(1)