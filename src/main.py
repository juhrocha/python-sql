import sqlite3

con = sqlite3.connect('/home/juliana/Projeto_SQL/usuarios.db')
cur = con.cursor()

# cur.execute("create table usuarios (id, nome, nascimento)")
# cur.execute("insert into usuarios values ('3', 'Eduardo', '1982-09-13');")
# cur.execute("update usuarios set nascimento = 1998 where nascimento = 1993;")
#
# # for row in cur.execute("select * from usuarios"):
# #     print(row)
#
# con.close()

for row in cur.execute("select * from usuarios"):
    print(row)

con.close()
#
# cur.execute("update usuarios set nascimento = 1998 where nascimento = 1993;")
