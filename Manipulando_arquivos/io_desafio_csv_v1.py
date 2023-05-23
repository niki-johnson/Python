"""
    Desafio: Ler o arquivo csv e retornar a coluna 4 e 9
"""

import csv

with open('desafio-ibge.csv', newline='') as csvfile:
    reader_dict = csv.DictReader(csvfile)
    for cidade in reader_dict:
        print('{}: {}'.format(cidade['nome_desti'], cidade['nome_orige']))
