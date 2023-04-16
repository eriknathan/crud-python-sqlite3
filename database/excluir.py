import sqlite3


def excluir_pessoas(id):
    con = sqlite3.connect('dbcrudpy.db')
    cur = con.cursor()

    cur.execute("DELETE FROM pessoas WHERE id = ?", (id,))

    con.commit()
    con.close()

