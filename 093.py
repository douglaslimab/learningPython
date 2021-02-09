player = dict()
points = list()
counter = 0
player['name'] = str(input('Player name: '))
num = int(input(f'How many matches did {player["name"].capitalize()} played? '))
for i in range(0, num):
    points.append(int(input(f'How many scores in the {i + 1}º match? ')))
    counter += points[i]
player['scores'] = points
player['total'] = counter
print(player)
for k, v in player.items():
    print(f'The pointer {k} has {v}.')
for k, v in enumerate(player['scores']):
    print(f'In the {k + 1}º match the player made {v} scores.')
print(f'The player got a total of {player["total"]}.')