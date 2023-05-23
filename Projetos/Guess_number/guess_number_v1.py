"""
    Computador tem um número 'secreto' e a ideia é tentar adivinhar
"""

import random


def num_aleatorio():

    num_aleatorio = random.randrange(0, 100)

    return num_aleatorio


def intervalo(numero):

    num_str = str(numero)
    inicio_int = int(num_str[0]) * 10
    final_int = inicio_int + 9

    return (inicio_int, final_int)


def main():

    codigo_jogar = 1
    while (codigo_jogar):
        numero_secreto = num_aleatorio()
        print("Adivinhe o número!")
        intervalo_num = intervalo(numero_secreto)
        print(
            f'Dica: O número está entre {intervalo_num[0]} e {intervalo_num[1]}')
        print("Você tem 3 tentativas")

        for i in range(0, 3):
            numero_user = int(input(f'Tentativa {i + 1}: '))
            if numero_user is numero_secreto:
                print(
                    f'Parabéns!! Você acertou!! O número secreto era {numero_secreto}')
                break

            elif i == 2 and not numero_user is numero_secreto:
                print(
                    f'Infelizmente você não acertou. O número secreto era {numero_secreto}')

        codigo_jogar = int(
            input('Quer tentar novamente?\n[1] para S, [0] para N\n'))
    print("Foi um bom jogo. Espero te ver denovo!")


if __name__ == '__main__':
    main()
