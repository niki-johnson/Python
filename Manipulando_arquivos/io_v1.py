"""
    carregando o arquivo todo e fzd a leitura
"""
arquivo = open('pessoas.csv')
dados = arquivo.read()  # lê arquivo completo
arquivo.close()
for registros in dados.splitlines():
    print('Nome: {}. Idade: {}'.format(*registros.split(',')))
