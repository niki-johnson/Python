def busca_binaria(vetor, valor_buscado):

    menor = 0
    maior = len(vetor) - 1
    while menor <= maior:
        meio = (menor + maior) // 2
        if valor_buscado == vetor[meio]:
            return meio

        elif valor_buscado < vetor[meio]:
            maior = meio - 1

        else:
            menor = meio + 1

    return -1
