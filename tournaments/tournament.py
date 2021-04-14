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


def create_tournament():
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
    teams = sum(pools, [])

    # generation of `.pkt` file
    res = f"Started\n{n} teams\n\n"
    for team in teams:
        res += f"{team}\n"
    print(res)
    return res


def display_tournament():
    """Display the current tournament."""
    pass


def update_tournament():
    """Update the current tournament."""
    pass


if __name__ == '__main__':
    f = open(ADDR, "r+")
    tournament_started = (f.readlines()[0] != "finished\n")
    if not tournament_started:
        create_tournament()
    display_tournament()
    update_tournament()
