"""
    lendo o arquivo em forma de stream
    evitando erros e fechando o arquivo
"""

# o with garante que ao final do bloco, o arquivo será fechado
with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:  # criando um novo arquivo onde pode ser editado
        for registro in arquivo:
            print('Nome: {}. Idade: {}'.format(
                *registro.rstrip().split(',')), file=saida)

if arquivo.closed and saida.closed:
    print('Arquivos já foram fechados')
