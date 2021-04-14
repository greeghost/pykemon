import db_gen as db  # accès aux bdd
import sys

# sys.argv déjà utilisé donc on part du principe que c'est ss
con = db.sql_connection('ss')

types = [i[0] for i in con.cursor().execute(
    '''SELECT DISTINCT def FROM type_effectiveness''').fetchall()]
N = max([len(i) for i in types])


def prod(li):
    res = 1
    for i in li:
        res *= i[0]
    return res


def weaknesspt(pkmn, type):
    cursorObj = con.cursor()
    cursorObj.execute(
        '''SELECT effectiveness FROM type_effectiveness AS t JOIN pokemons AS p ON type1 = t.def OR type2 = t.def WHERE p.name = ? AND t.off = ?''', (pkmn, type))
    res = cursorObj.fetchall()
    a, b = ", you n00b!", "."
    # escape code \u001b[32m : pour la couleur verte
    print(f"\n\u001b[32mPokemon {pkmn}'s weakness to {type} factors {int(prod(res)) if int(prod(res)) == prod(res) else prod(res)}{a if prod(res) == 0 else b}\u001b[0m\n")
    return prod(res)


def weaknesst(type):
    cursorObj = con.cursor()
    cursorObj.execute(
        '''SELECT effectiveness, off FROM type_effectiveness WHERE def = ?''', (type,))
    res = cursorObj.fetchall()
    res.sort()
    print(f'\n\u001b[32mWeaknesses for type {type} factor :\n\u001b[0m')
    for e, t in res:
        print(t + ' ' * (N - len(t)) + ': ' + str(e))
    print()


def weaknessp(pkmn):
    cursorObj = con.cursor()
    res = []
    for t in types:
        cursorObj.execute(
            '''SELECT effectiveness FROM type_effectiveness AS t JOIN pokemons AS p ON type1 = t.def OR type2 = t.def WHERE p.name = ? AND t.off = ?''', (pkmn, t))
        res.append((prod(cursorObj.fetchall()), t))
    res.sort()
    print(f'\n\u001b[32mWeaknesses for pokemon {pkmn} factor :\n\u001b[0m')
    for e, t in res:
        print(t + ' ' * (N - len(t)) + ': ' + str(e))
    print()


if __name__ == '__main__':
    if len(sys.argv) >= 3:
        pkmn, type = (sys.argv[1], sys.argv[2])
        weaknesspt(pkmn, type)
    elif len(sys.argv) >= 2:
        e = sys.argv[1]
        if e in types:
            weaknesst(e)
        else:
            weaknessp(e)
    else:
        print('''Error: 1 or 2 arguments needed included in (pokemon, type)''')
