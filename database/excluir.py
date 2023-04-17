import sqlite3


def excluir(id):
    con = sqlite3.connect('pessoas.db')
    cur = con.cursor()

    cur.execute("DELETE FROM pessoas WHERE id = ?", (id,))

    con.commit()
    con.close()
