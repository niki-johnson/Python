"""
    Desafio: Ler o arquivo csv e retornar a coluna 4 e 9
"""
import csv
from urllib.request import urlopen


def get_csv(url):

    with urlopen(url) as entrada:
        i = 0
        for cidade in csv.DictReader(entrada.read().decode('latin1').splitlines()):
            print('{}: {}'.format(cidade['nome_desti'], cidade['nome_orige']))


if __name__ == '__main__':
    get_csv(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
