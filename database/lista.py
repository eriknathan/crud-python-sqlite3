import sqlite3


def listar_pessoas():
    con = sqlite3.connect('dbcrudpy.db')
    cur = con.cursor()

    cur.execute("SELECT * FROM pessoas")

    rows = cur.fetchall()
    con.close()

    return rows
