from random import shuffle
from math import ceil

ADDR = "../assets/tournament-master.pkt"
BLUE = "\033[38;5;111m"
RST = "\033[0m"

MAX_TEAM_PER_POOL = 5


def _blue_input(str=""):
    input_value = input(str + BLUE)
    print(RST, end="")
    return input_value


def create_tournament(f):
    """Create a new tournament.

    Request the amount of teams participating as well as their names, and
    computes a partial pkt representation of a random tournament featuring
    these teams.

    :return: pkt representation of a random new tournament
    :rtype: str, pkt-formatted
    """
    # getting user input : number and names of participating teams
    n = int(_blue_input("How many teams register in this tournament ? "))
    print(f"Please enter the names of the {n} teams:")
    teams = []
    for _ in range(n):
        teams.append(_blue_input("\t- "))
    shuffle(teams)

    # assignment of teams in different pools
    pool_amount = ceil(n / MAX_TEAM_PER_POOL)
    pools = [[] for _ in range(pool_amount)]
    current_pool = 0
    for team in teams:
        pools[current_pool % pool_amount].append(team)
        current_pool += 1
    # Sort the team alphabetically in each pool ?
    for pool in pools:
        pool.sort()
    teams = sum(pools, [])

    # generation of `.pkt` file
    # Header, amount of teams/pools, list of teams
    res = f"Started\n\n{n}, {len(pools)}\n\n"
    first_pool = True
    for pool in pools:
        if not first_pool:
            res += "===\n"
        for team in pool:
            res += f"{team}\n"
        first_pool = False

    # Matches to do
    res += "\n"
    for pool in pools:
        pl = len(pool)
        for i in range(pl):
            for j in range(i + 1, pl):
                res += f"{pool[i]} - {pool[j]}\n"

    f.seek(0)
    f.write(res)
    f.truncate()

    return res


def display_tournament():
    """Display the current tournament."""
    pass


def update_tournament(f):
    """Update the current tournament."""
    f.seek(0)



if __name__ == '__main__':
    f = open(ADDR, "r+")
    lines = f.readlines()
    tournament_started = (lines[0] != "finished\n" and lines[0] != "")
    if tournament_started:
        print("Tournament has started.")
        if (_blue_input("Shall we override the tournament with a new one ? [y/N] ") == "y"):
            create_tournament(f)
    else:
        create_tournament(f)
    display_tournament()
    update_tournament(f)
