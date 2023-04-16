import sqlite3


def cadastrar_pessoa(nome, idade):
    con = sqlite3.connect('dbcrudpy.db')
    cur = con.cursor()

    cur.execute("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", (nome, idade))

    con.commit()
    con.close()
