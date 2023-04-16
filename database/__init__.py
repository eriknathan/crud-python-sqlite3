import sqlite3


def connectDatabase():
    con = sqlite3.connect('dbcrudpy.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS dbcrudpy
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    idade INTEGER)''')

    con.commit()
    con.close()
