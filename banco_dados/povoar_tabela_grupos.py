from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = """
    INSERT INTO grupos (descrição) VALUES(   
        %s
    )
"""

grupos = [
    ('Casa',),
    ('Trabalho',)
]

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, grupos)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'{cursor.rowcount} linha(s) incluída(s)')
