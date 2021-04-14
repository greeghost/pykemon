import requests
import re
import json
import sqlite3
import sys
from sqlite3 import Error


def sql_connection(gen):
    '''
    Input : a 2-character string representing the pokemon generation whose
    database you want access to. Valid options are : 'ss', 'sm', 'xy', 'bw',
    'dp', 'rs', 'gs' and 'rb', ordered by age (increasing).

    Output : a sqlite3.Connection object representing said database.
    '''
    try:
        addr = 'databases/' + gen + '.db'
        con = sqlite3.connect(addr)
        print(f'Connection to {addr} successfully established.')
        return con
    except Error:
        print(Error)


def pk_table(con):
    cursorObj = con.cursor()
    try:
        cursorObj.execute("CREATE TABLE pokemons(id integer PRIMARY KEY AUTOINCREMENT, dex_number integer, name text, type1 text, type2 text, hp integer, atk integer, def integer, spa integer, spd integer, spe integer, ability1 text, ability2 text, ability3 text, format text)")
        print('Table successfully created')
        con.commit()
    except Error as e:
        print('Error:', e)
        print('Dropping table pokemons and recreating')
        cursorObj.execute('DROP table if exists pokemons')
        try:
            cursorObj.execute("CREATE TABLE pokemons(id integer PRIMARY KEY AUTOINCREMENT, dex_number integer, name text, type1 text, type2 text, hp integer, atk integer, def integer, spa integer, spd integer, spe integer, ability1 text, ability2 text, ability3 text, format text)")
            print('Table successfully created')
            con.commit()
        except Error as e:
            print('New error:', e)
            print('Giving up, manual repair needed')


def type_table(con):
    cursorObj = con.cursor()
    try:
        cursorObj.execute(
            "CREATE TABLE type_effectiveness(id integer PRIMARY KEY AUTOINCREMENT, def text, off text, effectiveness float)")
        print('Table successfully created')
        con.commit()
    except Error as e:
        print('Error:', e)
        print('Dropping table type_effectiveness and recreating')
        cursorObj.execute('DROP table if exists type_effectiveness')
        try:
            cursorObj.execute(
                "CREATE TABLE type_effectiveness(id integer PRIMARY KEY AUTOINCREMENT, def text, off text, effectiveness float)")
            print('Table successfully created')
            con.commit()
        except Error as e:
            print('New error:', e)
            print('Giving up, needing manual repair')


def pk_insert(con, row):
    cursorObj = con.cursor()
    T = row.get('types')
    T.sort()
    A = row.get('abilities')
    A.sort()
    entities = [row.get('oob')['dex_number'], row.get('name'), T[0], T[1] if len(T) > 1 else None, row.get('hp'), row.get('atk'), row.get('def'), row.get('spa'), row.get(
        'spd'), row.get('spe'), A[0], A[1] if len(A) > 1 else None, A[2] if len(A) > 2 else None, row.get('formats')[0] if len(row.get('formats')) > 0 else None]
    cursorObj.execute('''INSERT INTO pokemons(dex_number, name, type1, type2, hp, atk, def, spa, spd, spe, ability1, ability2, ability3, format) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', entities)
    con.commit()


def type_insert(con, row):
    cursorObj = con.cursor()
    E = row.get('atk_effectives')
    name = row.get('name')
    for D in E:
        cursorObj.execute('''INSERT INTO type_effectiveness(def, off, effectiveness) VALUES(?, ?, ?)''', [
                          D[0], name, D[1]])
    con.commit()


def pk_gen(poke_data, con):
    pk_table(con)
    i = 0
    for row in poke_data:
        try:
            pk_insert(con, row)
        except TypeError:
            row['oob'] = {'dex_number': None}
            pk_insert(con, row)
        i += 1
        if i % 59 == 0:
            print(round(i * 100 / len(poke_data), 2), ' %', sep='')


def type_gen(type_data, con):
    type_table(con)
    for type in type_data:
        type_insert(con, type)


def process(gen):
    con = sql_connection(gen)

    response = requests.get('https://www.smogon.com/dex/' + gen + '/pokemon/')

    data = "".join(re.findall(r'dexSettings = (\{.*\})', response.text))
    data = json.loads(data)
    data = data.get('injectRpcs', [])[1][1]

    # Autres champs : formats, natures, abilities, moves, types(name, atk_effectives, genfamily, description), items
    poke_data = data.get('pokemon', [])
    type_data = data.get('types', [])
    pk_gen(poke_data, con)
    type_gen(type_data, con)

    con.close()


'''Core'''


if __name__ == '__main__':
    gen = sys.argv[1] if len(sys.argv) > 1 else 'ss'

    if gen != 'all':
        process(gen)
    else:
        # 'gs', 'rb' failing because stats didn't work the same way back then
        for gen in ['ss', 'sm', 'xy', 'bw', 'dp', 'rs']:
            process(gen)
