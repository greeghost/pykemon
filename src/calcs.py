from math import floor
import db_gen as db
from err import InvalidPokemonName

con = db.sql_connection('ss')


def hp(base, iv, ev, lvl):
    return floor((2 * base + iv + floor(ev / 4)) * lvl / 100) + lvl + 10


def stat(base, iv, ev, lvl, nat):
    return floor((floor(lvl / 100 * (2 * base + iv + floor(ev / 4))) + 5) * nat)


def maxspeed(pkmn):
    cur = con.cursor()
    cur.execute('''SELECT spe FROM pokemons WHERE name = ?''', (pkmn,))
    f = cur.fetchall()
    if len(f) == 0:
        raise InvalidPokemonName(pkmn)
    base = f[0][0]
    return stat(base, iv=31, ev=252, lvl=100, nat=1.1)


if __name__ == '__main__':
    print(maxspeed("Gengar"))
