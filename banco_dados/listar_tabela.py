from bd import nova_conexao

with nova_conexao() as conexao:
    # try:
    cursor = conexao.cursor()
    cursor.execute('SHOW TABLES')  # armazena o proprio resultado

    for i, table in enumerate(cursor, start=1):
        print(f'Tabela {i}: {table[0]}')
