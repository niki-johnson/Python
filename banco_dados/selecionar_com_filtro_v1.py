from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = """
    SELECT * FROM contatos
    WHERE tel = '71991264097'
"""

with nova_conexao() as conexao:

    cursor = conexao.cursor()
    cursor.execute(sql)

    # x é uma tupla
    for x in cursor:
        print(x)
