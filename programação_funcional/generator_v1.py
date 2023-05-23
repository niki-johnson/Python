"""
    Criando generator 
    Conceito de retornos parciais
"""


def cores_arco_iris():
    # o yield é o proximo valor retornado pelo generator
    # o mesmo numero de retornos do generator é o num de yields
    yield 'vermelho'
    yield 'laranja'
    yield 'amarelo'
    yield 'verde'
    yield 'azul'
    yield 'indigo'
    yield 'violeta'


if __name__ == '__main__':
    generator = cores_arco_iris()
    print(type(generator))
    while True:
        print(next(generator))
