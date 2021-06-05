"""
Week 4 practice project template for Python Programming Essentials
Rock-paper-scissors-lizard-Spock
"""

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
    
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
        print ("Erro, número fora do intervalo")
    pass


def rpsls(player_choice):
    """
    Given string player_choice, play a game of RPSLS 
    and print results to console
    """
    
    # print a blank line to separate consecutive games
    print(" ")
    # print out the message for the player's choice
    print("A jogada do player é:",player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    player_num = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    pc_num = random.randrange(0,4)
    # convert comp_number to comp_choice using the function number_to_name()
    pc_choice = number_to_name (pc_num)
    # print out message for computer's choice
    print("A jogada do computador é:",pc_choice)
    # compute difference of player_number and comp_number modulo five
    dif = player_num - pc_num
    # use if/elif/else to determine winner and print winner message
    if dif < 0:
        dif = dif + 5
        if dif <=2:
            print("Player wins")
        else:
            print("Computer wins")
    elif dif == 0:
        print("PLAYER AND COMPUTER TIES!!")
    else:
        if dif <=2:
            print("Player wins")
        else:
            print("Computer wins")
    pass
     
    
# test your code
rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric