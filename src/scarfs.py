from calcs import maxspeed
from math import floor
from pprint import pprint

team1 = ['Tapu Bulu', 'Thundurus', 'Azelf', 'Diggersby', 'Aerodactyl',
         'Flapple', 'Gigalith', 'Vanilluxe', 'Clawitzer', 'Kadabra', 'Orbeetle']
team2 = ['Heatran', 'Gengar2', 'Primarina', 'Rotom-Wash', 'Flygon',
         'Galvantula', 'Goodra', 'Snorlax', 'Altaria', 'Gourgeist', 'Lapras']

ts1 = sorted([(i, maxspeed(i)) for i in team1], key=(lambda tup: tup[1]))
ts2 = sorted([(i, maxspeed(i)) for i in team2], key=(lambda tup: tup[1]))

m2 = max([maxspeed(i) for i in team2])
M2 = 1.5 * m2

flag = True
Flag = True
for i in ts1:
    if floor(i[1] * 1.5) > m2:
        if not flag and i == ts1[-1]:
            print(f"and {i[0]}.\n")
        elif not flag:
            print(f"{i[0]}, ", end='')
        if flag and i != ts1[-1]:
            print(f"\nPokemon {i[0]} and faster ones are good scarfers for team 1, as in they outspeed the entirety of team 2 once they hold a choice scarf\nThese are {i[0]}, ", end='')
            flag = False
        elif flag and i == ts1[-1]:
            print(
                f"\nPokemon {i[0]} is the only good scarfer for team 1, as in they outspeed the entirety of team 2 once they hold a choice scarf")
if flag:
    print("Team 1 has no good scarfers, meaning they have no pokemon outspeeding the entirety of team 2, even with a choice scarf :/")

for i in ts1:
    if floor(i[1] * 1.5) > M2:
        if not Flag and i == ts1[-1]:
            print(f"and {i[0]}.\n")
        elif not Flag:
            print(f"{i[0]}, ", end='')
        if Flag and i != ts1[-1]:
            print(f"\nPokemon {i[0]} and faster ones are outstanding scarfers for team 1, as in they outspeed the entirety of team 2, even scarfed, once they hold a choice scarf\nThese are {i[0]}, ", end='')
            Flag = False
        elif Flag and i == ts1[-1]:
            print(
                f"\nPokemon {i[0]} is the only outstanding scarfer for team 1, as in they outspeed the entirety of team 2, even scarfed, once they hold a choice scarf\n")
            Flag = False
if Flag:
    print("Team 1 has no outstanding scarfers, meaning they have no pokemon outspeeding the entirety of a scarfed team 2, even with a choice scarf :/")

print("Speed of both teams :")
print("\nTeam 1 :")
pprint(ts1)
print("\nTeam 2 :")
pprint(ts2)
