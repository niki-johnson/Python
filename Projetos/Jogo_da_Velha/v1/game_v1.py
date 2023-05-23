import random
from jogador_v1 import HumanPlayer, PcPlayer


class Game():

    def __init__(self):
        self.board = [" " for i in range(0, 9)]
        self.vencedor = None

    @staticmethod
    def start():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(0, 3)]

        for row in number_board:
            print(" | ".join(row))

    def print_game(self):
        # printa o jogo
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print(" | ".join(row))
        print("")

    def posicao_disponivel(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def moves_disponiveis(self):
        return ' ' in self.board

    def winner(self):
        """
            Transformar a linha e coluna e diagonal em somatorio
            Caso valor seja 3 - jogador 'x' ganha, caso de 0, jogador 'o' ganha
        """
        posicao_binaria = map(lambda i: 1 if i ==
                              'x' else 0 if i == 'o' else 5, self.board)
        posicao_binaria = list(posicao_binaria)
        linhas_somatorio = [sum(posicao_binaria[i*3:(i+1)*3])
                            for i in range(3)]
        colunas_somatorio = [sum([posicao_binaria[i] for i in range(j, 9, 3)])
                             for j in range(0, 3)]
        diagonal1 = [sum(posicao_binaria[i] for i in [0, 4, 8])]
        diagonal2 = [sum(posicao_binaria[i] for i in [2, 4, 6])]
        jogada_vencedora = linhas_somatorio + colunas_somatorio + diagonal1 + diagonal2

        if 0 in jogada_vencedora or 3 in jogada_vencedora:
            return True

    def __str__(self):
        self.start()
        return f'\nBem vindo ao Jogo da Velha!!\nAcima estão as posições disponiveis. Grave bem elas, vai precisar ;)\nTecle "H" sempre que precisar ver essas posições novamente\n'


def tictactoe(jogo, player1, player2):

    print(jogo)
    jogo.print_game()
    vez_jogador = 0

    while jogo.moves_disponiveis():
        if vez_jogador % 2 == 0:
            player1.make_move(jogo)
            vez_jogador += 1
            if jogo.winner():
                print("Player 1 ganhou")
                exit()
        else:
            player2.make_move(jogo)
            vez_jogador += 1
            if jogo.winner():
                print("Player 2 ganhou")
                exit()

    print("O jogo empatou")
    exit()


if __name__ == '__main__':
    game = Game()
    mateus = HumanPlayer('o')
    pc = PcPlayer('x')
    tictactoe(game, pc, mateus)
