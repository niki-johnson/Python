from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

selecionar_grupo = """
    SELECT id FROM grupos 
    WHERE descrição = %s
"""

atualizar_contato = """
    UPDATE contatos SET group_id = %s
    WHERE nome = %s
"""

contato_grupo = {
    'Mateus': 'Casa',
    'Joao': 'Trabalho',
    'Maria': 'Casa',
    'Julia': 'Casa',
    'Manuel': 'Trabalho',
    'Tetê': 'Casa',
    'Fernanda': 'Trabalho',
    'Ana': 'Trabalho',
    'Leandro': 'Trabalho'
}

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        for contato, grupo in contato_grupo.items():
            cursor.execute(selecionar_grupo, (grupo,))
            grupo_id = cursor.fetchone()[0]
            cursor.execute(atualizar_contato, (grupo_id, contato))
            conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('Contatos atualizados')
