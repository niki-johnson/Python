"""
    Week 4 practice project template for Python Programming Essentials
    Rock-paper-scissors-lizard-Spock

"""

import random


def name_to_number(name):

    # convert name to number using if/elif/else
    if name == "rock":
        name = 0
    elif name == "spock":
        name = 1
    elif name == "paper":
        name = 2
    elif name == "lizard":
        name = 3
    elif name == "scissors":
        name = 4
    else:
        raise TypeError
    return name


def play(opcoes):

    player_choice = input("\nA jogada do player é: ")
    while True:
        try:
            player_num = name_to_number(player_choice)
            break
        except TypeError:
            print(f'Insira uma jogada válida entre: {opcoes}')
            player_choice = input("\nA jogada do player é: ")

    pc_choice = random.choice(opcoes)
    pc_num = name_to_number(pc_choice)

    # compute difference of player_number and comp_number modulo five
    diferenca = player_num - pc_num
    if diferenca < 0:
        diferenca = diferenca + 5

    return pc_choice, diferenca


def main():

    opcoes = ["rock", "spock", "paper", "lizard", "scissors"]
    print("Selecione uma das opções abaixo para jogar:")
    for choice in opcoes:
        print("-", choice)
    resultado = play(opcoes)
    print("A jogada do computador é:", resultado[0])

    if resultado[1] == 0:
        print("PLAYER AND COMPUTER TIES!!\n")
    elif resultado[1] <= 2:
        print("Player wins\n")
    else:
        print("Computer wins\n")


if __name__ == '__main__':
    main()
