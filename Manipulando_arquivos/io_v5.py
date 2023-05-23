"""
    lendo o arquivo em forma de stream
    evitando erros e fechando o arquivo
"""

with open('pessoas.csv') as arquivo:  # o with garante que ao final do bloco, o arquivo será fechado
    for registro in arquivo:
        print('Nome: {}. Idade: {}'.format(*registro.rstrip().split(',')))

if arquivo.closed:
    print('Arquivo já foi fechado')
