"""
    Week 4 practice project template for Python Programming Essentials
    Rock-paper-scissors-lizard-Spock

"""

import random


def name_to_number(name):
    """
    Given string name, return integer 0, 1, 2, 3, or 4 
    corresponding to numbering in video
    """

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
        print("Erro. Cheque o valor posto:")

    return name


def number_to_name(number):
    """
    Given integer number (0, 1, 2, 3, or 4)
    corresponding name from video
    """
    # convert number to a name using if/elif/else
    if number == 0:
        return "rock"
    elif number == 1:
        return "spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print("Erro, número fora do intervalo")
    pass


def play(player_choice):

    # blank line para separar jogos consecutivos
    print(" ")
    print("A jogada do player é:", player_choice)
    player_num = name_to_number(player_choice)
    pc_num = random.randrange(0, 4)
    pc_choice = number_to_name(pc_num)
    print("A jogada do computador é:", pc_choice)

    # compute difference of player_number and comp_number modulo five
    dif = player_num - pc_num
    if dif < 0:
        dif = dif + 5
    # use if/elif/else to determine winner and print winner message

    if dif == 0:
        print("PLAYER AND COMPUTER TIES!!")
    elif dif <= 2:
        print("Player wins")
    else:
        print("Computer wins")
    pass


play("rock")
play("spock")
play("paper")
play("lizard")
play("scissors")
