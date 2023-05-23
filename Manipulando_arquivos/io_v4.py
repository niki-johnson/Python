"""
    lendo o arquivo em forma de stream
    evitando erros e fechando o arquivo
"""

arquivo = open('pessoas.csv')

try:
    for registro in arquivo:  # assim, o programa le o arquivo sobe demanda sem carregar todo o conteudo 1º
        print('Nome: {}. Idade: {}'.format(*registro.rstrip().split(',')))

finally:  # sempre é executado apesar do erro
    arquivo.close()
    print("Arquivo fechado")
