"""
Algoritmo que produz a sequencia de fibonacci
"""


def seq_fibonacci(flag):

    resultado = []

    for i in range(flag):

        if i == 0 or i == 1:
            resultado.append(i)

        else:
            resultado.append(sum(resultado[-2:]))

    return resultado


if __name__ == '__main__':

    print(seq_fibonacci(15))
