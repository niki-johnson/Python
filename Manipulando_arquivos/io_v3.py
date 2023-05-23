"""
    lendo o arquivo em forma de stream
"""

arquivo = open('pessoas.csv')
for registro in arquivo:  # assim, o programa le o arquivo sobe demanda sem carregar todo o conteudo 1º
    print('Nome: {}. Idade: {}'.format(*registro.rstrip().split(',')))
arquivo.close()
