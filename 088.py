from time import sleep
from random import randint
game = list()
data = list()
num_games = int(input('How sets do you want? '))
for lin in range(0, num_games):
    for col in range(0, 6):
        data.append(randint(1, 60))
    game.append(data[:])
    data.clear()
for lin in range(0, num_games):
    game[lin].sort()
    print(game[lin])
    sleep(1)