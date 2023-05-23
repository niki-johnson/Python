"""
    Selecionando com entrada de usuário e evitando o sql injection - 
    passando os argumentos separado, e não concatenando manualmente
"""

from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = """
    SELECT * FROM contatos
    WHERE nome like %s
"""

with nova_conexao() as conexao:

    contato = str(input('Informe o nome que deseja buscar: '))
    args = (f'%{contato}%', )
    cursor = conexao.cursor()
    cursor.execute(sql, args)

    # x é uma tupla
    for x in cursor:
        print(x)
