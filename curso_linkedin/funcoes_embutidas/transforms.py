# Usando funções transformadoras: sorted, filter, map

def quadrado(x):
    pass


def nota_para_conceito(x):
    pass


def main():
    # Definindo sequencias para usarmos nesta tarefa
    numeros = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    letras = "abcDeFGHiJklmnoP"
    notas = (81, 89, 94, 78, 61, 66, 99, 74)

    # TODO: Use filter para remover itens de uma lista
    impares = list(filter(lambda x: x % 2 != 0, numeros))
    print(impares)

    # TODO: Use filter numa sequência de caracteres que retorne minusculas
    minusculas = ''.join(list(filter(lambda letra: letra.islower(), letras)))
    print(minusculas)

    # TODO: Use map para criar uma nova sequência de valores ao quadrado
    quadrados = list(map(lambda x: x ** 2, numeros))
    print(quadrados)

    # TODO: Use sorted e map para mudar as notas para conceito


if __name__ == "__main__":
    main()
