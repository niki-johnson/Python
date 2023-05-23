"""
    Computador tem um número 'secreto' e a ideia é tentar adivinhar
"""

import random


def num_aleatorio():

    num_aleatorio = random.randrange(0, 100)

    return num_aleatorio


def intervalo(numero):

    num_str = str(numero)
    if numero < 10:
        inicio_int = 0
    else:
        inicio_int = int(num_str[0]) * 10
    final_int = inicio_int + 9

    return (inicio_int, final_int)


def selecionar_dificuldade(number):

    if number == 1:
        return (dificuldade_facil, 5)
    elif number == 2:
        return (dificuldade_medio_dificil, 5)
    elif number == 3:
        return (dificuldade_medio_dificil, 3)
    else:
        raise TypeError


def dificuldade_facil(num_secreto, tentativas):
    print(f'\nVocê tem {tentativas} tentativas')
    for i in range(1, 6):
        numero_user = int(input(f'Tentativa {i}: '))
        if numero_user < num_secreto:
            print("Tentativa muito baixa")
        elif numero_user > num_secreto:
            print("Tentativa muito alta")
        elif numero_user is num_secreto:
            return 1
        elif i == 5 and not numero_user is num_secreto:
            return 0


def dificuldade_medio_dificil(num_secreto, tentativas):
    print(f'\nVocê tem {tentativas} tentativas')

    for i in range(1, tentativas + 1):
        numero_user = int(input(f'Tentativa {i}: '))
        if numero_user is num_secreto:
            return 1
        elif i == tentativas and not numero_user is num_secreto:
            return 0


def jogar():
    numero_secreto = num_aleatorio()
    intervalo_num = intervalo(numero_secreto)
    dificuldade = int(input())
    while True:
        try:
            parametros = selecionar_dificuldade(dificuldade)
            break
        except TypeError:
            dificuldade = int(input('Insira um número válido entre 1 e 3: '))

    print(
        f'\nO número está entre {intervalo_num[0]} e {intervalo_num[1]}')
    parametros = selecionar_dificuldade(dificuldade)
    return (parametros[0](numero_secreto, parametros[1]), numero_secreto)


def main():

    codigo_jogar = 1
    while (codigo_jogar):
        print("Adivinhe o número!")
        print("Escolha a dificuldade:\n\nFácil: 5 tentativas com dicas\nMédio: 5 tentativas sem dicas\nDifícil:3 tentativas sem dicas\n\nEscolha:\nFácil - 1\nMédio - 2\nDifícil - 3\n")
        resultado = jogar()

        if resultado[0]:
            print(f'\nParabéns!! Você acertou. O número é {resultado[1]}')
        else:
            print(
                f'\nPoxa, não foi dessa vez!\nO número era {resultado[1]}!\nA próxima partida vai ser melhor ;)')

        codigo_jogar = int(
            input('\nQuer jogar novamente?\n[1] para S, [0] para N\n'))


if __name__ == '__main__':
    main()
    print("Foi um bom jogo. Até a próxima!")
