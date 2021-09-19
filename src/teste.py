import sqlite3

arquivo = './Projeto.SQL'
con = sqlite3.connect(arquivo)
cur = con.cursor()

cur.execute("insert into Usúarios values ('1', 'Juliana', '1993-12-29'")

con.close()