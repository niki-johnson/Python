from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = """
    INSERT INTO contatos (nome, tel) VALUES
    (%s, %s)
"""
args = [
    ('Manuel', '77988327574'),
    ('Tetê', '71999320534'),
    ('Fernanda', '11991323325'),
    ('Ana', '33999465503'),
    ('Bia', '77988282708'),
    ('Leandro', '25991332608')
]

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Foram incluídos {cursor.rowcount} registros')
