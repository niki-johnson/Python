"""
Algoritmo que produz a sequencia de fibonacci
"""


def seq_fibonacci(flag):

    lista = []

    for i in range(flag):

        if i == 0 or i == 1:
            lista.append(i)

        else:
            lista.append(lista[i-2] + lista[i-1])

    return lista


if __name__ == '__main__':

    print(seq_fibonacci(40))
