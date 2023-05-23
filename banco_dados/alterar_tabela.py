from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = """
    ALTER TABLE contatos ADD COLUMN
        id INT AUTO_INCREMENT PRIMARY KEY
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
