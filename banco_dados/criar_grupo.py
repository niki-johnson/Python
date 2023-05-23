from bd import nova_conexao
from mysql.connector import ProgrammingError

tabela_grupo = """
    CREATE TABLE IF NOT EXISTS grupos(
        id INT AUTO_INCREMENT PRIMARY KEY,
        descrição VARCHAR(50)
    )
"""
alterar_tabela_contato = """
    ALTER TABLE contatos
    ADD group_id INT;
    
    ALTER TABLE contatos
    ADD FOREIGN KEY (grupo_id) REFERENCES grupos(id)
"""


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(tabela_grupo)
        cursor.execute(alterar_tabela_contato)

    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
