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
        print("Erro. Cheque o valor posto")

    return name


def play(player_choice, opcoes):

    player_num = name_to_number(player_choice)
    pc_choice = random.choice(opcoes)
    pc_num = name_to_number(pc_choice)
    print("A jogada do computador é:", pc_choice)

    # compute difference of player_number and comp_number modulo five
    dif = player_num - pc_num
    if dif < 0:
        dif = dif + 5
    # use if/elif/else to determine winner and print winner message

    if dif == 0:
        print("PLAYER AND COMPUTER TIES!!\n")
    elif dif <= 2:
        print("Player wins\n")
    else:
        print("Computer wins\n")
    pass


def main():

    opcoes = ["rock", "spock", "paper", "lizard", "scissors"]
    print("Selecione uma das opções abaixo para jogar:")
    for choice in opcoes:
        print("-", choice)
    player_choice = input()
    print("A jogada do player é:", player_choice)
    play(player_choice, opcoes)


if __name__ == '__main__':
    main()
