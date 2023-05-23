import math
import random


class Player():

    def __init__(self, letra):
        self.letra = letra

    def make_move(self):
        pass


class PcPlayer(Player):

    count = 0

    def __init__(self, letra):
        super().__init__(letra)
        PcPlayer.count += 1
        self.nome = f'Pc_{PcPlayer.count}'

    def make_move(self, game):
        jogada = random.choice(game.posicao_disponivel())
        return jogada


class HumanPlayer(Player):

    def __init__(self, letra, nome):
        super().__init__(letra)
        self.nome = nome

    def make_move(self, game):
        posicao = input("Faça sua jogada: ")
        return posicao
