"""
    estudo de caso resolvendo como usar obj mutavel como valor default
"""


def fibonacci(sequencia=None):
    # como None retorna Falso, 0,1 se torna o valor "defalut"
    sequencia = sequencia or [0, 1]
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == "__main__":
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()  # expectativa da lista voltar a 0 e 1
    # valor contina sendo incrementado - erro se propaga
    print(restart, id(restart))
