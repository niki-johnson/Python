from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = """INSERT INTO contatos (nome, tel) VALUES
         (%s, %s) 
"""

# valores serão passados por meio de uma tupla
args = ('Mateus', '71991264097')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('1 registro concluído. ID:', cursor.lastrowid)
