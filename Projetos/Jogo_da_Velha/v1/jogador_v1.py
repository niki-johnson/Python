import math
import random


class Player():

    def __init__(self, letra):
        self.letra = letra

    def make_move(self):
        pass


class PcPlayer(Player):
    def __init__(self, letra):
        super().__init__(letra)

    def make_move(self, game):
        jogada = random.choice(game.posicao_disponivel())
        game.board[jogada] = self.letra
        game.print_game()


class HumanPlayer(Player):
    def __init__(self, letra):
        super().__init__(letra)

    def make_move(self, game):

        posicao = input("Faça sua jogada: ")
        if posicao == 'h':
            while posicao == 'h':
                print("Ok. Aqui estão as posições do jogo")
                game.start()
                posicao = input("Agora escolha: ")

        while True:
            try:
                posicao = int(posicao)

                if posicao not in game.posicao_disponivel():
                    raise ValueError
                break

            except ValueError:
                posicao = int(input(
                    "Valor indisponível. Tente um numero de 0 a 9!\nAgora escolha: "))

        game.board[posicao] = self.letra
        game.print_game()
