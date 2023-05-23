from math import inf as infinity
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


class AIPlayer(Player):

    count = 0

    def __init__(self, letra):
        super().__init__(letra)
        AIPlayer.count += 1
        self.nome = f'AI {AIPlayer.count}'

    def evaluate(self, state, adversario_letra):
        """
        Function to heuristic evaluation of state.
        :param state: the state of the current board
        :return: +1 if the computer wins; -1 if the human wins; 0 draw
        """

        pre_score = state.winner()[1]
        if pre_score == self.letra:
            score = 1
        elif pre_score == adversario_letra:
            score = -1
        else:
            score = 0

        return score

    def minimax(self, state, letra):

        adversario_letra = 'x' if self.letra == 'o' else 'o'
        if letra == self.letra:
            best_move = [None, -infinity]
        else:
            best_move = [None, +infinity]

        if not state.moves_disponiveis() or state.winner()[0]:
            sim_score = self.evaluate(state, adversario_letra)
            return [None, sim_score]

        for casa in state.posicao_disponivel():
            state.board[casa] = letra
            jogada_simulada = self.minimax(state, adversario_letra if letra !=
                                           adversario_letra else self.letra)

            state.board[casa] = ' '
            jogada_simulada[0] = casa

            if letra == self.letra:
                if jogada_simulada[1] > best_move[1]:
                    best_move = jogada_simulada  # max value
            else:
                if jogada_simulada[1] < best_move[1]:
                    best_move = jogada_simulada  # min value

        return best_move

    def make_move(self, jogo):

        if jogo.posicao_disponivel() == 9:
            jogada = random.choice(jogo.posicao_disponivel())
            return jogada
        else:
            jogada = self.minimax(jogo, self.letra)[0]
            return jogada
