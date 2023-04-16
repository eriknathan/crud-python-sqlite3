import sqlite3


def editar_pessoa(id, nome, idade):
    con = sqlite3.connect('dbcrudpy.db')
    cur = con.cursor()

    cur.execute("UPDATE pessoas SET nome = ?, idade = ? WHERE id = ?", (nome, idade, id))

    con.commit()
    con.close()
