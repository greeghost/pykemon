from calcs import maxspeed
from math import floor

team1 = ['Dragapult', 'Jolteon', 'Pidgeot-Mega', 'Kartana', 'Thundurus-Therian', 'Alomomola', 'Rhyperior', 'Swampert']
team2 = ['Ninjask', 'Shedinja', 'Nidoking', 'Nidoqueen', 'Alakazam', 'Slowbro', 'Dragalge', 'Jirachi']

ts1 = sorted([(i, maxspeed(i)) for i in team1], key = (lambda tup: tup[1]))

m2 = max([maxspeed(i) for i in team2])

flag = True
for i in ts1:
    if floor(i[1] * 1.5) > m2:
        if not flag and i == ts1[-1]:
            print(f"and {i[0]}.\n")
        elif not flag:
            print(f"{i[0]}, ", end = '')
        if flag and i != ts1[-1]:
            print(f"\nPokemon {i[0]} and faster ones are good scarfers for team 1, as in they outspeed the entirety of team 2 once they hold a choice scarf\nThese are {i[0]}, ", end = '')
            flag = False
        elif flag and i == ts1[-1]:
            print(f"\nPokemon {i[0]} is the only good scarfer for team 1, as in they outspeed the entirety of team 2 once they hold a choice scarf")
if flag:
    print("Team 1 has no good scarfers, meaning they hae no pokemon outspeeding the entirety of team 2, even with a choice scarf :/")
