"""
    estudo de caso do por quê n se deve usar obj mutaveis como valor padrao
"""


def fibonacci(sequencia=[0, 1]):
    # uso de mutaveis como valor default (armadilha)
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == "__main__":
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()  # expectativa da lista voltar a 0 e 1
    # valor contina sendo incrementado - erro se propaga
    print(restart, id(restart))
