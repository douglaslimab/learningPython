general_players = list()
player = dict()
points = list()
counter = 0
while True:
    player.clear()
    player['name'] = str(input('Player name: ')).strip().capitalize()
    num = int(input(f'How many matches did {player["name"].capitalize()} played? '))
    points.clear()
    for i in range(0, num):
        points.append(int(input(f'How many scores in the {i + 1}º match? ')))
    player['scores'] = points[:]
    player['total'] = sum(points)
    general_players.append(player.copy())

    exit = str(input('Do you want to quit? [Y/N] ')).strip().upper()[0]
    if exit == 'Y':
        break
print('Code ', end='')
for i in player.keys():
    print(f'{i:<15}',end='')
print()
print('-'*60)
for k, v in enumerate(general_players):
    print(f'{k:<5}', end='')
    for col in v.values():
        print(f'{str(col):<15}', end='')
    print()
print('-'*60)
while True:
    player_index = int(input(f'Enter the player number. '))
    print(f'Stats of {general_players[player_index]["name"]}:')
    for k, v in enumerate(general_players[player_index]['scores']):
        print(f'The player got {v} marks in the match {k + 1}')
    exit = str(input('Do you want to quit? [Y/N] ')).strip().upper()[0]
    if exit == 'Y':
        break
