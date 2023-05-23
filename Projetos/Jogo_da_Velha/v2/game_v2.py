from jogador_v2 import HumanPlayer, PcPlayer


class Game():

    def __init__(self):
        self.board = [" " for _ in range(0, 9)]
        self.vencedor = None

    @staticmethod
    def posicao_tabela():
        """Imprime as posicoes na tabela"""
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
            Para decidir se há vencedor
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
        jogada_final = linhas_somatorio + colunas_somatorio + diagonal1 + diagonal2

        if 0 in jogada_final or 3 in jogada_final:
            return True

        return False

    def __str__(self):
        self.posicao_tabela()
        return f'\nBem vindo ao Jogo da Velha!!\nAcima estão as posições disponiveis. Grave bem elas, vai precisar ;)\nTecle "H" sempre que precisar ver essas posições novamente\n'


def tictactoe(jogo, player):

    jogada = player.make_move(jogo)
    if isinstance(player, HumanPlayer):
        if jogada == 'h':
            while jogada == 'h':
                print("Ok. Aqui estão as posições do jogo")
                jogo.posicao_tabela()
                jogada = input("Hora da nova jogada: ")

        while True:
            try:
                jogada = int(jogada)

                if jogada not in jogo.posicao_disponivel():
                    raise ValueError
                break

            except ValueError:
                jogada = int(input(
                    "Valor indisponível. Tente um numero de 0 a 9!\nAgora escolha: "))
    else:
        print(f'Jogada do {player.nome}')

    jogo.board[jogada] = player.letra
    jogo.print_game()
    if jogo.winner():
        print(f'{player.nome} ganhou')
        exit()


def main(jogo, player1, player2):

    print(jogo)
    jogo.print_game()
    vez_jogador = 0

    while jogo.moves_disponiveis():
        if vez_jogador % 2 == 0:
            tictactoe(jogo, player1)
            vez_jogador += 1

        else:
            tictactoe(jogo, player2)
            vez_jogador += 1

    print("O jogo empatou")
    exit()


if __name__ == '__main__':
    game = Game()
    o_player = HumanPlayer('o', input("Nome jogador 'o': "))
    x_player = PcPlayer('x')
    main(game, o_player, x_player)
