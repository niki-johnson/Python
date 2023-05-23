# Usando funções iterators como enumarate, zip, iter, next

def main():

    dias = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab']
    dias_en = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

    # TODO: use a função iter para criar um iterador sobre uma lista
    iterador_dias = iter(dias)
    print(next(iterador_dias))
    print(next(iterador_dias))
    print(next(iterador_dias))
    print(next(iterador_dias))

    # TODO: USE UMA FUNÇÃO PARA ITERAR SOBRE UM ARQUIVO
    with open('dados.txt') as fp:
        for linha in iter(fp.readline, ''):
            print(linha)

    # TODO: usar a função enumerate reduz a quantidade de código e
    # te dá um contador
    for i, dia in enumerate(dias):
        print(i, dia)

    # TODO: Use a função zip para combinar as listas
    for d in zip(dias, dias_en):
        print(d)

    # TODO: combine zip e enumerate para formatar o resultado
    for i, d in enumerate(zip(dias, dias_en)):
        print(f'{i} {d[0]} = {d[1]} em inglês')


if __name__ == '__main__':
    main()
