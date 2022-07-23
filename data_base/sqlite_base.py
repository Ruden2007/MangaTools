import sqlite3 as sq

base = sq.connect('MangaSounds.db')
cur = base.cursor()


def sqlite_start():
    if base:
        print('data base connect OK!')
    else:
        print('!!!data base connect ERROR!!!')
    base.commit()

