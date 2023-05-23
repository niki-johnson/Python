from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = """
    UPDATE contatos SET tel = %s
    WHERE id = %s;
"""
args = ('402333409', 7)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'{cursor.rowcount} registro(s) atualizado(s)')
