"""
    Estudando o conceito de função de alta ordem
"""

from funcao_primeira_classe import dobro, quadrado


def processar(titulo, lista, funcao):
    print(f'Processando {titulo}')
    for item in lista:
        print(f'{item} -> {funcao(item)}')


if __name__ == '__main__':
    processar('Dobros de 1 a 10', range(1, 11), dobro)
    processar('Quadrado de 1 a 10', range(1, 11), quadrado)
