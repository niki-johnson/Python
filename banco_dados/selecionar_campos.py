from mysql.connector.errors import ProgrammingError
from bd import nova_conexao


sql = """
    SELECT nome, tel FROM contatos
"""
with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)

    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        for contato in cursor.fetchall():  # contato é uma tupla - representa 1 linha
            print('\t'.join(str(campo) for campo in contato))
