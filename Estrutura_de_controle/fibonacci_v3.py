"""
Algoritmo que produz a sequencia de fibonacci de forma recursiva
"""


def seq_fibonacci(sequencia, flag):

    if len(sequencia) == flag:
        return sequencia

    sequencia.append(sum(sequencia[-2:]))
    return seq_fibonacci(sequencia, flag)


if __name__ == '__main__':

    inicio = [0, 1]
    print(seq_fibonacci(inicio, 20))
