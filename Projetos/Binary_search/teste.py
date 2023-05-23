"""
    Testando velocidade bisca_binaria_v1, v2 e busca sequencial
"""

from busca_binaria_v1 import busca_binaria as busca_binaria1
from busca_binaria_v2 import busca_binaria as busca_binaria2
import random
import time


def busca_sequencial(vetor, valor_procurado):
    for i in range(len(vetor)):
        if vetor[i] == valor_procurado:
            return i


if __name__ == '__main__':

    iteracoes = 1000
    lista = set()
    while len(lista) < iteracoes:
        lista.add(random.randint(-3*iteracoes, 3*iteracoes))
    lista_cresc = sorted(list(lista))

    start = time.time()
    for alvo in lista_cresc:
        busca_sequencial(lista_cresc, alvo)
    end = time.time()
    print("Tempo da busca sequencial:", (end - start)/iteracoes, "segundos")

    start = time.time()
    for alvo in lista_cresc:
        busca_binaria1(lista_cresc, alvo)
    end = time.time()
    print("Tempo da busca binaria v1:", (end - start)/iteracoes, "segundos")

    start = time.time()
    for alvo in lista_cresc:
        busca_binaria2(lista_cresc, alvo)
    end = time.time()
    print("Tempo da busca binaria v2:", (end - start)/iteracoes, "segundos")
