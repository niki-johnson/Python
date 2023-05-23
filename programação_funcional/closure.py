def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular


if __name__ == '__main__':
    dobro = multiplicar(2)  # retornou a função calcular -> dobro é uma funcao
    triplo = multiplicar(3)

    print(f'Triplo de 3 é {triplo(3)}')
    print(f'Dobro de 3 é {dobro(3)}')
