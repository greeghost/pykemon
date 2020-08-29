from math import floor
import db_gen as db
import sys

con = db.sql_connection('ss')

def hp(base, iv, ev, lvl):
    return floor((2 * base + iv + floor(ev / 4)) * lvl / 100) + lvl + 10

def stat(base, iv, ev, lvl, nat):
    return floor((floor(lvl / 100 * (2 * base + iv + floor(ev / 4))) + 5) * nat)

def maxspeed(pkmn):
    cur = con.cursor()
    cur.execute('''SELECT spe FROM pokemons WHERE name = ?''', (pkmn,))
    base = cur.fetchall()[0][0]
    return stat(base, 31, 252, 100, 1.1)

if __name__ == '__main__':
    cont = True
    choice = "\nWhat would you want to calc ?\n1) A given pokemon's maximum speed\n2) Nothing\n"
    while cont:
        ch = int(input(choice))
        if ch == 1:
            pkmn = input("\nWhat pokemon ? ")
            print(f"{pkmn}'s max speed is {maxspeed(pkmn)}\n")
        if ch == 2:
            cont = False
