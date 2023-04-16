import sqlite3


def cadastro(nome, idade):
    con = sqlite3.connect('pessoas.db')
    cur = con.cursor()

    cur.execute("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", (nome, idade))

    con.commit()
    con.close()
