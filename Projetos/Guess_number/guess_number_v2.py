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
        return dificuldade_facil
    elif number == 2:
        return dificuldade_medio
    elif number == 3:
        return dificuldade_dificil
    else:
        print("Erro, número fora do intervalo")
    pass


def dificuldade_facil(**kwargs):
    print(
        f'Dica: O número está entre {kwargs["intervalo"][0]} e {kwargs["intervalo"][1]}')
    print("Você tem 5 tentativas")

    for i in range(1, 6):
        numero_user = int(input(f'Tentativa {i}: '))
        if numero_user < kwargs["secreto"]:
            print("Tentativa muito baixa")
        elif numero_user > kwargs["secreto"]:
            print("Tentativa muito alta")
        elif numero_user is kwargs["secreto"]:
            return 1
        elif i == 5 and not numero_user is kwargs["secreto"]:
            return 0


def dificuldade_medio(**kwargs):
    print(
        f'O número está entre {kwargs["intervalo"][0]} e {kwargs["intervalo"][1]}')
    print("Você tem 5 tentativas")

    for i in range(1, 6):
        numero_user = int(input(f'Tentativa {i}: '))
        if numero_user is kwargs["secreto"]:
            return 1
        elif i == 5 and not numero_user is kwargs["secreto"]:
            return 0


def dificuldade_dificil(**kwargs):
    print(
        f'O número está entre {kwargs["intervalo"][0]} e {kwargs["intervalo"][1]}')
    print("Você tem 3 tentativas")

    for i in range(1, 4):
        numero_user = int(input(f'Tentativa {i}: '))
        if numero_user is kwargs["secreto"]:
            return 1
        elif i == 3 and not numero_user is kwargs["secreto"]:
            return 0


def main():

    codigo_jogar = 1
    while (codigo_jogar):
        numero_secreto = num_aleatorio()
        intervalo_num = intervalo(numero_secreto)
        print("Adivinhe o número!")
        print("Escolha a dificuldade:\n\nFácil: 5 tentativas com dicas\nMédio: 5 tentativas sem dicas\nDifícil:3 tentativas sem dicas\n\nEscolha:\nFácil - 1\nMédio - 2\nDifícil - 3\n")
        dificuldade = int(input(""))
        nome_funcao = selecionar_dificuldade(dificuldade)
        resultado = nome_funcao(secreto=numero_secreto,
                                intervalo=intervalo_num)
        if resultado:
            print(f'\nParabéns!! Você acertou. O número é {numero_secreto}')
        else:
            print(
                f'\nPoxa, não foi dessa vez!\nO número era:{numero_secreto}!\nA próxima partida vai ser melhor ;)')

        codigo_jogar = int(
            input('\nQuer jogar novamente?\n[1] para S, [0] para N\n'))
    print("Foi um bom jogo. Espero te ver denovo!")


if __name__ == '__main__':
    main()
