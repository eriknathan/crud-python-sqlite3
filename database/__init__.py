import sqlite3


def connect_database():
    con = sqlite3.connect('pessoas.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS pessoas
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    idade INTEGER)''')

    con.commit()
    con.close()
