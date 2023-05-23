def busca_binaria(vetor, valor_buscado, menor=None, maior=None):

    if menor is None:
        menor = 0
    if maior is None:
        maior = len(vetor) - 1

    if maior < menor:
        return -1

    meio = (menor + maior) // 2
    if valor_buscado == vetor[meio]:
        return meio
    elif valor_buscado < vetor[meio]:
        maior = meio - 1
        return busca_binaria(vetor, valor_buscado, menor, maior)
    else:
        menor = meio + 1
        return busca_binaria(vetor, valor_buscado, menor, maior)
