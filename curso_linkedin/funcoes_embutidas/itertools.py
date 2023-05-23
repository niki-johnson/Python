import itertools


def condicao():
    pass


def main():
    # TODO: Iterador cycle pode ser usado como o iter para iterar sobre
    # uma lista
    pessoas = ["Jessica", "Leticia", "Gustavo"]
    ciclo = itertools.cycle(pessoas)
    """print(next(ciclo))
    print(next(ciclo))
    print(next(ciclo))
    print(next(ciclo))"""

    # TODO: Use count para criar um contador
    contador = itertools.count(100, 10)
    """print(next(contador))
    print(next(contador))
    print(next(contador))
    print(next(contador))"""

    # TODO: A função accumulate cria um iterdor que acumula valores
    valores = [10, 20, 30, 40, 50, 40, 30]
    acumulado = itertools.accumulate(valores)
    # print(list(acumulado))

    # TODO: Use a função chain para conectar listas

    # TODO: As funções dropwhile e takewhile vai retornar valores até
    # que uma condição seja atingida


if __name__ == "__main__":
    main()
